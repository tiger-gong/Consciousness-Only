#!/usr/bin/env python3
"""Split long lecture paragraphs, keeping four languages aligned.

Primary key: matching newline-units already parallel across ZH/EN/FR/VI.
Fallback: sentence split when a leftover unit is still too long.

Dry-run:  python3 _build/split_long_paras.py
Apply:    python3 _build/split_long_paras.py --apply
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

DIR = Path("/Users/uphold/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/Hundred Dharmas")

SEC_RE = re.compile(
    r'\*\*§(\d+)\*\*\s*\n'
    r'\*\*中文\*\*\s*\n(.*?)'
    r'\n\*\*English\*\*\s*\n(.*?)'
    r'\n\*\*Français\*\*\s*\n(.*?)'
    r'\n\*\*Tiếng Việt\*\*\s*\n(.*?)'
    r'(?=\n---|\n\*\*§|\Z)',
    re.S,
)
WIKI = re.compile(r'\[\[Glossary/[^|\]]+\|([^\]]+)\]\]')

THRESH = {**{i: 300 for i in range(1, 14)}, **{i: 260 for i in range(14, 23)}}
TARGET = 185
PACK_MAX = 250
MIN_PIECE = 70
HEADING_MAX = 28
UNIT_SENT_SPLIT = 300


def plain(s: str) -> str:
    return WIKI.sub(r'\1', s)


def nchars(s: str) -> int:
    return len(re.sub(r'\s', '', plain(s)))


def is_heading_line(s: str) -> bool:
    t = plain(s).strip()
    if not t:
        return True
    if nchars(t) <= HEADING_MAX and not re.search(r'[。！？.!?]', t):
        return True
    # lecture marker only
    if re.fullmatch(r'（第[一二三四五六七八九十]+講）', t):
        return True
    if re.fullmatch(r'\(Lecture [A-Za-z]+\)', t):
        return True
    return False


def zh_sents(s: str) -> list[str]:
    s = s.strip()
    parts = re.split(r'(?<=[。！？])', s)
    out, buf = [], ''
    for p in parts:
        if not p.strip():
            continue
        buf += p
        if buf.count('『') > buf.count('』') or buf.count('「') > buf.count('」'):
            continue
        out.append(buf)
        buf = ''
    if buf.strip():
        out.append(buf)
    return [x.strip() for x in out if x.strip()]


def west_sents(s: str) -> list[str]:
    s = s.strip()
    protect = [('e.g.', 'e§g§'), ('i.e.', 'i§e§'), ('etc.', 'et§c§')]
    tmp = s
    for a, b in protect:
        tmp = tmp.replace(a, b)
    parts = re.split(r'(?<=[.!?…])\s+(?=\S)', tmp)
    out = []
    for p in parts:
        for a, b in protect:
            p = p.replace(b, a)
        p = p.strip()
        if p:
            out.append(p)
    return out


def vi_sents(s: str) -> list[str]:
    return [p.strip() for p in re.split(r'(?<=[.!?…。！？])\s+', s.strip()) if p.strip()]


def map_cuts(src: list[str], dst: list[str], src_cuts: list[int]) -> list[int]:
    if not dst:
        return [0]
    if len(dst) == 1:
        return [0]
    src_lens = [nchars(x) for x in src]
    src_total = sum(src_lens) or 1
    src_cum, t = [], 0
    for ln in src_lens:
        t += ln
        src_cum.append(t)
    dst_lens = [nchars(x) for x in dst]
    dst_total = sum(dst_lens) or 1
    dst_cum, t = [], 0
    for ln in dst_lens:
        t += ln
        dst_cum.append(t)
    close = abs(len(src) - len(dst)) <= 2
    out = [0]
    for c in src_cuts[1:]:
        if close and 0 < c < len(dst):
            out.append(c)
            continue
        before = src_cum[c - 1]
        target = (before / src_total) * dst_total
        best_i, best_d = 1, 10**9
        for i, cum in enumerate(dst_cum[:-1], start=1):
            d = abs(cum - target)
            if d < best_d:
                best_d, best_i = d, i
        if best_i not in out:
            out.append(best_i)
    out = sorted({i for i in out if 0 <= i < len(dst)})
    if not out or out[0] != 0:
        out = [0] + [i for i in out if i]
    return out


def auto_cuts(sents: list[str]) -> list[int]:
    if len(sents) < 2:
        return [0]
    lens = [nchars(x) for x in sents]
    cuts = [0]
    acc = 0
    for i, ln in enumerate(lens):
        acc += ln
        if i == len(sents) - 1:
            break
        rest = sum(lens[i + 1:])
        if rest < MIN_PIECE:
            break
        if acc >= TARGET and rest >= MIN_PIECE:
            cuts.append(i + 1)
            acc = 0
    return cuts


def slice_join(sents: list[str], cuts: list[int], west: bool) -> list[str]:
    bounds = cuts + [len(sents)]
    out = []
    for a, b in zip(bounds, bounds[1:]):
        chunk = sents[a:b]
        out.append(' '.join(chunk) if west else ''.join(chunk))
    return out


def sentence_split_unit(zh: str, en: str, fr: str, vi: str) -> list[tuple[str, str, str, str]]:
    zs, es, fs, vs = zh_sents(zh), west_sents(en), west_sents(fr), vi_sents(vi)
    if len(zs) < 2:
        return [(zh, en, fr, vi)]
    cuts = auto_cuts(zs)
    if len(cuts) < 2:
        return [(zh, en, fr, vi)]
    z_parts = slice_join(zs, cuts, False)
    e_parts = slice_join(es, map_cuts(zs, es, cuts), True)
    f_parts = slice_join(fs, map_cuts(zs, fs, cuts), True)
    v_parts = slice_join(vs, map_cuts(zs, vs, cuts), True)
    n = len(z_parts)

    def pad(ps):
        ps = list(ps)
        if len(ps) < n:
            ps += [''] * (n - len(ps))
        if len(ps) > n:
            ps = ps[:n - 1] + [' '.join(ps[n - 1:])]
        return ps

    e_parts, f_parts, v_parts = pad(e_parts), pad(f_parts), pad(v_parts)
    out = []
    for z, e, f, v in zip(z_parts, e_parts, f_parts, v_parts):
        if out and (not e or not f or not v or nchars(z) < 45):
            pz, pe, pf, pv = out[-1]
            out[-1] = (pz + z, (pe + ' ' + e).strip(), (pf + ' ' + f).strip(), (pv + ' ' + v).strip())
        else:
            out.append((z, e, f, v))
    out = merge_mid_starts(out)
    return out if len(out) >= 2 else [(zh, en, fr, vi)]


def glue_headings(units: list[tuple[str, str, str, str]]) -> list[tuple[str, str, str, str]]:
    out: list[tuple[str, str, str, str]] = []
    i = 0
    while i < len(units):
        z, e, f, v = units[i]
        if is_heading_line(z) and i + 1 < len(units):
            nz, ne, nf, nv = units[i + 1]
            units[i + 1] = (z + '\n' + nz, e + '\n' + ne, f + '\n' + nf, v + '\n' + nv)
            i += 1
            continue
        out.append((z, e, f, v))
        i += 1
    return out


def starts_mid_sentence(s: str) -> bool:
    t = plain(s).lstrip()
    t = t.lstrip('«‹“"\'（(')
    if not t:
        return True
    return t[0].islower()


def pack_units(units: list[tuple[str, str, str, str]]) -> list[tuple[str, str, str, str]]:
    if not units:
        return []
    pieces: list[tuple[str, str, str, str]] = []
    cz, ce, cf, cv = units[0]
    for z, e, f, v in units[1:]:
        # Keep a short title/quote with the next unit even if slightly over PACK_MAX.
        if nchars(cz) < 80 or nchars(cz) + nchars(z) <= PACK_MAX or nchars(z) < MIN_PIECE:
            cz = cz + '\n' + z
            ce = ce + '\n' + e
            cf = cf + '\n' + f
            cv = cv + '\n' + v
        else:
            pieces.append((cz, ce, cf, cv))
            cz, ce, cf, cv = z, e, f, v
    pieces.append((cz, ce, cf, cv))
    return pieces


def merge_mid_starts(parts: list[tuple[str, str, str, str]]) -> list[tuple[str, str, str, str]]:
    """If EN/FR/VI of a later piece starts mid-sentence, glue it back."""
    if len(parts) < 2:
        return parts
    out = [parts[0]]
    for z, e, f, v in parts[1:]:
        if starts_mid_sentence(e) or starts_mid_sentence(f) or starts_mid_sentence(v):
            pz, pe, pf, pv = out[-1]
            out[-1] = (
                (pz + '\n' + z).strip(),
                (pe + ' ' + e).strip(),
                (pf + ' ' + f).strip(),
                (pv + ' ' + v).strip(),
            )
        else:
            out.append((z, e, f, v))
    return out


def split_block(zh: str, en: str, fr: str, vi: str, lec: int) -> list[tuple[str, str, str, str]] | None:
    if nchars(zh) < THRESH[lec]:
        return None
    zl, el, fl, vl = zh.split('\n'), en.split('\n'), fr.split('\n'), vi.split('\n')
    aligned = len(zl) == len(el) == len(fl) == len(vl)

    if aligned and len(zl) >= 2:
        units: list[tuple[str, str, str, str]] = []
        for z, e, f, v in zip(zl, el, fl, vl):
            if nchars(z) >= UNIT_SENT_SPLIT:
                units.extend(sentence_split_unit(z, e, f, v))
            else:
                units.append((z, e, f, v))
        units = glue_headings(units)
        pieces = pack_units(units)
    elif aligned and len(zl) == 1:
        pieces = sentence_split_unit(zh, en, fr, vi)
    else:
        pieces = sentence_split_unit(zh, en, fr, vi)

    pieces = merge_mid_starts(pieces)
    if len(pieces) < 2:
        return None
    return pieces


def format_block(n: int, zh: str, en: str, fr: str, vi: str) -> str:
    return (
        f"**§{n}**\n\n"
        f"**中文**\n{zh.strip()}\n\n"
        f"**English**\n{en.strip()}\n\n"
        f"**Français**\n{fr.strip()}\n\n"
        f"**Tiếng Việt**\n{vi.strip()}\n"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--from-lec', type=int, default=1)
    ap.add_argument('--to-lec', type=int, default=22)
    args = ap.parse_args()

    split_n = extra = 0
    for lec in range(args.from_lec, args.to_lec + 1):
        path = DIR / f"Hundred Dharmas NO.{lec}.md"
        text = path.read_text(encoding='utf-8')
        matches = list(SEC_RE.finditer(text))
        if not matches:
            continue
        preamble = text[:matches[0].start()]
        after = re.sub(r'^\s*---\s*', '', text[matches[-1].end():], count=1)
        new_blocks = []
        for m in matches:
            n = int(m.group(1))
            zh, en, fr, vi = [x.strip() for x in m.groups()[1:]]
            parts = split_block(zh, en, fr, vi, lec)
            if not parts:
                new_blocks.append((n, zh, en, fr, vi))
                continue
            split_n += 1
            extra += len(parts) - 1
            print(f"L{lec:02d} §{n:4d} {nchars(zh):4d}c → {len(parts)} "
                  f"{[nchars(p[0]) for p in parts]}")
            for j, (z, e, f, v) in enumerate(parts):
                print(f"    [{j+1}] ZH {plain(z).replace(chr(10),' / ')[:48]}")
                print(f"        EN {plain(e).replace(chr(10),' / ')[:48]}")
            for z, e, f, v in parts:
                new_blocks.append((n, z, e, f, v))

        if not args.apply:
            continue
        out = [preamble]
        for n, zh, en, fr, vi in new_blocks:
            out.append(format_block(n, zh, en, fr, vi))
            out.append("\n---\n\n")
        if after.strip():
            out.append(after.rstrip() + "\n")
        path.write_text(''.join(out).rstrip() + "\n", encoding='utf-8')

    print(f"\nsplit={split_n} extra_paras={extra}")
    if not args.apply:
        print("(dry-run; pass --apply to write)")


if __name__ == '__main__':
    main()
