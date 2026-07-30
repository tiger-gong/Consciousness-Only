#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))

D['法名轨持'] = {
 'zh': "解释‘法’字之义：法有‘轨生物解、任持自性’二义——轨则能令人生起认识，自性能保持各自的体性，故名为法。",
 'en': "An explanation of the word \u201cdharma\u201d: dharma has two senses\u2014\u201cserving as a norm that gives rise to understanding\u201d and \u201cmaintaining its own nature.\u201d As a norm it enables one to form cognition; by \u201cmaintaining\u201d it preserves each thing's own essence\u2014hence it is called dharma.",
 'fr': "Une explication du mot « dharma » : dharma a deux sens\u2014« servir de norme qui fait naître la compréhension » et « maintenir sa propre nature ». Comme norme, il permet de former une cognition ; par « maintien », il préserve l'essence propre de chaque chose\u2014d'où le nom de dharma.",
 'vi': "Giải thích nghĩa chữ “pháp”: pháp có hai nghĩa\u2014“quỹ sinh vật giải” và “nhậm trì tự tính”. Làm khuôn phép khiến người khởi nhận thức, giữ được thể tính riêng, nên gọi là pháp.",
}

D['我名主宰'] = {
 'zh': "解释‘我’字之义：我有‘主宰’义，即认为有一个常一、能自在支配身心的实体。佛法则说此‘我’不可得，故立‘无我’。",
 'en': "An explanation of the word \u201cself\u201d: \u201cself\u201d has the sense of \u201csovereign controller\u201d\u2014the notion that there is a permanent, unitary substance that can freely govern body and mind. The Buddha-Dharma, however, teaches that this \u201cself\u201d cannot be found, and so sets forth \u201cno-self.\u201d",
 'fr': "Une explication du mot « soi » : « soi » a le sens de « contrôleur souverain »\u2014l'idée qu'il existe une substance permanente et unitaire capable de gouverner librement le corps et l'esprit. Le Dharma, cependant, enseigne que ce « soi » est introuvable, et pose donc le « non-soi ».",
 'vi': "Giải thích nghĩa chữ “ngã”: ngã có nghĩa “chủ tể”, tức cho rằng có một thực thể thường nhất, tự tại chi phối thân tâm. Còn Phật pháp nói cái “ngã” ấy bất khả đắc, nên lập “vô ngã”.",
}

D['兜率天'] = {
 'zh': "梵语 Tuṣita，意译知足天，欲界六天中的第四天。内院为一生补处菩萨说法之处，弥勒菩萨现居于此。",
 'en': "Sanskrit Tuṣita, rendered \u201cthe Heaven of Contentment,\u201d the fourth of the six heavens of the desire realm. Its inner court is where the bodhisattva of one-more-birth expounds the Dharma; the bodhisattva Maitreya now dwells there.",
 'fr': "Sanskrit Tuṣita, rendu « le Ciel du Contentement », le quatrième des six cieux du monde du désir. Sa cour intérieure est le lieu où le bodhisattva à une naissance près expose le Dharma ; le bodhisattva Maitreya y demeure à présent.",
 'vi': "Phạn ngữ Tuṣita, dịch nghĩa Tri Túc thiên, tầng thứ tư trong sáu tầng trời cõi dục. Nội viện là nơi Bồ Tát nhất sinh bổ xứ thuyết pháp; Bồ Tát Di-lặc hiện ở đó.",
}

D['阎浮提'] = {
 'zh': "梵语 Jambudvīpa，意译南赡部洲，须弥山四大洲之南洲，即我人所居的世界。",
 'en': "Sanskrit Jambudvīpa, rendered \u201cthe Southern Continent of the Jambu tree,\u201d the southern of the four great continents around Mount Sumeru\u2014that is, the world we inhabit.",
 'fr': "Sanskrit Jambudvīpa, rendu « le Continent méridional de l'arbre Jambu », le continent sud parmi les quatre grands continents autour du mont Sumeru\u2014c'est-à-dire le monde que nous habitons.",
 'vi': "Phạn ngữ Jambudvīpa, dịch nghĩa Nam Thiệm Bộ Châu, châu phía nam trong bốn đại châu quanh núi Tu-di, tức thế giới mà con người chúng ta ở.",
}

