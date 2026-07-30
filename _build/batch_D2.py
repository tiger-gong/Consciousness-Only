#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))

D['天亲菩萨'] = {
 'zh': "即世亲菩萨（梵名婆薮盘豆，Vasubandhu），无著之弟。初习小乘造《俱舍论》，后受兄劝转入大乘，造《唯识三十颂》、《百法明门论》等，为唯识宗集大成者。",
 'en': "That is, the bodhisattva Vasubandhu (Sanskrit Vasubandhu), the younger brother of Asaṅga. He first studied the Lesser Vehicle and composed the Abhidharmakośa; later, at his brother's urging, he turned to the Great Vehicle and composed the Thirty Verses on Consciousness-Only, the Treatise on the Hundred Dharmas, and others, becoming the one who brought the Consciousness-Only school to completion.",
 'fr': "C'est-à-dire le bodhisattva Vasubandhu (sanskrit Vasubandhu), frère cadet d'Asaṅga. Il étudia d'abord le Petit Véhicule et composa l'Abhidharmakośa ; plus tard, sur l'exhortation de son frère, il passa au Grand Véhicule et composa les Trente Stances, le Traité des Cent Dharmas et d'autres, parachevant l'école du Rien-que-conscience.",
 'vi': "Tức Bồ Tát Thế Thân (Phạn danh Bà-tẩu-bàn-đậu, Vasubandhu), em của Vô Trước. Ban đầu học Tiểu thừa tạo Câu-xá Luận, sau nghe anh khuyên chuyển sang Đại thừa, tạo Duy Thức Tam Thập Tụng, Bách Pháp Minh Môn Luận v.v., là người đại thành Duy Thức tông.",
}

D['无著菩萨'] = {
 'zh': "梵名 Asaṅga，天亲之兄，约生于佛灭后九百年。传承弥勒之教，造《瑜伽师地论》（记录）、《摄大乘论》等，为印度瑜伽行派的创立者之一。",
 'en': "Sanskrit Asaṅga, the elder brother of Vasubandhu, born about nine hundred years after the Buddha's parinirvāṇa. Transmitting the teaching of Maitreya, he recorded the Yogācārabhūmi-śāstra and composed the Mahāyāna-saṃgraha and others; he was one of the founders of the Indian Yogācāra school.",
 'fr': "Sanskrit Asaṅga, frère aîné de Vasubandhu, né environ neuf cents ans après le parinirvāṇa du Buddha. Transmettant l'enseignement de Maitreya, il consigna le Yogācārabhūmi-śāstra et composa le Mahāyāna-saṃgraha et d'autres ; il fut l'un des fondateurs de l'école Yogācāra indienne.",
 'vi': "Phạn danh Asaṅga, anh của Thế Thân, sinh khoảng chín trăm năm sau Phật diệt độ. Bẩm thừa giáo pháp của Di-lặc, ghi chép Du Già Sư Địa Luận, tạo Nhiếp Đại Thừa Luận v.v.; là một trong những người sáng lập học phái Du Già ở Ấn Độ.",
}

D['弥勒菩萨'] = {
 'zh': "梵名 Maitreya，意译慈氏。现居兜率天，为一生补处菩萨，未来将下生成佛。瑜伽行派尊为祖师，传说《瑜伽师地论》等‘五部大论’即其所说。",
 'en': "Sanskrit Maitreya, rendered \u201cthe Compassionate One.\u201d He now dwells in Tuṣita Heaven as the bodhisattva of one-more-birth, and will in the future descend to be born and attain Buddhahood. Revered as a patriarch by the Yogācāra school, he is said to have expounded the \u201cFive Great Treatises,\u201d including the Yogācārabhūmi-śāstra.",
 'fr': "Sanskrit Maitreya, rendu « le Compatissant ». Il demeure à présent au ciel Tuṣita comme bodhisattva à une naissance près, et descendra à l'avenir pour naître et atteindre la bouddhéité. Vénéré comme patriarche par l'école Yogācāra, on dit qu'il exposa les « Cinq Grands Traités », dont le Yogācārabhūmi-śāstra.",
 'vi': "Phạn danh Maitreya, dịch nghĩa Từ Thị. Nay ở cung trời Đâu-suất, là Bồ Tát nhất sinh bổ xứ, tương lai sẽ hạ sinh thành Phật. Học phái Du Già tôn làm tổ sư, tương truyền “Ngũ Bộ Đại Luận” như Du Già Sư Địa Luận chính là do ngài nói.",
}

D['师子觉'] = {
 'zh': "梵名 Buddhasiṃha，无著、世亲同门之弟子（或作无著弟子），瑜伽行派论师之一，与无性等同弘唯识。",
 'en': "Sanskrit Buddhasiṃha, a fellow disciple (or disciple) of Asaṅga and Vasubandhu, one of the Yogācāra commentator-masters who propagated Consciousness-Only alongside such figures as Asvabhāva.",
 'fr': "Sanskrit Buddhasiṃha, condisciple (ou disciple) d'Asaṅga et Vasubandhu, l'un des maîtres commentateurs Yogācāra qui propagèrent le Rien-que-conscience aux côtés de figures telles qu'Asvabhāva.",
 'vi': "Phạn danh Buddhasiṃha, là bạn đồng môn (hoặc đệ tử) của Vô Trước, Thế Thân, một trong các luận sư Du Già, cùng hoằng Duy Thức với các vị như Vô Tính.",
}

