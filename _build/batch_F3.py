#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))

D['阿逾阇国'] = {
 'zh': "梵名 Ayodhyā，中印度古国，又作阿瑜陀。无著、世亲曾于此国弘法，弥勒菩萨传说于此为无著说五部大论。",
 'en': "Sanskrit Ayodhyā, an ancient kingdom of central India, also written Ayodhya. Asaṅga and Vasubandhu propagated the Dharma there, and it is said that the bodhisattva Maitreya expounded the Five Great Treatises for Asaṅga in this land.",
 'fr': "Sanskrit Ayodhyā, un ancien royaume de l'Inde centrale, aussi écrit Ayodhya. Asaṅga et Vasubandhu y propagèrent le Dharma, et l'on dit que le bodhisattva Maitreya y exposa les Cinq Grands Traités pour Asaṅga.",
 'vi': "Phạn danh Ayodhyā, nước cổ miền Trung Ấn, còn viết A-du-đà. Vô Trước, Thế Thân từng hoằng pháp tại đây; tương truyền Bồ Tát Di-lặc vì Vô Trước nói Ngũ Bộ Đại Luận tại nước này.",
}

D['中天竺'] = {
 'zh': "古印度地理区分之一，指恒河中游一带的中印度诸国，如摩揭陀、憍萨罗等，为佛陀说法及部派佛教兴盛之地。",
 'en': "One of the geographical divisions of ancient India, referring to the central Indian kingdoms along the middle Ganges\u2014such as Magadha and Kośala\u2014where the Buddha taught and where sectarian Buddhism flourished.",
 'fr': "L'une des divisions géographiques de l'Inde ancienne, désignant les royaumes de l'Inde centrale le long du Gange moyen\u2014tels Magadha et Kośala\u2014où le Buddha enseigna et où le bouddhisme sectaire prospéra.",
 'vi': "Một trong các phân vùng địa lý Ấn Độ cổ, chỉ các nước Trung Ấn vùng trung lưu sông Hằng\u2014như Ma-kiệt-đà, Kiều-tát-la\u2014là nơi Phật thuyết pháp và Phật giáo bộ phái thịnh hành.",
}

D['东毘提诃'] = {
 'zh': "梵名 Videha，四大洲中东胜神洲（或作东毘提诃）之简称，亦指古印度东部的毗提诃国。",
 'en': "Sanskrit Videha, an abbreviation for the eastern continent among the four great continents (Pūrvavideha), and also referring to the ancient eastern Indian kingdom of Videha.",
 'fr': "Sanskrit Videha, abréviation pour le continent oriental parmi les quatre grands continents (Pūrvavideha), et désignant aussi l'ancien royaume indien oriental de Videha.",
 'vi': "Phạn danh Videha, tên gọi tắt của Đông Thắng Thần Châu trong bốn đại châu, cũng chỉ nước Tì-đề-ha ở miền đông Ấn Độ cổ.",
}

D['拨无因果'] = {
 'zh': "否定因果报应的邪见，以为造善不受乐报、造恶不受苦报。属断见，为佛法所破斥的重大邪见之一。",
 'en': "The wrong view that denies karmic cause and effect\u2014holding that doing good does not bring a pleasant retribution and doing evil does not bring a painful one. It belongs to nihilism and is one of the major wrong views refuted by the Buddha-Dharma.",
 'fr': "La vue fausse qui nie la cause et l'effet karmiques\u2014soutenant que faire le bien n'apporte pas de rétribution agréable et faire le mal n'apporte pas de rétribution douloureuse. Elle relève du nihilisme et est l'une des vues fausses majeures réfutées par le Dharma.",
 'vi': "Tà kiến phủ định nhân quả báo ứng, cho rằng làm thiện không thọ lạc báo, làm ác không thọ khổ báo. Thuộc đoạn kiến, là một trong những tà kiến trọng đại bị Phật pháp phá trừ.",
}

D['野狐禅'] = {
 'zh': "禅宗公案。百丈禅师座下有一老人自言昔为禅师，因答‘不落因果’而五百世堕野狐身；后改答‘不昧因果’乃得脱。喻错解因果、堕于邪见。",
 'en': "A Chan kōan. Under Chan Master Baizhang there was an old man who said that in a former life he had been a Chan master, and for answering \u201cnot falling under cause and effect\u201d he fell into a fox's body for five hundred lives; later, changing his answer to \u201cnot blind to cause and effect,\u201d he was freed. It is a metaphor for misunderstanding cause and effect and falling into wrong views.",
 'fr': "Un kōan Chan. Sous le maître Chan Baizhang se trouvait un vieillard qui dit qu'en une vie antérieure il avait été maître Chan, et pour avoir répondu « ne pas tomber sous la cause et l'effet » il était tombé dans un corps de renard pendant cinq cents vies ; changeant ensuite sa réponse en « ne pas être aveugle à la cause et l'effet », il fut libéré. Métaphore d'une mauvaise compréhension de la cause et l'effet et d'une chute dans les vues fausses.",
 'vi': "Công án Thiền tông. Dưới tòa Bách Trượng thiền sư có một ông già tự xưng xưa là thiền sư, vì đáp “bất lạc nhân quả” mà năm trăm đời đọa thân dã hồ; sau đổi đáp “bất muội nhân quả” mới được thoát. Ví dụ hiểu sai nhân quả, đọa vào tà kiến.",
}

