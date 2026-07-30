#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))

D['善知识'] = {
 'zh': "梵语 kalyāṇamitra，指能教导正法、引人入善、助人修行成就的良师益友。",
 'en': "Sanskrit kalyāṇamitra, referring to a good teacher and beneficial friend who can instruct in the true Dharma, lead one toward the good, and help one accomplish the practice.",
 'fr': "Sanskrit kalyāṇamitra, désignant un bon maître et un ami bénéfique qui peut instruire dans le vrai Dharma, mener vers le bien et aider à accomplir la pratique.",
 'vi': "Phạn ngữ kalyāṇamitra, chỉ bậc thầy hiền bạn tốt có thể dạy chính pháp, dẫn người vào thiện, giúp người tu hành thành tựu.",
}

D['一切法无我'] = {
 'zh': "谓一切有为无为诸法，皆无独立常一的实体我。为三法印之一（诸法无我），是《百法明门论》立论的宗旨。",
 'en': "The teaching that all dharmas, conditioned and unconditioned, are without an independent, permanent, unitary substantial self. It is one of the three Dharma-seals (\u201call dharmas are without self\u201d) and is the guiding tenet of the Treatise on the Hundred Dharmas.",
 'fr': "L'enseignement selon lequel tous les dharmas, conditionnés et inconditionnés, sont dépourvus d'un soi substantiel indépendant, permanent et unitaire. C'est l'un des trois sceaux du Dharma (« tous les dharmas sont sans soi ») et la thèse directrice du Traité des Cent Dharmas.",
 'vi': "Nói hết thảy pháp hữu vi vô vi đều không có thực thể ngã độc lập thường nhất. Là một trong ba pháp ấn (chư pháp vô ngã), là tông chỉ lập luận của Bách Pháp Minh Môn Luận.",
}

D['人无我'] = {
 'zh': "梵语 pudgala-nairātmya，二无我之一。谓有情的生命只是五蕴假合，并无常一主宰的实体我，与‘法无我’相对。",
 'en': "Sanskrit pudgala-nairātmya, one of the two selflessnesses. It teaches that a sentient being's life is merely the provisional assemblage of the five aggregates, with no permanent, unitary, controlling substantial self; the counterpart of the \u201cselflessness of dharmas.\u201d",
 'fr': "Sanskrit pudgala-nairātmya, l'une des deux absences-de-soi. Elle enseigne que la vie d'un être n'est que l'assemblage provisoire des cinq agrégats, sans soi substantiel permanent, unitaire et dominant ; le pendant de l'« absence-de-soi des dharmas ».",
 'vi': "Phạn ngữ pudgala-nairātmya, một trong hai vô ngã. Nói sinh mệnh của hữu tình chỉ là năm uẩn giả hợp, không có thực thể ngã thường nhất chủ tể; đối lại với “pháp vô ngã”.",
}

D['万法唯识'] = {
 'zh': "梵语 vijñapti-mātra，唯识宗的根本主张，谓宇宙万有皆是内识所变现，离识别无独立实境。",
 'en': "Sanskrit vijñapti-mātra, the fundamental thesis of the Consciousness-Only school: that all existence in the universe is a manifestation of the inner consciousness, and apart from consciousness there is no independent, real object.",
 'fr': "Sanskrit vijñapti-mātra, thèse fondamentale de l'école du Rien-que-conscience : toute l'existence de l'univers est une manifestation de la conscience intérieure, et hors de la conscience il n'y a pas d'objet réel indépendant.",
 'vi': "Phạn ngữ vijñapti-mātra, chủ trương căn bản của Duy Thức tông, nói vạn hữu trong vũ trụ đều do nội thức biến hiện, lìa thức không có cảnh thật độc lập.",
}

D['毕竟空'] = {
 'zh': "梵语 atyanta-śūnyatā，指彻底、究竟的空，一切法自性本空、连‘空’亦不可得，为般若所显的最高空义。",
 'en': "Sanskrit atyanta-śūnyatā, referring to thoroughgoing, ultimate emptiness: all dharmas are by nature originally empty, and even \u201cemptiness\u201d itself cannot be grasped; it is the highest sense of emptiness revealed by the Prajñāpāramitā.",
 'fr': "Sanskrit atyanta-śūnyatā, désignant la vacuité radicale et ultime : tous les dharmas sont par nature originellement vides, et même la « vacuité » elle-même ne peut être saisie ; c'est le sens le plus élevé de la vacuité révélé par la Prajñāpāramitā.",
 'vi': "Phạn ngữ atyanta-śūnyatā, chỉ cái không triệt để, rốt ráo: hết thảy pháp tự tính vốn không, ngay cả “không” cũng bất khả đắc; là nghĩa không tối cao do Bát-nhã hiển bày.",
}

