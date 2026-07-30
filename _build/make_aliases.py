#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为常用别名建薄入口笔记，链到正式词条。"""
import os
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.join(VAULT, '名相词典')

# alias_zh -> target_zh, and multilingual labels
ALIASES = [
    {
        'zh': '三自性', 'zh_target': '三性',
        'en': 'three natures (tri-svabhāva)', 'en_target': 'three natures',
        'fr': 'trois natures (tri-svabhāva)', 'fr_target': 'trois natures',
        'vi': 'ba tự tính', 'vi_target': 'tam tính (ba tự tính)',
        'note_zh': '「三自性」即「三性」的全称，详见主词条。',
        'note_en': '“Three self-natures” is the full name of the “three natures.” See the main entry.',
        'note_fr': '« Trois natures propres » est le nom complet des « trois natures ». Voir l\'entrée principale.',
        'note_vi': '“Ba tự tính” là tên đầy đủ của “tam tính”. Xem từ mục chính.',
    },
    {
        'zh': '四分', 'zh_target': '识体四分',
        'en': 'four portions', 'en_target': 'four portions of the substance of consciousness',
        'fr': 'quatre portions', 'fr_target': 'quatre portions de la substance de la conscience',
        'vi': 'tứ phần', 'vi_target': 'thức thể tứ phần',
        'note_zh': '「四分」通常指「识体四分」（见分、相分、自证分、证自证分），详见主词条。',
        'note_en': '“Four portions” usually means the four portions of the substance of consciousness. See the main entry.',
        'note_fr': '« Quatre portions » désigne en général les quatre portions de la substance de la conscience. Voir l\'entrée principale.',
        'note_vi': '“Tứ phần” thường chỉ “thức thể tứ phần”. Xem từ mục chính.',
    },
]

FOLDER = {'zh': '中文', 'en': 'English', 'fr': 'Français', 'vi': 'TiếngViệt'}
SECT = {'zh': '释义', 'en': 'Explanation', 'fr': 'Explication', 'vi': 'Giải thích'}
OTHER = {'zh': '其它语言', 'en': 'Other languages', 'fr': 'Autres langues', 'vi': 'Các ngôn ngữ khác'}
LABEL = {'zh': '中文', 'en': 'English', 'fr': 'Français', 'vi': 'Tiếng Việt'}

def write_alias(a):
    for lang in ('zh', 'en', 'fr', 'vi'):
        title = a[lang]
        target = a[f'{lang}_target']
        note = a[f'note_{lang}']
        body = f'''---
concept: {a['zh']}
lang: {lang}
aliases:
  - {title}
tags:
  - 名相
  - 别名
---

# {title}

## {SECT[lang]}（{LABEL[lang]}）
{note}

→ 主词条：[[名相词典/{FOLDER[lang]}/{target}|{target}]]

## {OTHER[lang]}
'''
        for code in ('zh', 'en', 'fr', 'vi'):
            if code == lang:
                continue
            body += f'- {LABEL[code]}：[[名相词典/{FOLDER[code]}/{a[code]}|{a[code]}]]\n'
        path = os.path.join(ROOT, FOLDER[lang], title + '.md')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'w', encoding='utf-8').write(body)
        print('alias', path)

for a in ALIASES:
    write_alias(a)
print('done')
