#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""收回善十一：词典主名 ≠ 正文采用词。只改讲记 English / Français 段。

用法: python3 fix_wholesome11.py [--apply]
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
    r"(^\*\*§\d+\*\*\s*\n\*\*中文\*\*\s*\n.*?\n)"
    r"(\*\*English\*\*\s*\n)(.*?)(\n)"
    r"(\*\*Français\*\*\s*\n)(.*?)(\n)"
    r"(\*\*Tiếng Việt\*\*)",
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


def sub_many(text: str, rules: list[tuple[str, str]]) -> str:
    for pat, repl in rules:
        text = re.sub(pat, repl, text)
    return text


# —— English ——
# 长串在前。shame/embarrassment 对子先于单独 shame。
EN_COMMON = [
    (r"the constantly ashamed-and-embarrassed monk", "the monk of constant conscience and sense of shame"),
    (r"shame-and-embarrassment", "conscience and sense of shame"),
    (r"shame and of embarrassment", "conscience and of sense of shame"),
    (r"shame and embarrassment", "conscience and sense of shame"),
    (r"shame or embarrassment", "conscience or sense of shame"),
    (r"lack of embarrassment", "shamelessness"),
    (r"Embarrassment \(apatrāpya\)", "Sense of shame (apatrāpya)"),
    (r"embarrassment \(apatrāpya\)", "sense of shame (apatrāpya)"),
    (r"\bembarrassment\b", "sense of shame"),
    (r"\bUnembarrassed\b", "Without a sense of shame"),
    # 精进
    (r"diligence / vigor", "vigor"),
    (r"Diligence / vigor", "Vigor"),
    (r"Vigor and diligence", "Vigor"),
    (r"vigor and diligence", "vigor"),
    (r"“vigor” and “diligence”", "“vigor”"),
    (r"diligence \(vīrya\)", "vigor (vīrya)"),
    (r"Namely diligence", "Namely vigor"),
    (r"strength of diligence", "strength of vigor"),
    (r"objects of diligence", "objects of vigor"),
    (r"nature of diligence", "nature of vigor"),
    (r"mind of diligence", "mind of vigor"),
    (r"Through diligence", "Through vigor"),
    (r"function of diligence", "function of vigor"),
    (r"power of “diligence”", "power of “vigor”"),
    (r"Such diligence", "Such vigor"),
    (r"also diligence and", "also vigor and"),
    (r"power of diligence and", "power of vigor and"),
    (r"urges diligence", "urges vigor"),
    (r"the second, “diligence”", "the second, “vigor”"),
    (r"inspire “diligence,", "inspire “vigor,"),
    (r"2\. Diligence\b", "2. Vigor"),
    (r"2\. diligence\b", "2. vigor"),
    (r"“diligence”", "“vigor”"),
    # 无瞋 / 旧闭式
    (r"\bNon-aversion\b", "Non-hatred"),
    (r"\bnon-aversion\b", "non-hatred"),
    (r"\bnongreed\b", "noncraving"),
    (r"\bnonhatred\b", "non-hatred"),
    (r"\bnondelusion\b", "non-delusion"),
    # 行舍
    (r"Equanimity of formations", "Indifference"),
    (r"equanimity of formations", "indifference"),
    (r"equanimity in formations", "indifference"),
    (r"equanimity in activity", "indifference"),
    # 不放逸
    (r"\bNon-negligence\b", "Vigilance"),
    (r"\bnon-negligence\b", "vigilance"),
    (r"\bnon-heedlessness\b", "vigilance"),
    # 轻安
    (r"serenity / ease", "serenity"),
    (r"lightness-and-ease", "serenity"),
    # 惭 标题 / 括注
    (r"Shame \(hrī\)", "Conscience (hrī)"),
    (r"shame \(hrī\)", "conscience (hrī)"),
    (r"the third, “shame”", "the third, “conscience”"),
    (r"“Shame”", "“Conscience”"),
    (r"“shame”", "“conscience”"),
    (r"3\. Shame\b", "3. Conscience"),
    (r"conscience and shame\b", "conscience and sense of shame"),
    (r"(\x00W\d+\x00) and shame\b", r"\1 and sense of shame"),
    (r"lack of conscience and lack of sense of shame", "lack of conscience and shamelessness"),
]


def fix_en(text: str, lec: int) -> str:
    text, wikis = protect(text)
    text = sub_many(text, EN_COMMON)
    # 保护已收成的 sense of shame，再收第 7–10 讲残留 shame（惭主名）
    text = re.sub(r"sense of shame", "\x00SOS\x00", text, flags=re.I)
    if 7 <= lec <= 10:
        text = re.sub(r"\bShame\b", "Conscience", text)
        text = re.sub(r"\bshame\b", "conscience", text)
    text = text.replace("\x00SOS\x00", "sense of shame")
    return restore(text, wikis)


