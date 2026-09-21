# -*- coding: utf-8 -*-
"""补一轮 LVP 法语专名（见分、增上缘）。

底本：LVP《俱舍论》法译（Geuthner, 1923–31）+ 法语唯识通称。
2017 Lodrö Sangpo 第三卷对照表不可得，且实为页码对照而非术语表。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DICT = ROOT / '名相词典'
FR = DICT / 'Français'
OTHER = [DICT / x for x in ('中文', 'English', 'TiếngViệt')]
LECTURES = sorted((ROOT / 'Hundred Dharmas').glob('Hundred Dharmas NO.*.md'))
APPLY = '--apply' in sys.argv

NEW = {
    'partie qui voit': 'partie voyante',
    'condition prédominante': 'condition souveraine',
}
EXTRAPOLATED = set()  # 均有出处
stat = {'renamed': 0, 'links': 0, 'prose': 0, 'files': 0}


def write(path: Path, new: str, old: str) -> None:
    if new == old:
        return
    stat['files'] += 1
    if APPLY:
        path.write_text(new, encoding='utf-8')


def add_alias(text: str, name: str) -> str:
    m = re.search(r'^aliases:\s*(\[\]|\n(?:  - .*\n)*)', text, re.M)
    if not m:
        return text
    if m.group(1).strip() == '[]':
        return text[:m.start(1)] + f'\n  - {name}\n' + text[m.end(1):]
    if f'  - {name}\n' in m.group(1):
        return text
    return text[:m.end(1)] + f'  - {name}\n' + text[m.end(1):]


def update_body(raw: str, old: str, new: str) -> str:
    out = re.sub(rf'^# {re.escape(old)}\s*$', f'# {new}', raw, count=1, flags=re.M)
    if out == raw:
        out = raw.replace(f'# {old}', f'# {new}', 1)
    out = add_alias(out, old)
    marker = (
        f'> 校准自「{old}」，依 La Vallée Poussin 法译体例'
        f'（《俱舍论》法译 / 法语唯识通称 darśanabhāga = partie voyante）。\n\n'
    )
    h = re.search(r'^# .*\n', out, re.M)
    return out[:h.end()] + marker + out[h.end():] if h else out


def rename_fr() -> None:
    staged = {}
    for old, new in NEW.items():
        src = FR / f'{old}.md'
        if not src.exists():
            raise SystemExit(f'缺少 {src}')
        tmp = FR / f'.__tmp__{new}.md'
        dst = FR / f'{new}.md'
        if dst.exists():
            raise SystemExit(f'目标已存在 {dst}')
        staged[tmp] = dst
        body = update_body(src.read_text(encoding='utf-8'), old, new)
        if APPLY:
            tmp.write_text(body, encoding='utf-8')
            src.unlink()
        stat['renamed'] += 1
    for tmp, dst in staged.items():
        if APPLY:
            tmp.rename(dst)


LINK_RE = re.compile(r'\[\[((?:名相词典/)?Français/)([^\]|]+)\|([^\]]+)\]\]')


def fix_links(text: str) -> str:
    def sub(m):
        prefix, target, display = m.groups()
        new_t = NEW.get(target)
        if not new_t:
            return m.group(0)
        stat['links'] += 1
        new_d = new_t[0].upper() + new_t[1:] if display[:1].isupper() else new_t
        return f'[[{prefix}{new_t}|{new_d}]]'
    return LINK_RE.sub(sub, text)


PROSE = sorted(NEW.items(), key=lambda kv: -len(kv[0]))
PROSE_RE = [(re.compile(rf'(?<![\w/|-]){re.escape(o)}(?![\w-])', re.I), n)
            for o, n in PROSE]


def swap(segment: str) -> str:
    parts = re.split(r'(\[\[[^\]]*\]\])', segment)
    for i, piece in enumerate(parts):
        if piece.startswith('[['):
            continue
        for rx, new in PROSE_RE:
            def keep_case(m, new=new):
                return new[0].upper() + new[1:] if m.group(0)[:1].isupper() else new
            piece, n = rx.subn(keep_case, piece)
            stat['prose'] += n
        parts[i] = piece
    return ''.join(parts)


FR_BLOCK = re.compile(r'(?ms)^(\*\*Français\*\*\n)(.*?)(?=^\*\*Tiếng Việt\*\*)')
EXPLICATION = re.compile(r'(?ms)^(## Explication（Français）\n)(.*?)(?=^## |\Z)')


def main() -> None:
    print(f'模式: {"应用" if APPLY else "试运行"}')
    rename_fr()
    for folder in OTHER:
        for f in folder.glob('*.md'):
            raw = f.read_text(encoding='utf-8')
            write(f, fix_links(raw), raw)
    for f in FR.glob('*.md'):
        raw = f.read_text(encoding='utf-8')
        write(f, EXPLICATION.sub(lambda m: m.group(1) + swap(m.group(2)), fix_links(raw)), raw)
    for f in LECTURES:
        raw = f.read_text(encoding='utf-8')
        write(f, FR_BLOCK.sub(lambda m: m.group(1) + swap(m.group(2)), fix_links(raw)), raw)
    print(f'  改名 {stat["renamed"]}  链接 {stat["links"]}  散文 {stat["prose"]}  文件 {stat["files"]}')
    if not APPLY:
        print('（未写盘；加 --apply 执行）')


if __name__ == '__main__':
    main()
