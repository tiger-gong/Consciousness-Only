#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))

D['心识'] = {
 'zh': "梵语 citta-vijñāna，泛指能了别、思量、积集的精神主体，即八识的总称，为唯识学讨论的核心。",
 'en': "Sanskrit citta-vijñāna, broadly referring to the mental subject that discerns, deliberates, and accumulates\u2014that is, a general term for the eight consciousnesses; it is the central concern of Consciousness-Only studies.",
 'fr': "Sanskrit citta-vijñāna, désignant largement le sujet mental qui discerne, délibère et accumule\u2014c'est-à-dire un terme général pour les huit consciences ; c'est le cœur des études du Rien-que-conscience.",
 'vi': "Phạn ngữ citta-vijñāna, chỉ chung tâm thể có khả năng liễu biệt, tư lương, tích tập\u2014tức tên gọi chung của tám thức; là trung tâm bàn luận của Duy Thức học.",
}

D['十法界'] = {
 'zh': "指佛、菩萨、缘觉、声闻四圣法界，与天、人、阿修罗、畜生、饿鬼、地狱六凡法界，合称十法界，摄尽一切迷悟境界。",
 'en': "Refers to the four noble dharma-realms\u2014Buddhas, bodhisattvas, pratyekabuddhas, and śrāvakas\u2014together with the six ordinary dharma-realms of gods, humans, asuras, animals, hungry ghosts, and hells; jointly called the ten dharma-realms, they encompass all realms of delusion and awakening.",
 'fr': "Désigne les quatre réalmes-de-dharma nobles\u2014Buddhas, bodhisattvas, pratyekabuddhas et śrāvakas\u2014avec les six réalmes ordinaires des dieux, humains, asuras, animaux, esprits affamés et enfers ; appelés ensemble les dix réalmes-de-dharma, ils englobent tous les domaines d'illusion et d'éveil.",
 'vi': "Chỉ bốn thánh pháp giới\u2014Phật, Bồ Tát, Duyên Giác, Thanh Văn\u2014cùng sáu phàm pháp giới trời, người, a-tu-la, súc sinh, ngạ quỷ, địa ngục; hợp gọi mười pháp giới, thâu nhiếp hết thảy cảnh giới mê ngộ.",
}

D['三恶道'] = {
 'zh': "指六道中的地狱、饿鬼、畜生三道，因造作重恶业所感的苦报处，又称三涂。",
 'en': "Refers to the three destinies of hell, hungry ghosts, and animals among the six destinies\u2014the places of painful retribution called forth by grave evil karma; also called the three evil paths.",
 'fr': "Désigne les trois destinées de l'enfer, des esprits affamés et des animaux parmi les six destinées\u2014les lieux de rétribution douloureuse appelés par un grave karma mauvais ; aussi appelés les trois voies mauvaises.",
 'vi': "Chỉ ba đường địa ngục, ngạ quỷ, súc sinh trong sáu đường\u2014nơi thọ khổ báo do tạo ác nghiệp nặng chiêu cảm; còn gọi tam đồ.",
}

D['第八识'] = {
 'zh': "即阿赖耶识，八识中的第八，为诸识之根本、种子的藏处，能变现根身器界，是生命相续与万法生起的所依。",
 'en': "That is, the ālaya-consciousness, the eighth of the eight consciousnesses\u2014the root of all the consciousnesses and the storehouse of seeds. It manifests the body-with-faculties and the receptacle-world and is the basis for the continuity of life and the arising of the myriad dharmas.",
 'fr': "C'est-à-dire la conscience-ālaya, la huitième des huit consciences\u2014la racine de toutes les consciences et le réceptacle des semences. Elle manifeste le corps doté de facultés et le monde-réceptacle, et est la base de la continuité de la vie et de la naissance des innombrables dharmas.",
 'vi': "Tức thức a-lại-da, thức thứ tám trong tám thức\u2014là gốc của các thức, chỗ chứa chủng tử. Nó biến hiện căn thân khí giới, là chỗ nương cho sự tương tục của sinh mệnh và sự sinh khởi của vạn pháp.",
}

D['第六意识'] = {
 'zh': "八识中的第六，依意根（末那）而起，遍缘一切法，具分别、比较、推理、想象等功能，通善恶无记三性，为造业的主力。",
 'en': "The sixth of the eight consciousnesses; arising in dependence on the mental faculty (manas), it cognizes all dharmas universally and possesses the functions of discrimination, comparison, reasoning, and imagination. It pertains to all three moral natures\u2014good, evil, and neutral\u2014and is the chief agent in creating karma.",
 'fr': "La sixième des huit consciences ; surgissant en dépendance de la faculté mentale (manas), elle connaît universellement tous les dharmas et possède les fonctions de discrimination, comparaison, raisonnement et imagination. Elle relève des trois natures morales\u2014bonne, mauvaise, neutre\u2014et est le principal agent dans la création du karma.",
 'vi': "Thức thứ sáu trong tám thức; nương ý căn (mạt-na) mà khởi, duyên khắp hết thảy pháp, đủ các công năng phân biệt, so sánh, suy lý, tưởng tượng; thông cả ba tính thiện, ác, vô ký; là chủ lực tạo nghiệp.",
}

