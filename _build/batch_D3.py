#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))

D['舍利弗尊者'] = {
 'zh': "梵名 Śāriputra，佛陀十大弟子之一，以智慧第一著称。常代佛说法，为诸经中问答的当机者。",
 'en': "Sanskrit Śāriputra, one of the Buddha's ten great disciples, renowned as foremost in wisdom. He often expounded the Dharma on the Buddha's behalf and is the chief interlocutor in the questions and answers of many sūtras.",
 'fr': "Sanskrit Śāriputra, l'un des dix grands disciples du Buddha, réputé premier en sagesse. Il exposait souvent le Dharma au nom du Buddha et est le principal interlocuteur dans les questions-réponses de nombreux sūtras.",
 'vi': "Phạn danh Śāriputra (Xá-lợi-phất), một trong mười đại đệ tử của Phật, nổi tiếng trí tuệ đệ nhất. Thường thay Phật thuyết pháp, là người đương cơ vấn đáp trong nhiều kinh.",
}

D['阿难尊者'] = {
 'zh': "梵名 Ānanda，佛陀堂弟，侍佛二十五年，多闻第一。佛灭后于结集大会中诵出经藏，经首‘如是我闻’即出其口。",
 'en': "Sanskrit Ānanda, the Buddha's cousin, who attended upon the Buddha for twenty-five years and was foremost in hearing (learning). After the Buddha's parinirvāṇa he recited the scripture-basket at the council; the \u201cThus have I heard\u201d that opens the sūtras issued from his mouth.",
 'fr': "Sanskrit Ānanda, cousin du Buddha, qui servit le Buddha pendant vingt-cinq ans et fut premier en écoute (érudition). Après le parinirvāṇa, il récita la corbeille des écritures au concile ; le « Ainsi ai-je entendu » qui ouvre les sūtras sortit de sa bouche.",
 'vi': "Phạn danh Ānanda (A-nan), em họ của Phật, hầu Phật hai mươi lăm năm, đa văn đệ nhất. Sau khi Phật diệt độ, trong đại hội kết tập tụng ra Kinh tạng; câu “Như thị ngã văn” mở đầu các kinh chính là từ miệng ngài.",
}

D['波斯匿王'] = {
 'zh': "梵名 Prasenajit，中印度憍萨罗国王，与佛陀同时，皈依三宝，为佛教重要护法。《楞严经》等多有其问法记载。",
 'en': "Sanskrit Prasenajit, king of Kośala in central India, a contemporary of the Buddha who took refuge in the Three Jewels and was an important protector of Buddhism. His questioning of the Dharma is recorded in the Śūraṅgama-sūtra and elsewhere.",
 'fr': "Sanskrit Prasenajit, roi de Kośala en Inde centrale, contemporain du Buddha, qui prit refuge dans les Trois Joyaux et fut un important protecteur du bouddhisme. Ses questions sur le Dharma sont consignées dans le Śūraṅgama-sūtra et ailleurs.",
 'vi': "Phạn danh Prasenajit (Ba-tư-nặc), vua nước Kiều-tát-la miền Trung Ấn, đồng thời với Phật, quy y Tam Bảo, là vị hộ pháp quan trọng của Phật giáo. Kinh Lăng Nghiêm v.v. có nhiều ghi chép việc ngài hỏi pháp.",
}

D['茉莉夫人'] = {
 'zh': "梵名 Mallikā，波斯匿王之王后，虔信佛法。因持斋护戒、劝王向善，为佛所称叹的在家女众典范。",
 'en': "Sanskrit Mallikā, queen of King Prasenajit, a devout believer in the Buddha-Dharma. Because she observed the fast and precepts and urged the king toward the good, she was praised by the Buddha as a model laywoman.",
 'fr': "Sanskrit Mallikā, reine du roi Prasenajit, croyante fervente du Dharma. Parce qu'elle observait le jeûne et les préceptes et exhortait le roi au bien, elle fut louée par le Buddha comme un modèle de laïque.",
 'vi': "Phạn danh Mallikā (Mạt-lợi), vương hậu của vua Ba-tư-nặc, thành tín Phật pháp. Vì trì trai giữ giới, khuyên vua hướng thiện, được Phật khen ngợi là mẫu mực nữ cư sĩ.",
}

