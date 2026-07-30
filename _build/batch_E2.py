#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))

D['凡夫'] = {
 'zh': "梵语 pṛthagjana，指未见真谛、未断惑证理、犹在三界生死中轮回的一般众生，相对于‘圣人’而言。",
 'en': "Sanskrit pṛthagjana, referring to ordinary beings who have not yet seen the true reality, have not severed delusion or realized the principle, and still transmigrate in the birth-and-death of the three realms; set in contrast to the \u201cnoble ones.\u201d",
 'fr': "Sanskrit pṛthagjana, désignant les êtres ordinaires qui n'ont pas encore vu la réalité véritable, n'ont pas tranché l'illusion ni réalisé le principe, et transmigrent encore dans la naissance-et-mort des trois mondes ; par contraste avec les « nobles ».",
 'vi': "Phạn ngữ pṛthagjana, chỉ chúng sinh phàm thường chưa thấy chân đế, chưa đoạn hoặc chứng lý, còn luân hồi trong sinh tử ba cõi; đối lại với “thánh nhân”.",
}

D['圣人'] = {
 'zh': "梵语 ārya，指已见真谛、断惑证理、超越凡夫位的修行者，如声闻四果、辟支佛、菩萨与佛。",
 'en': "Sanskrit ārya, referring to practitioners who have seen the true reality, severed delusion and realized the principle, and transcended the stage of ordinary beings\u2014such as those of the four śrāvaka fruits, pratyekabuddhas, bodhisattvas, and Buddhas.",
 'fr': "Sanskrit ārya, désignant les pratiquants qui ont vu la réalité véritable, tranché l'illusion et réalisé le principe, et transcendé l'état d'êtres ordinaires\u2014tels ceux des quatre fruits des śrāvakas, les pratyekabuddhas, les bodhisattvas et les Buddhas.",
 'vi': "Phạn ngữ ārya, chỉ hành giả đã thấy chân đế, đoạn hoặc chứng lý, vượt khỏi địa vị phàm phu\u2014như bốn quả Thanh Văn, Bích-chi-phật, Bồ Tát và Phật.",
}

D['三宝'] = {
 'zh': "梵语 Triratna，指佛、法、僧三种可尊可贵者：佛为觉者，法为教法真理，僧为奉行佛法的清净僧团，为佛教徒皈依的对象。",
 'en': "Sanskrit Triratna, referring to the three honorable and precious ones: the Buddha (the awakened one), the Dharma (the teaching and its truth), and the Saṅgha (the pure community that practices the Dharma); they are the objects of refuge for Buddhists.",
 'fr': "Sanskrit Triratna, désignant les trois vénérables et précieux : le Buddha (l'éveillé), le Dharma (l'enseignement et sa vérité) et le Saṅgha (la communauté pure qui pratique le Dharma) ; ce sont les objets de refuge des bouddhistes.",
 'vi': "Phạn ngữ Triratna, chỉ ba ngôi tôn quý: Phật (bậc giác ngộ), Pháp (giáo pháp chân lý), Tăng (tăng đoàn thanh tịnh phụng hành Phật pháp); là đối tượng quy y của người Phật tử.",
}

D['皈依'] = {
 'zh': "又作归依，指身心归投、依靠三宝以求救护解脱。受三皈是成为佛弟子的根本仪式。",
 'en': "Also written \u201ctaking refuge,\u201d it means to turn one's body and mind toward and rely upon the Three Jewels, seeking protection and liberation. Receiving the three refuges is the fundamental rite of becoming a disciple of the Buddha.",
 'fr': "Aussi écrit « prendre refuge », cela signifie tourner son corps et son esprit vers les Trois Joyaux et s'appuyer sur eux, cherchant protection et libération. Recevoir les trois refuges est le rite fondamental pour devenir disciple du Buddha.",
 'vi': "Còn viết là quy y, chỉ việc thân tâm quay về nương tựa Tam Bảo để cầu cứu hộ giải thoát. Thọ tam quy là nghi thức căn bản để trở thành đệ tử Phật.",
}

D['烦恼'] = {
 'zh': "梵语 kleśa，指扰乱身心、令众生流转生死的一切迷惑妄想，根本者为贪、瞋、痴等，唯识立六根本烦恼与二十随烦恼。",
 'en': "Sanskrit kleśa, referring to all the confusions and deluded imaginings that disturb body and mind and cause beings to transmigrate in birth-and-death; the root ones are greed, hatred, delusion, and so forth. Consciousness-Only establishes six root afflictions and twenty secondary afflictions.",
 'fr': "Sanskrit kleśa, désignant toutes les confusions et imaginations trompeuses qui troublent le corps et l'esprit et font transmigrer les êtres dans la naissance-et-mort ; les racines en sont la convoitise, la haine, l'ignorance, etc. Le Rien-que-conscience établit six afflictions-racines et vingt afflictions secondaires.",
 'vi': "Phạn ngữ kleśa, chỉ hết thảy mê hoặc vọng tưởng làm rối loạn thân tâm, khiến chúng sinh lưu chuyển sinh tử; căn bản là tham, sân, si v.v. Duy Thức lập sáu căn bản phiền não và hai mươi tùy phiền não.",
}

