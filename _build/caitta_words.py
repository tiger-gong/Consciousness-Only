#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""心所细目：写入短名主词条（释义取自××心所）+ 四语词形。"""
import json, os
BASE = os.path.dirname(__file__)

# short: (src_key or None, skt, en, fr, vi)  src_key=None 表示自写释义
META = {
'作意': ('作意心所', 'manaskāra', 'attention (mental engagement)', 'attention (application de l\'esprit)', 'tác ý'),
'触': ('触心所', 'sparśa', 'contact', 'contact', 'xúc'),
'受': ('受心所', 'vedanā', 'feeling (sensation)', 'sensation (vedanā)', 'thọ'),
'想': ('想心所', 'saṃjñā', 'perception (conception)', 'perception (notion)', 'tưởng'),
'思': ('思心所', 'cetanā', 'volition', 'volition (cetanā)', 'tư'),
'欲': ('欲', 'chanda', 'desire (aspiration)', 'désir (aspiration)', 'dục'),
'胜解': ('胜解心所', 'adhimokṣa', 'resolution (decisive understanding)', 'résolution (compréhension décisive)', 'thắng giải'),
'念': ('念心所', 'smṛti', 'mindfulness (recollection)', 'attention mémorielle (smṛti)', 'niệm'),
'定': ('定心所', 'samādhi', 'concentration', 'concentration (samādhi)', 'định'),
'慧': ('慧心所', 'prajñā', 'wisdom (discernment)', 'sagesse (discernement)', 'tuệ'),
'信': ('信心所', 'śraddhā', 'faith', 'foi', 'tín'),
'精进': ('精进心所', 'vīrya', 'diligence (vigor)', 'énergie (diligence)', 'tinh tiến'),
'惭': ('惭心所', 'hrī', 'shame (self-respect)', 'pudeur (respect de soi)', 'tàm'),
'愧': ('愧心所', 'apatrāpya', 'embarrassment (regard for others)', 'décence (égard pour autrui)', 'quý'),
'无贪': ('无贪心所', 'alobha', 'non-greed', 'non-convoitise', 'vô tham'),
'无瞋': (None, 'adveṣa', 'non-hatred', 'non-haine', 'vô sân'),
'无痴': ('无痴心所', 'amoha', 'non-delusion', 'non-ignorance', 'vô si'),
'轻安': ('轻安心所', 'praśrabdhi', 'pliancy (ease)', 'flexibilité (aisance)', 'khinh an'),
'不放逸': ('不放逸心所', 'apramāda', 'carefulness (non-laxity)', 'vigilance (non-négligence)', 'bất phóng dật'),
'行舍': ('行舍心所', 'upekṣā', 'equanimity (of formations)', 'équanimité (des formations)', 'hành xả'),
'不害': ('不害心所', 'avihiṃsā', 'non-harming', 'non-nuisance', 'bất hại'),
'贪': ('贪心所', 'rāga', 'greed', 'convoitise', 'tham'),
'瞋': (None, 'dveṣa', 'hatred', 'haine', 'sân'),
'痴': ('痴心所', 'moha', 'delusion', 'ignorance (moha)', 'si'),
'慢': ('慢', 'māna', 'conceit (pride)', 'orgueil', 'mạn'),
'疑': ('疑', 'vicikitsā', 'doubt', 'doute', 'nghi'),
'恶见': ('恶见心所', 'dṛṣṭi', 'wrong view', 'vue fausse', 'ác kiến'),
'忿': ('忿心所', 'krodha', 'anger (fury)', 'colère (emportement)', 'phẫn'),
'恨': ('恨心所', 'upanāha', 'resentment', 'rancune', 'hận'),
'恼': ('恼心所', 'pradāśa', 'spite (vexation)', 'malveillance (irritation)', 'não'),
'覆': ('覆心所', 'mrakṣa', 'concealment (of faults)', 'dissimulation (des fautes)', 'phú'),
'诳': ('诳心所', 'māyā', 'deception', 'tromperie', 'cuống'),
'谄': ('谄心所', 'śāṭhya', 'dissimulation (flattery)', 'duplicité (flatterie)', 'siểm'),
'憍': ('憍心所', 'mada', 'haughtiness', 'arrogance', 'kiêu'),
'害': ('害心所', 'vihiṃsā', 'harmfulness', 'nuisance', 'hại'),
'嫉': ('嫉心所', 'īrṣyā', 'envy', 'envie', 'tật'),
'悭': ('悭心所', 'mātsarya', 'stinginess', 'avarice', 'xan'),
'无惭': ('无惭心所', 'āhrīkya', 'shamelessness', 'impudeur', 'vô tàm'),
'无愧': ('无愧心所', 'anapatrāpya', 'non-embarrassment', 'indécence', 'vô quý'),
'掉举': ('掉举心所', 'auddhatya', 'restlessness', 'agitation', 'trạo cử'),
'昏沉': (None, 'styāna', 'torpor', 'torpeur', 'hôn trầm'),
'不信': ('不信心所', 'āśraddhya', 'lack of faith', 'défaut de foi', 'bất tín'),
'懈怠': ('懈怠心所', 'kausīdya', 'laziness', 'paresse', 'giải đãi'),
'放逸': ('放逸心所', 'pramāda', 'laxity (heedlessness)', 'négligence', 'phóng dật'),
'失念': ('失念心所', 'muṣitasmṛtitā', 'forgetfulness', 'oubli', 'thất niệm'),
'散乱': ('散乱心所', 'vikṣepa', 'distraction', 'distraction', 'tán loạn'),
'不正知': ('不正知心所', 'asaṃprajanya', 'non-introspection (incorrect knowing)', 'non-introspection', 'bất chính tri'),
'悔': ('悔心所', 'kaukṛtya', 'regret (remorse)', 'remords', 'hối'),
'眠': ('眠心所', 'middha', 'sleep (drowsiness)', 'sommeil (assoupissement)', 'miên'),
'寻': ('寻心所', 'vitarka', 'initial inquiry (vitarka)', 'investigation initiale (vitarka)', 'tầm'),
'伺': (None, 'vicāra', 'sustained scrutiny (vicāra)', 'investigation soutenue (vicāra)', 'tứ'),
}