D['灭度'] = {
 'zh': "梵语 parinirvāṇa，即入涅槃、般涅槃。谓灭尽烦恼、度脱生死，多指佛及圣者舍报入寂。",
 'en': "Sanskrit parinirvāṇa\u2014entering nirvāṇa, complete extinction. It means the extinction of the afflictions and deliverance from birth-and-death, mostly referring to a Buddha or sage relinquishing the body and entering quiescence.",
 'fr': "Sanskrit parinirvāṇa\u2014entrer dans le nirvāṇa, l'extinction complète. Il signifie l'extinction des afflictions et la délivrance de la naissance-et-mort, désignant surtout un Buddha ou un sage abandonnant le corps et entrant dans la quiétude.",
 'vi': "Phạn ngữ parinirvāṇa, tức nhập niết-bàn, bát-niết-bàn. Nói diệt tận phiền não, độ thoát sinh tử, phần nhiều chỉ Phật và bậc thánh xả báo nhập tịch.",
}

D['惑业苦'] = {
 'zh': "指烦恼（惑）、造作（业）、苦果（苦）三者辗转相生的流转过程：由惑造业，由业感苦，苦中又起惑，循环不已。",
 'en': "Refers to the three\u2014affliction (delusion), karma (fabrication), and suffering (the painful fruit)\u2014which arise from one another in turn as the process of transmigration: from delusion one creates karma, from karma one calls forth suffering, and within suffering delusion again arises, cycling without end.",
 'fr': "Désigne les trois\u2014l'affliction (illusion), le karma (fabrication) et la souffrance (le fruit douloureux)\u2014qui naissent tour à tour l'un de l'autre comme processus de transmigration : de l'illusion on crée le karma, du karma on appelle la souffrance, et dans la souffrance l'illusion renaît, cyclant sans fin.",
 'vi': "Chỉ ba thứ phiền não (hoặc), tạo tác (nghiệp), khổ quả (khổ) xoay vần sinh lẫn nhau trong quá trình lưu chuyển: do hoặc tạo nghiệp, do nghiệp cảm khổ, trong khổ lại khởi hoặc, tuần hoàn không dứt.",
}

D['离苦得乐'] = {
 'zh': "指出离生死轮回之苦、证得涅槃解脱之乐，为佛法修行的基本旨趣。",
 'en': "Refers to escaping the suffering of the cycle of birth-and-death and attaining the bliss of nirvāṇa and liberation; it is the basic aim of Buddhist practice.",
 'fr': "Désigne le fait d'échapper à la souffrance du cycle des naissances et des morts et d'atteindre la félicité du nirvāṇa et de la libération ; c'est le but fondamental de la pratique bouddhique.",
 'vi': "Chỉ việc ra khỏi khổ luân hồi sinh tử, chứng được lạc niết-bàn giải thoát; là chỉ thú căn bản của việc tu hành Phật pháp.",
}

D['心心所法'] = {
 'zh': "指心法（八识心王）与心所有法（五十一心所）的合称。心王为认识的主体，心所为伴随心王生起的种种心理作用。",
 'en': "A joint term for mind dharmas (the eight ruling minds) and mental-factor dharmas (the fifty-one mental factors). The mind-king is the subject of cognition, and the mental factors are the various psychological functions that arise in company with the mind-king.",
 'fr': "Terme conjoint pour les dharmas-esprit (les huit esprits-rois) et les facteurs mentaux (les cinquante et un facteurs). L'esprit-roi est le sujet de la connaissance, et les facteurs mentaux sont les diverses fonctions psychologiques qui surgissent en compagnie de l'esprit-roi.",
 'vi': "Là tên gọi chung của tâm pháp (tám tâm vương) và tâm sở hữu pháp (năm mươi mốt tâm sở). Tâm vương là chủ thể nhận thức, tâm sở là các tác dụng tâm lý khởi lên đi kèm với tâm vương.",
}

D['心所'] = {
 'zh': "梵语 caitta，全称心所有法，指从属于心王、与之相应而起的心理作用，五位百法立五十一种，分遍行、别境、善、烦恼、随烦恼、不定六位。",
 'en': "Sanskrit caitta, fully \u201cmental-factor dharmas,\u201d referring to the psychological functions that are subordinate to and arise in correspondence with the mind-king. The Five Categories and Hundred Dharmas establish fifty-one of them, in six divisions: universally active, object-specific, wholesome, afflictive, secondary afflictive, and indeterminate.",
 'fr': "Sanskrit caitta, pleinement « dharmas facteurs mentaux », désignant les fonctions psychologiques subordonnées à l'esprit-roi et surgissant en correspondance avec lui. Les Cinq Catégories et Cent Dharmas en établissent cinquante et un, en six divisions : universellement actifs, spécifiques à l'objet, salutaires, afflictifs, afflictifs secondaires et indéterminés.",
 'vi': "Phạn ngữ caitta, toàn xưng tâm sở hữu pháp, chỉ các tác dụng tâm lý phụ thuộc tâm vương, tương ưng với nó mà khởi; Ngũ vị bách pháp lập năm mươi mốt thứ, chia sáu vị: biến hành, biệt cảnh, thiện, phiền não, tùy phiền não, bất định.",
}

json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('batch_E3 →', len(D))
