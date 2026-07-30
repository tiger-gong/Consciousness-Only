#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""解析《唯识名词白话新解》(于凌波) 三卷 HTML，抽取词条。"""
import re, html, csv, glob, os

def strip_tags(s):
    s = re.sub(r'(?is)<script.*?</script>', '', s)
    s = re.sub(r'(?is)<style.*?</style>', '', s)
    s = re.sub(r'(?s)<[^>]+>', '', s)
    s = html.unescape(s)
    return s

text_all = []
for fn in ['bhxj_2085.html','bhxj_2086.html','bhxj_2087.html']:
    raw = open(os.path.join(os.path.dirname(__file__), fn), encoding='utf-8', errors='ignore').read()
    text_all.append(strip_tags(raw))
text = '\n'.join(text_all)

# 规范空白：把全角空格与多余空白压缩，但保留换行用于分段
text = text.replace('\u3000', ' ')
# 词条以【…】开头。用【 作为分隔符切分。
# 先找到第一个词条位置，丢弃前面的序言/目录。
parts = text.split('【')
entries = []
for p in parts[1:]:
    if '】' not in p:
        continue
    term, rest = p.split('】', 1)
    term = term.strip()
    # 释义：截到下一处笔画标题或结尾。清理换行/多空格。
    desc = rest
    # 去掉行尾出现的“X划”“XX划”单独成行的笔画标题及页面噪音
    desc = re.sub(r'\n\s*[一二三四五六七八九十百]+划\s*\n', '\n', desc)
    desc = re.sub(r'\s+', ' ', desc).strip()
    # 词条名过滤：应为较短的中文名相
    if not term or len(term) > 20:
        continue
    if not re.search(r'[\u4e00-\u9fff]', term):
        continue
    # 截断释义末尾可能混入的下一卷标题/版权噪音
    desc = re.split(r'(?:唯识名词白话新解|简明成唯识论|返回目录|回目录|Copyright|版权所有)', desc)[0].strip()
    if len(desc) < 2:
        continue
    entries.append((term, desc))

# 去重（同名词条保留首个，通常只出现一次）
seen = {}
order = []
for t, d in entries:
    if t not in seen:
        seen[t] = d
        order.append(t)
    else:
        # 若重复且释义不同，合并
        if d not in seen[t]:
            seen[t] = seen[t] + ' ／（又）' + d

# 抽取梵文：从释义中找“梵语 xxx”“梵名 xxx”“梵 xxx”
def extract_skt(desc):
    m = re.search(r'梵(?:语|名|文)?\s*([A-Za-zĀ-ɏāīūṛṝḷṃḥṅñṭḍṇśṣĀĪŪṚṜḶṂḤṄÑṬḌṆŚṢ][A-Za-zĀ-ɏāīūṛṝḷṃḥṅñṭḍṇśṣ\-\u00c0-\u017f]*)', desc)
    return m.group(1) if m else ''

rows = []
for t in order:
    d = seen[t]
    rows.append({'名词': t, '梵文': extract_skt(d), '中文释义（白话新解）': d,
                 'English': '', 'Français': '', 'Tiếng Việt': '',
                 '来源': '唯识名词白话新解'})

out = os.path.join(os.path.dirname(__file__), 'bhxj_entries.csv')
with open(out, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['名词','梵文','中文释义（白话新解）','English','Français','Tiếng Việt','来源'])
    w.writeheader()
    w.writerows(rows)

print('词条总数:', len(rows))
print('含梵文抽取:', sum(1 for r in rows if r['梵文']))
print('示例:')
for r in rows[:8]:
    print(' ', r['名词'], '|', (r['梵文'] or '-'), '|', r['中文释义（白话新解）'][:40])
print('...')
# 打印几个关键唯识名相确认解析正确
for key in ['阿赖耶识','种子','末那识','遍计所执','转识成智','三自性']:
    if key in seen:
        print('[OK]', key, '->', seen[key][:50])
    else:
        print('[MISS]', key)
