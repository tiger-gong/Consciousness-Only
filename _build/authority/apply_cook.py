#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按 Cook《Three Texts on Consciousness Only》校准英文名相。

改动三处并保持一致：
  1. 名相词典/English/*.md          —— 文件名、标题、aliases
  2. 名相词典/{中文,Français,TiếngViệt}/*.md —— 指向 English 的跨语链接
  3. Hundred Dharmas/*.md           —— 讲记中的 [[名相词典/English/...]] 及英文正文散文

用法:  python3 apply_cook.py [--apply]     缺省为试运行
"""
from __future__ import annotations

import os
import re
import sys
import pathlib
import collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cook_map import RENAME, EXTRAPOLATED  # noqa: E402

VAULT = pathlib.Path(__file__).resolve().parents[2]
EN = VAULT / '名相词典' / 'English'
OTHER_LANGS = [VAULT / '名相词典' / d for d in ('中文', 'Français', 'TiếngViệt')]
LECTURES = sorted((VAULT / 'Hundred Dharmas').glob('Hundred Dharmas NO.*.md'))

APPLY = '--apply' in sys.argv
NEW = {old: new for old, (new, _) in RENAME.items()}
stat = collections.Counter()


def write(path: pathlib.Path, text: str, original: str) -> None:
    if text == original:
        return
    stat['files_changed'] += 1
    if APPLY:
        path.write_text(text, encoding='utf-8')


# ---------------------------------------------------------------- 1. 改名
def rename_english() -> None:
    """两阶段改名，避免 shamelessness 这类互换造成覆盖。"""
    tmp = {}
    for old, new in NEW.items():
        src = EN / f'{old}.md'
        if not src.exists():
            raise SystemExit(f'缺少源文件: {src}')
        dst = EN / f'.__tmp__{new}.md'
        tmp[dst] = EN / f'{new}.md'
        raw = src.read_text(encoding='utf-8')
        body = update_english_body(raw, old, new)
        if APPLY:
            dst.write_text(body, encoding='utf-8')
            src.unlink()
        stat['renamed'] += 1
    for src, dst in tmp.items():
        if dst.exists() and APPLY:
            raise SystemExit(f'目标已存在: {dst}')
        if APPLY:
            src.rename(dst)


def update_english_body(raw: str, old: str, new: str) -> str:
    """更新条目内的一级标题与 aliases，并保留旧名作为别名。"""
    out = re.sub(rf'^# {re.escape(old)}\s*$', f'# {new}', raw, count=1, flags=re.M)
    if out == raw and f'# {old}' in raw:
        out = raw.replace(f'# {old}', f'# {new}', 1)
    # 旧名写进 aliases，保证历史链接与搜索仍可命中
    m = re.search(r'^aliases:\s*(\[\]|\n(?:  - .*\n)*)', out, re.M)
    if m:
        block = m.group(1)
        if block.strip() == '[]':
            out = out[:m.start(1)] + f'\n  - {old}\n' + out[m.end(1):]
        else:
            out = out[:m.end(1)] + f'  - {old}\n' + out[m.end(1):]
    tag = '，权威未直接用此词形，依同组体例推衍' if new in EXTRAPOLATED else ''
    marker = f'> 校准自「{old}」，依 Cook, *Three Texts on Consciousness Only*{tag}。\n\n'
    m = re.search(r'^# .*\n', out, re.M)
    if m:
        out = out[:m.end()] + marker + out[m.end():]
    return out


# ------------------------------------------------- 2/3. 链接与正文
LINK_RE = re.compile(r'\[\[((?:名相词典/)?English/)([^\]|]+)\|([^\]]+)\]\]')


def fix_links(text: str) -> str:
    def sub(m):
        prefix, target, display = m.group(1), m.group(2), m.group(3)
        new_t = NEW.get(target)
        if not new_t:
            return m.group(0)
        stat['links'] += 1
        # display 与 target 在本库中始终一致，仅保留首字母大小写
        new_d = new_t[0].upper() + new_t[1:] if display[:1].isupper() else new_t
        return f'[[{prefix}{new_t}|{new_d}]]'
    return LINK_RE.sub(sub, text)


# 讲记英文散文中未加链接的裸术语：仅替换歧义低且为多词的旧名
PROSE = {old: new for old, new in NEW.items()
         if ' ' in old and old.lower() not in {
             'lesser vehicle', 'four portions', 'mind dharmas', 'form dharmas'}}
PROSE_RE = [(re.compile(rf'(?<![\w/|-]){re.escape(o)}(?![\w-])'), n)
            for o, n in sorted(PROSE.items(), key=lambda kv: -len(kv[0]))]

EN_BLOCK = re.compile(r'(?m)^\*\*English\*\*\n(.*?)(?=\n\*\*Français\*\*)', re.S)


def swap_terms(segment: str) -> str:
    """替换裸术语，跳过 wiki 链接内部。"""
    parts = re.split(r'(\[\[[^\]]*\]\])', segment)
    for i, seg in enumerate(parts):
        if seg.startswith('[['):
            continue
        for rx, new in PROSE_RE:
            seg, n = rx.subn(new, seg)
            stat['prose'] += n
        parts[i] = seg
    return ''.join(parts)


def fix_prose(text: str) -> str:
    """讲记：只在 **English** 段内替换。"""
    return EN_BLOCK.sub(lambda m: '**English**\n' + swap_terms(m.group(1)), text)


EXPLAIN = re.compile(r'(?ms)^(## Explanation（English）\n)(.*?)(?=^## |\Z)')


def fix_explanation(text: str) -> str:
    """英文词条：只在 Explanation 段内替换释义用语。"""
    return EXPLAIN.sub(lambda m: m.group(1) + swap_terms(m.group(2)), text)


def main() -> None:
    print(f'模式: {"应用" if APPLY else "试运行"}   改名 {len(NEW)} 条\n')
    rename_english()

    for folder in OTHER_LANGS:
        for f in folder.glob('*.md'):
            raw = f.read_text(encoding='utf-8')
            write(f, fix_links(raw), raw)
    for f in EN.glob('*.md'):
        raw = f.read_text(encoding='utf-8')
        write(f, fix_explanation(fix_links(raw)), raw)

    for f in LECTURES:
        raw = f.read_text(encoding='utf-8')
        out = fix_prose(fix_links(raw))
        write(f, out, raw)

    print(f'  条目改名      {stat["renamed"]}')
    print(f'  链接更新      {stat["links"]}')
    print(f'  英文散文替换  {stat["prose"]}')
    print(f'  文件写入      {stat["files_changed"]}')
    if not APPLY:
        print('\n（未写盘；加 --apply 执行）')


if __name__ == '__main__':
    main()
