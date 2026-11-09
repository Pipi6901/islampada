# -*- coding: utf-8 -*-
"""Строки контекста к отрывкам: кто говорит, к кому и по какому поводу.

Правила: только то, что общеизвестно и надёжно передаётся, без толкования и оценок;
не длиннее 34 слов. Где повод ниспослания спорный, пишем только, о ком или о чём аят.
Для остальных отрывков — справка о суре (место ниспослания и число аятов), собранная
из метаданных Tanzil.

Ключ строки в корпусе (`Card.passage`):
    a{сура}-{аят}  — особая справка об отрывке, начинающемся с этого аята
    n{сура}        — справка об отдельной суре
    s{сура}        — справка по умолчанию (сура, место ниспослания, число аятов)
"""

# (сура, первый аят): (ru, en, ar)
AYAH_NOTES = {
    (1, 1): ("Открывающая Коран сура; её читают в каждом ракаате молитвы.",
             "The opening surah of the Quran, recited in every unit of prayer.",
             "فاتحة الكتاب، تُقرأ في كل ركعة من الصلاة."),
    (2, 255): ("Аят аль-Курси. В хадисе он назван величайшим аятом Корана.",
               "Ayat al-Kursi. A hadith calls it the greatest ayah of the Quran.",
               "آية الكرسي، وقد جاء في الحديث أنها أعظم آية في القرآن."),
    (2, 286): ("Последний аят суры «Аль-Бакара». В хадисе сказано: кто прочтёт два последних аята "
               "этой суры ночью, тому их будет достаточно.",
               "The last ayah of Al-Baqarah. A hadith says that whoever recites the last two ayat "
               "of this surah at night, they will suffice him.",
               "آخر آية من سورة البقرة. وفي الحديث: «من قرأ بالآيتين من آخر سورة البقرة في ليلة كفتاه»."),
    (24, 35): ("Аят ан-Нур («Света»): притча о свете Аллаха и светильнике в нише.",
               "The Light Verse (Ayat an-Nur): a parable of God's light and a lamp in a niche.",
               "آية النور: مَثَل نور الله والمصباح في المشكاة."),
    (9, 40): ("Слова обращены к Пророку и Абу Бакру: они скрывались в пещере Саур по пути в Медину.",
              "Said to the Prophet and Abu Bakr as they hid in the cave of Thawr on the way to Medina.",
              "قيلت للنبي ولأبي بكر في غار ثور أثناء الهجرة إلى المدينة."),
    (20, 46): ("Аллах говорит Мусе и Харуну, посылая их к фараону.",
               "God speaks to Musa and Harun as He sends them to Pharaoh.",
               "خطاب الله لموسى وهارون حين أرسلهما إلى فرعون."),
    (20, 68): ("Аллах говорит Мусе перед состязанием с колдунами фараона.",
               "God speaks to Musa before the contest with Pharaoh's magicians.",
               "خطاب الله لموسى قبل مواجهة سحرة فرعون."),
    (20, 21): ("Аллах говорит Мусе, когда его посох превращается в змею.",
               "God speaks to Musa when his staff turns into a serpent.",
               "خطاب الله لموسى حين انقلبت عصاه حية."),
    (27, 10): ("Аллах говорит Мусе у огня, который тот увидел в пути.",
               "God speaks to Musa at the fire he saw on his journey.",
               "خطاب الله لموسى عند النار التي رآها في طريقه."),
    (28, 31): ("Аллах говорит Мусе, когда тот подошёл к огню.",
               "God speaks to Musa as he comes near the fire.",
               "خطاب الله لموسى حين أتى النار."),
    (28, 7): ("Откровение матери Мусы о её младенце.",
              "A revelation to the mother of Musa about her infant.",
              "وحي الله إلى أم موسى في شأن وليدها."),
    (86, 1): None,
    (12, 86): ("Якуб говорит о своём горе после потери сыновей.",
               "Ya'qub speaks of his grief after losing his sons.",
               "قول يعقوب عن حزنه بعد فقد ولديه."),
    (12, 84): ("Якуб скорбит об Юсуфе.",
               "Ya'qub mourns for Yusuf.",
               "يعقوب يحزن على يوسف."),
    (12, 87): ("Якуб велит сыновьям искать Юсуфа и его брата и не отчаиваться.",
               "Ya'qub tells his sons to seek Yusuf and his brother and not to lose hope.",
               "يعقوب يأمر أبناءه أن يبحثوا عن يوسف وأخيه وألا ييأسوا."),
    (12, 92): ("Юсуф прощает своих братьев.",
               "Yusuf forgives his brothers.",
               "يوسف يعفو عن إخوته."),
    (12, 64): ("Ответ Якуба сыновьям, просящим отпустить с ними Бунъямина.",
               "Ya'qub answers his sons who ask to take Binyamin with them.",
               "جواب يعقوب لأبنائه حين طلبوا أن يرسل معهم بنيامين."),
    (12, 18): ("Слова Якуба, когда братья принесли окровавленную рубашку Юсуфа.",
               "Ya'qub's words when his sons bring Yusuf's shirt stained with blood.",
               "قول يعقوب حين جاءه أبناؤه بقميص يوسف ملطخًا بالدم."),
    (12, 83): ("Слова Якуба, когда сыновья вернулись без Бунъямина.",
               "Ya'qub's words when his sons return without Binyamin.",
               "قول يعقوب حين رجع أبناؤه بلا بنيامين."),
    (12, 67): ("Якуб наставляет сыновей перед дорогой в Египет.",
               "Ya'qub advises his sons before their journey to Egypt.",
               "وصية يعقوب لأبنائه قبل سفرهم إلى مصر."),
    (21, 87): ("Мольба Юнуса из чрева кита.",
               "The prayer of Yunus from inside the whale.",
               "دعاء يونس في بطن الحوت."),
    (21, 83): ("Мольба Аййуба (Иова).",
               "The prayer of Ayyub (Job).",
               "دعاء أيوب."),
    (21, 89): ("Мольба Закарии.",
               "The prayer of Zakariyya.",
               "دعاء زكريا."),
    (19, 4): ("Мольба Закарии о сыне.",
              "Zakariyya's prayer for a son.",
              "دعاء زكريا أن يرزقه الله ولدًا."),
    (19, 24): ("Слова, обращённые к Марьям во время родов.",
               "Words addressed to Maryam during childbirth.",
               "كلمات وُجِّهت إلى مريم عند الولادة."),
    (28, 24): ("Мольба Мусы в Мадьяне, куда он пришёл один и без средств.",
               "Musa's prayer in Madyan, where he arrived alone and with nothing.",
               "دعاء موسى في مدين حين وصل وحيدًا بلا مال."),
    (28, 16): ("Муса просит прощения у Аллаха.",
               "Musa asks God for forgiveness.",
               "موسى يستغفر ربه."),
    (7, 23): ("Мольба Адама и его жены.",
              "The prayer of Adam and his wife.",
              "دعاء آدم وزوجه."),
    (2, 37): ("Адам получил от Господа слова, и Аллах принял его покаяние.",
              "Adam received words from his Lord, and God accepted his repentance.",
              "تلقّى آدم من ربه كلمات فتاب الله عليه."),
    (11, 41): ("Слова Нуха, когда он взошёл на ковчег.",
               "The words of Nuh as he boarded the ark.",
               "قول نوح حين ركب السفينة."),
    (23, 29): ("Мольба Нуха.",
               "The prayer of Nuh.",
               "دعاء نوح."),
    (14, 40): ("Мольба Ибрахима.",
               "The prayer of Ibrahim.",
               "دعاء إبراهيم."),
    (6, 78): ("Рассказ о том, как Ибрахим искал истинного Господа.",
              "The account of how Ibrahim searched for his true Lord.",
              "قصة بحث إبراهيم عن ربه الحق."),
    (2, 260): ("Просьба Ибрахима показать, как Аллах оживляет мёртвых.",
               "Ibrahim asks to be shown how God gives life to the dead.",
               "طلب إبراهيم أن يريه الله كيف يحيي الموتى."),
    (27, 19): ("Сулейман улыбается, услышав слова муравья.",
               "Sulayman smiles, amused at the words of an ant.",
               "سليمان يتبسم ضاحكًا من قول نملة."),
    (27, 40): ("Сулейман видит трон царицы Билкис перед собой.",
               "Sulayman sees the throne of Bilqis set before him.",
               "سليمان يرى عرش بلقيس مستقرًّا عنده."),
    (34, 13): ("Обращение к семье Дауда.",
               "An address to the family of Dawud.",
               "خطاب لآل داود."),
    (18, 10): ("Мольба юношей, укрывшихся в пещере.",
               "The prayer of the young men who took refuge in the cave.",
               "دعاء الفتية الذين أَوَوْا إلى الكهف."),
    (18, 23): ("Обращено к Пророку: не говорить «сделаю это завтра», не добавив «если пожелает Аллах».",
               "Addressed to the Prophet: never say \"I will do it tomorrow\" without adding \"if God wills\".",
               "خطاب للنبي: لا تقل إني فاعل ذلك غدًا إلا أن تقول إن شاء الله."),
    (3, 139): ("Ниспослано мусульманам после поражения при Ухуде.",
               "Revealed to the Muslims after the setback at Uhud.",
               "نزلت في المسلمين بعد ما أصابهم يوم أحد."),
    (3, 173): ("Связано с походом к Хамра аль-Асад после Ухуда.",
               "Linked to the march to Hamra al-Asad after Uhud.",
               "في خروج المسلمين إلى حمراء الأسد بعد أحد."),
    (3, 154): ("Об Ухуде: Аллах ниспослал на сражавшихся дремоту.",
               "About Uhud: God sent drowsiness upon those who fought.",
               "في غزوة أحد: أنزل الله النعاس على المقاتلين."),
    (8, 10): ("О битве при Бадре.",
              "About the Battle of Badr.",
              "في غزوة بدر."),
    (8, 11): ("О битве при Бадре.",
              "About the Battle of Badr.",
              "في غزوة بدر."),
    (9, 26): ("О битве при Хунайне.",
              "About the Battle of Hunayn.",
              "في غزوة حنين."),
    (48, 4): ("Сура «Аль-Фатх» ниспослана после заключения мира в аль-Худайбии.",
              "Surah Al-Fath was revealed after the treaty of Hudaybiyyah.",
              "نزلت سورة الفتح بعد صلح الحديبية."),
    (62, 10): ("Аят о пятничной молитве и о том, что следует после неё.",
               "An ayah about the Friday prayer and what follows it.",
               "آية عن صلاة الجمعة وما بعدها."),
    (96, 1): ("Первые аяты, ниспосланные Пророку.",
              "The first ayat revealed to the Prophet.",
              "أول ما نزل على النبي من القرآن."),
    (2, 185): ("Аят о посте в месяц Рамадан.",
               "An ayah about fasting in the month of Ramadan.",
               "آية عن صيام شهر رمضان."),
    (24, 22): ("Связано с Абу Бакром, который хотел прекратить помощь Мистаху.",
               "Linked to Abu Bakr, who had wanted to stop supporting Mistah.",
               "في أبي بكر حين همّ أن يقطع نفقته عن مِسطح."),
    (59, 9): ("Об ансарах, жителях Медины, принявших переселенцев.",
              "About the Ansar, the people of Medina who welcomed the emigrants.",
              "في الأنصار الذين آووا المهاجرين في المدينة."),
    (59, 10): ("О тех, кто пришёл после первых мусульман, и об их мольбе.",
               "About those who came after the first Muslims, and their prayer.",
               "في الذين جاؤوا من بعد المهاجرين والأنصار ودعائهم."),
    (20, 25): ("Мольба Мусы, когда Аллах поручил ему идти к фараону.",
               "Musa's prayer when God charged him to go to Pharaoh.",
               "دعاء موسى حين كلّفه الله بالذهاب إلى فرعون."),
    (20, 14): ("Аллах говорит Мусе у огня.",
               "God speaks to Musa at the fire.",
               "خطاب الله لموسى عند النار."),
    (73, 1): ("Пророку велено вставать на ночную молитву.",
              "The Prophet is told to rise for prayer at night.",
              "أمر للنبي بقيام الليل."),
    (17, 79): ("Об ночной молитве (тахаджуд).",
               "About the night prayer (tahajjud).",
               "عن صلاة الليل (التهجد)."),
    (55, 13): ("Припев суры «Ар-Рахман»: он повторяется в ней 31 раз.",
               "The refrain of Surah Ar-Rahman: it recurs 31 times.",
               "الآية المتكررة في سورة الرحمن، وردت فيها إحدى وثلاثين مرة."),
    (35, 34): ("Слова обитателей Рая.",
               "The words of the people of Paradise.",
               "قول أهل الجنة."),
    (3, 159): ("О мягкости Пророка с людьми; ниспослано после Ухуда.",
               "On the Prophet's gentleness with people; revealed after Uhud.",
               "في لين النبي مع الناس؛ نزلت بعد أحد."),
    (5, 23): ("Из рассказа о народе Мусы, отказавшемся войти в Святую землю.",
              "From the account of Musa's people, who refused to enter the Holy Land.",
              "من قصة قوم موسى حين أبَوا دخول الأرض المقدسة."),
    (10, 84): ("Слова Мусы своему народу.",
               "Musa's words to his people.",
               "قول موسى لقومه."),
    (10, 85): ("Ответ народа Мусы.",
               "The reply of Musa's people.",
               "جواب قوم موسى."),
    (7, 128): ("Слова Мусы своему народу.",
                "Musa's words to his people.",
                "قول موسى لقومه."),
    (40, 44): ("Слова верующего из семьи фараона.",
               "The words of the believer from Pharaoh's family.",
               "قول مؤمن آل فرعون."),
    (11, 56): ("Слова пророка Худа своему народу.",
               "The words of the prophet Hud to his people.",
               "قول النبي هود لقومه."),
    (15, 56): ("Слова Ибрахима посланникам, принёсшим ему весть.",
               "Ibrahim's words to the messengers who brought him the news.",
               "قول إبراهيم للرسل الذين بشّروه."),
}
AYAH_NOTES.pop((86, 1))

