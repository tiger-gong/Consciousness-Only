#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""无释义条目——典籍（补写简短中文释义 zh + 三语）。"""
import json, os
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))

D['百法明门论直解'] = {
 'zh': "明代蕅益大师（智旭）对《大乘百法明门论》所作的注解，逐句直释论文，为汉传学习百法的重要注本之一。",
 'en': "A commentary on the Treatise on the Hundred Dharmas by the Ming-dynasty master Ǒuyì (Zhixu), giving a direct, line-by-line explanation of the treatise; it is one of the important commentaries for studying the hundred dharmas in Chinese Buddhism.",
 'fr': "Un commentaire du Traité des Cent Dharmas par le maître Ǒuyì (Zhixu) sous les Ming, donnant une explication directe, ligne à ligne, du traité ; c'est l'un des commentaires importants pour l'étude des cent dharmas dans le bouddhisme chinois.",
 'vi': "Bản chú giải Đại Thừa Bách Pháp Minh Môn Luận của Đại sư Ngẫu Ích (Trí Húc) đời Minh, giải thích trực tiếp từng câu luận văn; là một trong những bản chú quan trọng để học bách pháp trong Phật giáo Hán truyền.",
}

D['瑜伽师地论'] = {
 'zh': "弥勒菩萨说、无著记录，玄奘译，凡百卷。瑜伽行学派根本论典，广说三乘境、行、果，尤以‘十七地’为纲，故名瑜伽师地论。",
 'en': "Expounded by the bodhisattva Maitreya and recorded by Asaṅga, translated by Xuanzang; in one hundred fascicles. The foundational treatise of the Yogācāra school, it expounds at length the objects, practices, and fruits of the three vehicles, structured especially around the \u201cseventeen stages,\u201d whence its name.",
 'fr': "Exposé par le bodhisattva Maitreya et consigné par Asaṅga, traduit par Xuanzang ; en cent fascicules. Traité fondamental de l'école Yogācāra, il expose en détail les objets, pratiques et fruits des trois véhicules, structuré notamment autour des « dix-sept stades », d'où son nom.",
 'vi': "Do Bồ Tát Di-lặc thuyết, Vô Trước ghi chép, Huyền Trang dịch; gồm trăm quyển. Là bộ luận căn bản của học phái Du Già, nói rộng cảnh, hành, quả của ba thừa, đặc biệt lấy “mười bảy địa” làm cương, nên gọi Du Già Sư Địa Luận.",
}

D['大毘婆沙论'] = {
 'zh': "全称《阿毗达磨大毗婆沙论》，玄奘译，凡二百卷。说一切有部集大成的论书，广释《发智论》，为部派佛教教义之渊薮。",
 'en': "Fully titled the Abhidharma-mahāvibhāṣā-śāstra, translated by Xuanzang; in two hundred fascicles. The magnum opus of the Sarvāstivāda school, an extensive commentary on the Jñānaprasthāna, it is a treasury of the doctrines of sectarian (Abhidharma) Buddhism.",
 'fr': "Titre complet : Abhidharma-mahāvibhāṣā-śāstra, traduit par Xuanzang ; en deux cents fascicules. Œuvre maîtresse de l'école Sarvāstivāda, vaste commentaire du Jñānaprasthāna, c'est un trésor des doctrines du bouddhisme sectaire (Abhidharma).",
 'vi': "Toàn xưng A-tì-đạt-ma Đại Tì-bà-sa Luận, Huyền Trang dịch; gồm hai trăm quyển. Là bộ luận tập đại thành của Thuyết Nhất Thiết Hữu Bộ, giải thích rộng Phát Trí Luận, là kho tàng giáo nghĩa của Phật giáo bộ phái.",
}

