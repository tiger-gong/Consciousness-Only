# -*- coding: utf-8 -*-
"""按 Hôbôgirin 所代表的古典法-比学派术语校准法语名相。

用法：
    python3 _build/authority/apply_fr.py            # 试运行
    python3 _build/authority/apply_fr.py --apply    # 写盘
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fr_map import RENAME, EXTRAPOLATED, ORPHAN_MERGE  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DICT = ROOT / '名相词典'
FR = DICT / 'Français'
OTHER = [DICT / x for x in ('中文', 'English', 'TiếngViệt')]
LECTURES = sorted((ROOT / 'Hundred Dharmas').glob('Hundred Dharmas NO.*.md'))

APPLY = '--apply' in sys.argv
NEW = {old: v[0] for old, v in RENAME.items()}
stat = {'renamed': 0, 'merged': 0, 'links': 0, 'prose': 0, 'files': 0}


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


# ------------------------------------------------------- 0. 合并孤儿重复条目
def merge_orphans() -> None:
    for orphan, keep in ORPHAN_MERGE.items():
        src, dst = FR / f'{orphan}.md', FR / f'{keep}.md'
        if not src.exists():
            continue
        if not dst.exists():
            raise SystemExit(f'合并目标不存在: {dst}')
        stat['merged'] += 1
        if APPLY:
            dst.write_text(add_alias(dst.read_text(encoding='utf-8'), orphan),
                           encoding='utf-8')
            src.unlink()


# ------------------------------------------------------------------ 1. 改名
def update_body(raw: str, old: str, new: str) -> str:
    out = re.sub(rf'^# {re.escape(old)}\s*$', f'# {new}', raw, count=1, flags=re.M)
    if out == raw:
        out = raw.replace(f'# {old}', f'# {new}', 1)
    out = add_alias(out, old)
    tag = '，权威未直接用此词形，据 Cook 英译回推' if new in EXTRAPOLATED else ''
    marker = f'> 校准自「{old}」，依 Hôbôgirin（法-比古典学派体例）{tag}。\n\n'
    h = re.search(r'^# .*\n', out, re.M)
    return out[:h.end()] + marker + out[h.end():] if h else out


def precheck() -> None:
    for old, new in NEW.items():
        if not (FR / f'{old}.md').exists():
            raise SystemExit(f'缺少源文件: {old}.md')
        if (FR / f'{new}.md').exists() and new not in NEW:
            raise SystemExit(f'目标已被占用且不在改名表中: {new}.md')
    if len(set(NEW.values())) != len(NEW):
        raise SystemExit('改名表存在重名目标')


def rename_fr() -> None:
    staged = {}
    for old, new in NEW.items():
        src = FR / f'{old}.md'
        tmp = FR / f'.__tmp__{new}.md'
        staged[tmp] = FR / f'{new}.md'
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
LINK_RE = re.compile(r'\[\[((?:名相词典/)?Français/)([^\]|]+)\|([^\]]+)\]\]')
REDIRECT = {**NEW, **ORPHAN_MERGE}


def fix_links(text: str) -> str:
    def sub(m):
        prefix, target, display = m.groups()
        new_t = REDIRECT.get(target)
        if not new_t:
            return m.group(0)
        stat['links'] += 1
        new_d = new_t[0].upper() + new_t[1:] if display[:1].isupper() else new_t
        return f'[[{prefix}{new_t}|{new_d}]]'
    return LINK_RE.sub(sub, text)


# --------------------------------------------------------------- 3. 改散文
# 顺序敏感：长串、否定式在前，避免被短规则抢先吃掉
PROSE_RULES = [
    (r"non[- ]contaminée?s?\b",                'pur'),
    (r"\bnon[- ]souillée?s?\b",                'pur'),
    (r"contaminées\b",                         'impures'),
    (r"contaminés\b",                          'impurs'),
    (r"contaminée\b",                          'impure'),
    (r"contaminé\b",                           'impur'),
    (r"activités? présentes?\b",               'activité'),
    (r"empreintes résiduelles\b",              'imprégnations'),
    (r"empreinte résiduelle\b",                'imprégnation'),
    (r"\bmaturations\b",                       'rétributions'),
    (r"\bmaturation\b",                        'rétribution'),
    (r"afflictions-racines\b",                 'passions fondamentales'),
    # passion 以辅音起首，缩合形须先还原，否则会写出 d'passion
    (r"\bd'afflictions\b",                     'de passions'),
    (r"\bd'affliction\b",                      'de passion'),
    (r"\bl'afflictions\b",                     'les passions'),
    (r"\bl'affliction\b",                      'la passion'),
    (r"\bafflictions\b",                       'passions'),
    (r"\baffliction\b",                        'passion'),
    (r"\bafflictifs\b",                        'passionnels'),
    (r"\bafflictif\b",                         'passionnel'),
    (r"\bafflictives\b",                       'passionnelles'),
    (r"\bafflictive\b",                        'passionnelle'),
    (r"quatre portions de la substance de la conscience", 'quatre parties de la conscience'),
    (r"portion-image\b",                       'partie vue'),
    (r"portions?\b",                           lambda m: 'parties' if m.group(0).endswith('s') else 'partie'),
]
COMPILED = [(re.compile(p, re.I), r) for p, r in PROSE_RULES]


def swap(segment: str) -> str:
    parts = re.split(r'(\[\[[^\]]*\]\])', segment)
    for i, piece in enumerate(parts):
        if piece.startswith('[['):
            continue
        for rx, rep in COMPILED:
            def keep_case(m, rep=rep):
                out = rep(m) if callable(rep) else rep
                return out[0].upper() + out[1:] if m.group(0)[:1].isupper() else out
            piece, n = rx.subn(keep_case, piece)
            stat['prose'] += n
        parts[i] = piece
    return ''.join(parts)


FR_BLOCK = re.compile(r'(?ms)^(\*\*Français\*\*\n)(.*?)(?=^\*\*Tiếng Việt\*\*)')
EXPLICATION = re.compile(r'(?ms)^(## Explication（Français）\n)(.*?)(?=^## |\Z)')


def main() -> None:
    print(f'模式: {"应用" if APPLY else "试运行"}   改名 {len(NEW)} 条   合并 {len(ORPHAN_MERGE)} 条\n')
    precheck()
    merge_orphans()
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

    print(f'  条目改名      {stat["renamed"]}')
    print(f'  重复条合并    {stat["merged"]}')
    print(f'  链接更新      {stat["links"]}')
    print(f'  法语散文替换  {stat["prose"]}')
    print(f'  文件写入      {stat["files"]}')
    if not APPLY:
        print('\n（未写盘；加 --apply 执行）')


if __name__ == '__main__':
    main()
