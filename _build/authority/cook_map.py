# -*- coding: utf-8 -*-
"""英文名相 -> Cook《Three Texts on Consciousness Only》用语映射。

值为 (新名, 证据)；证据为该措辞在权威正文中的出现次数，
0 表示权威未直接使用该词形，由同组已证词形按体例推衍（见 note）。
"""

RENAME = {
    # ---- 一、确凿错误 / 专名失准 ----
    'causes and conditions':                  ('condition as cause', 20),
    'perception (conception)':                ('conceptualization', 30),
    'mindfulness (recollection)':             ('memory', 45),
    'concealment (of faults)':                ('dissimulation', 9),
    'dissimulation (flattery)':               ('hypocrisy', 6),

    # ---- 二、基础范畴 ----
    'mental factors':                         ('mental activities', 267),
    'mental-factor dharmas':                  ('dharmas that are mental activities', 0),
    'mind and mental factors':                ('mind and mental activities', 40),
    'six divisions of mental factors':        ('six groups of mental activities', 2),
    'universally active mental factors':      ('universal mental activities', 14),
    'five universally active mental factors': ('five universal mental activities', 2),
    'object-specific mental factors':         ('mental activities with specific objects', 4),
    'wholesome mental factors':               ('good mental activities', 23),
    'indeterminate mental factors':           ('nondetermined mental activities', 0),
    'affliction':                             ('passions', 353),
    'root afflictions':                       ('fundamental passions', 6),
    'mind dharmas':                           ('mind', 0),
    'form dharmas':                           ('form', 815),

    # ---- 三、有漏无漏 / 异熟 / 熏习 ----
    'contaminated (with outflows)':           ('impure', 158),
    'uncontaminated (without outflows)':      ('pure', 460),
    'contaminated seeds':                     ('impure seeds', 12),
    'maturation (ripened result)':            ('retribution', 174),
    'maturation consciousness':               ('consciousness as retribution', 21),
    'matured fruit':                          ('result of retribution', 6),
    'maturation residual impressions':        ('habit energy of retribution', 3),
    'homogeneous-outflow residual impressions': ('habit energy of equal flow', 0),
    'present activity (manifestation)':       ('activity', 152),

    # ---- 四、八识 ----
    'storehouse-consciousness':               ('store consciousness', 69),
    'manas-consciousness':                    ('manas', 184),
    'eye-consciousness':                      ('visual consciousness', 44),
    'ear-consciousness':                      ('auditory consciousness', 3),
    'nose-consciousness':                     ('olfactory consciousness', 0),
    'tongue-consciousness':                   ('gustatory consciousness', 0),
    'body-consciousness':                     ('tactile consciousness', 0),

    # ---- 五、四分 ----
    'image portion (seen portion)':               ('seen part', 42),
    'perceiving portion (seeing portion)':        ('seeing part', 54),
    'self-aware portion':                         ('self-authenticating part', 6),
    're-aware portion (awareness of self-awareness)': ('part that authenticates self-authentication', 2),
    'four portions of the substance of consciousness': ('four parts of consciousness', 5),
    'four portions':                              ('four parts', 5),
    'two-portion school':                         ('two-part school', 0),
    'four-portion school':                        ('four-part school', 0),

    # ---- 六、三性 / 二障 / 四缘 ----
    'imagined nature (thoroughly imagined)':  ('imagined nature', 21),
    'retribution':                            ('karmic result', 0),   # 果报，让位给异熟
    'other-dependent nature':                 ('dependent on others', 62),
    'perfectly accomplished nature':          ('perfected nature', 26),
    'hindrance of afflictions':               ('obstacle of the passions', 24),
    'hindrance to the knowable':              ('obstacle to the knowable', 1),
    'two hindrances':                         ('two obstacles', 13),
    'predominant condition':                  ('dominant condition', 35),
    'object-as-condition':                    ('condition as perceptual object', 1),
    'immediate-antecedent condition':         ('immediately antecedent condition', 35),

    # ---- 七、心所别名 ----
    'concentration':                          ('samādhi', 160),
    'wisdom (discernment)':                   ('discernment', 108),
    'greed':                                  ('craving', 120),
    'non-greed':                              ('noncraving', 14),
    'shame (self-respect)':                   ('conscience', 29),
    'embarrassment (regard for others)':      ('sense of shame', 7),
    'shamelessness':                          ('lack of conscience', 8),      # 无惭
    'non-embarrassment':                      ('shamelessness', 9),           # 无愧（与上条互换，需两阶段改名）
    'conceit (pride)':                        ('pride', 63),
    'diligence (vigor)':                      ('vigor', 28),
    'pliancy (ease)':                         ('serenity', 22),
    'carefulness (non-laxity)':               ('vigilance', 20),
    'equanimity (of formations)':             ('indifference', 48),
    'non-harming':                            ('harmlessness', 7),
    'resentment':                             ('hostility', 8),
    'spite (vexation)':                       ('vexation', 11),
    'stinginess':                             ('avarice', 8),
    'deception':                              ('deceit', 7),
    'haughtiness':                            ('vanity', 7),
    'restlessness':                           ('agitation', 30),
    'lack of faith':                          ('unbelief', 9),
    'laziness':                               ('indolence', 10),
    'laxity (heedlessness)':                  ('negligence', 9),
    'non-introspection (incorrect knowing)':  ('incorrect knowing', 6),
    'sleep (drowsiness)':                     ('sloth', 37),
    'initial inquiry (vitarka)':              ('applied thought', 35),
    'sustained scrutiny (vicāra)':            ('sustained thought', 41),

    # ---- 八、其它 ----
    'suchness':                               ('true suchness', 82),
    'birth-and-death':                        ('birth and death', 30),
    'mind of enlightenment':                  ('thought of enlightenment', 3),
    'selflessness of dharmas':                ('emptiness of dharmas', 17),
    'selflessness of persons':                ('absence of self', 11),
    'subsequently attained wisdom':           ('subsequently acquired knowledge', 30),
    'non-discriminating wisdom':              ('nondiscriminative knowledge', 3),
    # 'Lesser Vehicle' -> 'Hinayana'：已回退，见校准表「刻意保留」一节
}

# 权威未直接给出词形、由同组已证体例推衍者
EXTRAPOLATED = {
    'gustatory consciousness', 'tactile consciousness', 'olfactory consciousness',
    'nondetermined mental activities', 'karmic result',
    'dharmas that are mental activities', 'habit energy of equal flow',
    'two-part school', 'four-part school', 'mind',
}