D['前六识'] = {
 'zh': "指眼、耳、鼻、舌、身、意六识，为直接了别外境（色声香味触法）的认识作用，相对于第七、第八识而言。",
 'en': "Refers to the six consciousnesses of eye, ear, nose, tongue, body, and mind\u2014the cognitive functions that directly discern external objects (form, sound, smell, taste, touch, and dharmas); set in contrast to the seventh and eighth consciousnesses.",
 'fr': "Désigne les six consciences de l'œil, de l'oreille, du nez, de la langue, du corps et du mental\u2014les fonctions cognitives qui discernent directement les objets externes (forme, son, odeur, saveur, toucher et dharmas) ; par contraste avec les septième et huitième consciences.",
 'vi': "Chỉ sáu thức nhãn, nhĩ, tỷ, thiệt, thân, ý\u2014tác dụng nhận thức trực tiếp liễu biệt ngoại cảnh (sắc thanh hương vị xúc pháp); đối lại với thức thứ bảy, thứ tám.",
}

D['前七识'] = {
 'zh': "指前六识加第七末那识，共七识。此七识皆由第八阿赖耶识所生起，又称七转识，相对于作为根本的第八识。",
 'en': "Refers to the first six consciousnesses plus the seventh, the manas\u2014seven in all. All seven arise from the eighth, ālaya, consciousness and are also called the seven evolving consciousnesses, set in contrast to the eighth consciousness which is their root.",
 'fr': "Désigne les six premières consciences plus la septième, le manas\u2014sept en tout. Toutes les sept surgissent de la huitième conscience ālaya et sont aussi appelées les sept consciences évoluantes, par contraste avec la huitième conscience qui en est la racine.",
 'vi': "Chỉ sáu thức trước cộng thức thứ bảy mạt-na, cộng bảy thức. Bảy thức này đều do thức thứ tám a-lại-da sinh khởi, còn gọi bảy chuyển thức, đối lại với thức thứ tám làm căn bản.",
}

D['四智'] = {
 'zh': "转八识所成的四种无漏智慧：转前五识成成所作智、转第六识成妙观察智、转第七识成平等性智、转第八识成大圆镜智。",
 'en': "The four uncontaminated wisdoms formed by transforming the eight consciousnesses: transforming the first five yields the Wisdom of Accomplishing What Is to Be Done; the sixth, the Wisdom of Wondrous Observation; the seventh, the Wisdom of Equality; and the eighth, the Great Perfect Mirror Wisdom.",
 'fr': "Les quatre sagesses non contaminées formées en transformant les huit consciences : transformer les cinq premières donne la Sagesse de l'Accomplissement de ce qui est à faire ; la sixième, la Sagesse de l'Observation Merveilleuse ; la septième, la Sagesse de l'Égalité ; et la huitième, la Grande Sagesse du Miroir Parfait.",
 'vi': "Bốn trí vô lậu do chuyển tám thức mà thành: chuyển tiền ngũ thức thành Thành Sở Tác Trí, chuyển thức thứ sáu thành Diệu Quán Sát Trí, chuyển thức thứ bảy thành Bình Đẳng Tính Trí, chuyển thức thứ tám thành Đại Viên Cảnh Trí.",
}

D['正报'] = {
 'zh': "指依过去业因所感、能受用的身心果报本身（如人的五蕴身），与作为依止环境的‘依报’相对。",
 'en': "Refers to the very body-and-mind retribution that one receives and experiences, called forth by past karmic causes (such as a human's five-aggregate body); set in contrast to the \u201ccircumstantial retribution\u201d that is the supporting environment.",
 'fr': "Désigne la rétribution corps-et-esprit même que l'on reçoit et éprouve, appelée par des causes karmiques passées (tel le corps aux cinq agrégats d'un humain) ; par contraste avec la « rétribution circonstancielle » qu'est l'environnement de support.",
 'vi': "Chỉ chính bản thân quả báo thân tâm mà mình thọ dụng, do nghiệp nhân quá khứ chiêu cảm (như thân năm uẩn của người); đối lại với “y báo” là hoàn cảnh nương tựa.",
}

D['依报'] = {
 'zh': "指众生正报之身所依止、受用的国土环境（如山河、器物、居所等），与作为主体的‘正报’相对。",
 'en': "Refers to the land and environment on which and by which the body of one's \u201cdirect retribution\u201d depends and which it enjoys (such as mountains and rivers, utensils, and dwellings); set in contrast to the \u201cdirect retribution\u201d that is the subject.",
 'fr': "Désigne la terre et l'environnement dont dépend et dont jouit le corps de la « rétribution directe » (tels les montagnes et rivières, les ustensiles et les demeures) ; par contraste avec la « rétribution directe » qu'est le sujet.",
 'vi': "Chỉ quốc độ hoàn cảnh mà thân chính báo của chúng sinh nương tựa, thọ dụng (như núi sông, khí vật, chỗ ở v.v.); đối lại với “chính báo” là chủ thể.",
}

json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('batch_E4 →', len(D))