D['阿毘达磨俱舍论'] = {
 'zh': "世亲菩萨造，玄奘译，凡三十卷。略称《俱舍论》，总结说一切有部教义并加以批判，立五位七十五法，为部派佛教的代表论书。",
 'en': "Composed by the bodhisattva Vasubandhu, translated by Xuanzang; in thirty fascicles. Abbreviated the Kośa, it summarizes and critically examines the doctrines of the Sarvāstivāda, establishing the Five Categories and Seventy-five Dharmas; it is the representative treatise of sectarian Buddhism.",
 'fr': "Composé par le bodhisattva Vasubandhu, traduit par Xuanzang ; en trente fascicules. Abrégé en Kośa, il résume et examine de façon critique les doctrines du Sarvāstivāda, établissant les Cinq Catégories et Soixante-quinze Dharmas ; c'est le traité représentatif du bouddhisme sectaire.",
 'vi': "Do Bồ Tát Thế Thân tạo, Huyền Trang dịch; gồm ba mươi quyển. Gọi tắt Câu-xá Luận, tổng kết và phê phán giáo nghĩa Thuyết Nhất Thiết Hữu Bộ, lập Ngũ vị thất thập ngũ pháp; là bộ luận tiêu biểu của Phật giáo bộ phái.",
}

D['法华经'] = {
 'zh': "全称《妙法莲华经》，鸠摩罗什译，凡七卷。大乘要典，倡‘会三归一’、开权显实，宣一切众生皆可成佛，为天台宗所依根本经。",
 'en': "Fully titled the Saddharmapuṇḍarīka-sūtra (Lotus Sūtra of the Wondrous Dharma), translated by Kumārajīva; in seven fascicles. A key Mahāyāna scripture, it teaches the \u201cconvergence of the three vehicles into the one,\u201d revealing the real through the provisional, and proclaims that all beings can attain Buddhahood; it is the root scripture of the Tiantai school.",
 'fr': "Titre complet : Saddharmapuṇḍarīka-sūtra (Sūtra du Lotus du Dharma merveilleux), traduit par Kumārajīva ; en sept fascicules. Écriture Mahāyāna clé, elle enseigne la « convergence des trois véhicules en l'un », révélant le réel à travers le provisoire, et proclame que tous les êtres peuvent atteindre la bouddhéité ; c'est l'écriture-racine de l'école Tiantai.",
 'vi': "Toàn xưng Diệu Pháp Liên Hoa Kinh, Cưu-ma-la-thập dịch; gồm bảy quyển. Là kinh yếu Đại thừa, xướng “hội tam quy nhất”, khai quyền hiển thật, tuyên bố hết thảy chúng sinh đều có thể thành Phật; là kinh căn bản mà Thiên Thai tông y cứ.",
}

D['金刚经'] = {
 'zh': "全称《金刚般若波罗蜜经》，鸠摩罗什译，一卷。般若部要典，说一切法空、无住生心、破我法二执，汉地流通极广。",
 'en': "Fully titled the Vajracchedikā-prajñāpāramitā-sūtra (Diamond Sūtra), translated by Kumārajīva; in one fascicle. A key text of the Prajñāpāramitā corpus, it teaches the emptiness of all dharmas, giving rise to the mind without abiding anywhere, and the breaking of the two graspings at self and dharmas; it is very widely circulated in China.",
 'fr': "Titre complet : Vajracchedikā-prajñāpāramitā-sūtra (Sūtra du Diamant), traduit par Kumārajīva ; en un fascicule. Texte clé du corpus de la Prajñāpāramitā, il enseigne la vacuité de tous les dharmas, faire naître l'esprit sans demeurer nulle part, et la rupture des deux saisies du soi et des dharmas ; il est très largement diffusé en Chine.",
 'vi': "Toàn xưng Kim Cang Bát-nhã Ba-la-mật Kinh, Cưu-ma-la-thập dịch; một quyển. Là kinh yếu thuộc bộ Bát-nhã, nói hết thảy pháp không, vô trụ sinh tâm, phá hai chấp ngã pháp; lưu thông rất rộng ở Hán địa.",
}

