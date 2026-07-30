#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为 83 个高频唯识词补四语词形+梵文，写回 master.json。"""
import json, os
BASE = os.path.dirname(__file__)
VAULT = os.path.dirname(BASE)

# zh: (skt, en, fr, vi)
META = {
'末那识': ('manas', 'manas-consciousness', 'conscience-manas', 'thức mạt-na'),
'阿陀那识': ('ādāna-vijñāna', 'ādāna-consciousness (appropriating consciousness)', 'conscience-ādāna (conscience appropriatrice)', 'thức a-đà-na (thức chấp trì)'),
'三能变': ('', 'three transformers (of consciousness)', 'trois transformateurs (de la conscience)', 'ba năng biến'),
'因能变': ('', 'causal transformer', 'transformateur causal', 'nhân năng biến'),
'果能变': ('', 'resultant transformer', 'transformateur résultant', 'quả năng biến'),
'异熟能变': ('', 'maturation transformer', 'transformateur de maturation', 'dị thục năng biến'),
'思量能变识': ('', 'deliberating transforming consciousness', 'conscience transformante délibérante', 'tư lương năng biến thức'),
'了别境能变': ('', 'object-discerning transformer', 'transformateur discernant les objets', 'liễu biệt cảnh năng biến'),
'七转识': ('', 'seven evolving consciousnesses', 'sept consciences évoluantes', 'bảy chuyển thức'),
'转识': ('', 'evolving consciousness', 'conscience évoluante', 'chuyển thức'),
'三性': ('tri-svabhāva', 'three natures', 'trois natures', 'tam tính (ba tự tính)'),
'遍计所执性': ('parikalpita-svabhāva', 'imagined nature (thoroughly imagined)', 'nature imaginée (complètement conçue)', 'biến kế sở chấp tính'),
'依他起性': ('paratantra-svabhāva', 'other-dependent nature', 'nature dépendante d\'autrui', 'y tha khởi tính'),
'圆成实性': ('pariniṣpanna-svabhāva', 'perfectly accomplished nature', 'nature parfaitement accomplie', 'viên thành thật tính'),
'能遍计': ('', 'that which imagines (the imagining mind)', 'ce qui imagine (l\'esprit imaginant)', 'năng biến kế'),
'所遍计': ('', 'that which is imagined', 'ce qui est imaginé', 'sở biến kế'),
'识体四分': ('', 'four portions of the substance of consciousness', 'quatre portions de la substance de la conscience', 'thức thể tứ phần'),
'见分': ('darśana-bhāga', 'perceiving portion (seeing portion)', 'portion percevante (portion voyante)', 'kiến phần'),
'相分': ('nimitta-bhāga', 'image portion (seen portion)', 'portion-image (portion vue)', 'tướng phần'),
'自证分': ('svasaṃvitti-bhāga', 'self-aware portion', 'portion d\'auto-connaissance', 'tự chứng phần'),
'证自证分': ('', 're-aware portion (awareness of self-awareness)', 'portion de ré-connaissance (conscience de l\'auto-connaissance)', 'chứng tự chứng phần'),
'四分家': ('', 'four-portion school', 'école des quatre portions', 'tứ phần gia'),
'二分家': ('', 'two-portion school', 'école des deux portions', 'nhị phần gia'),
'现行': ('', 'present activity (manifestation)', 'activité présente (manifestation)', 'hiện hành'),
'种子生现行': ('', 'seeds giving rise to present activity', 'les semences donnant naissance à l\'activité présente', 'chủng tử sinh hiện hành'),
'名言种子': ('', 'name-and-word seeds', 'semences des noms-et-paroles', 'danh ngôn chủng tử'),
'业种子': ('karma-bīja', 'karmic seeds', 'semences karmiques', 'nghiệp chủng tử'),
'有漏种子': ('', 'contaminated seeds', 'semences contaminées', 'hữu lậu chủng tử'),
'异熟习气': ('', 'maturation residual impressions', 'empreintes résiduelles de maturation', 'dị thục tập khí'),
'等流习气': ('', 'homogeneous-outflow residual impressions', 'empreintes résiduelles d\'écoulement homogène', 'đẳng lưu tập khí'),
'我执': ('ātma-grāha', 'grasping at a self', 'saisie d\'un soi', 'ngã chấp'),
'法执': ('dharma-grāha', 'grasping at dharmas', 'saisie des dharmas', 'pháp chấp'),
'俱生我执': ('', 'innate grasping at a self', 'saisie innée d\'un soi', 'câu sinh ngã chấp'),
'分别我执': ('', 'discriminative grasping at a self', 'saisie discriminative d\'un soi', 'phân biệt ngã chấp'),
'二我执': ('', 'two kinds of grasping at a self', 'deux sortes de saisie d\'un soi', 'nhị ngã chấp'),
'烦恼障': ('kleśāvaraṇa', 'hindrance of afflictions', 'obstacle des afflictions', 'phiền não chướng'),
'所知障': ('jñeyāvaraṇa', 'hindrance to the knowable', 'obstacle au connaissable', 'sở tri chướng'),
'二障': ('', 'two hindrances', 'deux obstacles', 'nhị chướng'),
'心王': ('citta-rāja', 'mind-king (ruling mind)', 'esprit-roi', 'tâm vương'),
'心所有法': ('caitta', 'mental-factor dharmas', 'dharmas facteurs mentaux', 'tâm sở hữu pháp'),
'六位心所': ('', 'six divisions of mental factors', 'six divisions des facteurs mentaux', 'lục vị tâm sở'),
'五遍行心所': ('', 'five universally active mental factors', 'cinq facteurs mentaux universellement actifs', 'năm biến hành tâm sở'),
'遍行心所': ('', 'universally active mental factors', 'facteurs mentaux universellement actifs', 'biến hành tâm sở'),
'别境心所': ('', 'object-specific mental factors', 'facteurs mentaux spécifiques à l\'objet', 'biệt cảnh tâm sở'),
'善心所': ('', 'wholesome mental factors', 'facteurs mentaux salutaires', 'thiện tâm sở'),
'根本烦恼': ('mūla-kleśa', 'root afflictions', 'afflictions-racines', 'căn bản phiền não'),
'不定心所': ('', 'indeterminate mental factors', 'facteurs mentaux indéterminés', 'bất định tâm sở'),
'眼识': ('cakṣur-vijñāna', 'eye-consciousness', 'conscience visuelle', 'nhãn thức'),
'耳识': ('śrotra-vijñāna', 'ear-consciousness', 'conscience auditive', 'nhĩ thức'),
'鼻识': ('ghrāṇa-vijñāna', 'nose-consciousness', 'conscience olfactive', 'tỷ thức'),
'舌识': ('jihvā-vijñāna', 'tongue-consciousness', 'conscience gustative', 'thiệt thức'),
'身识': ('kāya-vijñāna', 'body-consciousness', 'conscience corporelle', 'thân thức'),
'意识': ('mano-vijñāna', 'mental consciousness', 'conscience mentale', 'ý thức'),
'意根': ('mana-indriya', 'mental faculty', 'faculté mentale', 'ý căn'),
'五境': ('', 'five sense-objects', 'cinq objets des sens', 'năm cảnh'),
'六境': ('', 'six sense-objects', 'six objets des sens', 'sáu cảnh'),
'六根': ('ṣaḍ-indriya', 'six sense-faculties', 'six facultés sensorielles', 'sáu căn'),
'五蕴': ('pañca-skandha', 'five aggregates', 'cinq agrégats', 'năm uẩn'),
'十二处': ('dvādaśāyatana', 'twelve sense-bases', 'douze bases sensorielles', 'mười hai xứ'),
'十八界': ('aṣṭādaśa-dhātu', 'eighteen elements', 'dix-huit éléments', 'mười tám giới'),
'有漏': ('sāsrava', 'contaminated (with outflows)', 'contaminé (avec écoulements)', 'hữu lậu'),
'无漏': ('anāsrava', 'uncontaminated (without outflows)', 'non contaminé (sans écoulements)', 'vô lậu'),
'有覆无记': ('nivṛtāvyākṛta', 'obscuring-neutral', 'neutre-obscurcissant', 'hữu phú vô ký'),
'无覆无记': ('anivṛtāvyākṛta', 'non-obscuring-neutral', 'neutre-non-obscurcissant', 'vô phú vô ký'),
'异熟': ('vipāka', 'maturation (ripened result)', 'maturation (résultat mûri)', 'dị thục'),
'异熟识': ('vipāka-vijñāna', 'maturation consciousness', 'conscience de maturation', 'dị thục thức'),
'异熟果': ('vipāka-phala', 'matured fruit', 'fruit mûri', 'dị thục quả'),
'四缘': ('catuḥ-pratyaya', 'four conditions', 'quatre conditions', 'bốn duyên'),
'所缘缘': ('ālambana-pratyaya', 'object-as-condition', 'condition-objet', 'sở duyên duyên'),
'等无间缘': ('samanantara-pratyaya', 'immediate-antecedent condition', 'condition d\'antécédent immédiat', 'đẳng vô gián duyên'),
'增上缘': ('adhipati-pratyaya', 'predominant condition', 'condition prédominante', 'tăng thượng duyên'),
'无分别智': ('nirvikalpajñāna', 'non-discriminating wisdom', 'sagesse non discriminative', 'vô phân biệt trí'),
'后得智': ('pṛṣṭhalabdha-jñāna', 'subsequently attained wisdom', 'sagesse ultérieurement obtenue', 'hậu đắc trí'),
'根本智': ('mūla-jñāna', 'fundamental wisdom', 'sagesse fondamentale', 'căn bản trí'),
'赖耶缘起': ('', 'ālaya-based dependent arising', 'coproduction fondée sur l\'ālaya', 'lại-da duyên khởi'),
'阿赖耶缘起': ('', 'ālaya-based dependent arising', 'coproduction fondée sur l\'ālaya', 'a-lại-da duyên khởi'),
'唯识无境': ('', 'consciousness-only, no [external] objects', 'rien-que-conscience, pas d\'objets [externes]', 'duy thức vô cảnh'),
'五重唯识观': ('', 'fivefold contemplation of consciousness-only', 'quintuple contemplation du rien-que-conscience', 'ngũ trùng duy thức quán'),
'成唯识论': ('Vijñaptimātratāsiddhi', 'Treatise on the Establishment of Consciousness-Only', 'Traité de l\'établissement du Rien-que-conscience', 'Thành Duy Thức Luận'),
'安慧': ('Sthiramati', 'Sthiramati', 'Sthiramati', 'An Huệ (Sthiramati)'),
'护法': ('Dharmapāla', 'Dharmapāla', 'Dharmapāla', 'Hộ Pháp (Dharmapāla)'),
'窥基': ('', 'Kuiji', 'Kuiji', 'Khuy Cơ'),
'戒贤': ('Śīlabhadra', 'Śīlabhadra', 'Śīlabhadra', 'Giới Hiền (Śīlabhadra)'),
}

master = json.load(open(os.path.join(BASE, 'master.json'), encoding='utf-8'))
updated = 0
for e in master:
    if e['zh'] in META:
        skt, en, fr, vi = META[e['zh']]
        if skt and not e.get('skt'):
            e['skt'] = skt
        elif skt:
            e['skt'] = skt  # 优先用规范梵文
        e['en'] = en
        e['fr'] = fr
        e['vi'] = vi
        updated += 1
json.dump(master, open(os.path.join(BASE, 'master.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# 另存 meta 便于复查
json.dump(META, open(os.path.join(BASE, 'core83_meta.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'已更新 master 词形 {updated}/{len(META)}')
# 缺漏？
have = {e['zh'] for e in master}
for t in META:
    if t not in have:
        print('MISSING IN MASTER', t)
