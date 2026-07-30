#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))

D['性相圆融'] = {
 'zh': "谓诸法的体性（性）与相状（相）本来无碍、互摄互融，非一非异。华严、天台等宗常用以显真俗不二之理。",
 'en': "Means that the essence-nature (nature) and the characteristics (mark) of all dharmas are originally unobstructed, mutually embracing and interfusing, neither identical nor different. The Huayan and Tiantai schools often use it to reveal the principle of the non-duality of the ultimate and conventional.",
 'fr': "Signifie que la nature-essence (nature) et les caractéristiques (marque) de tous les dharmas sont originellement sans obstacle, s'embrassant et s'interpénétrant mutuellement, ni identiques ni différentes. Les écoles Huayan et Tiantai l'emploient souvent pour révéler le principe de la non-dualité de l'ultime et du conventionnel.",
 'vi': "Nói thể tính (tính) và tướng trạng (tướng) của các pháp vốn vô ngại, nhiếp nhau dung nhau, chẳng một chẳng khác. Các tông Hoa Nghiêm, Thiên Thai thường dùng để hiển lý chân tục bất nhị.",
}

D['相'] = {
 'zh': "梵语 lakṣaṇa，指事物显现于外、可资分别认识的相状、形态，与内在的‘性（体性）’相对。",
 'en': "Sanskrit lakṣaṇa, referring to the outward-appearing form or feature of a thing by which it can be distinguished and cognized; set in contrast to the inner \u201cnature (essence).\u201d",
 'fr': "Sanskrit lakṣaṇa, désignant la forme ou le trait extérieur d'une chose par lequel on peut la distinguer et la connaître ; par contraste avec la « nature (essence) » intérieure.",
 'vi': "Phạn ngữ lakṣaṇa, chỉ tướng trạng, hình thái hiện ra bên ngoài của sự vật, có thể dùng để phân biệt nhận thức; đối lại với “tính (thể tính)” bên trong.",
}

D['转轮圣王'] = {
 'zh': "梵语 cakravartin，转动轮宝、以正法统治天下的理想君王。具七宝、四德，不以兵威而以德化统摄四方。",
 'en': "Sanskrit cakravartin, the ideal monarch who turns the wheel-treasure and governs the world by the true Dharma. Possessing the seven treasures and four virtues, he rules the four quarters not by military might but by the transforming power of virtue.",
 'fr': "Sanskrit cakravartin, le monarque idéal qui fait tourner le trésor-roue et gouverne le monde par le vrai Dharma. Possédant les sept trésors et quatre vertus, il régit les quatre régions non par la force militaire mais par le pouvoir transformateur de la vertu.",
 'vi': "Phạn ngữ cakravartin, vị vua lý tưởng chuyển động luân bảo, dùng chính pháp thống trị thiên hạ. Đủ bảy báu, bốn đức, không dùng binh uy mà dùng đức hóa nhiếp phục bốn phương.",
}

D['舍利'] = {
 'zh': "梵语 śarīra，意译身骨、灵骨，指佛及圣者遗体火化后所遗的坚固结晶。被尊为修行德业的结晶，为信众供奉礼敬的对象。",
 'en': "Sanskrit śarīra, rendered \u201cbodily bones\u201d or \u201cspiritual bones,\u201d referring to the solid crystalline relics left after the cremation of the body of a Buddha or a sage. Revered as the crystallization of one's meritorious cultivation, they are objects of enshrinement and veneration by the faithful.",
 'fr': "Sanskrit śarīra, rendu « ossements corporels » ou « ossements spirituels », désignant les reliques cristallines solides laissées après la crémation du corps d'un Buddha ou d'un sage. Vénérées comme la cristallisation de la culture méritoire, elles sont des objets d'enchâssement et de vénération pour les fidèles.",
 'vi': "Phạn ngữ śarīra, dịch nghĩa thân cốt, linh cốt, chỉ kết tinh cứng chắc còn lại sau khi hỏa táng di thể của Phật và bậc thánh. Được tôn là kết tinh của đức nghiệp tu hành, là đối tượng để tín chúng cúng dường lễ kính.",
}

D['回小向大'] = {
 'zh': "指原修小乘的行者，回转自度的小乘心，转向自利利他的大乘菩萨道。",
 'en': "Refers to a practitioner who formerly cultivated the Lesser Vehicle turning away from the self-delivering Lesser-Vehicle mind and turning toward the Great-Vehicle bodhisattva path of benefiting both self and others.",
 'fr': "Désigne un pratiquant qui cultivait autrefois le Petit Véhicule et se détourne de l'esprit du Petit Véhicule (se délivrer soi-même) pour se tourner vers la voie du bodhisattva du Grand Véhicule, qui bénéficie à soi et à autrui.",
 'vi': "Chỉ hành giả vốn tu Tiểu thừa, xoay chuyển tâm tự độ của Tiểu thừa, hướng về Bồ Tát đạo Đại thừa tự lợi lợi tha.",
}

