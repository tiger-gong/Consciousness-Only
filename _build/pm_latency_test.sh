#!/usr/bin/env bash
# Polymarket latency + geo probe for trading nodes
# Usage: bash pm_latency_test.sh [label]
set -euo pipefail

LABEL="${1:-$(hostname)}"
ROUNDS="${ROUNDS:-20}"
OUT_DIR="${OUT_DIR:-./pm_latency_results}"
TS="$(date -u +%Y%m%dT%H%M%SZ)"
mkdir -p "$OUT_DIR"
REPORT="$OUT_DIR/${LABEL}_${TS}.txt"

HOSTS=(
  "clob|https://clob.polymarket.com/time"
  "gamma|https://gamma-api.polymarket.com/markets?limit=1"
  "geoblock|https://polymarket.com/api/geoblock"
  "site|https://polymarket.com/"
)

WS_URL="${WS_URL:-wss://ws-subscriptions-clob.polymarket.com/ws/market}"

log() { echo "$@" | tee -a "$REPORT"; }

measure_http() {
  local name="$1" url="$2"
  local tmp
  tmp="$(mktemp)"
  log ""
  log "=== HTTP $name ==="
  log "URL: $url"

  # One verbose sample for status / headers
  local sample
  sample="$(curl -sS -o /tmp/pm_body_"$name".txt -D /tmp/pm_hdr_"$name".txt \
    -w "code=%{http_code} dns=%{time_namelookup} connect=%{time_connect} tls=%{time_appconnect} ttfb=%{time_starttransfer} total=%{time_total} size=%{size_download} ip=%{remote_ip}\n" \
    --connect-timeout 5 --max-time 15 "$url" || true)"
  log "sample: $sample"
  log "body_head: $(head -c 240 /tmp/pm_body_"$name".txt | tr '\n' ' ')"
  log "cf-ray: $(grep -i '^cf-ray:' /tmp/pm_hdr_"$name".txt | tr -d '\r' || true)"
  log "server: $(grep -i '^server:' /tmp/pm_hdr_"$name".txt | tr -d '\r' || true)"

  # Warm rounds
  : > "$tmp"
  for i in $(seq 1 "$ROUNDS"); do
    curl -sS -o /dev/null \
      -w "%{time_namelookup} %{time_connect} %{time_appconnect} %{time_starttransfer} %{time_total} %{http_code}\n" \
      --connect-timeout 5 --max-time 15 "$url" >> "$tmp" || echo "NaN NaN NaN NaN NaN 000" >> "$tmp"
  done

  python3 - "$tmp" <<'PY' | tee -a "$REPORT"
import sys, statistics as st
rows=[]
for line in open(sys.argv[1]):
    p=line.split()
    if len(p)<6 or p[0]=="NaN":
        continue
    rows.append([float(x) for x in p[:5]] + [p[5]])
if not rows:
    print("stats: no successful samples")
    raise SystemExit
cols=list(zip(*[r[:5] for r in rows]))
names=["dns","connect","tls","ttfb","total"]
codes={}
for r in rows:
    codes[r[5]]=codes.get(r[5],0)+1
print(f"ok={len(rows)} codes={codes}")
for n,c in zip(names, cols):
    ms=[x*1000 for x in c]
    print(f"{n}_ms: min={min(ms):.2f} p50={st.median(ms):.2f} avg={st.fmean(ms):.2f} p95={sorted(ms)[max(0,int(len(ms)*0.95)-1)]:.2f} max={max(ms):.2f}")
PY
  rm -f "$tmp"
}

measure_tcp() {
  local host="$1" port="$2"
  log ""
  log "=== TCP $host:$port ==="
  if command -v nc >/dev/null 2>&1; then
    local tmp; tmp="$(mktemp)"
    for i in $(seq 1 "$ROUNDS"); do
      python3 - <<PY >>"$tmp"
import socket, time
host, port = "$host", int("$port")
s=socket.socket(); s.settimeout(5)
t0=time.perf_counter()
try:
    s.connect((host, port)); dt=(time.perf_counter()-t0)*1000
    print(f"{dt:.3f}")
except Exception as e:
    print(f"ERR {e}")
finally:
    s.close()
PY
    done
    python3 - "$tmp" <<'PY' | tee -a "$REPORT"
import sys, statistics as st
vals=[]
for line in open(sys.argv[1]):
    line=line.strip()
    if line.startswith("ERR") or not line:
        continue
    vals.append(float(line))
print(f"tcp_connect_ms ok={len(vals)} " + (
  f"min={min(vals):.2f} p50={st.median(vals):.2f} avg={st.fmean(vals):.2f} max={max(vals):.2f}" if vals else "no data"))
PY
    rm -f "$tmp"
  else
    log "nc/python socket fallback unavailable"
  fi
}

measure_ws() {
  log ""
  log "=== WebSocket $WS_URL ==="
  python3 - <<'PY' | tee -a "$REPORT"
import asyncio, ssl, time, statistics as st
try:
    import websockets
except Exception as e:
    print(f"websockets not installed: {e}")
    raise SystemExit

URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
async def one():
    t0 = time.perf_counter()
    try:
        async with websockets.connect(URL, open_timeout=8, close_timeout=2) as ws:
            open_ms = (time.perf_counter()-t0)*1000
            # try a lightweight ping-ish round if server allows; else just open latency
            return open_ms, None
    except Exception as e:
        return None, str(e)

async def main():
    opens, errs = [], []
    for _ in range(10):
        o, e = await one()
        if o is None:
            errs.append(e)
        else:
            opens.append(o)
    if opens:
        print(f"ws_open_ms ok={len(opens)} min={min(opens):.2f} p50={st.median(opens):.2f} avg={st.fmean(opens):.2f} max={max(opens):.2f}")
    else:
        print("ws_open_ms: no success")
    if errs:
        print("ws_errors:", sorted(set(errs))[:3])

asyncio.run(main())
PY
}

{
  log "Polymarket latency probe"
  log "label=$LABEL ts=$TS"
  log "host=$(hostname) uname=$(uname -a)"
  log "public_ip=$(curl -4 -sS --max-time 8 ifconfig.me || curl -4 -sS --max-time 8 icanhazip.com || echo unknown)"
  log "resolver_check:"
  for h in clob.polymarket.com gamma-api.polymarket.com polymarket.com ws-subscriptions-clob.polymarket.com; do
    ips=$(python3 - <<PY
import socket
host="$h"
try:
    print(",".join(sorted({ai[4][0] for ai in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)})))
except Exception as e:
    print(f"ERR:{e}")
PY
)
    log "  $h -> $ips"
  done

  measure_tcp clob.polymarket.com 443
  measure_tcp gamma-api.polymarket.com 443

  for item in "${HOSTS[@]}"; do
    name="${item%%|*}"
    url="${item#*|}"
    measure_http "$name" "$url"
  done

  # Optional WS if websockets present
  if python3 -c "import websockets" 2>/dev/null; then
    measure_ws
  else
    log ""
    log "=== WebSocket skipped (pip install websockets to enable) ==="
  fi

  log ""
  log "DONE report=$REPORT"
} 

echo "Wrote $REPORT"