D['贪'] = {
 'zh': "梵语 rāga，三毒之一，六根本烦恼之一。对顺境、五欲、名利等起贪爱染著、无有厌足的心理。",
 'en': "Sanskrit rāga, one of the three poisons and one of the six root afflictions. It is the mental state of craving, attachment, and insatiable clinging toward favorable circumstances, the five desires, fame and gain, and the like.",
 'fr': "Sanskrit rāga, l'un des trois poisons et l'une des six afflictions-racines. C'est l'état mental de convoitise, d'attachement et de saisie insatiable envers les circonstances favorables, les cinq désirs, la renommée et le gain, etc.",
 'vi': "Phạn ngữ rāga, một trong ba độc, một trong sáu căn bản phiền não. Là tâm lý tham ái nhiễm trước, không biết chán đối với thuận cảnh, ngũ dục, danh lợi v.v.",
}

D['瞋'] = {
 'zh': "梵语 dveṣa，三毒之一，六根本烦恼之一。对逆境、违缘起憎恚恼怒、欲加损害的心理。",
 'en': "Sanskrit dveṣa, one of the three poisons and one of the six root afflictions. It is the mental state of hatred, resentment, and anger toward adverse circumstances and unfavorable conditions, with the wish to do harm.",
 'fr': "Sanskrit dveṣa, l'un des trois poisons et l'une des six afflictions-racines. C'est l'état mental de haine, de ressentiment et de colère envers les circonstances adverses et les conditions défavorables, avec le désir de nuire.",
 'vi': "Phạn ngữ dveṣa, một trong ba độc, một trong sáu căn bản phiền não. Là tâm lý sân hận não nộ, muốn gây tổn hại đối với nghịch cảnh, duyên trái ý.",
}

D['痴'] = {
 'zh': "梵语 moha，又名无明，三毒之一，六根本烦恼之一。指心性暗昧、不明事理、不达因果缘起，为一切烦恼的根本。",
 'en': "Sanskrit moha, also called ignorance (avidyā); one of the three poisons and one of the six root afflictions. It refers to the mind's being dark and unclear, not understanding the truth of things, and failing to comprehend cause-and-effect and dependent arising; it is the root of all afflictions.",
 'fr': "Sanskrit moha, aussi appelé ignorance (avidyā) ; l'un des trois poisons et l'une des six afflictions-racines. Il désigne l'esprit obscur et confus, qui ne comprend pas la vérité des choses ni la cause-et-effet et la coproduction conditionnée ; c'est la racine de toutes les afflictions.",
 'vi': "Phạn ngữ moha, còn gọi vô minh, một trong ba độc, một trong sáu căn bản phiền não. Chỉ tâm tính ám muội, không rõ sự lý, không thấu nhân quả duyên khởi; là gốc của hết thảy phiền não.",
}

D['菩提心'] = {
 'zh': "梵语 bodhicitta，全称阿耨多罗三藐三菩提心，即上求佛道、下化众生的觉悟之心，为大乘行者发心的根本。",
 'en': "Sanskrit bodhicitta, fully \u201cthe mind of anuttarā-samyak-saṃbodhi\u201d\u2014the awakened mind that seeks Buddhahood above and transforms beings below; it is the fundamental aspiration aroused by a Mahāyāna practitioner.",
 'fr': "Sanskrit bodhicitta, pleinement « l'esprit de l'anuttarā-samyak-saṃbodhi »\u2014l'esprit d'éveil qui recherche la bouddhéité en haut et transforme les êtres en bas ; c'est l'aspiration fondamentale que suscite un pratiquant du Mahāyāna.",
 'vi': "Phạn ngữ bodhicitta, toàn xưng A-nậu-đa-la Tam-miệu Tam-bồ-đề tâm, tức tâm giác ngộ trên cầu Phật đạo, dưới hóa độ chúng sinh; là căn bản phát tâm của hành giả Đại thừa.",
}

D['禅定'] = {
 'zh': "梵语 dhyāna（禅那）与 samādhi（三昧）的合称，指止息散乱、系心一境、令心专注寂静的修习，为三学之一、六度之一。",
 'en': "A combined term for the Sanskrit dhyāna and samādhi, referring to the cultivation of quieting distraction, fixing the mind on a single object, and making the mind focused and still; it is one of the three trainings and one of the six perfections.",
 'fr': "Terme combinant les sanskrits dhyāna et samādhi, désignant la culture consistant à apaiser la distraction, fixer l'esprit sur un objet unique et rendre l'esprit concentré et paisible ; c'est l'une des trois disciplines et l'une des six perfections.",
 'vi': "Là tên gọi chung của Phạn ngữ dhyāna (thiền-na) và samādhi (tam-muội), chỉ sự tu tập dứt tán loạn, buộc tâm một cảnh, khiến tâm chuyên chú tịch tĩnh; là một trong ba học, một trong sáu độ.",
}

json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('batch_E2 →', len(D))
