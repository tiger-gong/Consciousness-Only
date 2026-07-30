#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(__file__)
p = os.path.join(BASE, 'defs_i18n.json')
D = json.load(open(p, encoding='utf-8'))

D['承圣言以标宗'] = {
 'zh': "本论科判用语。指承接着佛陀的圣言量，标举出本论的宗旨——‘一切法无我’。",
 'en': "A term of outline division in this treatise. It means receiving the Buddha's authoritative sacred word so as to set forth the tenet of the treatise\u2014\u201call dharmas are without self.\u201d",
 'fr': "Terme de division du plan dans ce traité. Il signifie recevoir la parole sacrée autoritative du Buddha afin d'énoncer la thèse du traité\u2014« tous les dharmas sont sans soi ».",
 'vi': "Thuật ngữ khoa phán của bộ luận này. Nghĩa là thừa tiếp thánh ngôn lượng của đức Phật, nêu rõ tông chỉ của luận\u2014“nhất thiết pháp vô ngã”.",
}

D['设问答以明宗'] = {
 'zh': "本论科判用语。指设立问答的形式，进一步阐明本论‘一切法无我’的宗旨。",
 'en': "A term of outline division in this treatise. It means setting up a question-and-answer format so as to further clarify the tenet of the treatise\u2014\u201call dharmas are without self.\u201d",
 'fr': "Terme de division du plan dans ce traité. Il signifie poser un format de questions et réponses afin de clarifier davantage la thèse du traité\u2014« tous les dharmas sont sans soi ».",
 'vi': "Thuật ngữ khoa phán của bộ luận này. Nghĩa là đặt hình thức vấn đáp để làm rõ thêm tông chỉ của luận\u2014“nhất thiết pháp vô ngã”.",
}

D['随文释义'] = {
 'zh': "讲义科判用语。指随顺论文的文字，逐句解释其中的义理；本课程四大科之一。",
 'en': "A term of outline division in the lecture notes. It means following along with the words of the treatise and explaining the doctrinal meaning sentence by sentence; one of the four main sections of this course.",
 'fr': "Terme de division du plan dans les notes de cours. Il signifie suivre les mots du traité et expliquer le sens doctrinal phrase par phrase ; l'une des quatre grandes sections de ce cours.",
 'vi': "Thuật ngữ khoa phán của bài giảng. Nghĩa là tùy thuận văn tự của luận văn, giải thích từng câu nghĩa lý trong đó; là một trong bốn khoa lớn của khóa học này.",
}

D['论主略史'] = {
 'zh': "讲义科判用语。指略述论主（天亲菩萨）的生平事迹，为本课程四大科之一。",
 'en': "A term of outline division in the lecture notes. It means briefly recounting the life and deeds of the author of the treatise (the bodhisattva Vasubandhu); one of the four main sections of this course.",
 'fr': "Terme de division du plan dans les notes de cours. Il signifie relater brièvement la vie et les actes de l'auteur du traité (le bodhisattva Vasubandhu) ; l'une des quatre grandes sections de ce cours.",
 'vi': "Thuật ngữ khoa phán của bài giảng. Nghĩa là lược thuật cuộc đời sự tích của luận chủ (Bồ Tát Thiên Thân); là một trong bốn khoa lớn của khóa học này.",
}

D['结示劝修'] = {
 'zh': "讲义科判用语。指在全论讲解完毕后，总结要义并劝勉学人依教修持；本课程四大科之一。",
 'en': "A term of outline division in the lecture notes. It means, after the whole treatise has been explained, summarizing the essentials and exhorting students to practice according to the teaching; one of the four main sections of this course.",
 'fr': "Terme de division du plan dans les notes de cours. Il signifie, après que tout le traité a été expliqué, résumer l'essentiel et exhorter les étudiants à pratiquer selon l'enseignement ; l'une des quatre grandes sections de ce cours.",
 'vi': "Thuật ngữ khoa phán của bài giảng. Nghĩa là sau khi giảng xong toàn luận, kết thúc nêu rõ yếu nghĩa và khuyên người học y giáo tu trì; là một trong bốn khoa lớn của khóa học này.",
}

