# -*- coding: utf-8 -*-
"""越南语名相校准映射。

底本：
  TS  = Tuệ Sỹ dịch và chú, 《Luận Thành Duy Thức》(Hồng Đức, 720 tr.)  —— 主
  TSi = Thích Thiện Siêu dịch, 《Thành Duy Thức Luận》(1995)            —— 旁证

数值为 (TS 命中, TSi 命中)，旧名在前、新名在后。
凡上下文抽查为误配者（thức thân = 六识身；thức tỷ = 顿号枚举）一律不改。
"""

# 旧名 -> (新名, 旧证据, 新证据, 理由)
RENAME = {
    # ---- 一、用字与形式：硬错 ----
    'tinh tiến':          ('tinh tấn',        (0, 0),  (32, 35), '越南佛教统一作 tinh tấn；本库自身的 thiện tâm sở 条即已用 tinh tấn'),
    'đệ lục ý thức':      ('thức thứ sáu',    (0, 4),  (53, 85), '汉语序音译不通行'),
    'nhị chướng':         ('hai chướng',      (0, 0),  (21, 1),  '权威用越语数词'),
    'tứ phần':            ('bốn phần',        (0, 0),  (13, 8),  '同上'),
    'thức thể tứ phần':   ('bốn phần của thức', (0, 0), (0, 2),  '同上，并改属格'),
    'tam tính (ba tự tính)': ('ba tự tính',   (0, 0),  (7, 0),   '主名 tam tính 无据，括注形反为权威用语'),
    'huân tập (thọ huân)': ('huân tập',       (191, 145), (191, 145), '去括注；thọ huân 仅 6/7 次且非同义'),

    # ---- 二、词序：权威用越语「中心语在前」，本库误用汉语序 ----
    'A-lại-da thức':        ('thức A-lại-da',       (11, 0),  (41, 0),  '词序'),
    'dị thục thức':         ('thức dị thục',        (20, 30), (24, 74), '词序'),
    'biến hành tâm sở':     ('tâm sở biến hành',    (2, 5),   (6, 24),  '词序'),
    'năm biến hành tâm sở': ('năm tâm sở biến hành',(0, 2),   (1, 3),   '词序'),
    'biệt cảnh tâm sở':     ('tâm sở biệt cảnh',    (0, 2),   (5, 11),  '词序'),
    'thiện tâm sở':         ('tâm sở thiện',        (0, 12),  (15, 9),  '词序'),
    'bất định tâm sở':      ('tâm sở bất định',     (0, 3),   (3, 5),   '词序'),
    'hữu lậu chủng tử':     ('chủng tử hữu lậu',    (0, 0),   (13, 22), '词序'),
    'danh ngôn chủng tử':   ('chủng tử danh ngôn',  (0, 0),   (2, 0),   '词序'),
    'nghiệp chủng tử':      ('chủng tử nghiệp',     (0, 2),   (2, 8),   '词序'),
    'đẳng lưu tập khí':     ('tập khí đẳng lưu',    (0, 0),   (3, 0),   '词序'),
    'dị thục tập khí':      ('tập khí dị thục',     (0, 2),   (3, 0),   '词序'),
    'vô phân biệt trí':     ('trí vô phân biệt',    (8, 1),   (15, 7),  '词序'),

    # ---- 三、三自性：统一为权威的 tự tính + X ----
    'biến kế sở chấp tính': ('tự tính biến kế sở chấp', (0, 0), (5, 0), '三性体例统一'),
    'y tha khởi tính':      ('tự tính y tha khởi',      (5, 0), (1, 0), '三性体例统一'),
    'viên thành thật tính': ('tự tính viên thành thật', (3, 0), (5, 0), '三性体例统一'),
}

# 上下文抽查后明确排除，勿再自动改
EXCLUDED = {
    'thân thức':   'thức thân 实为「六识身 sáu thức thân」，概念不同',
    'tỷ thức':     'thức tỷ 系「hai thức tỷ, thiệt」顿号枚举；且权威用 tỷ 字，本库用字正确',
    'tâm thức':    'tâm thức 为越语通用词，不宜改动',
    'căn bản trí': '两形持平（9 : 13）',
    'hậu đắc trí': '两形持平（40 : 43）',
    'bảy thức trước': '权威作 bảy chuyển thức（七转识），概念范围不同',
    'ba năng biến':   '两形皆无据',
}
