# -*- coding: utf-8 -*-
"""按 Tuệ Sỹ《Luận Thành Duy Thức》校准越南语名相。

用法：
    python3 _build/authority/apply_vi.py            # 试运行
    python3 _build/authority/apply_vi.py --apply    # 写盘
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from vi_map import RENAME  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DICT = ROOT / '名相词典'
VI = DICT / 'TiếngViệt'
OTHER = [DICT / x for x in ('中文', 'English', 'Français')]
LECTURES = sorted((ROOT / 'Hundred Dharmas').glob('Hundred Dharmas NO.*.md'))

APPLY = '--apply' in sys.argv
NEW = {old: v[0] for old, v in RENAME.items()}
stat = {'renamed': 0, 'links': 0, 'prose': 0, 'files': 0}


def write(path: Path, new: str, old: str) -> None:
    if new == old:
        return
    stat['files'] += 1
    if APPLY:
        path.write_text(new, encoding='utf-8')


# ------------------------------------------------------------------ 1. 改名
def update_body(raw: str, old: str, new: str) -> str:
    """改一级标题、把旧名存入 aliases、插入校准说明。"""
    out = re.sub(rf'^# {re.escape(old)}\s*$', f'# {new}', raw, count=1, flags=re.M)
    if out == raw:
        out = raw.replace(f'# {old}', f'# {new}', 1)

    m = re.search(r'^aliases:\s*(\[\]|\n(?:  - .*\n)*)', out, re.M)
    if m:
        block = m.group(1)
        if block.strip() == '[]':
            out = out[:m.start(1)] + f'\n  - {old}\n' + out[m.end(1):]
        else:
            out = out[:m.end(1)] + f'  - {old}\n' + out[m.end(1):]

    marker = f'> 校准自「{old}」，依 Tuệ Sỹ, *Luận Thành Duy Thức*。\n\n'
    h = re.search(r'^# .*\n', out, re.M)
    if h:
        out = out[:h.end()] + marker + out[h.end():]
    return out


def rename_vi() -> None:
    """两阶段改名，避免同批内互相覆盖。"""
    staged = {}
    for old, new in NEW.items():
        src = VI / f'{old}.md'
        if not src.exists():
            raise SystemExit(f'缺少源文件: {src}')
        tmp = VI / f'.__tmp__{new}.md'
        staged[tmp] = VI / f'{new}.md'
        body = update_body(src.read_text(encoding='utf-8'), old, new)
        if APPLY:
            tmp.write_text(body, encoding='utf-8')
            src.unlink()
        stat['renamed'] += 1
    for tmp, dst in staged.items():
        if APPLY:
            if dst.exists():
                raise SystemExit(f'目标已存在: {dst}')
            tmp.rename(dst)


# --------------------------------------------------------------- 2. 改链接
LINK_RE = re.compile(r'\[\[((?:名相词典/)?TiếngViệt/)([^\]|]+)\|([^\]]+)\]\]')


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


# --------------------------------------------------------------- 3. 改散文
# 长名优先，避免 'tứ phần' 抢先吃掉 'thức thể tứ phần'
PROSE = sorted(((o.split(' (')[0], n) for o, n in NEW.items()),
               key=lambda kv: -len(kv[0]))
PROSE_RE = [(re.compile(rf'(?<![\w/|-]){re.escape(o)}(?![\w-])', re.I), n)
            for o, n in PROSE]


def swap(segment: str) -> str:
    """替换裸术语，跳过 wiki 链接内部。"""
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


VI_BLOCK = re.compile(r'(?ms)^(\*\*Tiếng Việt\*\*\n)(.*?)(?=^---\s*$|\Z)')
GIAITHICH = re.compile(r'(?ms)^(## Giải thích（Tiếng Việt）\n)(.*?)(?=^## |\Z)')


def main() -> None:
    print(f'模式: {"应用" if APPLY else "试运行"}   改名 {len(NEW)} 条\n')
    rename_vi()

    for folder in OTHER:
        for f in folder.glob('*.md'):
            raw = f.read_text(encoding='utf-8')
            write(f, fix_links(raw), raw)

    for f in VI.glob('*.md'):
        raw = f.read_text(encoding='utf-8')
        out = GIAITHICH.sub(lambda m: m.group(1) + swap(m.group(2)), fix_links(raw))
        write(f, out, raw)

    for f in LECTURES:
        raw = f.read_text(encoding='utf-8')
        out = VI_BLOCK.sub(lambda m: m.group(1) + swap(m.group(2)), fix_links(raw))
        write(f, out, raw)

    print(f'  条目改名      {stat["renamed"]}')
    print(f'  链接更新      {stat["links"]}')
    print(f'  越语散文替换  {stat["prose"]}')
    print(f'  文件写入      {stat["files"]}')
    if not APPLY:
        print('\n（未写盘；加 --apply 执行）')


if __name__ == '__main__':
    main()
