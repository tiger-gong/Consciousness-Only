#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 Hundred Dharmas 讲次中的名相挂上指向名相词典的双链（修正版）。

流程：
  1) 先把所有已有 [[...]] 还原成纯文本（取 | 后别名，或整段）
  2) 再按词长降序最长匹配挂链
  3) 替换时跳过已在 [[...]] 内的区域，防止短词嵌进长词链接
  4) 中文词表同时匹配简体与繁体表面形式，链接目标仍指向词典简体文件名
"""
import json, os, re

try:
    import opencc
    ZH_CC = [opencc.OpenCC(cfg) for cfg in ('s2tw', 's2t')]
except Exception:
    ZH_CC = []

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LECTURE_DIR = os.path.join(VAULT, 'Hundred Dharmas')
FILES = [
    'Hundred Dharmas NO.1.md',
    'Hundred Dharmas NO.2.md',
    'Hundred Dharmas NO.3.md',
    'Hundred Dharmas NO.4.md',
    'Hundred Dharmas NO.5.md',
    'Hundred Dharmas NO.6.md',
    'Hundred Dharmas NO.7.md',
    'Hundred Dharmas NO.8.md',
    'Hundred Dharmas NO.9.md',
    'Hundred Dharmas NO.10.md',
]
FOLDER = {'zh': '中文', 'en': 'English', 'fr': 'Français', 'vi': 'TiếngViệt'}
BLOCK_START = {
    '**中文**': 'zh',
    '**English**': 'en',
    '**Français**': 'fr',
    '**Tiếng Việt**': 'vi',
}


def title_of(word):
    w = word.strip()
    if '/' in w:
        w = re.split(r'\s*/\s*', w)[0].strip()
    return re.sub(r'[\\/:*?"<>|#^\[\]]', '', w).strip()


def link_of(lang, display, title=None):
    return f'[[名相词典/{FOLDER[lang]}/{title_of(title or display)}|{display}]]'


def load_terms():
    master = json.load(open(os.path.join(VAULT, '_build', 'master.json'), encoding='utf-8'))
    by_lang = {'zh': [], 'en': [], 'fr': [], 'vi': []}
    zh_file_title = {}  # 表面词形 → 词典文件名（简体）
    file_exists = {lang: set() for lang in by_lang}
    for lang, folder in FOLDER.items():
        d = os.path.join(VAULT, '名相词典', folder)
        for fn in os.listdir(d):
            if fn.endswith('.md'):
                file_exists[lang].add(fn[:-3])

    def add_zh_surface(surface, file_title):
        if not surface or len(surface) < 2:
            return
        if file_title not in file_exists['zh']:
            return
        prev = zh_file_title.get(surface)
        if prev is None or len(file_title) > len(prev):
            zh_file_title[surface] = file_title

    for e in master:
        if not (e.get('en') and e.get('fr') and e.get('vi')):
            continue
        words = {
            'zh': e['zh'].strip(),
            'en': e['en'].strip(),
            'fr': e['fr'].strip(),
            'vi': e['vi'].strip(),
        }
        for lang, w in words.items():
            if not w:
                continue
            # 只挂「词典里确实有对应文件」的词形，避免死链
            if title_of(w) in file_exists[lang]:
                by_lang[lang].append(w)
                if lang == 'zh':
                    ft = title_of(w)
                    add_zh_surface(w, ft)
                    for cc in ZH_CC:
                        add_zh_surface(cc.convert(w), ft)
            # 对含 / 的，若主段有文件也已覆盖；半边若单独成文件则另挂
            if ' / ' in w:
                for part in w.split(' / '):
                    part = part.strip()
                    if part and title_of(part) in file_exists[lang]:
                        by_lang[lang].append(part)
                        if lang == 'zh':
                            ft = title_of(part)
                            add_zh_surface(part, ft)
                            for cc in ZH_CC:
                                add_zh_surface(cc.convert(part), ft)
    for lang in by_lang:
        if lang == 'zh':
            uniq = sorted(zh_file_title.keys(), key=lambda s: (-len(s), s))
        else:
            uniq = sorted(set(by_lang[lang]), key=lambda s: (-len(s), s))
            uniq = [t for t in uniq if len(t) >= 3]
        by_lang[lang] = uniq
    return by_lang, zh_file_title


def unwrap_links(text):
    """彻底剥掉双链，还原纯文本（可处理嵌套残留）。

    策略：先删掉所有「[[名相词典/...|」前缀，再删掉全部 [[ 与 ]]。
    """
    # 反复去掉路径前缀（嵌套时可能多层）
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r'\[\[名相词典/[^\]|]+\|', '', text)
    text = text.replace('[[', '').replace(']]', '')
    return text


def replace_outside_links(text, pattern, repl_fn):
    """只在 [[...]] 之外做替换。"""
    parts = re.split(r'(\[\[[^\]]+\]\])', text)
    out = []
    for part in parts:
        if part.startswith('[[') and part.endswith(']]'):
            out.append(part)
        else:
            out.append(pattern.sub(repl_fn, part))
    return ''.join(out)


def link_block(text, terms, lang, zh_file_title=None):
    text = unwrap_links(text)
    if lang == 'zh':
        if not terms:
            return text
        pat = re.compile('|'.join(re.escape(t) for t in terms))
        def repl(m):
            surface = m.group(0)
            title = (zh_file_title or {}).get(surface, surface)
            return link_of('zh', surface, title)
        # 单次扫描即最长优先（terms 已按长度降序）
        return replace_outside_links(text, pat, repl)
    # 英/法/越：逐词，每次跳过已有链接；大小写不敏感（越南语句首大写等）
    # 含 Latin Extended Additional（ệ/ộ/ấ 等）与连字符，避免 nghi|ệp、A-|dục 误切
    WORD = r'A-Za-zÀ-ɏĀ-ɏ\u1E00-\u1EFF\u0300-\u036Fāīūṛṃḥṅñṭḍṇśṣ'
    BOUND_L = rf'(?<![{WORD}-])'
    BOUND_R = rf'(?![{WORD}-])'
    for w in terms:
        pat = re.compile(BOUND_L + re.escape(w) + BOUND_R, re.IGNORECASE)
        def make(word):
            # 显示保留原文大小写；文件名用词表标准词形
            return lambda m: f'[[名相词典/{FOLDER[lang]}/{title_of(word)}|{m.group(0)}]]'
        text = replace_outside_links(text, pat, make(w))
    return text


def process_file(path, by_lang, zh_file_title=None):
    lines = open(path, encoding='utf-8').read().split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        lang = None
        for marker, code in BLOCK_START.items():
            if line.strip() == marker:
                lang = code
                break
        if lang is None:
            out.append(line)
            i += 1
            continue
        out.append(line)
        i += 1
        block_lines = []
        while i < len(lines):
            stripped = lines[i].strip()
            if stripped in BLOCK_START or stripped == '---' or stripped.startswith('**§'):
                break
            block_lines.append(lines[i])
            i += 1
        if block_lines:
            block = '\n'.join(block_lines)
            out.append(link_block(block, by_lang[lang], lang, zh_file_title))
    text = '\n'.join(out)
    open(path, 'w', encoding='utf-8').write(text)
    counts = {lang: len(re.findall(rf'\[\[名相词典/{FOLDER[lang]}/', text)) for lang in FOLDER}
    # 检查嵌套
    nested = len(re.findall(r'\[\[[^\]]*?\[\[[^\]]+\]\]', text))
    return counts, nested


def main():
    by_lang, zh_file_title = load_terms()
    print('词表规模：', {k: len(v) for k, v in by_lang.items()})
    files = FILES
    only = os.environ.get('LECTURE_ONLY')
    if only:
        files = [fn for fn in FILES if fn in only.split(',')]
    for fn in files:
        path = os.path.join(LECTURE_DIR, fn)
        if not os.path.exists(path):
            print('SKIP missing', fn)
            continue
        counts, nested = process_file(path, by_lang, zh_file_title)
        print(f'{fn}: 链接 {counts} 合计 {sum(counts.values())} 嵌套残留 {nested}')
    # 死链检查
    miss = 0
    seen = set()
    for fn in files:
        t = open(os.path.join(LECTURE_DIR, fn), encoding='utf-8').read()
        for path, alias in re.findall(r'\[\[名相词典/([^\]|]+)\|([^\]]+)\]\]', t):
            if path in seen:
                continue
            seen.add(path)
            fp = os.path.join(VAULT, '名相词典', path + '.md')
            if not os.path.exists(fp):
                miss += 1
                if miss <= 20:
                    print('MISS', path, '←', alias)
    print(f'唯一链接目标 {len(seen)}，死链 {miss}')


if __name__ == '__main__':
    main()