# 自写缺条中文释义
HAND_DEF = {
'无瞋': "此为心所有法中的十一善心所之一。无瞋是于苦及苦具不生嗔恚。《成唯识论》曰：‘云何无嗔，于苦苦具无恚为性，对治嗔恚，作善为业。’苦指三苦等逼恼，苦具指能生苦之因缘。无嗔以慈愍为用，能予有情安乐，对治嗔恚而助成诸善。",
'瞋': "此为心所有法中的根本烦恼心所之一。嗔是于苦及苦具起憎恚，欲加损害的精神作用。《成唯识论》曰：‘云何为嗔，于苦苦具憎恚为性，能障无嗔，不安隐性，恶行所依为业。’嗔能障无嗔，令身心热恼不安，并依之造作恶业。",
'昏沉': "此为心所有法中的大随烦恼心所之一。昏沉令心于境不明了，沉重暗昧，障碍轻安与毗钵舍那（观）。《成唯识论》曰：‘云何昏沉，令心于境无堪任为性，能障轻安毗钵舍那为业。’",
'伺': "此为心所有法中的不定心所之一。伺者伺察，对事理精细深入的思考。《成唯识论》曰：‘伺谓伺察，令心偬遽，于意言境，细转为性。’寻为粗转，伺为细转，二者皆令心急遽转于意言境。",
}

master = json.load(open(os.path.join(BASE, 'master.json'), encoding='utf-8'))
by = {e['zh']: e for e in master}
added = updated = 0
for short, (src, skt, en, fr, vi) in META.items():
    if src and src in by and by[src].get('zh_def'):
        zh_def = by[src]['zh_def']
    elif short in HAND_DEF:
        zh_def = HAND_DEF[short]
    else:
        print('NO DEF', short); continue
    if short in by:
        e = by[short]
        e['zh_def'] = zh_def or e.get('zh_def')
        e['skt'] = skt or e.get('skt') or ''
        e['en'], e['fr'], e['vi'] = en, fr, vi
        if not e.get('source'):
            e['source'] = '唯识名词白话新解' if src else '补写'
        updated += 1
    else:
        master.append({
            'zh': short, 'skt': skt, 'zh_def': zh_def,
            'en': en, 'fr': fr, 'vi': vi,
            'source': '唯识名词白话新解' if src else '补写',
        })
        added += 1

json.dump(master, open(os.path.join(BASE, 'master.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(META, open(os.path.join(BASE, 'caitta_meta.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'新增 {added}，更新 {updated}，合计心所短名 {len(META)}')
