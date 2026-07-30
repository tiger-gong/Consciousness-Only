#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用 DILA Glossaries API 为《白话新解》词条补充规范梵文。

规则（保守抽取，避免把英文释义误当梵文）：
  1) 中文辞典（丁福保/佛光等）："梵Manas"、"梵語 bīja" → 取拉丁串。
  2) DDB（電子佛教辭典）："Basic Meaning: (Skt. manas)" → 括号内 Skt. 后的词。
  3) DDB 裸 Basic Meaning，仅当含梵文变音符（ā ī ū ṛ ṃ ḥ ṅ ñ ṭ ḍ ṇ ś ṣ…）才采纳。
查询必须用繁体（简体在 DILA 返回 0）。仅填补 梵文 为空的条目。
"""
import urllib.parse, urllib.request, json, re, csv, os, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import opencc

BASE = os.path.dirname(__file__)
S2T = opencc.OpenCC('s2t')

# 规范化修正表：来源（书/DDB）只给了无变音符 ASCII 转写或有讹误的条目，
# 统一为学界通用 IAST 标准拼写（这些均为确定无疑的名相/人名）。
SKT_FIX = {
    '三摩地': 'samādhi', '三摩泗多': 'samāhita', '生': 'jāti',
    '世亲': 'Vasubandhu', '天亲': 'Vasubandhu', '火辨': 'Citrabhāna',
    '如来藏': 'tathāgata-garbha', '我': 'ātman', '阿毗跋致': 'avinivartanīya',
    '毗钵舍那': 'vipaśyanā', '唯识': 'vijñapti-mātratā', '净月': 'Śuddhacandra',
    '奢摩他': 'śamatha', '智月': 'Jñānacandra', '亲胜': 'Bandhuśrī',
    '护法': 'Dharmapāla', '胜友': 'Viśeṣamitra', '德慧': 'Guṇamati',
    '有顶天': 'Bhavāgra', '安慧': 'Sthiramati', '难陀': 'Nanda',
    '护月': 'Candragupta', '胜子': 'Jinaputra', '胜军': 'Jayasena',
    '恶叉聚': 'akṣa', '相应': 'yoga',
}

DIAC = 'āīūṛṝḷḹṃḥṅñṭḍṇśṣĀĪŪṚṜḶḸṂḤṄÑṬḌṆŚṢ'
# 拉丁+各类变音符（含扬抑符 â、附点/长音等 Latin Extended 与 Additional 区段）
LATIN = r'A-Za-z\u00c0-\u024f\u1e00-\u1eff'
CONN = r'\-\uff0d\u2013\u2014\u00b7'  # 连字符：ASCII/全角/短破折/中点
TOKEN = r'[' + LATIN + r'][' + LATIN + CONN + r']*'  # 单词或带连字符复合词


def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = s.replace('&quot;', '"').replace('&amp;', '&')
    return re.sub(r'\s+', ' ', s).strip()


def has_diac(s):
    return any(c in DIAC for c in s)


def clean(cand):
    # 全角连字符归一为 ASCII，去英文说明尾巴与首尾杂符
    cand = cand.replace('\uff0d', '-').replace('\u2013', '-')
    cand = re.split(r'\s+(?:DDB|explanation|non-members|之譯)', cand)[0]
    return cand.strip(' -.,;:')


def extract_skt(desc):
    """返回 (梵文, 来源标签) 或 (None, None)。中文辞典优先。

    只采纳明确标注的梵文，弃用 DDB 的 Basic Meaning（那是英文释义字段）。
    """
    # 1) 中文辞典：梵語/梵 紧跟拉丁串（丁福保/佛光，可含空格与连字符复合）
    m = re.search(r'梵(?:語|语|文|名)?\s*[:：]?\s*(' + TOKEN + r'(?:\s' + TOKEN + r')*)', desc)
    if m:
        cand = clean(m.group(1))
        if len(cand) >= 2:
            return cand, 'zh-dict'
    # 1b) 梵名/梵語 + 中文音译 + 拉丁（如「梵名阿僧伽Asaṅga」）
    m = re.search(r'梵(?:語|语|文|名)[\u4e00-\u9fff]{1,8}?(' + TOKEN + r')', desc)
    if m:
        cand = clean(m.group(1))
        if len(cand) >= 2:
            return cand, 'zh-dict'
    # 2) DDB: (Skt. X)，取单个（可连字符）复合词，遇空格即止避免混入英文
    m = re.search(r'Skt\.?\s*(' + TOKEN + r')', desc)
    if m:
        cand = clean(m.group(1))
        if len(cand) >= 2:
            return cand, 'ddb-skt'
    return None, None


def query(term_trad):
    url = 'https://glossaries.dila.edu.tw/search.json?type=match&term=' + urllib.parse.quote(term_trad)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (glossary-builder)'})
    for _ in range(3):
        try:
            return json.load(urllib.request.urlopen(req, timeout=25))
        except Exception:
            continue
    return None


def lookup(row):
    term = row['名词']
    trad = S2T.convert(term)
    data = query(trad)
    if not data:
        return term, None, None
    # 收集所有条目的抽取结果，中文辞典优先，其次 ddb-skt，最后 ddb-basic
    best = {'zh-dict': None, 'ddb-skt': None, 'ddb-basic': None}
    for e in data:
        desc = strip_tags(e.get('desc', ''))
        skt, tag = extract_skt(desc)
        if skt and not best.get(tag):
            best[tag] = skt
    for tag in ('zh-dict', 'ddb-skt', 'ddb-basic'):
        if best[tag]:
            return term, best[tag], tag
    return term, None, None


def main():
    rows = list(csv.DictReader(open(os.path.join(BASE, 'bhxj_entries.csv'), encoding='utf-8')))
    todo = [r for r in rows if not (r.get('梵文') or '').strip()]
    print(f'总词条 {len(rows)}，已有梵文 {len(rows)-len(todo)}，待查 {len(todo)}')
    results = {}
    done = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(lookup, r): r for r in todo}
        for fut in as_completed(futs):
            term, skt, tag = fut.result()
            done += 1
            if skt:
                results[term] = (skt, tag)
            if done % 100 == 0:
                print(f'  进度 {done}/{len(todo)}  已补 {len(results)}', flush=True)
    # 写回
    tagcount = {}
    for r in rows:
        if r['名词'] in results:
            skt, tag = results[r['名词']]
            r['梵文'] = skt
            tagcount[tag] = tagcount.get(tag, 0) + 1
    # 应用规范化修正（无论此前是否有值）
    fixed = 0
    for r in rows:
        if r['名词'] in SKT_FIX and r['梵文'].strip() != SKT_FIX[r['名词']]:
            r['梵文'] = SKT_FIX[r['名词']]
            fixed += 1
    print(f'规范化修正 {fixed} 条')
    out = os.path.join(BASE, 'bhxj_entries.csv')
    with open(out, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['名词', '梵文', '中文释义（白话新解）', 'English', 'Français', 'Tiếng Việt', '来源'])
        w.writeheader(); w.writerows(rows)
    total = sum(1 for r in rows if (r.get('梵文') or '').strip())
    print(f'\n本轮新增梵文 {len(results)}，来源分布 {tagcount}')
    print(f'现在含梵文总数 {total}/{len(rows)}')
    print('新增样本：')
    for t, (s, tag) in list(results.items())[:25]:
        print(f'  {t} -> {s}  [{tag}]')


if __name__ == '__main__':
    main()