# —— Français ——
FR_COMMON = [
    # 无瞋 / 无贪 / 无痴（先处理冠词阴阳性）
    (r"\bNon-aversion\b", "Non-haine"),
    (r"\bnon-aversion\b", "non-haine"),
    (r"\bnon-avidité\b", "non-convoitise"),
    (r"du non-égarement", "de la non-ignorance"),
    (r"Du non-égarement", "De la non-ignorance"),
    (r"le « non-égarement »", "la « non-ignorance »"),
    (r"Le « non-égarement »", "La « non-ignorance »"),
    (r"le non-égarement", "la non-ignorance"),
    (r"Le non-égarement", "La non-ignorance"),
    (r"Non-égarement", "Non-ignorance"),
    (r"non-égarement", "non-ignorance"),
    # 轻安
    (r"l’aisance / souplesse", "la flexibilité"),
    (r"l'aisance / souplesse", "la flexibilité"),
    (r"aisance / souplesse", "flexibilité"),
    (r"8\. Souplesse\b", "8. Flexibilité"),
    (r"la souplesse", "la flexibilité"),
    (r"« la souplesse »", "« la flexibilité »"),
    (r"\bSouplesse\b", "Flexibilité"),
    (r"\bsouplesse\b", "flexibilité"),
    # 不放逸
    (r"\bNon-négligence\b", "Vigilance"),
    (r"\bnon-négligence\b", "vigilance"),
    # 第 8 讲总表更旧的词
    (r"légèreté-aisance", "flexibilité"),
    (r"non-insouciance", "vigilance"),
    (r"l’équanimité dans l’activité", "l’équanimité des formations"),
    (r"l'équanimité dans l’activité", "l’équanimité des formations"),
    (r"l’équanimité dans les formations", "l’équanimité des formations"),
]


FR_VIGUEUR = [
    (r"de la « vigueur »", "de l’« énergie »"),
    (r"de la vigueur", "de l’énergie"),
    (r"la « vigueur »", "l’« énergie »"),
    (r"« la vigueur »", "« l’énergie »"),
    (r"La vigueur", "L’énergie"),
    (r"la vigueur", "l’énergie"),
    (r"Les objets de l’énergie", "Les objets de l’énergie"),
    (r"2\. La vigueur", "2. L’énergie"),
    (r"2\. la vigueur", "2. l’énergie"),
    (r"Une telle vigueur", "Une telle énergie"),
    (r"une telle vigueur", "une telle énergie"),
    (r"vigueur \(vīrya\)", "énergie (vīrya)"),
    (r"vraie vigueur", "vraie énergie"),
    (r"apparence de vigueur", "apparence d’énergie"),
    (r"comme vigueur", "comme énergie"),
    (r", vigueur,", ", énergie,"),
    (r"« foi », vigueur,", "« foi », énergie,"),
    (r"patience, vigueur,", "patience, énergie,"),
    (r"\bvigueur\b", "énergie"),
]

FR_DILIGENCE = [
    (r"l’énergie et la diligence", "l’énergie"),
    (r"« l’énergie » et « la diligence »", "« l’énergie »"),
    (r"la diligence \(vīrya\)", "l’énergie (vīrya)"),
    (r"diligence \(vīrya\)", "énergie (vīrya)"),
    (r"force de la diligence", "force de l’énergie"),
]


