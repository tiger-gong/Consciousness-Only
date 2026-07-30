#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))

D['天台宗'] = {
 'zh': "汉传大乘八宗之一，隋代智者大师依《法华经》创立，判教立五时八教，主‘一念三千’‘一心三观’‘性具’之说。",
 'en': "One of the eight Mahāyāna schools of China, founded by the Sui-dynasty master Zhiyi on the basis of the Lotus Sūtra. It classifies the teachings into the five periods and eight teachings and upholds the doctrines of \u201cthree thousand worlds in a single thought,\u201d \u201cthe threefold contemplation in one mind,\u201d and \u201cnature-inclusion.\u201d",
 'fr': "L'une des huit écoles Mahāyāna de Chine, fondée par le maître Zhiyi sous les Sui sur la base du Sūtra du Lotus. Elle classe les enseignements en cinq périodes et huit enseignements et soutient les doctrines des « trois mille mondes en une seule pensée », de la « triple contemplation en un seul esprit » et de l'« inclusion par nature ».",
 'vi': "Một trong tám tông Đại thừa Hán truyền, do Trí Giả đại sư đời Tùy y Kinh Pháp Hoa sáng lập. Phán giáo lập ngũ thời bát giáo, chủ trương “nhất niệm tam thiên”, “nhất tâm tam quán”, “tính cụ”.",
}

D['萨婆多部'] = {
 'zh': "梵名 Sarvāstivāda，即说一切有部，部派佛教中势力最大的一派，主张‘三世实有、法体恒有’，立五位七十五法。",
 'en': "Sanskrit Sarvāstivāda, the \u201cSchool that Asserts the Existence of All,\u201d the most influential school of sectarian Buddhism. It maintains that \u201cthe three times are really existent and the essence of dharmas is eternally existent,\u201d and establishes the Five Categories and Seventy-five Dharmas.",
 'fr': "Sanskrit Sarvāstivāda, l'« École qui affirme l'existence de tout », la plus influente du bouddhisme sectaire. Elle soutient que « les trois temps existent réellement et l'essence des dharmas existe éternellement » et établit les Cinq Catégories et Soixante-quinze Dharmas.",
 'vi': "Phạn danh Sarvāstivāda, tức Thuyết Nhất Thiết Hữu Bộ, phái có thế lực lớn nhất trong Phật giáo bộ phái, chủ trương “tam thế thật hữu, pháp thể hằng hữu”, lập Ngũ vị thất thập ngũ pháp.",
}

D['经部'] = {
 'zh': "梵名 Sautrāntika，即经量部，部派之一。只依经藏为量，不承认论藏为佛说，主张‘现在实有、过未无体’，多与有部对立。",
 'en': "Sanskrit Sautrāntika, the \u201cSūtra-authority School,\u201d one of the sectarian schools. Taking only the scripture-basket (sūtra) as authoritative and not accepting the treatise-basket as the Buddha's word, it holds that \u201conly the present is really existent, while past and future have no essence,\u201d and often stands opposed to the Sarvāstivāda.",
 'fr': "Sanskrit Sautrāntika, l'« École de l'autorité des sūtras », l'une des écoles sectaires. Ne prenant pour autorité que la corbeille des écritures (sūtra) et n'acceptant pas la corbeille des traités comme parole du Buddha, elle soutient que « seul le présent existe réellement, tandis que le passé et le futur n'ont pas d'essence », et s'oppose souvent au Sarvāstivāda.",
 'vi': "Phạn danh Sautrāntika, tức Kinh Lượng Bộ, một trong các bộ phái. Chỉ y Kinh tạng làm lượng, không thừa nhận Luận tạng là lời Phật, chủ trương “hiện tại thật hữu, quá vị vô thể”, phần nhiều đối lập với Hữu Bộ.",
}

D['婆罗门教'] = {
 'zh': "古印度传统宗教，以《吠陀》为圣典，奉梵天为创造主，主张种姓制度与祭祀万能，为佛陀时代的主流外道。",
 'en': "The traditional religion of ancient India, taking the Vedas as its sacred canon, revering Brahmā as creator, and upholding the caste system and the omnipotence of sacrifice; it was the mainstream outer-path religion in the Buddha's time.",
 'fr': "La religion traditionnelle de l'Inde ancienne, prenant les Vedas pour canon sacré, révérant Brahmā comme créateur, et soutenant le système des castes et la toute-puissance du sacrifice ; c'était la religion « voie extérieure » dominante du temps du Buddha.",
 'vi': "Tôn giáo truyền thống của Ấn Độ cổ, lấy Vệ-đà làm thánh điển, tôn Phạm Thiên làm đấng sáng tạo, chủ trương chế độ giai cấp và tế tự vạn năng; là ngoại đạo chủ lưu thời đức Phật.",
}

D['大乘'] = {
 'zh': "梵语 Mahāyāna，意为大的车乘。以成佛度尽众生为目标，自利利他、悲智双运，修六度万行，相对于小乘而言。",
 'en': "Sanskrit Mahāyāna, meaning \u201cthe great vehicle.\u201d Its goal is to attain Buddhahood and deliver all beings; it benefits both self and others, unites compassion and wisdom, and cultivates the six perfections and myriad practices\u2014set in contrast to the Lesser Vehicle.",
 'fr': "Sanskrit Mahāyāna, « le grand véhicule ». Son but est d'atteindre la bouddhéité et de délivrer tous les êtres ; il bénéficie à soi et à autrui, unit compassion et sagesse, et cultive les six perfections et les innombrables pratiques\u2014par contraste avec le Petit Véhicule.",
 'vi': "Phạn ngữ Mahāyāna, nghĩa là cỗ xe lớn. Lấy thành Phật độ hết chúng sinh làm mục tiêu, tự lợi lợi tha, bi trí song vận, tu sáu độ muôn hạnh; đối lại với Tiểu thừa.",
}

