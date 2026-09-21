# -*- coding: utf-8 -*-
"""法语名相校准映射。

底本：Hôbôgirin, *Dictionnaire encyclopédique du bouddhisme d'après les sources
chinoises et japonaises*, fasc. I–III (Maison franco-japonaise, 1929–1937)。
括号内数字为该词在 Hôbôgirin 全文中的出现次数。

编辑方针
--------
法语佛学有两套术语传统：
  (1) 古典法-比学派（La Vallée Poussin、Lamotte、Hôbôgirin）——passions / impur /
      rétribution；
  (2) 现代通行辞典（Cornu）——afflictions / contaminé / maturation，受藏传影响。
本库英文已对齐 Cook，而 Cook 的英译正出自古典学派（其 passions、impure、
retribution、part 皆为 La Vallée Poussin 法译的直译），故法语一并归入 (1)，
四语方能互为表里。

Hôbôgirin 自身另有一套高度自创的译名（Notation = 识 287 次、Masse = 蕴、
Coulée = 等流、Actualiser = 现行），属该书体例，不予采用。
"""

# 旧名 -> (新名, 依据)
RENAME = {
    # ---- 一、烦恼 kleśa = passion（Hôbôgirin: Passion(s) 932；affliction 2）----
    'affliction':                       ('passion',                      'Passion(s) 932 : affliction 2'),
    'afflictions-racines':              ('passions fondamentales',       '同上；Cook: fundamental passions'),
    'affliction, karma et souffrance':  ('passion, karma et souffrance', '同上'),
    'obstacle des afflictions':         ('obstacle des passions',        '同上；obstacle 48'),

    # ---- 二、异熟 vipāka = rétribution（rétribution 55；maturation 5）----
    # 果报须先让出 rétribution 一名，与英文 retribution -> karmic result 同理
    'rétribution':                      ('résultat karmique',            '让位给异熟；参英文 karmic result'),
    'maturation (résultat mûri)':       ('rétribution',                  'rétribution 55 : maturation 5'),
    'conscience de maturation':         ('conscience de rétribution',    '同上'),
    'transformateur de maturation':     ('transformateur de rétribution','同上'),
    'fruit mûri':                       ('fruit de rétribution',         '同上'),

    # ---- 三、习气 vāsanā = imprégnation（imprégnation(s) 29；empreinte 0）----
    'empreintes résiduelles de maturation':        ('imprégnations de rétribution',      'imprégnation(s) 29'),
    "empreintes résiduelles d'écoulement homogène": ("imprégnations d'effusion homogène", '同上'),

    # ---- 四、有漏无漏 sāsrava / anāsrava = impur / pur ----
    'contaminé (avec écoulements)':     ('impur (avec écoulement)',      'impur 56、écoulement 111；contaminé 0'),
    'non contaminé (sans écoulements)': ('pur (sans écoulement)',        'pur 441、sans Écoulement 60'),
    'semences contaminées':             ('semences impures',             '同上'),

    # ---- 五、现行 = activité（activité 31）----
    'activité présente (manifestation)':                    ('activité',                                 'activité 31；Cook: activity'),
    "les semences donnant naissance à l'activité présente": ("les semences donnant naissance à l'activité", '同上'),

    # ---- 六、四分 portion -> partie（推衍：Hôbôgirin 无相关条目，据 Cook «part» 回译）----
    'quatre portions':                                        ('quatre parties',                         '推衍'),
    'quatre portions de la substance de la conscience':       ('quatre parties de la conscience',        '推衍；Cook: four parts of consciousness'),
    'portion-image (portion vue)':                            ('partie vue',                             '推衍；Cook: seen part'),
    'portion percevante (portion voyante)':                   ('partie qui voit',                        '推衍；Cook: seeing part'),
    "portion d'auto-connaissance":                            ("partie d'auto-attestation",              '推衍；Cook: self-authenticating part'),
    "portion de ré-connaissance (conscience de l'auto-connaissance)": ("partie qui atteste l'auto-attestation", '推衍'),
    'école des deux portions':                                ('école des deux parties',                 '推衍'),
    'école des quatre portions':                              ('école des quatre parties',               '推衍'),
}

# 推衍条目（权威未直接用此词形）
EXTRAPOLATED = {
    'quatre parties', 'quatre parties de la conscience', 'partie vue', 'partie qui voit',
    "partie d'auto-attestation", "partie qui atteste l'auto-attestation",
    'école des deux parties', 'école des quatre parties',
}

# 零入链的重复条目：删除，其名并入活条目的 aliases
ORPHAN_MERGE = {
    'avidité':   'convoitise',        # 贪；convoitise 17 且有 19 处入链
    'égarement': 'ignorance (moha)',  # 痴；ignorance 9 且有 3 处入链
}

# 明确不改
KEPT = {
    'facteurs mentaux': 'Cornu 等现代法语辞典通行用法，且 Hôbôgirin 无对应条目；'
                        '改作 activités mentales 属纯推衍，影响面过大',
    'conscience-réceptacle': '现代法语通行译名，Hôbôgirin 无覆盖',
    'effusion homogène': 'Hôbôgirin 作 Coulée，属该书自创体例，不采用',
    'équanimité (des formations)': 'équanimité 为地道法语；Cook 改 indifference，'
                                   '但法语 indifférence 贬义过重',
}
