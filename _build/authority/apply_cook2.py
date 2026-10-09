#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第二遍：统一英文散文中残留的旧术语（词条释义 + 讲记 English 段）。

第一遍只改了词条名与链接；此遍处理释义与正文里未加链接的裸术语。
刻意保留者见文末 KEEP 说明。

用法:  python3 apply_cook2.py [--apply]
"""
from __future__ import annotations

import pathlib
import re
import sys

VAULT = pathlib.Path(__file__).resolve().parents[2]
APPLY = '--apply' in sys.argv

# 顺序敏感：长串在前，防止被短串先吃掉
RULES: list[tuple[str, str]] = [
    # —— 四分 ——
    (r're-aware portion \(awareness of self-awareness\)', 'part that authenticates self-authentication'),
    (r're-aware portion', 'part that authenticates self-authentication'),
    (r'self-aware portion', 'self-authenticating part'),
    (r'perceiving portion \(seeing portion\)', 'seeing part'),
    (r'perceiving portion', 'seeing part'),
    (r'image portion \(seen portion\)', 'seen part'),
    (r'image portion', 'seen part'),
    (r'seen portion', 'seen part'),
    (r'seeing portion', 'seeing part'),
    (r'four portions of the substance of consciousness', 'four parts of consciousness'),
    (r'\bfour portions\b', 'four parts'),
    (r'\bportions\b', 'parts'),
    (r'\bportion\b', 'part'),

    # —— 心所六位 ——
    (r'universally active mental factors', 'universal mental activities'),
    (r'universally active mental factor', 'universal mental activity'),
    (r'\buniversally active\b', 'universal'),
    (r'object-specific mental factors', 'mental activities with specific objects'),
    (r'object-specific mental factor', 'mental activity with specific objects'),
    (r'\bobject-specific\b', 'with specific objects'),
    (r'indeterminate mental factors', 'nondetermined mental activities'),
    (r'indeterminate mental factor', 'nondetermined mental activity'),
    (r'afflictive mental factors', 'passions'),
    (r'afflictive mental factor', 'passion'),
    (r'\bafflictive\b', 'of the passions'),
    (r'mental factors', 'mental activities'),
    (r'mental factor', 'mental activity'),

    # —— 烦恼 ——
    (r'root afflictions', 'fundamental passions'),
    (r'secondary afflictions', 'secondary passions'),
    (r'\bafflictions\b', 'passions'),
    (r'\baffliction\b', 'passion'),

    # —— 有漏无漏 / 异熟 / 现行 ——
    (r'\buncontaminated\b', 'pure'),
    (r'\bcontaminated\b', 'impure'),
    (r'maturation consciousness', 'consciousness as retribution'),
    (r'\bmaturation\b', 'retribution'),
    (r'\bripened\b', 'retributive'),
    (r'present activity \(manifestation\)', 'activity'),
    (r'present activity', 'activity'),

    # —— 八识 ——
    (r'storehouse[- ]consciousness', 'store consciousness'),
    (r'manas-consciousness', 'manas'),
    (r'eye-consciousness', 'visual consciousness'),
    (r'ear-consciousness', 'auditory consciousness'),
    (r'nose-consciousness', 'olfactory consciousness'),
    (r'tongue-consciousness', 'gustatory consciousness'),
    (r'body-consciousness', 'tactile consciousness'),

    # —— 三性 / 二障 / 四缘 ——
    (r'perfectly accomplished nature', 'perfected nature'),
    (r'\bperfectly accomplished\b', 'perfected'),
    (r'other-dependent nature', 'nature dependent on others'),
    (r'\bother-dependent\b', 'dependent on others'),
    (r'hindrance of afflictions', 'obstacle of the passions'),
    (r'hindrance to the knowable', 'obstacle to the knowable'),
    (r'two hindrances', 'two obstacles'),
    (r'\bhindrances\b', 'obstacles'),
    (r'\bhindrance\b', 'obstacle'),
    (r'object-as-condition', 'condition as perceptual object'),
    (r'predominant condition', 'dominant condition'),
    (r'immediate-antecedent condition', 'immediately antecedent condition'),

    # —— 心所别名 ——
    (r'equanimity of formations', 'indifference'),
    (r'equanimity \(of formations\)', 'indifference'),
    (r'feeling of equanimity', 'feeling of indifference'),
    (r'pliancy \(ease\)', 'serenity'),
    (r'\bpliancy\b', 'serenity'),
    (r'conceit \(pride\)', 'pride'),
    (r'\bconceit\b', 'pride'),
    (r'\bnon-greed\b', 'noncraving'),
    (r'\bgreed\b', 'craving'),
    (r'\bstinginess\b', 'avarice'),
    (r'\bhaughtiness\b', 'vanity'),
    (r'\brestlessness\b', 'agitation'),
    (r'\blaziness\b', 'indolence'),
    (r'laxity \(heedlessness\)', 'negligence'),
    (r'\blaxity\b', 'negligence'),
    (r'\bdeception\b', 'deceit'),
    (r'\bnon-harming\b', 'harmlessness'),
    (r'\bresentment\b', 'hostility'),
    (r'spite \(vexation\)', 'vexation'),
    (r'\bspite\b', 'vexation'),
    (r'lack of faith', 'unbelief'),
    (r'non-introspection \(incorrect knowing\)', 'incorrect knowing'),
    (r'\bnon-introspection\b', 'incorrect knowing'),
    (r'\bnon-embarrassment\b', 'shamelessness'),
    (r'initial inquiry', 'applied thought'),
    (r'sustained scrutiny', 'sustained thought'),
    # 别境之「念」：仅在与其余四法并列时替换，避免误伤「念佛／正念」
    (r'mindfulness \(smṛti\)', 'memory (smṛti)'),
    # 定：避开「禅定 meditative concentration」
    (r'(?<!meditative )\bconcentration\b', 'samādhi'),

    # —— 其它 ——
    (r'birth-and-death', 'birth and death'),
    (r'(?<!true )\bsuchness\b', 'true suchness'),
]
COMPILED = [(re.compile(p), r) for p, r in RULES]

# 刻意保留，不纳入替换：
KEEP = """
  wholesome karma / unwholesome karma / wholesome roots  —— 善业、不善业、善根，非「善心所」范畴
  mindfulness of the Buddha / right mindfulness          —— 念佛、正念，非别境之「念」
  Great Vehicle / Lesser Vehicle                         —— 保留义译，梵文已于行内以括号给出
  meditative concentration                               —— 禅定，独立词条
