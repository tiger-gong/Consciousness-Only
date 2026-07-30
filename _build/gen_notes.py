#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""结构 B 笔记生成器：每个名相 × 每种语言各一笔记，四语互相 [[双链]]。

输入：
  _build/master.json      —— 合并主数据（词形 + 中文释义）
  _build/defs_i18n.json   —— 释义的英/法/越翻译 { zh: {en,fr,vi} }
输出：
  名相词典/中文/ *.md      名相词典/English/ *.md
  名相词典/Français/ *.md  名相词典/TiếngViệt/ *.md

只生成 defs_i18n.json 中出现、且四语词形齐全的名相（分批可控）。
"""
import json, os, re

BASE = os.path.dirname(__file__)
VAULT = os.path.dirname(BASE)
ROOT = os.path.join(VAULT, '名相词典')

LANGS = [
    ('zh', '中文', '中文', '中文'),
    ('en', 'English', 'English', 'English'),
    ('fr', 'Français', 'Français', 'Français'),
    ('vi', 'TiếngViệt', 'Tiếng Việt', 'Tiếng Việt'),
]
FOLDER = {'zh': '中文', 'en': 'English', 'fr': 'Français', 'vi': 'TiếngViệt'}
LABEL = {'zh': '中文', 'en': 'English', 'fr': 'Français', 'vi': 'Tiếng Việt'}
SECT = {'zh': '释义', 'en': 'Explanation', 'fr': 'Explication', 'vi': 'Giải thích'}
OTHERS = {'zh': '其它语言', 'en': 'Other languages', 'fr': 'Autres langues', 'vi': 'Các ngôn ngữ khác'}

ILLEGAL = re.compile(r'[\\/:*?"<>|#^\[\]]')


def title_of(word):
    w = word.strip()
    if '/' in w:
        w = re.split(r'\s*/\s*', w)[0].strip()
    w = ILLEGAL.sub('', w).strip()
    return w


def yaml_list(items):
    items = [i for i in items if i]
    if not items:
        return ' []'
    return '\n' + '\n'.join(f'  - {i}' for i in items)


def build_note(concept, lang, titles, words, defs, skt):
    """生成某概念某语言的笔记正文。"""
    title = titles[lang]
    full = words[lang]
    lines = ['---']
    lines.append(f'concept: {concept}')
    lines.append(f'lang: {lang}')
    if skt:
        lines.append(f'sanskrit: {skt}')
    aliases = []
    if full and full != title:
        aliases.append(full)
    if skt and lang != 'zh':
        aliases.append(skt)
    lines.append('aliases:' + yaml_list(aliases))
    lines.append('tags:\n  - 名相')
    lines.append('---')
    lines.append('')
    lines.append(f'# {full or title}')
    if skt:
        lines.append(f'**梵 / Sanskrit**：*{skt}*')
    lines.append('')
    lines.append(f'## {SECT[lang]}（{LABEL[lang]}）')
    lines.append(defs.get(lang, '').strip() or '（待补充）')
    lines.append('')
    lines.append(f'## {OTHERS[lang]}')
    for code in ('zh', 'en', 'fr', 'vi'):
        if code == lang:
            continue
        # 带文件夹路径 + 显示别名，避免跨语言同名（如 EN/FR 的 nirvāṇa）双链歧义
        lines.append(f'- {LABEL[code]}：[[{FOLDER[code]}/{titles[code]}|{titles[code]}]]')
    lines.append('')
    return '\n'.join(lines)


def main():
    master = {e['zh']: e for e in json.load(open(os.path.join(BASE, 'master.json'), encoding='utf-8'))}
    i18n = json.load(open(os.path.join(BASE, 'defs_i18n.json'), encoding='utf-8'))
    for code, folder, _, _ in LANGS:
        os.makedirs(os.path.join(ROOT, folder), exist_ok=True)
    made = 0
    skipped = []
    for zh, tr in i18n.items():
        e = master.get(zh)
        if not e:
            skipped.append((zh, 'not-in-master')); continue
        if not (e['en'] and e['fr'] and e['vi']):
            skipped.append((zh, 'missing-word')); continue
        words = {'zh': zh, 'en': e['en'], 'fr': e['fr'], 'vi': e['vi']}
        titles = {c: title_of(words[c]) for c in words}
        # 中文释义：优先用白话新解原文；若空（讲义专名/典籍），用 i18n 里补写的 zh
        zh_def = e['zh_def'] or tr.get('zh', '')
        defs = {'zh': zh_def, 'en': tr.get('en', ''), 'fr': tr.get('fr', ''), 'vi': tr.get('vi', '')}
        skt = e['skt']
        for code in ('zh', 'en', 'fr', 'vi'):
            body = build_note(zh, code, titles, words, defs, skt)
            path = os.path.join(ROOT, FOLDER[code], titles[code] + '.md')
            open(path, 'w', encoding='utf-8').write(body)
        made += 1
    print(f'生成概念 {made} 个 → 笔记 {made*4} 篇，输出目录：名相词典/')
    if skipped:
        print('跳过：', skipped)


if __name__ == '__main__':
    main()
