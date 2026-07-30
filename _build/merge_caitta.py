#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, glob
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))
for fn in sorted(glob.glob(os.path.join(BASE, 'batch_caitta_*.json'))):
    b = json.load(open(fn, encoding='utf-8'))
    n = 0
    for k, v in b.items():
        if isinstance(v, dict) and v.get('en') and v.get('fr') and v.get('vi'):
            D[k] = {'en': v['en'], 'fr': v['fr'], 'vi': v['vi']}
            n += 1
    print('合并', os.path.basename(fn), n, '条')
json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
meta = json.load(open(os.path.join(BASE, 'caitta_meta.json'), encoding='utf-8'))
miss = [t for t in meta if not (D.get(t, {}).get('en') and D.get(t, {}).get('fr') and D.get(t, {}).get('vi'))]
print('defs_i18n', len(D), '心所缺译', len(miss), miss)