D['不昧因果'] = {
 'zh': "百丈野狐公案中的正解：虽悟无我空性，仍深明因果丝毫不爽、不敢轻忽，与‘不落因果’相对。",
 'en': "The correct understanding in Baizhang's wild-fox kōan: even though one has awakened to the emptiness of no-self, one still deeply understands that cause and effect are not off by a hair and dare not treat them lightly\u2014the counterpart of \u201cnot falling under cause and effect.\u201d",
 'fr': "La compréhension correcte dans le kōan du renard sauvage de Baizhang : même si l'on s'est éveillé à la vacuité du non-soi, on comprend encore profondément que la cause et l'effet ne s'écartent pas d'un cheveu et l'on n'ose pas les traiter à la légère\u2014le pendant de « ne pas tomber sous la cause et l'effet ».",
 'vi': "Chính giải trong công án dã hồ của Bách Trượng: tuy ngộ vô ngã không tính, vẫn thấu rõ nhân quả mảy may không sai, chẳng dám khinh thường; đối lại với “bất lạc nhân quả”.",
}

D['不落因果'] = {
 'zh': "百丈野狐公案中的错答：以为悟道即超越因果、不受业报拘束。此见拨无因果，故感五百世野狐身。",
 'en': "The wrong answer in Baizhang's wild-fox kōan: thinking that awakening to the Way means transcending cause and effect and no longer being bound by karmic retribution. This view denies cause and effect, and so called forth five hundred lives as a wild fox.",
 'fr': "La mauvaise réponse dans le kōan du renard sauvage de Baizhang : penser que s'éveiller à la Voie signifie transcender la cause et l'effet et n'être plus lié par la rétribution karmique. Cette vue nie la cause et l'effet, et appela ainsi cinq cents vies en renard sauvage.",
 'vi': "Lời đáp sai trong công án dã hồ của Bách Trượng: cho rằng ngộ đạo tức vượt khỏi nhân quả, không còn bị nghiệp báo ràng buộc. Kiến này bác vô nhân quả, nên cảm năm trăm đời thân dã hồ.",
}

D['圣言量'] = {
 'zh': "梵语 āptavacana，量论三种量之一，指以佛陀等圣者的言教为可靠认识的依据，相对于现量（直接经验）与比量（推理）。",
 'en': "Sanskrit āptavacana, one of the three means of knowledge in epistemology: taking the verbal teaching of the Buddha and other sages as a reliable basis for cognition\u2014set in contrast to direct perception (pratyakṣa) and inference (anumāna).",
 'fr': "Sanskrit āptavacana, l'un des trois moyens de connaissance en épistémologie : prendre l'enseignement verbal du Buddha et des autres sages comme base fiable de cognitions\u2014par contraste avec la perception directe (pratyakṣa) et l'inférence (anumāna).",
 'vi': "Phạn ngữ āptavacana, một trong ba lượng của lượng luận, chỉ lấy lời dạy của Phật và các bậc thánh làm căn cứ nhận thức đáng tin; đối lại với hiện lượng (kinh nghiệm trực tiếp) và tỷ lượng (suy lý).",
}

D['如是我闻'] = {
 'zh': "诸经开首的定式，意为‘我（阿难）亲自听闻佛陀如是宣说’。结集时阿难依此起首，以证经文真实可信。",
 'en': "The fixed formula that opens the sūtras, meaning \u201cI (Ānanda) personally heard the Buddha expound thus.\u201d At the council Ānanda began with this phrase to certify that the scripture-text is true and trustworthy.",
 'fr': "La formule fixe qui ouvre les sūtras, signifiant « Moi (Ānanda) j'ai personnellement entendu le Buddha exposer ainsi ». Au concile, Ānanda commença par cette phrase pour certifier que le texte de l'écriture est vrai et digne de foi.",
 'vi': "Công thức mở đầu các kinh, nghĩa là “tôi (A-nan) thân nghe đức Phật tuyên thuyết như vậy”. Khi kết tập, A-nan lấy câu này làm mở đầu để chứng kinh văn chân thật đáng tin.",
}

json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('batch_F3 →', len(D))
