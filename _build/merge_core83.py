#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并 core T1/T2/T3 翻译进 defs_i18n.json，并生成笔记。"""
import json, os, glob
BASE = os.path.dirname(__file__)
VAULT = os.path.dirname(BASE)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))
for fn in sorted(glob.glob(os.path.join(BASE, 'batch_core_T*.json'))):
    b = json.load(open(fn, encoding='utf-8'))
    # 规范化
    for k, v in b.items():
        if isinstance(v, dict) and v.get('en') and v.get('fr') and v.get('vi'):
            D[k] = {'en': v['en'], 'fr': v['fr'], 'vi': v['vi']}
        else:
            print('SKIP bad', k, fn)
    print('合并', os.path.basename(fn), '→', len(b), '条')
json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('defs_i18n 现有', len(D))

# 检查 83 词覆盖
meta = json.load(open(os.path.join(BASE, 'core83_meta.json'), encoding='utf-8'))
missing = [t for t in meta if t not in D or not D[t].get('en')]
print('83词中仍缺释义翻译:', len(missing))
for t in missing:
    print(' ', t)
