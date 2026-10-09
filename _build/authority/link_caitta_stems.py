#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""遍行五 + 别境五主干挂链。不跑全库 link_lectures.py。

策略：
  - 先挂辨识度高的（胜解、三摩地、作意、智慧、带梵文括注的英文/法文）
  - 「」『』引号里的单字主名
  - 顿号列举、N、欲 / 1. desire
  - 第 7–8 讲专段对短词再放开（仍跳过五欲、念佛、禪定等）
  - 每条规则后重新保护 [[wiki]]，防止短词吃进刚挂的链

用法: python3 link_caitta_stems.py [--apply]
"""
from __future__ import annotations

import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parents[2]
LEC = VAULT / "Hundred Dharmas"
APPLY = "--apply" in sys.argv

WIKI_RE = re.compile(r"\[\[Glossary/[^\]]+\]\]")
SEC_RE = re.compile(
    r"(^\*\*§\d+\*\*\s*\n\*\*中文\*\*\s*\n)(.*?)(\n)"
    r"(\*\*English\*\*\s*\n)(.*?)(\n)"
    r"(\*\*Français\*\*\s*\n)(.*?)(\n)"
    r"(\*\*Tiếng Việt\*\*\n)(.*?)(?=\n---|\n\*\*§|\Z)",
    re.S | re.M,
)


def protect(text: str) -> tuple[str, list[str]]:
    store: list[str] = []

    def repl(m: re.Match) -> str:
        store.append(m.group(0))
        return f"\x00W{len(store) - 1}\x00"

    return WIKI_RE.sub(repl, text), store


def restore(text: str, store: list[str]) -> str:
    def repl(m: re.Match) -> str:
        return store[int(m.group(1))]

    return re.sub(r"\x00W(\d+)\x00", repl, text)


def wikify(folder: str, title: str, display: str) -> str:
    return f"[[Glossary/{folder}/{title}|{display}]]"


def apply_rules(text: str, folder: str, rules: list[tuple[str, str]]) -> str:
    for pat, title in rules:
        text, store = protect(text)

        def repl(m: re.Match, title=title) -> str:
            return wikify(folder, title, m.group(0))

        text = re.sub(pat, repl, text)
        text = restore(text, store)
    return text


# —— 全书：辨识度高 ——
ZH_GLOBAL = [
    (r"勝解", "胜解"),
    (r"胜解", "胜解"),
    (r"三摩地", "定"),
    (r"作意", "作意"),
    (r"智慧", "慧"),
]

# 引号内单字：只替换字，保留引号
ZH_QUOTED = [
    (r"(?<=[「『])欲(?=[」』])", "欲"),
    (r"(?<=[「『])念(?=[」』])", "念"),
    (r"(?<=[「『])定(?=[」』])", "定"),
    (r"(?<=[「『])慧(?=[」』])", "慧"),
    (r"(?<=[「『])觸(?=[」』])", "触"),
    (r"(?<=[「『])触(?=[」』])", "触"),
    (r"(?<=[「『])受(?=[」』])", "受"),
    (r"(?<=[「『])想(?=[」』])", "想"),
    (r"(?<=[「『])思(?=[」』])", "思"),
]

ZH_XINSUO = [
    (r"欲(?=心所)", "欲"),
    (r"念(?=心所)", "念"),
    (r"(?<![禪禅不])定(?=心所)", "定"),
    (r"(?<!智)慧(?=心所)", "慧"),
    (r"觸(?=心所)", "触"),
    (r"触(?=心所)", "触"),
    (r"受(?=心所)", "受"),
    (r"想(?=心所)", "想"),
    (r"思(?=心所)", "思"),
]

# 第 7–8 讲短词（跳过合成）
ZH_L78 = [
    (r"(?<![五六三])(?<![貪贪愛爱樂乐情])欲(?!界)(?!望)", "欲"),
    (r"(?<![失正憶忆惡恶一])念(?!佛)(?!誦)(?!诵)(?!頭)(?!头)", "念"),
    (r"(?<![禪禅決决一安入出不正在固確确無无滅灭想盡尽])定(?!業)(?!业)(?!義)(?!义)(?!力)(?!了)(?!報)(?!报)", "定"),
    (r"(?<!智)慧", "慧"),
    (r"(?<!接)(?<![味香味])觸(?!法)(?!覺)(?!觉)", "触"),
    (r"(?<!接)(?<![味香味])触(?!法)(?!觉)", "触"),
    (r"(?<!感)(?<!接)(?<!享)(?<!忍)受(?!到)(?!戒)(?!持)(?!苦)(?!傷)(?!伤)", "受"),
    (r"(?<!思)(?<!妄)想(?!法)(?!起)(?!像)(?!到)(?!念)", "想"),
    (r"(?<!意)思(?!惟)(?!維)(?!维)(?!想)(?!考)", "思"),
]

EN_GLOBAL = [
    (r"resolution \(decisive understanding\)", "resolution (decisive understanding)"),
    (r"attention \(mental engagement\)", "attention (mental engagement)"),
    (r"attention \(manaskāra\)", "attention (mental engagement)"),
    (r"feeling \(sensation\)", "feeling (sensation)"),
    (r"feeling \(vedanā\)", "feeling (sensation)"),
    (r"desire \(aspiration\)", "desire (aspiration)"),
    (r"desire \(chanda\)", "desire (aspiration)"),
    (r"resolve \(adhimokṣa\)", "resolution (decisive understanding)"),
    (r"memory \(smṛti\)", "memory"),
    (r"wisdom \(prajñā\)", "discernment"),
    (r"conception \(saṃjñā\)", "conceptualization"),
    (r"volition \(cetanā\)", "volition"),
    (r"contact \(sparśa\)", "contact"),
    (r"\bconceptualization\b", "conceptualization"),
    (r"\bConceptualization\b", "conceptualization"),
    (r"\bdiscernment\b", "discernment"),
    (r"\bDiscernment\b", "discernment"),
    (r"\bsamādhi\b", "samādhi"),
    (r"\bSamādhi\b", "samādhi"),
]

EN_QUOTED = [
    (r"(?<=[“\"])desire(?=[”\"])", "desire (aspiration)"),
    (r"(?<=[“\"])memory(?=[”\"])", "memory"),
    (r"(?<=[“\"])wisdom(?=[”\"])", "discernment"),
    (r"(?<=[“\"])contact(?=[”\"])", "contact"),
    (r"(?<=[“\"])volition(?=[”\"])", "volition"),
    (r"(?<=[“\"])resolve(?=[”\"])", "resolution (decisive understanding)"),
]

EN_L78 = [
    (r"\bresolve\b", "resolution (decisive understanding)"),
    (r"\bResolve\b", "resolution (decisive understanding)"),
    (r"(?<!five )(?<!Five )(?<!unwholesome )(?<!wholesome )\bdesire\b(?! realm)(?!-realm)(?!s\b)", "desire (aspiration)"),
    (r"\bDesire\b(?! realm)", "desire (aspiration)"),
    (r"\bmemory\b", "memory"),
    (r"\bMemory\b", "memory"),
    (r"\bvolition\b", "volition"),
    (r"\bVolition\b", "volition"),
    (r"\bcontact\b", "contact"),
    (r"\bContact\b", "contact"),
]

FR_GLOBAL = [
    (r"résolution \(compréhension décisive\)", "résolution (compréhension décisive)"),
    (r"compréhension décisive \(adhimokṣa\)", "résolution (compréhension décisive)"),
    (r"\bcompréhension décisive\b", "résolution (compréhension décisive)"),
    (r"attention \(application de l’esprit\)", "attention (application de l'esprit)"),
    (r"attention \(application de l'esprit\)", "attention (application de l'esprit)"),
    (r"attention \(manaskāra\)", "attention (application de l'esprit)"),
    (r"attention mémorielle", "attention mémorielle (smṛti)"),
    (r"attention / mémoire \(smṛti\)", "attention mémorielle (smṛti)"),
    (r"sensation \(vedanā\)", "sensation (vedanā)"),
    (r"perception \(notion\)", "perception (notion)"),
    (r"volition \(cetanā\)", "volition (cetanā)"),
    (r"désir \(aspiration\)", "désir (aspiration)"),
    (r"désir \(chanda\)", "désir (aspiration)"),
    (r"concentration \(samādhi\)", "concentration (samādhi)"),
    (r"sagesse \(discernement\)", "sagesse (discernement)"),
    (r"sagesse \(prajñā\)", "sagesse (discernement)"),
    (r"\bsamādhi\b", "concentration (samādhi)"),
]

FR_L78 = [
    (r"(?<!cinq )(?<!Cinq )\bdésir\b(?!s\b)", "désir (aspiration)"),
    (r"\bDésir\b", "désir (aspiration)"),
    (r"\bvolition\b", "volition (cetanā)"),
    (r"\bVolition\b", "volition (cetanā)"),
]

VI_GLOBAL = [
    (r"thắng giải", "thắng giải"),
    (r"Thắng giải", "thắng giải"),
    (r"tam-ma-địa", "định"),
    (r"tác ý", "tác ý"),
    (r"Tác ý", "tác ý"),
]

VI_L78 = [
    (r"\bniệm\b", "niệm"),
    (r"\bNiệm\b", "niệm"),
    (r"\bdục\b", "dục"),
    (r"\bDục\b", "dục"),
    (r"\bđịnh\b", "định"),
    (r"\bĐịnh\b", "định"),
    (r"\btuệ\b", "tuệ"),
    (r"\bTuệ\b", "tuệ"),
    (r"\bxúc\b", "xúc"),
    (r"\bXúc\b", "xúc"),
    (r"\bthọ\b", "thọ"),
    (r"\bThọ\b", "thọ"),
    (r"\btưởng\b", "tưởng"),
    (r"\bTưởng\b", "tưởng"),
    (r"(?<![A-Za-zÀ-ỹ])tư(?![A-Za-zÀ-ỹ])", "tư"),
    (r"(?<![A-Za-zÀ-ỹ])Tư(?![A-Za-zÀ-ỹ])", "tư"),
]


def rules_for(lang: str, lec: int) -> list[tuple[str, str]]:
    if lang == "zh":
        r = ZH_GLOBAL + ZH_QUOTED + ZH_XINSUO
        if lec in (7, 8):
            r = r + ZH_L78
        return r
    if lang == "en":
        r = EN_GLOBAL + EN_QUOTED
        if lec in (7, 8):
            r = r + EN_L78
        return r
    if lang == "fr":
        r = FR_GLOBAL[:]
        if lec in (7, 8):
            r = r + FR_L78
        return r
    if lang == "vi":
        r = VI_GLOBAL[:]
        if lec in (7, 8):
            r = r + VI_L78
        return r
    return []


def process_file(path: pathlib.Path, lec: int) -> tuple[str, dict[str, int]]:
    raw = path.read_text(encoding="utf-8")
    counts = {"zh": 0, "en": 0, "fr": 0, "vi": 0}

    def repl(m: re.Match) -> str:
        zh_h, zh, z1, en_h, en, e1, fr_h, fr, f1, vi_h, vi = m.groups()
        nzh = apply_rules(zh, "Chinese", rules_for("zh", lec))
        nen = apply_rules(en, "English", rules_for("en", lec))
        nfr = apply_rules(fr, "Français", rules_for("fr", lec))
        nvi = apply_rules(vi, "TiếngViệt", rules_for("vi", lec))
        if nzh != zh:
            counts["zh"] += 1
        if nen != en:
            counts["en"] += 1
        if nfr != fr:
            counts["fr"] += 1
        if nvi != vi:
            counts["vi"] += 1
        return f"{zh_h}{nzh}{z1}{en_h}{nen}{e1}{fr_h}{nfr}{f1}{vi_h}{nvi}"

    return SEC_RE.sub(repl, raw), counts


def main() -> None:
    print(f"{'':>4} {'zh':>4} {'en':>4} {'fr':>4} {'vi':>4}")
    tot = {"zh": 0, "en": 0, "fr": 0, "vi": 0}
    for i in range(1, 23):
        p = LEC / f"Hundred Dharmas NO.{i}.md"
        new, c = process_file(p, i)
        for k in tot:
            tot[k] += c[k]
        if any(c.values()) and APPLY:
            p.write_text(new, encoding="utf-8")
        print(
            f"L{i:2d}  {c['zh']:4d} {c['en']:4d} {c['fr']:4d} {c['vi']:4d}"
            + ("  written" if APPLY and any(c.values()) else "")
        )
    print(f"段   {tot['zh']:4d} {tot['en']:4d} {tot['fr']:4d} {tot['vi']:4d}" + (" — 已写" if APPLY else " — dry-run"))


if __name__ == "__main__":
    main()