D['弘一大师'] = {
 'zh': "近代高僧李叔同（1880–1942），出家后专弘南山律，行持精严，为民国佛教复兴律学的代表人物。",
 'en': "The modern eminent monk Li Shutong (1880\u20131942). After going forth he devoted himself to propagating the Nanshan Vinaya, keeping the precepts with great strictness; he was a representative figure in the revival of Vinaya studies in Republican-era Buddhism.",
 'fr': "Le moine éminent moderne Li Shutong (1880\u20131942). Après avoir pris l'habit, il se consacra à propager le Vinaya de Nanshan, gardant les préceptes avec grande rigueur ; il fut une figure représentative du renouveau des études du Vinaya dans le bouddhisme de l'ère républicaine.",
 'vi': "Cao tăng cận đại Lý Thúc Đồng (1880\u20131942). Sau khi xuất gia chuyên hoằng Luật Nam Sơn, hành trì tinh nghiêm; là nhân vật tiêu biểu cho việc phục hưng luật học trong Phật giáo thời Dân Quốc.",
}

D['百丈禅师'] = {
 'zh': "唐代禅宗高僧怀海（720–814），制定《百丈清规》，立‘一日不作，一日不食’的丛林规范。‘野狐禅’‘不落因果、不昧因果’公案即出其门。",
 'en': "The Tang-dynasty Chan master Huaihai (720\u2013814), who drew up the Baizhang Monastic Rules and established the monastic norm \u201ca day without work is a day without food.\u201d The kōan of the \u201cwild-fox Chan\u201d and \u201cnot falling under / not blind to cause and effect\u201d comes from his community.",
 'fr': "Le maître Chan des Tang Huaihai (720\u2013814), qui rédigea les Règles monastiques de Baizhang et établit la norme monastique « un jour sans travail est un jour sans nourriture ». Le kōan du « Chan du renard sauvage » et du « ne pas tomber sous / ne pas être aveugle à la cause et l'effet » provient de sa communauté.",
 'vi': "Cao tăng Thiền tông đời Đường Hoài Hải (720\u2013814), chế định Bách Trượng Thanh Quy, lập quy phạm tùng lâm “một ngày không làm, một ngày không ăn”. Công án “dã hồ thiền”, “bất lạc nhân quả / bất muội nhân quả” chính từ môn hạ của ngài.",
}

D['迦叶佛'] = {
 'zh': "梵名 Kāśyapa Buddha，过去七佛之第六位，释迦牟尼佛前一佛，于贤劫中先释尊而成佛、说法度生。",
 'en': "Sanskrit Kāśyapa Buddha, the sixth of the seven past Buddhas and the Buddha immediately before Śākyamuni; within the present Auspicious Aeon he attained Buddhahood and taught beings before Śākyamuni.",
 'fr': "Sanskrit Kāśyapa Buddha, le sixième des sept Buddhas passés et le Buddha immédiatement avant Śākyamuni ; dans l'Ère fortunée présente, il atteignit la bouddhéité et enseigna les êtres avant Śākyamuni.",
 'vi': "Phạn danh Kāśyapa Buddha (Ca-diếp Phật), vị thứ sáu trong bảy đức Phật quá khứ, là đức Phật ngay trước Phật Thích-ca Mâu-ni; trong Hiền kiếp thành Phật và thuyết pháp độ sinh trước đức Thích Tôn.",
}

D['大梵天'] = {
 'zh': "梵名 Mahābrahmā，色界初禅天之主，名尸弃。外道每误以其为世界的创造主，佛教则视之为护法天神，仍在生死轮回之中。",
 'en': "Sanskrit Mahābrahmā, lord of the first-dhyāna heaven of the form realm, named Śikhin. Outer paths often mistake him for the creator of the world, whereas Buddhism regards him as a Dharma-protecting deity still within the cycle of birth-and-death.",
 'fr': "Sanskrit Mahābrahmā, seigneur du ciel du premier dhyāna du monde de la forme, nommé Śikhin. Les voies extérieures le prennent souvent pour le créateur du monde, tandis que le bouddhisme le considère comme une divinité protectrice du Dharma, encore prise dans le cycle des naissances et des morts.",
 'vi': "Phạn danh Mahābrahmā (Đại Phạm Thiên), chủ của Sơ thiền thiên cõi sắc, tên Thi-khí. Ngoại đạo thường lầm cho là đấng sáng tạo thế giới, còn Phật giáo xem là thiên thần hộ pháp, vẫn còn trong luân hồi sinh tử.",
}

json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('batch_D3 →', len(D))