def fix_fr(text: str, lec: int) -> str:
    text, wikis = protect(text)
    text = sub_many(text, FR_COMMON)

    # 保护副词 / 日常
    text = text.replace("vigueur juvénile", "\x00VJ\x00")
    text = text.replace("avec vigueur", "\x00AV\x00")
    if 7 <= lec <= 22:
        text = sub_many(text, FR_VIGUEUR)
        text = sub_many(text, FR_DILIGENCE)
    # L6 六度
    if lec in (4, 6):
        # L4：名词「sa vigueur dans les préceptes」= 精进；avec vigueur 已保护
        text = text.replace("sa vigueur dans les préceptes", "son énergie dans les préceptes")
        text = text.replace("la vigueur et la concentration", "l’énergie et la concentration")
        text = text.replace("la vigueur et le dhyāna", "l’énergie et le dhyāna")
    text = text.replace("\x00VJ\x00", "vigueur juvénile")
    text = text.replace("\x00AV\x00", "avec vigueur")

    # 惭 / 愧两阶段。先把愧侧 pudeur/embarras 收成占位，再把对子和惭侧 honte 收成 pudeur。
    if 7 <= lec <= 10:
        decence_first = [
            (r"Réserve / pudeur devant autrui", "\x00DEC\x00"),
            (r"réserve / pudeur devant autrui", "\x00DEC\x00"),
            (r"pudeur \(apatrāpya\)", "\x00DEC\x00 (apatrāpya)"),
            (r"Cette « pudeur »", "Cette « \x00DEC\x00 »"),
            (r"cette « pudeur »", "cette « \x00DEC\x00 »"),
            (r"Telle est la « pudeur »", "Telle est la « \x00DEC\x00 »"),
            (r"Lorsque la « pudeur »", "Lorsque la « \x00DEC\x00 »"),
            (r"la « pudeur »", "la « \x00DEC\x00 »"),
            (r"« pudeur »", "« \x00DEC\x00 »"),
            (r"facteur mental de la pudeur", "facteur mental de la \x00DEC\x00"),
            (r"Avoir de la pudeur", "Avoir de la \x00DEC\x00"),
            (r"de la pudeur devant", "de la \x00DEC\x00 devant"),
            (r"pudeur devant les fautes", "\x00DEC\x00 devant les fautes"),
            (r"l’absence de pudeur", "l’indécence"),
            (r"absence de pudeur", "indécence"),
            (r"l’embarras", "la \x00DEC\x00"),
            (r"\bembarras\b", "\x00DEC\x00"),
            (r"honteux et pudique", "pudique et décent"),
        ]
        text = sub_many(text, decence_first)
        pairs = [
            (r"honte-et-pudeur", "pudeur-et-\x00DEC\x00"),
            (r"honte et de la pudeur", "pudeur et de la \x00DEC\x00"),
            (r"honte et de pudeur", "pudeur et de \x00DEC\x00"),
            (r"honte et la pudeur", "pudeur et la \x00DEC\x00"),
            (r"la honte et la pudeur", "la pudeur et la \x00DEC\x00"),
            (r"de la honte et de la pudeur", "de la pudeur et de la \x00DEC\x00"),
            (r"honte et pudeur", "pudeur et \x00DEC\x00"),
            (r"honte ni pudeur", "pudeur ni \x00DEC\x00"),
            (r"cette honte et cette pudeur", "cette pudeur et cette \x00DEC\x00"),
            (r"la honte s’élève, la pudeur s’élève", "la pudeur s’élève, la \x00DEC\x00 s’élève"),
        ]
        text = sub_many(text, pairs)
        text = text.replace("a honte des", "\x00AHONTE\x00")
        honte_rules = [
            (r"l’absence de honte", "l’impudeur"),
            (r"absence de honte", "impudeur"),
            (r"Honte \(hrī\)", "Pudeur (hrī)"),
            (r"honte \(hrī\)", "pudeur (hrī)"),
            (r"3\. Honte\b", "3. Pudeur"),
            (r"La « honte »", "La « pudeur »"),
            (r"la « honte »", "la « pudeur »"),
            (r"« honte »", "« pudeur »"),
            (r"\bHonte\b", "Pudeur"),
            (r"\bhonte\b", "pudeur"),
        ]
        text = sub_many(text, honte_rules)
        text = text.replace("\x00AHONTE\x00", "a honte des")
        text = text.replace("\x00DEC\x00", "décence")

    # 第 17–19 讲：honte 残留 = 愧
    if lec >= 17:
        text = re.sub(r"(\x00W\d+\x00) et de honte", r"\1 et de décence", text)
        text = text.replace("pudeur et de honte", "pudeur et de décence")
        text = text.replace("conscience et de honte", "pudeur et de décence")
        text = text.replace("l’absence de honte", "l’indécence")
        text = text.replace("absence de honte", "indécence")

    return restore(text, wikis)


def process_file(path: pathlib.Path, lec: int) -> tuple[str, int]:
    raw = path.read_text(encoding="utf-8")
    nchg = 0

    def repl(m: re.Match) -> str:
        nonlocal nchg
        head, en_h, en, mid, fr_h, fr, mid2, vi_h = m.groups()
        new_en = fix_en(en, lec)
        new_fr = fix_fr(fr, lec)
        if new_en != en or new_fr != fr:
            nchg += 1
        return f"{head}{en_h}{new_en}{mid}{fr_h}{new_fr}{mid2}{vi_h}"

    new = SEC_RE.sub(repl, raw)
    return new, nchg


def main() -> None:
    total_sec = 0
    for i in range(1, 23):
        p = LEC / f"Hundred Dharmas NO.{i}.md"
        new, n = process_file(p, i)
        total_sec += n
        if n and APPLY:
            p.write_text(new, encoding="utf-8")
        print(f"L{i:2d}  改了 {n:3d} 段{'  (written)' if APPLY and n else ''}")
    print(f"合计 {total_sec} 段" + (" — 已写入" if APPLY else " — dry-run，加 --apply 才写"))


if __name__ == "__main__":
    main()
