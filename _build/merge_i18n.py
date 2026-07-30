#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并工具：把 batch_*.json 依次合并进 defs_i18n.json。"""
import json, os, glob
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
for fn in sorted(glob.glob(os.path.join(BASE, 'batch_*.json'))):
    b = json.load(open(fn, encoding='utf-8'))
    D.update(b)
    print('合并', os.path.basename(fn), '→', len(b), '条')
json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('defs_i18n.json 现有', len(D), '条')