D['小乘'] = {
 'zh': "梵语 Hīnayāna，意为小的车乘。指以自身解脱、证阿罗汉或辟支佛为目标的声闻、缘觉二乘教法，相对于大乘而言。",
 'en': "Sanskrit Hīnayāna, meaning \u201cthe lesser vehicle.\u201d It refers to the teachings of the two vehicles\u2014śrāvakas and pratyekabuddhas\u2014whose goal is one's own liberation, realizing arhatship or pratyekabuddhahood; set in contrast to the Great Vehicle.",
 'fr': "Sanskrit Hīnayāna, « le petit véhicule ». Il désigne les enseignements des deux véhicules\u2014śrāvakas et pratyekabuddhas\u2014dont le but est sa propre libération, la réalisation de l'état d'arhat ou de pratyekabuddha ; par contraste avec le Grand Véhicule.",
 'vi': "Phạn ngữ Hīnayāna, nghĩa là cỗ xe nhỏ. Chỉ giáo pháp của hai thừa Thanh Văn, Duyên Giác, lấy tự thân giải thoát, chứng A-la-hán hay Bích-chi-phật làm mục tiêu; đối lại với Đại thừa.",
}

D['二乘'] = {
 'zh': "指声闻乘与缘觉乘二种，皆以自度、出离生死为主，同属小乘，相对于菩萨乘（大乘）而言。",
 'en': "Refers to the two vehicles of the śrāvakas and the pratyekabuddhas, both chiefly aiming at delivering oneself and escaping birth-and-death; together they belong to the Lesser Vehicle, set in contrast to the Bodhisattva Vehicle (Great Vehicle).",
 'fr': "Désigne les deux véhicules des śrāvakas et des pratyekabuddhas, visant tous deux principalement à se délivrer soi-même et à échapper aux naissances et morts ; ensemble ils relèvent du Petit Véhicule, par contraste avec le Véhicule des Bodhisattvas (Grand Véhicule).",
 'vi': "Chỉ hai thừa Thanh Văn và Duyên Giác, đều chủ ở tự độ, xuất ly sinh tử, cùng thuộc Tiểu thừa; đối lại với Bồ Tát thừa (Đại thừa).",
}

D['声闻'] = {
 'zh': "梵语 Śrāvaka，意为闻佛声教而悟道者。观四谛、断见思惑，证阿罗汉果，为二乘之一。",
 'en': "Sanskrit Śrāvaka, meaning one who awakens to the Way by hearing the Buddha's spoken teaching. Contemplating the Four Truths and severing the afflictions of views and thought, such a one realizes the fruit of arhatship; one of the two vehicles.",
 'fr': "Sanskrit Śrāvaka, celui qui s'éveille à la Voie en entendant l'enseignement oral du Buddha. Contemplant les Quatre Vérités et tranchant les afflictions des vues et de la pensée, il réalise le fruit de l'état d'arhat ; l'un des deux véhicules.",
 'vi': "Phạn ngữ Śrāvaka, nghĩa là người nghe âm thanh giáo pháp của Phật mà ngộ đạo. Quán Tứ đế, đoạn kiến tư hoặc, chứng quả A-la-hán; là một trong hai thừa.",
}

D['缘觉'] = {
 'zh': "梵语 Pratyekabuddha，又作独觉、辟支佛。观十二因缘而悟道，多于无佛之世独自修证，为二乘之一。",
 'en': "Sanskrit Pratyekabuddha, also \u201csolitary-awakened.\u201d Awakening to the Way by contemplating the twelve links of dependent origination, such a one mostly cultivates and realizes alone in an age without a Buddha; one of the two vehicles.",
 'fr': "Sanskrit Pratyekabuddha, aussi « éveillé solitaire ». S'éveillant à la Voie en contemplant les douze liens de la coproduction conditionnée, il cultive et réalise le plus souvent seul dans un âge sans Buddha ; l'un des deux véhicules.",
 'vi': "Phạn ngữ Pratyekabuddha, còn gọi Độc Giác, Bích-chi-phật. Quán mười hai nhân duyên mà ngộ đạo, phần nhiều tự mình tu chứng trong đời không Phật; là một trong hai thừa.",
}

D['阿罗汉'] = {
 'zh': "梵语 arhat，声闻乘的最高果位。意译杀贼、应供、无生，谓断尽三界见思烦恼、不再受生死者。",
 'en': "Sanskrit arhat, the highest fruit of the śrāvaka vehicle. Rendered by meaning as \u201cslayer of the thieves [of affliction],\u201d \u201cworthy of offerings,\u201d and \u201cno-more-birth\u201d\u2014one who has utterly severed the afflictions of views and thought in the three realms and will no longer undergo birth-and-death.",
 'fr': "Sanskrit arhat, le fruit le plus élevé du véhicule des śrāvakas. Rendu par « tueur des voleurs [des afflictions] », « digne d'offrandes » et « sans nouvelle naissance »\u2014celui qui a entièrement tranché les afflictions des vues et de la pensée dans les trois mondes et ne subira plus la naissance-et-mort.",
 'vi': "Phạn ngữ arhat, quả vị cao nhất của Thanh Văn thừa. Dịch nghĩa sát tặc, ứng cúng, vô sinh\u2014chỉ người đoạn tận kiến tư phiền não trong ba cõi, không còn thọ sinh tử.",
}

json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('batch_E1 →', len(D))