# сура: (ru, en, ar)
SURA_NOTES = {
    93: ("Сура «Ад-Духа». Ниспослана Пророку после паузы в откровении, когда ему говорили, что Господь оставил его.",
         "Surah Ad-Duha. Revealed to the Prophet after a pause in revelation, when people said his Lord had left him.",
         "سورة الضحى. نزلت على النبي بعد انقطاع الوحي، حين قيل إن ربه تركه."),
    94: ("Сура «Аш-Шарх» утешает Пророка в трудное время мекканского периода.",
         "Surah Ash-Sharh comforts the Prophet in a hard time during the Meccan period.",
         "سورة الشرح، تسلية للنبي في وقت الشدة بمكة."),
    112: ("Сура «Аль-Ихляс». В хадисе сказано, что она равна трети Корана.",
          "Surah Al-Ikhlas. A hadith says that it equals a third of the Quran.",
          "سورة الإخلاص. جاء في الحديث أنها تعدل ثلث القرآن."),
    113: ("Одна из двух сур-прибежищ: Пророк читал их, прося защиты у Аллаха.",
          "One of the two surahs of refuge, which the Prophet recited to seek God's protection.",
          "إحدى المعوِّذتين، كان النبي يقرؤهما استعاذةً بالله."),
    114: ("Одна из двух сур-прибежищ: Пророк читал их, прося защиты у Аллаха.",
          "One of the two surahs of refuge, which the Prophet recited to seek God's protection.",
          "إحدى المعوِّذتين، كان النبي يقرؤهما استعاذةً بالله."),
}