D['蕅益大师'] = {
 'zh': "明末四大高僧之一，名智旭（1599–1655），融通台、禅、律、净，著述宏富，撰《大乘百法明门论直解》等，为汉传学习百法的重要注家。",
 'en': "One of the four eminent monks of the late Ming, named Zhixu (1599\u20131655). Harmonizing the Tiantai, Chan, Vinaya, and Pure Land traditions, he was a prolific author; among his works is the Direct Explanation of the Treatise on the Hundred Dharmas, making him an important commentator for the study of the hundred dharmas in Chinese Buddhism.",
 'fr': "L'un des quatre moines éminents de la fin des Ming, nommé Zhixu (1599\u20131655). Harmonisant les traditions Tiantai, Chan, Vinaya et Terre Pure, il fut un auteur prolifique ; parmi ses œuvres figure l'Explication directe du Traité des Cent Dharmas, ce qui en fait un commentateur important pour l'étude des cent dharmas.",
 'vi': "Một trong bốn vị cao tăng cuối đời Minh, tên Trí Húc (1599\u20131655). Dung thông Thai, Thiền, Luật, Tịnh, trước tác phong phú; soạn Đại Thừa Bách Pháp Minh Môn Luận Trực Giải v.v., là nhà chú giải quan trọng cho việc học bách pháp trong Phật giáo Hán truyền.",
}

D['玄奘大师'] = {
 'zh': "唐代高僧（602–664），西行印度求法十七年，从戒贤受学唯识。归国后主持译场，译经论七十五部，糅译《成唯识论》，创立法相唯识宗。",
 'en': "An eminent Tang-dynasty monk (602\u2013664) who traveled west to India in quest of the Dharma for seventeen years and studied Consciousness-Only under Śīlabhadra. On returning home he directed the translation bureau, translated seventy-five scriptures and treatises, produced the blended translation of the Cheng weishi lun, and founded the Dharma-characteristics Consciousness-Only school.",
 'fr': "Moine éminent des Tang (602\u2013664) qui voyagea vers l'ouest en Inde en quête du Dharma pendant dix-sept ans et étudia le Rien-que-conscience auprès de Śīlabhadra. De retour, il dirigea le bureau de traduction, traduisit soixante-quinze écritures et traités, produisit la traduction fondue du Cheng weishi lun et fonda l'école des Caractéristiques des dharmas / Rien-que-conscience.",
 'vi': "Cao tăng đời Đường (602\u2013664), Tây hành sang Ấn Độ cầu pháp mười bảy năm, theo Giới Hiền học Duy Thức. Về nước chủ trì dịch trường, dịch bảy mươi lăm bộ kinh luận, nhu dịch Thành Duy Thức Luận, sáng lập Pháp Tướng Duy Thức tông.",
}

D['净界法师'] = {
 'zh': "当代汉传佛教法师，讲说唯识、天台、净土诸学，本课程《大乘百法明门论·直解》即依其讲述录成。",
 'en': "A contemporary Chinese Buddhist master who lectures on Consciousness-Only, Tiantai, and Pure Land studies; the present course, the Direct Explanation of the Treatise on the Hundred Dharmas, was compiled from his lectures.",
 'fr': "Un maître bouddhiste chinois contemporain qui enseigne le Rien-que-conscience, le Tiantai et la Terre Pure ; le présent cours, l'Explication directe du Traité des Cent Dharmas, a été compilé à partir de ses conférences.",
 'vi': "Vị pháp sư Phật giáo Hán truyền đương đại, giảng thuyết các môn Duy Thức, Thiên Thai, Tịnh Độ; khóa học này\u2014Đại Thừa Bách Pháp Minh Môn Luận · Trực Giải\u2014chính là ghi lại từ lời giảng của ngài.",
}

D['宾头卢尊者'] = {
 'zh': "梵名 Piṇḍola，佛陀弟子，十六罗汉之一。因擅现神通被佛呵责，令其久住世间、不入涅槃，为末世众生作福田。",
 'en': "Sanskrit Piṇḍola, a disciple of the Buddha and one of the sixteen arhats. Because he displayed spiritual powers, he was rebuked by the Buddha and made to remain long in the world without entering nirvāṇa, so as to serve as a field of merit for beings of the final age.",
 'fr': "Sanskrit Piṇḍola, disciple du Buddha et l'un des seize arhats. Parce qu'il fit étalage de pouvoirs spirituels, il fut réprimandé par le Buddha et contraint de demeurer longuement dans le monde sans entrer dans le nirvāṇa, afin de servir de champ de mérite aux êtres de l'âge final.",
 'vi': "Phạn danh Piṇḍola, đệ tử của Phật, một trong mười sáu La-hán. Vì hiện thần thông nên bị Phật quở trách, khiến ngài trụ lâu ở thế gian, chẳng nhập niết-bàn, làm ruộng phước cho chúng sinh đời mạt.",
}

json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('batch_D2 →', len(D))