D['极乐世界'] = {
 'zh': "梵语 Sukhāvatī，阿弥陀佛的净土，在西方。众生念佛发愿即可往生，于彼永离众苦、但受诸乐，故名极乐。",
 'en': "Sanskrit Sukhāvatī, the Pure Land of Amitābha Buddha, in the west. Beings who are mindful of the Buddha and make the vow can be reborn there, where they are forever free of all suffering and experience only bliss\u2014hence \u201cUltimate Bliss.\u201d",
 'fr': "Sanskrit Sukhāvatī, la Terre pure du Buddha Amitābha, à l'ouest. Les êtres attentifs au Buddha et qui font le vœu peuvent y renaître, où ils sont à jamais libres de toute souffrance et n'éprouvent que la félicité\u2014d'où « Félicité suprême ».",
 'vi': "Phạn ngữ Sukhāvatī, Tịnh độ của Phật A-di-đà, ở phương Tây. Chúng sinh niệm Phật phát nguyện thì được vãng sinh, ở đó vĩnh viễn lìa mọi khổ, chỉ thọ các lạc, nên gọi Cực Lạc.",
}

D['往生'] = {
 'zh': "指命终后离此世界，转生于他方净土（多指弥陀极乐世界）。念佛法门以信愿持名、求生净土为宗。",
 'en': "Refers to leaving this world after death and being reborn in a Pure Land of another quarter (usually Amitābha's Land of Ultimate Bliss). The nianfo (Buddha-recitation) practice takes faith, vow, and holding the name, seeking rebirth in the Pure Land, as its tenet.",
 'fr': "Désigne le fait de quitter ce monde après la mort et de renaître dans une Terre pure d'une autre région (généralement la Terre de Félicité suprême d'Amitābha). La pratique du nianfo (récitation du Buddha) prend pour thèse la foi, le vœu et la tenue du nom, en quête de la renaissance en Terre pure.",
 'vi': "Chỉ sau khi mệnh chung lìa thế giới này, chuyển sinh về Tịnh độ phương khác (phần nhiều chỉ thế giới Cực Lạc của Phật Di-đà). Pháp môn niệm Phật lấy tín nguyện trì danh, cầu sinh Tịnh độ làm tông.",
}

D['信愿持名'] = {
 'zh': "净土法门的修行纲要：深信（信）、切愿往生（愿）、执持阿弥陀佛名号（持名），三者具足即得往生。",
 'en': "The essential framework of Pure Land practice: deep faith (faith), earnest vow to be reborn (vow), and firmly holding the name of Amitābha Buddha (holding the name); when these three are complete, one attains rebirth.",
 'fr': "Le cadre essentiel de la pratique de la Terre pure : foi profonde (foi), vœu ardent de renaître (vœu) et tenue ferme du nom du Buddha Amitābha (tenue du nom) ; lorsque ces trois sont complets, on obtient la renaissance.",
 'vi': "Cương yếu tu hành của pháp môn Tịnh độ: tin sâu (tín), thiết tha nguyện vãng sinh (nguyện), chấp trì danh hiệu Phật A-di-đà (trì danh); ba thứ đầy đủ liền được vãng sinh.",
}

D['诸行无常'] = {
 'zh': "三法印之一。谓一切有为造作的现象皆迁流变化、不能常住，是佛法判别真伪的根本教义之一。",
 'en': "One of the three Dharma-seals. It teaches that all conditioned, fabricated phenomena flow and change and cannot abide permanently; it is one of the fundamental teachings by which the Buddha-Dharma distinguishes the true from the false.",
 'fr': "L'un des trois sceaux du Dharma. Il enseigne que tous les phénomènes conditionnés et fabriqués s'écoulent et changent et ne peuvent demeurer de façon permanente ; c'est l'un des enseignements fondamentaux par lesquels le Dharma distingue le vrai du faux.",
 'vi': "Một trong ba pháp ấn. Nói hết thảy hiện tượng hữu vi tạo tác đều thiên lưu biến hóa, không thể thường trụ; là một trong những giáo nghĩa căn bản để Phật pháp phán biệt chân ngụy.",
}

D['应观法界性，一切唯心造'] = {
 'zh': "出自《华严经》。谓应当观照十法界的体性，一切境界、圣凡因果，无不由心所造，为唯心、唯识义的经证。",
 'en': "From the Avataṃsaka-sūtra. It teaches that one should contemplate the nature of the dharma-realm: all realms, and all cause-and-effect of sages and ordinary beings, are without exception created by the mind\u2014a scriptural proof of the \u201cmind-only\u201d and \u201cconsciousness-only\u201d meaning.",
 'fr': "Tiré de l'Avataṃsaka-sūtra. Il enseigne qu'il faut contempler la nature du réalm-de-dharma : tous les domaines, et toute la cause-et-effet des sages et des êtres ordinaires, sont sans exception créés par l'esprit\u2014une preuve scripturaire du sens « esprit seul » et « rien-que-conscience ».",
 'vi': "Xuất từ Kinh Hoa Nghiêm. Nói nên quán chiếu thể tính của mười pháp giới: hết thảy cảnh giới, nhân quả thánh phàm, không gì chẳng do tâm tạo\u2014là kinh chứng cho nghĩa duy tâm, duy thức.",
}

json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('batch_F1 →', len(D))