D['婆薮盘豆传'] = {
 'zh': "陈代真谛译，一卷。记述天亲（世亲，梵名婆薮盘豆）菩萨及其兄无著的生平事迹，为研究唯识祖师的重要传记。",
 'en': "Translated by Paramārtha in the Chen dynasty; in one fascicle. A biography recording the life and deeds of the bodhisattva Vasubandhu (Sanskrit Vasubandhu, transliterated Posoupandou) and his elder brother Asaṅga; an important biographical source for studying the Consciousness-Only patriarchs.",
 'fr': "Traduit par Paramārtha sous les Chen ; en un fascicule. Une biographie relatant la vie et les actes du bodhisattva Vasubandhu (sanskrit Vasubandhu) et de son frère aîné Asaṅga ; source biographique importante pour l'étude des patriarches du Rien-que-conscience.",
 'vi': "Chân Đế dịch đời Trần; một quyển. Ghi thuật cuộc đời sự tích của Bồ Tát Thiên Thân (Thế Thân, Phạn danh Bà-tẩu-bàn-đậu) và anh ngài là Vô Trước; là bộ truyện quan trọng để nghiên cứu chư tổ Duy Thức.",
}

D['邪因缘论'] = {
 'zh': "外道的一种错误因果见，主张万物由不平等、不相应的错误原因（如大自在天、时、方等）所生，非佛法正因缘。",
 'en': "A mistaken view of causation held by outer paths, asserting that all things are produced by wrong, unequal, and incongruous causes (such as Maheśvara, time, or space); it is not the correct causation of the Buddha-Dharma.",
 'fr': "Une vue erronée de la causalité soutenue par les voies extérieures, affirmant que toutes choses sont produites par des causes fausses, inégales et incongrues (tels Maheśvara, le temps ou l'espace) ; ce n'est pas la causalité correcte du Dharma.",
 'vi': "Một thứ tà kiến về nhân quả của ngoại đạo, chủ trương vạn vật do những nguyên nhân sai lầm, bất bình đẳng, bất tương ứng (như Đại Tự Tại Thiên, thời, phương v.v.) sinh ra; chẳng phải chính nhân duyên của Phật pháp.",
}

D['无因缘论'] = {
 'zh': "外道的一种断见，主张万物无因自然而生、自然而灭，否定因果，属邪见。",
 'en': "A nihilistic view held by outer paths, asserting that all things arise and perish spontaneously without any cause, thereby denying cause and effect; it is a wrong view.",
 'fr': "Une vue nihiliste soutenue par les voies extérieures, affirmant que toutes choses naissent et périssent spontanément sans aucune cause, niant ainsi la cause et l'effet ; c'est une vue fausse.",
 'vi': "Một thứ đoạn kiến của ngoại đạo, chủ trương vạn vật vô nhân tự nhiên sinh, tự nhiên diệt, phủ định nhân quả; thuộc tà kiến.",
}

D['本地分'] = {
 'zh': "《瑜伽师地论》五分中的第一分，广说‘十七地’的境相，为全论的主体与根本，《百法明门论》的百法名数即摘自此分。",
 'en': "The first of the five parts of the Yogācārabhūmi-śāstra, expounding at length the objects and characteristics of the \u201cseventeen stages\u201d; it is the main body and foundation of the whole treatise, and the enumeration of the hundred dharmas in the Treatise on the Hundred Dharmas is drawn from it.",
 'fr': "La première des cinq parties du Yogācārabhūmi-śāstra, exposant en détail les objets et caractéristiques des « dix-sept stades » ; c'est le corps principal et le fondement de tout le traité, et l'énumération des cent dharmas du Traité des Cent Dharmas en est tirée.",
 'vi': "Phần thứ nhất trong năm phần của Du Già Sư Địa Luận, nói rộng cảnh tướng của “mười bảy địa”; là chủ thể và căn bản của toàn luận, danh số bách pháp trong Bách Pháp Minh Môn Luận chính là trích từ phần này.",
}

json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('batch_D1 →', len(D))