D['五戒十善'] = {
 'zh': "五戒：不杀、不盗、不邪淫、不妄语、不饮酒，为在家佛弟子的根本戒。十善：身三、口四、意三共十种善业。行五戒十善得人天善果。",
 'en': "The five precepts\u2014not killing, not stealing, not engaging in sexual misconduct, not lying, and not drinking intoxicants\u2014are the fundamental precepts for lay disciples. The ten wholesome deeds are the ten good karmas\u2014three of body, four of speech, and three of mind. Practicing the five precepts and ten wholesome deeds yields the wholesome fruit of the human and heavenly destinies.",
 'fr': "Les cinq préceptes\u2014ne pas tuer, ne pas voler, ne pas se livrer à l'inconduite sexuelle, ne pas mentir et ne pas boire d'enivrants\u2014sont les préceptes fondamentaux des disciples laïcs. Les dix actes salutaires sont les dix bons karmas\u2014trois du corps, quatre de la parole et trois du mental. Pratiquer les cinq préceptes et les dix actes salutaires produit le fruit salutaire des destinées humaine et céleste.",
 'vi': "Năm giới: không sát, không trộm, không tà dâm, không vọng ngữ, không uống rượu, là giới căn bản của Phật tử tại gia. Mười thiện: thân ba, khẩu bốn, ý ba, cộng mười thứ thiện nghiệp. Hành năm giới mười thiện được thiện quả nhân thiên.",
}

D['忏悔'] = {
 'zh': "梵华合称，忏为陈露先罪、悔为改往修来。指发露过去所造罪业、生起惭愧而誓不再造，以净除业障。",
 'en': "A compound of a Sanskrit transliteration and a Chinese word: \u201cconfession\u201d means to disclose one's former faults, and \u201crepentance\u201d means to change the past and cultivate for the future. It refers to disclosing the evil karma one has created, arousing shame, and vowing not to repeat it, so as to purify away karmic hindrances.",
 'fr': "Un composé d'une translittération sanskrite et d'un mot chinois : la « confession » signifie dévoiler ses fautes passées, et le « repentir » signifie changer le passé et cultiver pour l'avenir. Il désigne le fait de dévoiler le karma mauvais que l'on a créé, de susciter la honte et de faire vœu de ne pas le répéter, afin de purifier les obstacles karmiques.",
 'vi': "Là tên ghép Phạn-Hán: sám là bày tỏ tội trước, hối là sửa xưa tu sau. Chỉ việc phát lồ tội nghiệp đã tạo, khởi tâm hổ thẹn mà thề không tái phạm, để tịnh trừ nghiệp chướng.",
}

D['迦湿弥罗国'] = {
 'zh': "梵名 Kaśmīra，古印度西北的国名，即今克什米尔一带。说一切有部盛行之地，《大毗婆沙论》即在此结集。",
 'en': "Sanskrit Kaśmīra, the name of an ancient country in northwest India\u2014present-day Kashmir. A place where the Sarvāstivāda school flourished; the Mahāvibhāṣā was compiled there.",
 'fr': "Sanskrit Kaśmīra, nom d'un ancien pays du nord-ouest de l'Inde\u2014l'actuel Cachemire. Lieu où l'école Sarvāstivāda prospéra ; le Mahāvibhāṣā y fut compilé.",
 'vi': "Phạn danh Kaśmīra, tên nước cổ ở tây bắc Ấn Độ, tức vùng Kashmir ngày nay. Là nơi Thuyết Nhất Thiết Hữu Bộ thịnh hành; Đại Tì-bà-sa Luận được kết tập tại đây.",
}

D['富娄沙国'] = {
 'zh': "梵名 Puruṣapura，古印度犍陀罗国的都城，即今巴基斯坦白沙瓦，为无著、世亲的故乡。",
 'en': "Sanskrit Puruṣapura, the capital of the ancient Indian kingdom of Gandhāra\u2014present-day Peshawar in Pakistan; the native place of Asaṅga and Vasubandhu.",
 'fr': "Sanskrit Puruṣapura, la capitale de l'ancien royaume indien du Gandhāra\u2014l'actuelle Peshawar au Pakistan ; le lieu natal d'Asaṅga et de Vasubandhu.",
 'vi': "Phạn danh Puruṣapura, kinh đô của nước Kiền-đà-la cổ Ấn Độ, tức Peshawar của Pakistan ngày nay; là quê hương của Vô Trước, Thế Thân.",
}

json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('batch_F2 →', len(D))
