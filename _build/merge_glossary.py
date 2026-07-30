#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把三讲四语译文挂到《白话新解》词条上，生成标准名相表。"""
import csv, re, os
base = os.path.dirname(__file__)
proj = os.path.dirname(base)

def norm(s):
    s = re.sub(r'[（(【].*?[）)】]', '', s)  # 去括注
    s = s.split('（')[0].split('(')[0]
    return s.strip()

# 载入我们的三讲词表
ours = {}
with open(os.path.join(proj, '大乘百法明門論_名词表_第一至三讲.csv'), encoding='utf-8') as f:
    for r in csv.DictReader(f):
        key = norm(r['Chinese'])
        ours[key] = {'skt': r['名词'].strip(), 'en': r['English'].strip(),
                     'fr': r['Français'].strip(), 'vi': r['Tiếng Việt'].strip(),
                     'zh_full': r['Chinese'].strip()}

# 载入白话新解词条
rows = list(csv.DictReader(open(os.path.join(base, 'bhxj_entries.csv'), encoding='utf-8')))

matched = []
for r in rows:
    key = norm(r['名词'])
    o = ours.get(key)
    if o:
        r['English'] = o['en']
        r['Français'] = o['fr']
        r['Tiếng Việt'] = o['vi']
        # 已匹配名相：优先采用我们校订过的规范梵文（含正确音标），修正原书讹误
        if o['skt'] and o['skt'] != '—':
            r['梵文'] = o['skt']
        matched.append((r['名词'], o['zh_full']))

# 输出最终表
out = os.path.join(proj, '唯识名词标准名相表_白话新解.csv')
with open(out, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['名词','梵文','中文释义（白话新解）','English','Français','Tiếng Việt','来源'])
    w.writeheader()
    w.writerows(rows)

print('总词条:', len(rows))
print('已挂四语翻译:', len(matched))
print('匹配到的词条:')
for t, zf in matched:
    print('  ', t, ('（我方词形:'+zf+'）' if t != zf else ''))

# 报告我们词表里未能匹配到白话新解的中文名相（多为专名/典籍/义译短语）
bhxj_keys = {norm(r['名词']) for r in rows}
unmatched = [ (k, v['zh_full']) for k,v in ours.items() if k not in bhxj_keys ]
print('\n我方词表未在白话新解中找到的条目数:', len(unmatched))
for k,zf in unmatched:
    print('   -', zf)
