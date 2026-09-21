# -*- coding: utf-8 -*-
"""把第 1–5 讲的简体中文还原为繁体，体例对齐第 6–10 讲。

- 链接目标 名相词典/中文/<简体文件名> 不动（与后五讲一致）
- 链接显示文字与中文正文转为繁体
- 用字以净界法师《直解》讲记 PDF 为准，覆盖 OpenCC 一对多

用法：
    python3 _build/authority/to_trad.py            # 试运行
    python3 _build/authority/to_trad.py --apply    # 写盘
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import opencc

ROOT = Path(__file__).resolve().parents[2]
LECTURE = ROOT / 'Hundred Dharmas'
APPLY = '--apply' in sys.argv
CC = opencc.OpenCC('s2tw')

# OpenCC s2tw 与底本不一致、且比对中反复出现的用字。
# 标点差异（破折号、引号、全角括号）一律保留讲记 Markdown，不跟 PDF OCR。
POST = [
    ('溼', '濕'),
    ('瞭', '了'),
    ('燻', '熏'),
    ('薰習', '熏習'),
    ('薰', '熏'),
    ('毁謗', '譭謗'),
    ('毀謗', '譭謗'),
    ('痴', '癡'),
    ('佈施', '布施'),
    ('佈', '布'),
    ('汙', '污'),
    ('唸', '念'),
    ('依託', '依托'),
    ('仗因託緣', '仗因托緣'),
    ('託', '托'),
    ('昇華', '升華'),
    ('上昇', '上升'),
    ('昇', '升'),
    ('不可逾', '不可踰'),
    ('逾越', '踰越'),
    ('醜陋', '丑陋'),
    ('醜', '丑'),
    ('特徵', '特征'),
    ('徵兆', '征兆'),
    ('徵', '征'),
    ('遊歷', '游歷'),
    ('遊', '游'),
    ('天臺', '天台'),
    ('臺', '台'),
    ('一隻', '一只'),
    ('隻', '只'),
    ('屍體', '尸體'),
    ('屍', '尸'),
]

# 上一輪比對：s2tw「周」底本「週」（1 次）、s2tw「回」底本「迴」（1 次）
# 這兩條語境敏感，放到 POST 末尾只改已確認的詞
POST_WORD = [
    ('回小向大', '迴小向大'),
    ('回向', '迴向'),
    ('周圍', '週圍'),
    ('周期', '週期'),
    ('舍離', '捨離'),
    ('取舍', '取捨'),
    ('舍去', '捨去'),
    ('施舍', '施捨'),
    ('舍掉', '捨掉'),
    ('舍棄', '捨棄'),
    ('複習', '複習'),
    ('重複', '重複'),
    ('發廊', '髮廊'),  # 不會出現
    ('願力', '願力'),
]


WIKI = re.compile(r'(\[\[(?:名相词典/)?中文/)([^\]|]+)(\|)([^\]]+)(\]\])')
ZH_BLOCK = re.compile(r'(?ms)^(\*\*中文\*\*\n)(.*?)(?=^\*\*English\*\*)')
FRONT = re.compile(
    r'(?s)\A(.*?)(?=^\*\*§)',
    re.M,
)


def convert_zh_text(text: str) -> str:
    """转换普通中文，保护 wiki 目标。"""
    parts = []
    last = 0
    for m in WIKI.finditer(text):
        parts.append(_convert_plain(text[last:m.start()]))
        display = _convert_plain(m.group(4))
        parts.append(f'{m.group(1)}{m.group(2)}{m.group(3)}{display}{m.group(5)}')
        last = m.end()
    parts.append(_convert_plain(text[last:]))
    return ''.join(parts)


def _convert_plain(s: str) -> str:
    if not s:
        return s
    out = CC.convert(s)
    for a, b in POST + POST_WORD:
        out = out.replace(a, b)
    return out


def convert_front(front: str) -> str:
    """文前说明与标题。越南语体例句去重。"""
    out = convert_zh_text(front)
    out = out.replace('簡體中文（原文，繁轉簡）', '繁體中文（原文）')
    out = out.replace('簡體中文（原文，繁转简）', '繁體中文（原文）')
    out = out.replace('中文部分依原繁體文本轉為簡體，', '中文部分依原繁體文本，')
    out = out.replace('中文部分依原繁体文本转为简体，', '中文部分依原繁體文本，')
    out = re.sub(
        r'(liên tục xuyên suốt Volume 1)(?:, liên tục xuyên suốt Volume 1)+',
        r'\1',
        out,
    )
    return out


def convert_file(raw: str) -> str:
    m = re.match(r'(?s)(.*?)(?=^\*\*§)', raw, re.M)
    if not m:
        return convert_zh_text(raw)
    front, rest = m.group(1), raw[m.end():]
    rest = ZH_BLOCK.sub(lambda x: x.group(1) + convert_zh_text(x.group(2)), rest)
    return convert_front(front) + rest


def main() -> None:
    n_files = 0
    n_bytes = 0
    for i in range(1, 6):
        p = LECTURE / f'Hundred Dharmas NO.{i}.md'
        raw = p.read_text(encoding='utf-8')
        out = convert_file(raw)
        if out == raw:
            print(f'  无变化  {p.name}')
            continue
        n_files += 1
        n_bytes += abs(len(out) - len(raw))
        print(f'  改写    {p.name}  {len(raw)} → {len(out)}')
        if APPLY:
            p.write_text(out, encoding='utf-8')
    print(f'\n文件 {n_files}    模式: {"应用" if APPLY else "试运行"}')
    if not APPLY:
        print('（未写盘；加 --apply 执行）')


if __name__ == '__main__':
    main()
