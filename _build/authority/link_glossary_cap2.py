#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全书四语：已有词条、语境合适则挂链；同一语种同一段同一词条最多 2 次。

不剥开已有链接（保留 resolve / 三摩地 等显示）。
先把第 3 次起的旧链收回纯文本，再按词长降序补挂。

用法: python3 link_glossary_cap2.py [--apply]
"""
from __future__ import annotations

import pathlib
import re
import sys
from collections import Counter, defaultdict

try:
    import opencc

    ZH_CC = [opencc.OpenCC(cfg) for cfg in ("s2tw", "s2t")]
except Exception:
    ZH_CC = []

VAULT = pathlib.Path(__file__).resolve().parents[2]
GLOSS = VAULT / "Glossary"
LEC = VAULT / "Hundred Dharmas"
APPLY = "--apply" in sys.argv
MAX_PER = 2

FOLDERS = {"zh": "Chinese", "en": "English", "fr": "Français", "vi": "TiếngViệt"}
WIKI_RE = re.compile(r"\[\[Glossary/([^\]|/]+)/([^\]|]+)\|([^\]]+)\]\]")
SEC_RE = re.compile(
    r"(^\*\*§\d+\*\*\s*\n\*\*中文\*\*\s*\n)(.*?)(\n)"
    r"(\*\*English\*\*\s*\n)(.*?)(\n)"
    r"(\*\*Français\*\*\s*\n)(.*?)(\n)"
    r"(\*\*Tiếng Việt\*\*\n)(.*?)(?=\n---|\n\*\*§|\Z)",
    re.S | re.M,
)
FM_RE = re.compile(r"^---\n(.*?)\n---", re.S)
WORD = r"A-Za-zÀ-ɏĀ-ɏ\u1E00-\u1EFF\u0300-\u036FāīūṛṃḥṅñṭḍṇśṣạảãáàăắằẵẳặâấầẫẩậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđĐ"
BOUND_L = rf"(?<![{WORD}-])"
BOUND_R = rf"(?![{WORD}-])"

# 短词 / 日常词：不新挂（专段里已有的保留，只受 2 次上限）
SKIP_ZH = {
    "定", "念", "欲", "受", "想", "思", "触", "慧", "信", "寻", "伺",
    "害", "嫉", "悔", "眠", "贪", "瞋", "痴", "慢", "疑", "恨", "忿",
    "覆", "诳", "谄", "憍", "恼", "悭",
}
SKIP_EN = {
    "form", "mind", "pure", "envy", "desire", "contact", "memory", "resolve",
    "wisdom", "shame", "result", "feeling", "attention", "nature", "path",
    "activity", "seed", "seeds", "faith", "pride", "doubt", "anger", "ease",
    "vow", "name", "self", "empty", "emptiness", "anger (fury)", "rebirth",
}
SKIP_FR = {
    "foi", "désir", "contact", "forme", "esprit", "nature", "voie", "graine",
    "sagesse", "honte", "orgueil", "doute", "vide", "soi", "attention",
    "concentration", "sommeil", "pur", "impur", "sensation", "activité",
    "ignorance", "perception", "colère", "renaissance",
}
SKIP_VI = {
    "dục", "niệm", "định", "tư", "thọ", "tưởng", "tuệ", "xúc", "nghi",
    "não", "tín", "sân", "tham", "si", "hận", "hối", "mạn", "phẫn",
    "phú", "kiêu", "xan", "tật", "tàm", "quý", "hại", "tầm", "tứ",
    "miên", "sắc", "tâm", "ngã", "không", "tướng", "nghiệp",
}


def load_glossary():
    """lang -> list[(surface, filename)] 按 surface 长度降序，同 surface 留长文件名。"""
    by_lang: dict[str, dict[str, str]] = {k: {} for k in FOLDERS}

    def add(lang: str, surface: str, filename: str):
        surface = surface.strip()
        if not surface:
            return
        if lang == "zh":
            if len(surface) < 2:
                return
        else:
            if len(surface) < 3:
                return
        prev = by_lang[lang].get(surface)
        if prev is None or len(filename) >= len(prev):
            by_lang[lang][surface] = filename

    for lang, folder in FOLDERS.items():
        d = GLOSS / folder
        if not d.is_dir():
            continue
        for p in d.glob("*.md"):
            raw = p.read_text(encoding="utf-8")
            filename = p.stem
            add(lang, filename, filename)
            hm = re.search(r"^#\s+(.+)$", raw, re.M)
            if hm:
                add(lang, hm.group(1).strip(), filename)
            aliases = []
            m = FM_RE.match(raw)
            if m:
                am = re.search(r"^aliases:\s*\n((?:  - .+\n)*)", m.group(1), re.M)
                if am:
                    aliases = re.findall(r"- (.+)", am.group(1))
            for a in aliases:
                a = a.strip()
                # 短梵语（moha、kleśa）易误伤；长或带连字符的（ālaya-vijñāna）无歧义
                if re.search(r"[āīūṛṃḥṅñṭḍṇśṣḱ]", a) and " " not in a and "-" not in a and len(a) < 6:
                    continue
                add(lang, a, filename)
            # 三自性等：正文常略「性」
            if lang == "zh" and filename.endswith("性") and len(filename) >= 4:
                add("zh", filename[:-1], filename)
                for cc in ZH_CC:
                    add("zh", cc.convert(filename[:-1]), filename)
            pm = re.match(r"^(.+?)\s+\((.+)\)$", filename)
            if pm:
                prefix, inner = pm.group(1).strip(), pm.group(2).strip()
                skip = {"zh": SKIP_ZH, "en": SKIP_EN, "fr": SKIP_FR, "vi": SKIP_VI}[lang]
                if len(prefix) >= 6 and prefix.lower() not in skip and prefix not in skip:
                    add(lang, prefix, filename)
                if (
                    inner
                    and inner.lower() not in skip
                    and inner not in skip
                    and (" " in inner or "-" in inner or len(inner) >= 8)
                    and not re.match(r"^(in|en|the|de|des|du|of)\b", inner, re.I)
                ):
                    add(lang, inner, filename)
            if lang == "zh":
                for cc in ZH_CC:
                    add("zh", cc.convert(filename), filename)
                    if hm:
                        add("zh", cc.convert(hm.group(1).strip()), filename)

    extras = [
        ("zh", "阿賴耶", "阿赖耶识"),
        ("zh", "阿赖耶", "阿赖耶识"),
        ("zh", "末那", "末那识"),
        ("zh", "遍計執", "遍计所执性"),
        ("zh", "遍计执", "遍计所执性"),
        ("en", "ālaya", "store consciousness"),
        ("fr", "ālaya", "conscience-réceptacle"),
        ("vi", "A-lại-da", "thức A-lại-da"),
        ("vi", "a-lại-da", "thức A-lại-da"),
        ("en", "Jingjie", "Master Jingjie"),
    ]
    for lang, surface, fn in extras:
        add(lang, surface, fn)

    out = {}
    for lang, mp in by_lang.items():
        items = sorted(mp.items(), key=lambda kv: (-len(kv[0]), kv[0]))
        out[lang] = items
    return out


def cap_existing(text: str, folder: str) -> tuple[str, int]:
    """同一词条第 3 次起收回显示文本。"""
    seen: Counter[str] = Counter()
    demoted = 0

    def repl(m: re.Match) -> str:
        nonlocal demoted
        fol, title, display = m.group(1), m.group(2), m.group(3)
        if fol != folder:
            return m.group(0)
        seen[title] += 1
        if seen[title] > MAX_PER:
            demoted += 1
            return display
        return m.group(0)

    return WIKI_RE.sub(repl, text), demoted


def existing_counts(text: str, folder: str) -> Counter:
    c: Counter = Counter()
    for m in WIKI_RE.finditer(text):
        if m.group(1) == folder:
            c[m.group(2)] += 1
    return c


_COMPILED: dict[str, tuple[re.Pattern, dict]] = {}


def _compile_lang(lang: str, surfaces: list[tuple[str, str]]) -> tuple[re.Pattern, dict] | None:
    skip = {"zh": SKIP_ZH, "en": SKIP_EN, "fr": SKIP_FR, "vi": SKIP_VI}[lang]
    if lang == "zh":
        usable = [(s, fn) for s, fn in surfaces if s not in skip]
        if not usable:
            return None
        pat = re.compile("|".join(re.escape(s) for s, _ in usable))
        return pat, {s: fn for s, fn in usable}
    usable = []
    seen = set()
    for surface, fn in surfaces:
        key = surface.lower()
        if key in skip or surface in skip:
            continue
        if key in seen:
            continue
        seen.add(key)
        usable.append((surface, fn))
    if not usable:
        return None
    pat = re.compile(
        BOUND_L + "(" + "|".join(re.escape(s) for s, _ in usable) + ")" + BOUND_R,
        re.I,
    )
    return pat, {s.lower(): fn for s, fn in usable}


def link_new(text: str, lang: str, surfaces: list[tuple[str, str]]) -> tuple[str, int]:
    folder = FOLDERS[lang]
    counts = existing_counts(text, folder)
    added = 0
    if lang not in _COMPILED:
        _COMPILED[lang] = _compile_lang(lang, surfaces)  # type: ignore
    compiled = _COMPILED[lang]
    if compiled is None:
        return text, 0
    pat, smap = compiled

    store: list[str] = []

    def prot(m: re.Match) -> str:
        store.append(m.group(0))
        return f"\x00W{len(store) - 1}\x00"

    work = WIKI_RE.sub(prot, text)

    def repl(m: re.Match) -> str:
        nonlocal added
        surface = m.group(0)
        fn = smap[surface.lower() if lang != "zh" else surface]
        if counts[fn] >= MAX_PER:
            return surface
        counts[fn] += 1
        added += 1
        return f"[[Glossary/{folder}/{fn}|{surface}]]"

    work = pat.sub(repl, work)

    def unprot(m: re.Match) -> str:
        return store[int(m.group(1))]

    return re.sub(r"\x00W(\d+)\x00", unprot, work), added


ADD_TALLY: Counter = Counter()
ADD_SAMPLES: list[str] = []


def process_file(path: pathlib.Path, surfaces: dict) -> tuple[str, dict]:
    raw = path.read_text(encoding="utf-8")
    stats = defaultdict(int)
    lec = path.name

    def repl(m: re.Match) -> str:
        zh_h, zh, z1, en_h, en, e1, fr_h, fr, f1, vi_h, vi = m.groups()
        bodies = {"zh": zh, "en": en, "fr": fr, "vi": vi}
        newb = {}
        for lang, body in bodies.items():
            folder = FOLDERS[lang]
            before = set(WIKI_RE.findall(body))
            capped, d = cap_existing(body, folder)
            linked, a = link_new(capped, lang, surfaces[lang])
            after = WIKI_RE.findall(linked)
            stats[f"{lang}_demote"] += d
            stats[f"{lang}_add"] += a
            if d or a:
                stats[f"{lang}_secs"] += 1
            if a:
                old_keys = {(fol, title, disp) for fol, title, disp in before}
                for fol, title, disp in after:
                    if (fol, title, disp) not in old_keys and fol == folder:
                        ADD_TALLY[(lang, title, disp)] += 1
                        if len(ADD_SAMPLES) < 80:
                            ADD_SAMPLES.append(f"{lec} {lang} [[{title}|{disp}]]")
            newb[lang] = linked
        return (
            f"{zh_h}{newb['zh']}{z1}{en_h}{newb['en']}{e1}"
            f"{fr_h}{newb['fr']}{f1}{vi_h}{newb['vi']}"
        )

    return SEC_RE.sub(repl, raw), stats


def main() -> None:
    print("加载词表…", flush=True)
    surfaces = load_glossary()
    print("词表:", {k: len(v) for k, v in surfaces.items()}, flush=True)
    grand = defaultdict(int)
    for i in range(1, 23):
        p = LEC / f"Hundred Dharmas NO.{i}.md"
        new, st = process_file(p, surfaces)
        for k, v in st.items():
            grand[k] += v
        if APPLY:
            p.write_text(new, encoding="utf-8")
        print(
            f"L{i:2d}  收回 {st['zh_demote']+st['en_demote']+st['fr_demote']+st['vi_demote']:4d}  "
            f"新挂 zh{st['zh_add']:3d} en{st['en_add']:3d} fr{st['fr_add']:3d} vi{st['vi_add']:3d}"
            + ("  written" if APPLY else "")
        )
    print(
        "合计收回",
        grand["zh_demote"] + grand["en_demote"] + grand["fr_demote"] + grand["vi_demote"],
        "新挂",
        {k: grand[k] for k in ("zh_add", "en_add", "fr_add", "vi_add")},
        "— 已写" if APPLY else "— dry-run",
        flush=True,
    )
    by_title: Counter = Counter()
    for (lang, title, _disp), n in ADD_TALLY.items():
        by_title[(lang, title)] += n
    print("\n新挂 Top 40（语种 词条）", flush=True)
    for (lang, title), n in by_title.most_common(40):
        print(f"  {n:4d}  {lang:2s}  {title}", flush=True)


if __name__ == "__main__":
    main()