"""

EXPLAIN = re.compile(r'(?ms)^(## Explanation（English）\n)(.*?)(?=^## |\Z)')
EN_BLOCK = re.compile(r'(?m)^(\*\*English\*\*\n)(.*?)(?=\n\*\*Français\*\*)', re.S)

changes: list[tuple[str, str, str]] = []


def swap(seg: str, where: str) -> str:
    """跳过 wiki 链接内部，替换裸术语。"""
    parts = re.split(r'(\[\[[^\]]*\]\])', seg)
    for i, piece in enumerate(parts):
        if piece.startswith('[['):
            continue
        for rx, rep in COMPILED:
            def record(m):
                changes.append((where, m.group(0), rep))
                return rep
            piece = rx.sub(record, piece)
        parts[i] = piece
    return ''.join(parts)


def main() -> None:
    touched = 0
    for f in sorted((VAULT / 'Glossary' / 'English').glob('*.md')):
        raw = f.read_text(encoding='utf-8')
        out = EXPLAIN.sub(lambda m: m.group(1) + swap(m.group(2), f.stem), raw)
        if out != raw:
            touched += 1
            if APPLY:
                f.write_text(out, encoding='utf-8')
    for f in sorted((VAULT / 'Hundred Dharmas').glob('Hundred Dharmas NO.*.md')):
        raw = f.read_text(encoding='utf-8')
        out = EN_BLOCK.sub(lambda m: m.group(1) + swap(m.group(2), f.stem), raw)
        if out != raw:
            touched += 1
            if APPLY:
                f.write_text(out, encoding='utf-8')

    agg: dict[tuple[str, str], int] = {}
    for _, found, rep in changes:
        agg[(found, rep)] = agg.get((found, rep), 0) + 1
    print(f'{"模式: 应用" if APPLY else "模式: 试运行"}   文件 {touched}   替换 {len(changes)}\n')
    for (found, rep), n in sorted(agg.items(), key=lambda kv: -kv[1]):
        print(f'  {n:>5}  {found}  ->  {rep}')
    if not APPLY:
        print('\n（未写盘；加 --apply 执行）')
    print('\n刻意保留：' + KEEP)


if __name__ == '__main__':
    main()