D['生命相续'] = {
 'zh': "指众生的生命在三世中前后连续、不相断绝。唯识以阿赖耶识持种、受熏，说明此相续之理。",
 'en': "Refers to the continuous, unbroken succession of a sentient being's life across the three times. Consciousness-Only explains this continuity by the ālaya-consciousness's holding of seeds and receiving of perfuming.",
 'fr': "Désigne la succession continue et ininterrompue de la vie d'un être à travers les trois temps. Le Rien-que-conscience explique cette continuité par le fait que la conscience-ālaya tient les semences et reçoit l'imprégnation.",
 'vi': "Chỉ sự liên tục trước sau, không đứt đoạn của sinh mệnh chúng sinh trong ba đời. Duy Thức lấy thức a-lại-da trì chủng, thọ huân để thuyết minh lý tương tục này.",
}

D['业果相续'] = {
 'zh': "指善恶业因与苦乐果报前后连续、不相断绝。业虽灭，种子仍熏在阿赖耶识中，遇缘即起现行感果。",
 'en': "Refers to the continuous, unbroken succession of wholesome and unwholesome karmic causes and their pleasant and painful retributions. Though the karma ceases, the seeds remain perfumed into the ālaya-consciousness, and when conditions are met they give rise to present activity and call forth the fruit.",
 'fr': "Désigne la succession continue et ininterrompue des causes karmiques salutaires et non-salutaires et de leurs rétributions agréables et douloureuses. Bien que le karma cesse, les semences restent imprégnées dans la conscience-ālaya, et lorsque les conditions sont réunies elles produisent l'activité présente et appellent le fruit.",
 'vi': "Chỉ sự liên tục trước sau, không đứt đoạn của nghiệp nhân thiện ác và quả báo khổ vui. Nghiệp tuy diệt, chủng tử vẫn huân trong thức a-lại-da, gặp duyên liền khởi hiện hành cảm quả.",
}

D['心识相续'] = {
 'zh': "指心识的生灭相续、念念不断。前念灭后念生，由阿赖耶识中种子辗转生起，构成精神生命的连续。",
 'en': "Refers to the continuous arising and ceasing of mind-consciousness, thought-moment after thought-moment without interruption. As the former thought ceases the next arises, arising in turn from the seeds in the ālaya-consciousness, constituting the continuity of mental life.",
 'fr': "Désigne la naissance et la cessation continues de la conscience mentale, instant de pensée après instant de pensée sans interruption. Alors que la pensée précédente cesse, la suivante naît, surgissant tour à tour des semences dans la conscience-ālaya, constituant la continuité de la vie mentale.",
 'vi': "Chỉ sự sinh diệt tương tục của tâm thức, niệm niệm không dứt. Niệm trước diệt niệm sau sinh, do chủng tử trong thức a-lại-da xoay vần sinh khởi, cấu thành sự liên tục của đời sống tinh thần.",
}

D['法性本来空寂，因果丝毫不爽'] = {
 'zh': "佛教的核心洞见：从体性看，诸法自性本空、本来寂静；从作用看，因果报应却毫厘不爽。空性与因果并行不悖，即‘不昧因果’之义。",
 'en': "A core Buddhist insight: from the side of essence, all dharmas are by nature originally empty and originally quiescent; from the side of function, karmic cause and effect are not off by a hair. Emptiness and cause-and-effect run parallel without conflict\u2014this is precisely the meaning of \u201cnot blind to cause and effect.\u201d",
 'fr': "Une intuition bouddhique centrale : du côté de l'essence, tous les dharmas sont par nature originellement vides et originellement paisibles ; du côté de la fonction, la cause et l'effet karmiques ne s'écartent pas d'un cheveu. La vacuité et la cause-et-effet vont de pair sans conflit\u2014c'est précisément le sens de « ne pas être aveugle à la cause et l'effet ».",
 'vi': "Cái thấy then chốt của Phật giáo: đứng về thể tính, các pháp tự tính vốn không, vốn tịch tĩnh; đứng về tác dụng, nhân quả báo ứng lại mảy may không sai. Không tính và nhân quả song hành không mâu thuẫn\u2014chính là nghĩa “bất muội nhân quả”.",
}

json.dump(D, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('batch_F4 →', len(D))
