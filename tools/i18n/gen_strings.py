# -*- coding: utf-8 -*-
"""Собирает LampadaCore/Sources/LampadaCore/Strings.swift из данных Misbah.

Русские и английские строки берутся из таблицы оригинала (base_strings.json) с заменой
терминологии (стих -> аят, verse -> ayah, Lampada -> Misbah) и ручными правками там, где
смысл меняется; арабские написаны заново (ar_a.py, ar_b.py, ar_c.py).
Образцы аятов в онбординге берутся из исходников Tanzil, а не набираются руками.

Запуск: python tools/i18n/gen_strings.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "corpus"))

from ar_a import AR_A  # noqa: E402
from ar_b import AR_B  # noqa: E402
from ar_c import AR_C, THEMES as THEMES_DATA  # noqa: E402
import build_corpus  # noqa: E402
import surah_names  # noqa: E402

REMOVED = {
    "sceneShepherd", "sceneClouds", "scenePastel", "sceneOldBook", "sceneFresco",
    "sceneChrist", "scenePaul", "sceneDavid", "sceneGalilee", "sceneStar",
    "sceneGethsemane", "sceneCross", "iconFlame", "iconVitrage", "iconCross",
    "iconChristmas", "iconEaster", "iconDove", "styleLavender",
}
ADDED = [
    "sceneDesert", "sceneStars", "sceneDome", "sceneLantern", "sceneGarden",
    "sceneMosaic", "sceneLattice", "iconMosaic", "iconStar", "iconDawn", "iconDome",
    "iconRosette", "iconLight", "styleEmerald", "showArabic",
]

# ключ: (ru, en) — там, где автозамена терминов не годится
OVERRIDE = {
    "epigraph": ("«Аллах — свет небес и земли»", "“Allah is the Light of the heavens and the earth”"),
    "heroTitle": ("Аят там, куда ты и так смотришь", "The ayah where you already look"),
    "heroSubtitle": (
        "Экран блокировки, рабочий стол, тумбочка у кровати. Ничего не надо помнить — аят просто есть.",
        "Lock screen, home screen, bedside table. Nothing to remember — the ayah is simply there."),
    "heroEditions": ("Оригинал на арабском · Pickthall · Саблуков",
                     "Arabic original · Pickthall · Sablukov"),
    "contextPill": ("Где и когда ниспослан", "Where and when it was revealed"),
    "placesProgress": (
        "Сейчас %d из %d — чем больше, тем чаще аят попадается на глаза",
        "%d of %d — the more places, the more often an ayah catches your eye"),
    "goalDaily": ("Помнить об Аллахе каждый день", "Remember Allah every day"),
    "obWhyQuestion": ("Сколько из них начнутся с аята?", "How many will start with an ayah?"),
    "pwTitle": ("Пусть свет не гаснет", "Let the light keep shining"),
    "pwSub": (
        "Misbah живёт без рекламы и без инвесторов — только на тех, кто им пользуется. "
        "Подписка помогает ему светить",
        "Misbah runs with no ads and no investors — only on the people who use it. "
        "A subscription helps it keep shining"),
    "pwComfortTitle": ("Аят рядом, когда тяжело", "An ayah close by when it is hard"),
    "pwFeedTitle": ("Меньше ленты — больше Корана", "Less feed, more Quran"),
    "styleEmerald": ("Изумруд", "Emerald"),
    "obIconEyebrow": ("ТВОЙ MISBAH", "YOUR MISBAH"),
    "stepPause3": ("Добавьте действие «Пауза с аятом»", "Add the “Pause with an ayah” action"),
    "stepPause3Hint": (
        "в поле действия выберите ту же соцсеть — в неё вас и вернёт",
        "in the action’s field pick the same app — that is where it returns you"),
    "wnIconsEyebrow": ("НОВОЕ В MISBAH", "NEW IN MISBAH"),
    "wnIconsTitle": ("Пять новых иконок", "Five new icons"),
    "wnIconsSub": (
        "«Ночь» — бесплатно, для всех: тапни, и она уже на рабочем столе. Остальные четыре — с Pro",
        "Night is free for everyone: tap it and it’s on your home screen. The other four come with Pro"),
    "wnPicturesTitle": ("Четыре новые картинки", "Four new pictures"),
    "analyticsNote": (
        "Анонимная статистика: какие экраны открывают и где застревают. Без текста аятов и без твоих ответов.",
        "Anonymous stats: which screens people open and where they get stuck. No ayah text and none of your answers."),
    "widgetDescription": ("Аят на каждый день там, где вы и так смотрите",
                          "An ayah for every day, where you already look"),
    "obTrackSub": (
        "Misbah находит людей через рекламу. Если разрешишь, мы узнаем, какая реклама привела тебя, — "
        "и перестанем платить за ту, что не работает. Аяты и твои ответы туда не уходят. "
        "Ответ можно поменять в Настройках iPhone",
        "Misbah finds people through ads. If you allow it, we learn which ad brought you here — and stop "
        "paying for the ones that don’t work. Your ayat and answers are never shared. "
        "You can change this in iPhone Settings"),
    "corpusFailedTitle": ("Не удалось прочитать аяты", "Could not read the ayat"),
    "themesEmpty": ("Можно ничего не выбирать — тогда будут все аяты", "Choose nothing and you get every ayah"),
    "versesUnit": ("аят|аята|аятов", "ayah|ayat"),
    # новые ключи
    "sceneDesert": ("Пустыня", "Desert"),
    "sceneStars": ("Звёзды", "Stars"),
    "sceneDome": ("Купол", "Dome"),
    "sceneLantern": ("Фонарь", "Lantern"),
    "sceneGarden": ("Сад", "Garden"),
    "sceneMosaic": ("Мозаика", "Mosaic"),
    "sceneLattice": ("Орнамент", "Lattice"),
    "iconMosaic": ("Мозаика", "Mosaic"),
    "iconStar": ("Звезда", "Star"),
    "iconDawn": ("Рассвет", "Dawn"),
    "iconDome": ("Купол", "Dome"),
    "iconRosette": ("Розетка", "Rosette"),
    "iconLight": ("Свет", "Light"),
    "showArabic": ("Показывать арабский текст", "Show the Arabic text"),
}

RU_SUF = {"": "", "ов": "ов", "а": "а", "и": "ы", "ом": "ом", "у": "у", "е": "е"}


def ru_fix(s):
    s = s.replace("Lampada", "Misbah").replace("LAMPADA", "MISBAH")
    s = s.replace("со стихом", "с аятом").replace("Со стихом", "С аятом")
    s = re.sub(r"\bСТИХ(ОВ|А|И|ОМ|У|Е)?\b", lambda m: "АЯТ" + (m.group(1) or "").replace("И", "Ы"), s)
    s = re.sub(r"\b([Сс])тих(ов|а|и|ом|у|е)?\b",
               lambda m: ("Аят" if m.group(1) == "С" else "аят") + RU_SUF[m.group(2) or ""], s)
    return s


def en_fix(s):
    s = s.replace("Lampada", "Misbah").replace("LAMPADA", "MISBAH")
    s = re.sub(r"\b([Aa]) verse\b", lambda m: ("An" if m.group(1) == "A" else "an") + " ayah", s)
    for old, new in (("verses", "ayat"), ("Verses", "Ayat"), ("VERSES", "AYAT"),
                     ("verse", "ayah"), ("Verse", "Ayah"), ("VERSE", "AYAH")):
        s = re.sub(rf"\b{old}\b", new, s)
    # Основной рынок английского — США: пишем по-американски.
    for old, new in (("colour", "color"), ("Colour", "Color"), ("Centre", "Center"),
                     ("centre", "center"), ("Centred", "Centered"), ("centred", "centered")):
        s = re.sub(rf"\b{old}", new, s)
    # Название действия в «Командах» — как в App Intents (PauseIntent.swift).
    s = s.replace("Pause with an ayah", "Ayah pause")
    return s


def demo_rows():
    """Образцы аятов для онбординга и паузы — из исходников, не из памяти."""
    ar = build_corpus.load_verses(os.path.join(build_corpus.SRC, "quran-uthmani.txt"))
    en = build_corpus.load_verses(os.path.join(build_corpus.SRC, "en.pickthall.txt"))
    ru = build_corpus.load_verses(os.path.join(build_corpus.SRC, "ru.sablukov.txt"))
    meta = build_corpus.load_meta()

    def card(sura, ayah):
        t = {lang: build_corpus.finish(build_corpus.clean(src[(sura, ayah)]), lang)
             for lang, src in (("ru", ru), ("en", en), ("ar", ar))}
        r = {lang: build_corpus.label(lang, meta, sura, ayah, ayah) for lang in ("ru", "en", "ar")}
        return t, r

    demo_t, demo_r = card(94, 6)
    pause_t, pause_r = card(23, 3)
    out = {}
    for key, t, r in (("demoVerse", demo_t, None), ("demoReference", None, demo_r),
                      ("pauseVerse", pause_t, None), ("pauseReference", None, pause_r)):
        out[key] = tuple((t or r)[lang] for lang in ("ru", "en", "ar"))
    return out


def q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'


def main():
    base = json.load(open(os.path.join(HERE, "base_strings.json"), encoding="utf-8"))
    keys = [k for k in base["keys"] if k not in REMOVED] + ADDED
    ar_all = {**AR_A, **AR_B, **AR_C}
    demo = demo_rows()

    rows = {}
    for key in keys:
        if key in demo:
            rows[key] = list(demo[key])
            continue
        if key in OVERRIDE:
            ru, en = OVERRIDE[key]
        else:
            ru, en = ru_fix(base["rows"][key][0]), en_fix(base["rows"][key][1])
        ar = ar_all.get(key)
        rows[key] = [ru, en, ar]

    missing_ar = [k for k, r in rows.items() if not r[2]]
    if missing_ar:
        sys.exit(f"нет арабского для: {missing_ar}")
    unused = [k for k in ar_all if k not in rows]
    if unused:
        sys.exit(f"арабские строки без ключа: {unused}")

    # проверка: в строках не осталось следов прежнего продукта
    bad = re.compile(r"Слов[оаеу]\b|\bWord\b|\bword\b|ламп|lamp|светильн|Писани|Scripture|Библ|Bible|"
                     r"Христ|Иисус|Jesus|Голуб|\bDove\b|Крест|\bCross\b|Пасх|Easter|Рожд|Christmas|"
                     r"Lampada|стих|verse", re.I)
    for k, r in rows.items():
        for lang, s in zip(("ru", "en"), r[:2]):
            if bad.search(s):
                print("СЛЕД:", k, lang, s)

    # плейсхолдеры должны совпадать во всех языках
    ph = re.compile(r"%(\d\$)?[@d]")
    for k, r in rows.items():
        sets = [sorted(m.group(0) for m in ph.finditer(s)) for s in r]
        if not (sets[0] == sets[1] == sets[2]):
            print("ПОДСТАНОВКИ:", k, sets)

    enum_lines = []
    line = []
    for k in keys:
        line.append(k)
        if len(line) == 6:
            enum_lines.append("        case " + ", ".join(line))
            line = []
    if line:
        enum_lines.append("        case " + ", ".join(line))

    table_lines = []
    for k in keys:
        ru, en, ar = rows[k]
        table_lines.append(f"        .{k}: [{q(ru)}, {q(en)}, {q(ar)}],")

    theme_lines = [f"        {q(t)}: [{q(r)}, {q(e)}, {q(a)}]," for t, (r, e, a) in sorted(THEMES_DATA.items())]

    swift = f'''import Foundation

/// Строки интерфейса на трёх языках: русский, английский, арабский.
///
/// Таблица в коде, а не `.strings`-файлы, по одной причине: язык интерфейса
/// здесь выбирает человек в настройках приложения, а не система. Стандартный
/// механизм локализации подставляет язык устройства и заставляет держать
/// отдельный `Bundle` на каждый `lproj`; здесь же достаточно словаря, который
/// к тому же виден на ревью целиком и не может «потерять ключ» в рантайме.
///
/// Порядок значений в каждой строке всегда один: ru, en, ar.
///
/// ФАЙЛ СГЕНЕРИРОВАН `tools/i18n/gen_strings.py` — не править руками: правки
/// пропадут при следующей сборке. Образцы аятов (`demoVerse`, `pauseVerse`) берутся
/// из исходников корпуса, а не набираются.
public struct L10n: Sendable, Hashable {{
    public let locale: AppLocale

    public init(_ locale: AppLocale) {{
        self.locale = locale
    }}

    public subscript(_ key: Key) -> String {{
        let row = L10n.table[key] ?? ["", "", ""]
        let value = switch locale {{
        case .ru: row[0]
        case .en: row[1]
        case .ar: row[2]
        }}
        guard value.isEmpty else {{ return value }}
        // Пустая строка означает недостающий перевод: показываем английский, а
        // не пустоту. Заметить это на глаз проще, чем дыру в интерфейсе.
        return row[1]
    }}

    /// Подстановка чисел: «Сейчас 3 из 7».
    public func callAsFunction(_ key: Key, _ arguments: CVarArg...) -> String {{
        String(format: self[key], arguments: arguments)
    }}

    /// Число со словом в нужной форме: «1 день», «22 дня», «45 дней».
    ///
    /// Формы лежат в строке таблицы через вертикальную черту: у русского три
    /// (1, 2–4, 5–20), у английского две, у арабского четыре (1, 2, 3–10, 11 и
    /// больше).
    public func count(_ number: Int, _ key: Key) -> String {{
        let forms = self[key].split(separator: "|").map(String.init)
        let index: Int
        switch locale {{
        case .ru:
            let ones = number % 10, tens = number % 100
            index = ones == 1 && tens != 11 ? 0
                : (2...4).contains(ones) && !(12...14).contains(tens) ? 1 : 2
        case .ar:
            let tens = number % 100
            index = number == 1 ? 0 : number == 2 ? 1 : (3...10).contains(tens) ? 2 : 3
        case .en:
            index = number == 1 ? 0 : 1
        }}
        return "\\(number) \\(forms[min(index, forms.count - 1)])"
    }}

    public enum Key: String, Sendable, Hashable, CaseIterable {{
{chr(10).join(enum_lines)}
    }}

    // Порядок в строке: ru, en, ar
    private static let table: [Key: [String]] = [
{chr(10).join(table_lines)}
    ]
}}

extension L10n {{
    /// Название состояния для чипов в онбординге.
    ///
    /// Состояния лежат в корпусе одинаковыми во всех языках — по ним
    /// фильтруется пул, и общий идентификатор здесь правильный. Но показывать
    /// его нельзя: идентификаторы русские. Отдельная таблица, а не ключи в общем
    /// перечислении, потому что список задаёт корпус, а не код; тест сверяет
    /// одно с другим.
    public func theme(_ id: String) -> String {{
        guard let row = L10n.themes[id] else {{ return id }}
        return row[index]
    }}

    /// Порядок значений тот же: ru, en, ar.
    static let themes: [String: [String]] = [
{chr(10).join(theme_lines)}
    ]

    /// Номер языка в строке таблицы.
    var index: Int {{
        switch locale {{
        case .ru: 0
        case .en: 1
        case .ar: 2
        }}
    }}

    /// Название поверхности. Отдельный метод, потому что у StandBy и Apple Watch
    /// переводить нечего — это имена продуктов Apple.
    public func name(_ surface: Surface) -> String {{
        surface.titleKey.map {{ self[$0] }} ?? surface.untranslatedTitle
    }}

    /// Дата для макета экрана блокировки.
    ///
    /// Число условное — как и 9:41 на всех снимках Apple, — но написано оно
    /// должно быть на языке интерфейса.
    public var mockDate: String {{
        let calendar = Calendar(identifier: .gregorian)
        guard let date = calendar.date(from: DateComponents(year: 2025, month: 9, day: 3))
        else {{ return "" }}
        return date.formatted(
            .dateTime.weekday(.wide).day().month(.wide)
                .locale(locale.formattingLocale)
        )
    }}
}}
'''
    out = os.path.join(ROOT, "LampadaCore", "Sources", "LampadaCore", "Strings.swift")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(swift)
    print(f"записано {out}: {len(keys)} ключей")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
