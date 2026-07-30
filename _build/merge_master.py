#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并两份词表为统一主数据 master.json。

来源：
  A) 唯识名词标准名相表_白话新解.csv (1507)  列: 名词(中文), 梵文, 中文释义（白话新解）, English, Français, Tiếng Việt, 来源
  B) 大乘百法明門論_名词表_第一至三讲.csv (140) 列: 名词(梵文), Chinese, English, Français, Tiếng Việt

以 A 为主体（含中文释义），用 B 的四语词形补充/覆盖（B 为讲义人工校订，优先）。
输出每条：zh(中文词), skt(梵文), zh_def(中文释义), en/fr/vi(各语词形), source。
"""
import csv, json, os, re

BASE = os.path.dirname(__file__)
VAULT = os.path.dirname(BASE)


def norm(s):
    s = (s or '').strip()
    s = re.sub(r'[（(【].*?[）)】]', '', s)
    return s.split('（')[0].split('(')[0].strip()


A = list(csv.DictReader(open(os.path.join(VAULT, '唯识名词标准名相表_白话新解.csv'), encoding='utf-8')))
B = list(csv.DictReader(open(os.path.join(VAULT, '大乘百法明門論_名词表_第一至三讲.csv'), encoding='utf-8')))

# 建立 B 的中文->词形 索引（人工校订，优先）
bidx = {}
for r in B:
    zh = norm(r.get('Chinese', ''))
    if not zh:
        continue
    bidx[zh] = {
        'skt': (r.get('名词') or '').strip(),
        'en': (r.get('English') or '').strip(),
        'fr': (r.get('Français') or '').strip(),
        'vi': (r.get('Tiếng Việt') or '').strip(),
    }

master = []
seen = set()
for r in A:
    zh = (r.get('名词') or '').strip()
    if not zh or zh in seen:
        continue
    seen.add(zh)
    b = bidx.get(norm(zh), {})
    skt = b.get('skt') or (r.get('梵文') or '').strip()
    if skt == '—':
        skt = ''
    entry = {
        'zh': zh,
        'skt': skt,
        'zh_def': (r.get('中文释义（白话新解）') or '').strip(),
        'en': b.get('en') or (r.get('English') or '').strip(),
        'fr': b.get('fr') or (r.get('Français') or '').strip(),
        'vi': b.get('vi') or (r.get('Tiếng Việt') or '').strip(),
        'source': (r.get('来源') or '').strip(),
    }
    master.append(entry)

# B 中有、A 中没有的中文词（讲义专名/典籍等），补进来（无中文释义）
for zh, b in bidx.items():
    if zh not in seen and zh and zh != '—':
        seen.add(zh)
        master.append({'zh': zh, 'skt': b['skt'] if b['skt'] != '—' else '',
                        'zh_def': '', 'en': b['en'], 'fr': b['fr'], 'vi': b['vi'],
                        'source': '讲义名词表'})

out = os.path.join(BASE, 'master.json')
json.dump(master, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 统计
n = len(master)
has_def = sum(1 for e in master if e['zh_def'])
has_all_words = sum(1 for e in master if e['en'] and e['fr'] and e['vi'])
has_any_word = sum(1 for e in master if e['en'] or e['fr'] or e['vi'])
has_skt = sum(1 for e in master if e['skt'])
print(f'总词条: {n}')
print(f'  有中文释义: {has_def}')
print(f'  有梵文: {has_skt}')
print(f'  英/法/越词形齐全: {has_all_words}')
print(f'  至少有一种译词: {has_any_word}')
print(f'  既有中文释义又四语词齐全（最佳完整候选）: {sum(1 for e in master if e["zh_def"] and e["en"] and e["fr"] and e["vi"])}')
print('\n示例（四语齐全的前 8 条）:')
for e in [e for e in master if e['en'] and e['fr'] and e['vi']][:8]:
    print(f'  {e["zh"]}｜{e["skt"]}｜EN:{e["en"]}｜FR:{e["fr"]}｜VI:{e["vi"]}｜def:{"有" if e["zh_def"] else "无"}')