def passage_key(sura, a, b):
    if (sura, a) in AYAH_NOTES:
        return f"a{sura}-{a}"
    if sura in SURA_NOTES:
        return f"n{sura}"
    return f"s{sura}"


def _plural_ru(n, forms):
    ones, tens = n % 10, n % 100
    if ones == 1 and tens != 11:
        return forms[0]
    if 2 <= ones <= 4 and not 12 <= tens <= 14:
        return forms[1]
    return forms[2]


def _ayat_ar(n):
    if n == 1:
        return "آية"
    if n == 2:
        return "آيتان"
    return "آيات" if 3 <= n <= 10 else "آية"


def context(lang, key, passage, meta):
    sura, a, b = passage
    idx = {"ru": 0, "en": 1, "ar": 2}[lang]
    if key.startswith("a"):
        return AYAH_NOTES[(sura, a)][idx]
    if key.startswith("n"):
        return SURA_NOTES[sura][idx]
    m = meta[sura]
    n = m["ayas"]
    medinan = m["type"] == "Medinan"
    if lang == "ru":
        from surah_names import RU
        place = "мединская" if medinan else "мекканская"
        word = _plural_ru(n, ("аят", "аята", "аятов"))
        return f"Сура «{RU[sura - 1]}» ({sura}), {place}, {n} {word}."
    if lang == "en":
        from surah_names import EN
        place = "Medinan" if medinan else "Meccan"
        return f"Surah {EN[sura - 1]} ({sura}), {place}, {n} ayat."
    place = "مدنية" if medinan else "مكية"
    return f"سورة {m['name_ar']} ({sura})، {place}، {n} {_ayat_ar(n)}."
