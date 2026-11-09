#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lampada — сборка бандлов с текстами изданий.

На выходе по одному файлу на язык: bundle/lampada-{lang}.json. В файле лежит
всё, что нужно приложению на этом языке, и ничего лишнего — карточки с готовым
текстом и ссылкой плюс строки контекста. Приложение грузит ровно один файл.

ПОЧЕМУ КАРТОЧКА, А НЕ СТИХ. Единица показа — карточка, и её текст собирается
здесь, на сборке. Значит в рантайме не нужны ни склейка стихов, ни пересчёт
нумерации псалмов, ни названия книг: всё уже посчитано и лежит строкой.

НУМЕРАЦИЯ. Ключи канонические (еврейские), а подпись под карточкой — в системе
своего издания: Синодальный по греческой, Segond по еврейским главам с
греческим сдвигом стиха. Пересчёт делает psalms_map.py на сборке.

ЗНАК В КОНЦЕ. Издания заканчивают стих так, как им удобно внутри главы, и
карточка может оборваться на запятой или двоеточии. Такой знак заменяется
точкой при сборке — раньше это планировалось делать при отрисовке, но здесь
результат проверяется тестом, а в рантайме пришлось бы верить на слово.
Тексты изданий в .cache при этом не трогаются.

ИЗДАНИЯ И ЛИЦЕНЗИИ (проверено по метаданным eBible.org, все Public Domain):
    en  engwebp     World English Bible
    ru  russyn      Синодальный перевод
    de  deu1912     Lutherbibel 1912
    fr  fraLSG      Louis Segond 1910
    es  spaRV1909   Reina-Valera 1909
    pt  porbr2018   Bíblia Livre 2018 — НЕ общественное достояние, а CC BY 4.0
                    (Diego Santos, Mario Sérgio, Marco Teles): в приложении и
                    в описании обязательна строка авторства и пометка, что
                    знаки в конце стиха правились (см. «ЗНАК В КОНЦЕ»)
    it  ita1927     Riveduta 1927 (Giovanni Luzzi)
    ko  kor         eBible подписывает «Korean Bible 1910» и «public domain», но по
                    тексту это 개역한글 1961 (современная орфография). В Корее
                    свободен с 2012; в США, по разбору проекта Scriptura,
                    восстановлен URAA до 2056, и Корейское библейское общество
                    права заявляет. Взят по решению владельца 07.11.2026, риск
                    известен (docs/new-languages.md)

Запуск:  python3 build-bundle.py [--refresh]
    --refresh перекачивает тексты изданий с eBible.org в .cache
"""

import os, sys, io, re, json, zipfile, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from context_data import P
from context_i18n import T
from context_i18n_more import T_MORE
from dependent_refs import DEPENDENT
from psalms_map import to_greek, to_segond, SEGOND_OFFSET

CACHE = os.path.join(HERE, ".cache")
OUT = os.path.join(HERE, "bundle")

EDITIONS = {
    "en": dict(id="engwebp",   name="World English Bible",  numbering="hebrew"),
    "ru": dict(id="russyn",    name="Синодальный перевод",  numbering="greek"),
    "de": dict(id="deu1912",   name="Lutherbibel 1912",     numbering="hebrew"),
    "fr": dict(id="fraLSG",    name="Louis Segond 1910",    numbering="segond"),
    "es": dict(id="spaRV1909", name="Reina-Valera 1909",    numbering="hebrew"),
    "pt": dict(id="porbr2018", name="Bíblia Livre",         numbering="hebrew",
               license="CC BY 4.0 — Diego Santos, Mario Sérgio, Marco Teles; "
                       "final punctuation adjusted"),
    "it": dict(id="ita1927",   name="Riveduta 1927",        numbering="hebrew"),
    "ko": dict(id="kor",       name="개역한글",              numbering="hebrew",
               supplement="https://sourceforge.net/projects/zefania-sharp/files/Bibles/KOR/"
                          "Korean%20Revised%20Version%201952-1961/"
                          "SF_2022-09-19_KOR_KORRV_%28Korean%20Revised%20Version%201952%201961%29.zip/download"),
}

# Названия книг берутся из самих изданий (\toc2). Здесь только замены там, где
# издательское название не годится для короткой подписи под карточкой.
BOOK_OVERRIDE = {
    "ru": {"PSA": "Псалом", "MAT": "От Матфея", "MRK": "От Марка", "LUK": "От Луки",
           "JHN": "От Иоанна", "ACT": "Деяния", "REV": "Откровение",
           "ROM": "Римлянам", "1CO": "1 Коринфянам", "2CO": "2 Коринфянам",
           "GAL": "Галатам", "EPH": "Ефесянам", "PHP": "Филиппийцам",
           "COL": "Колоссянам", "1TH": "1 Фессалоникийцам", "2TH": "2 Фессалоникийцам",
           "1TI": "1 Тимофею", "2TI": "2 Тимофею", "HEB": "Евреям",
           "JAS": "Иакова", "1PE": "1 Петра", "2PE": "2 Петра",
           "1JN": "1 Иоанна", "JUD": "Иуды", "LAM": "Плач Иеремии",
           "SNG": "Песнь песней", "ECC": "Екклесиаст", "PRO": "Притчи"},
    "es": {"PSA": "Salmo"},
    "fr": {"PSA": "Psaume"},
    "de": {"PSA": "Psalm"},
    "en": {"PSA": "Psalm"},
    "pt": {"PSA": "Salmo"},
    "it": {"PSA": "Salmo"},
    "ko": {"PSA": "시편"},
}


# ── тексты изданий ────────────────────────────────────────────────────────

def clean(s):
    s = re.sub(r"\\f\s.*?\\f\*", "", s)                       # сноски
    s = re.sub(r"\\x\s.*?\\x\*", "", s)                       # перекрёстные ссылки
    # Разметка Стронга. В Новом Завете WEB она вложена в \wj и записана как
    # \+w слово|strong="G1205"\+w* — без плюса регулярка её не видит.
    s = re.sub(r"\\\+?w\s+([^|\\]*?)(\|[^\\]*?)?\\\+?w\*", r"\1", s)
    s = re.sub(r"\\\+?[a-z]+\d?\s*\*?", "", s)                # остальные маркеры
    return re.sub(r"\s+", " ", s).strip()


def fetch(tid, path):
    blob = subprocess.run(["curl", "-sL", f"https://ebible.org/Scriptures/{tid}_usfm.zip"],
                          capture_output=True, check=True).stdout
    z = zipfile.ZipFile(io.BytesIO(blob))
    out, books, supers = {}, {}, {}
    for n in z.namelist():
        m = re.search(r"\d\d-([A-Z0-9]{3})", n)
        if not n.endswith(".usfm") or not m:
            continue
        code = m.group(1)
        raw = z.read(n).decode("utf-8", "replace")
        t = (re.search(r"\\toc2\s+(.+)", raw[:4000]) or re.search(r"\\h\s+(.+)", raw[:4000]))
        if t:
            books[code] = t.group(1).strip()
        out[code] = {}
        ch = vs = None
        buf = []

        def flush():
            if ch and vs:
                out[code].setdefault(str(ch), {})[str(vs)] = clean(" ".join(buf))

        for line in raw.splitlines():
            c = re.match(r"\\c\s+(\d+)", line)
            if c:
                flush(); ch = int(c.group(1)); vs = None; buf = []; continue
            if line.startswith("\\d ") and ch:
                supers.setdefault(code, []).append(ch)   # надписание отдельным маркером
                continue
            parts = re.split(r"\\v\s+(\d+)", line)
            if len(parts) == 1:
                if vs:
                    buf.append(re.sub(r"^\\[a-z]+\d?\s*", "", parts[0]))
                continue
            if parts[0].strip() and vs:
                buf.append(parts[0])
            for i in range(1, len(parts), 2):
                flush(); vs = int(parts[i]); buf = [parts[i + 1]]
        flush()
    json.dump({"verses": out, "books": books, "supers": supers},
              open(path, "w"), ensure_ascii=False)


# Корейский текст на eBible неполный: нет 114 стихов, в том числе всей 1 Пет 5
# и половины Пс 118, — а из них 27 в корпусе. Пробелы закрывает тот же
# 개역한글 из Zefania (выгрузка с Викитеки): стих берётся оттуда, только если
# в основном тексте его нет. Основным остаётся eBible — у него надписания
# псалмов в скобках, и их можно снять надёжно. А номера стихов главнее у
# Zefania: где eBible сдвинул нумерацию, глава выравнивается по нему (realign).
ZEFANIA_BOOKS = ["GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT", "1SA", "2SA", "1KI",
                 "2KI", "1CH", "2CH", "EZR", "NEH", "EST", "JOB", "PSA", "PRO", "ECC", "SNG",
                 "ISA", "JER", "LAM", "EZK", "DAN", "HOS", "JOL", "AMO", "OBA", "JON", "MIC",
                 "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL", "MAT", "MRK", "LUK", "JHN", "ACT",
                 "ROM", "1CO", "2CO", "GAL", "EPH", "PHP", "COL", "1TH", "2TH", "1TI", "2TI",
                 "TIT", "PHM", "HEB", "JAS", "1PE", "2PE", "1JN", "2JN", "3JN", "JUD", "REV"]


def fetch_zefania(url, path):
    import xml.etree.ElementTree as ET
    blob = subprocess.run(["curl", "-sL", url], capture_output=True, check=True).stdout
    z = zipfile.ZipFile(io.BytesIO(blob))
    name = next(n for n in z.namelist() if n.endswith(".xml"))
    root = ET.fromstring(z.read(name))
    out = {}
    for book in root.findall("BIBLEBOOK"):
        code = ZEFANIA_BOOKS[int(book.attrib["bnumber"]) - 1]
        for ch in book.findall("CHAPTER"):
            for v in ch.findall("VERS"):
                text = re.sub(r"\s+", " ", "".join(v.itertext())).strip()
                out.setdefault(code, {}).setdefault(ch.attrib["cnumber"], {})[v.attrib["vnumber"]] = text
    json.dump(out, open(path, "w"), ensure_ascii=False)


def load(refresh):
    data = {}
    for lang, ed in EDITIONS.items():
        path = os.path.join(CACHE, f"bundle-{lang}.json")
        if refresh or not os.path.exists(path):
            print(f"качаю {ed['id']}…")
            fetch(ed["id"], path)
        data[lang] = json.load(open(path, encoding="utf-8"))
        if "supplement" in ed:
            extra = os.path.join(CACHE, f"supplement-{lang}.json")
            if refresh or not os.path.exists(extra):
                print(f"качаю дополнение для {lang}…")
                fetch_zefania(ed["supplement"], extra)
            verses = data[lang]["verses"]
            moved = 0
            for book, chapters in json.load(open(extra, encoding="utf-8")).items():
                for ch, vs in chapters.items():
                    own = verses.setdefault(book, {}).setdefault(ch, {})
                    if not aligned(own, vs):
                        own, shift = realign(own, vs)
                        verses[book][ch] = own
                        moved += shift
                    for v, text in vs.items():
                        if not _placeholder(text):
                            own.setdefault(v, text)
            if moved:
                print(f"{lang}: {moved} стихов встали на свой номер по {os.path.basename(extra)}")
    return data


# Сдвиг нумерации в корейском eBible. В 개역한글 часть стихов склеена: у
# склеенного стиха номер есть, а текста нет («앞절과 동일» — «как в предыдущем»),
# и кое-где стиха просто нет. eBible такие номера выбросил и перенумеровал главу
# подряд, поэтому дальше по главе каждый стих стоит под чужим номером: в 2 Тим 4
# пропал 12-й, и под 12-м там текст 13-го, под 16-м — 17-го и так до конца. Так
# съехали 11 карточек, среди них 1 Цар 7:12. Zefania номера сохраняет, по нему и
# выравниваем: в главе, где тексты под одним номером не совпадают, каждому
# номеру Zefania ищется стих eBible с тем же текстом. Текст остаётся из eBible
# (у него запятые и кавычки), из Zefania — только то, чего в eBible нет.

def _plain(s):
    return re.sub(r"[\s\W_`'‘’“”\[\]()]+", "", s or "")


def _similar(a, b):
    import difflib
    a, b = _plain(a), _plain(b)
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def _placeholder(text):
    return text.startswith(("(앞절과 동일)", "(없음)"))


def aligned(own, ref):
    """Глава в порядке, если под каждым общим номером один и тот же стих."""
    if any(_placeholder(t) for t in ref.values()):
        return False
    return all(_similar(own[v], t) >= 0.5 for v, t in ref.items() if v in own)


def realign(own, ref):
    order = sorted(own, key=int)
    out, j, shift = {}, 0, 0
    for v in sorted(ref, key=int):
        if _placeholder(ref[v]):
            continue
        best, score = None, 0.5
        for i in range(j, min(j + 5, len(order))):
            s = _similar(own[order[i]], ref[v])
            if s > score:
                best, score = i, s
        if best is None:
            continue                     # в eBible этого стиха нет — возьмётся из Zefania
        out[v] = own[order[best]]
        shift += order[best] != v
        j = best + 1
    return out, shift


# ── сборка карточек ───────────────────────────────────────────────────────

def slices(p):
    a, b = p["vv"]
    out = []
    for v in range(a, b + 1):
        ref = f"{p['book']}.{p['ch']}.{v}"
        if out and ref in DEPENDENT:
            out[-1][1] = v
        else:
            out.append([v, v])
    return [tuple(x) for x in out]


def locate(lang, p, v):
    """Канонический (еврейский) адрес → адрес в системе издания."""
    if p["book"] != "PSA":
        return p["ch"], v
    h = p["psalm"][0]
    n = EDITIONS[lang]["numbering"]
    if n == "greek":
        return to_greek(h, v)
    if n == "segond":
        return to_segond(h, v)
    return h, v


# ── надписания псалмов ────────────────────────────────────────────────────
# WEB, Синодальный и Bíblia Livre выносят надписание в отдельный маркер \d, и
# оно в текст карточки не попадает. Luther, Segond, Reina-Valera и Riveduta
# вклеивают его внутрь первого стиха, и без чистки карточка начинается с
# «Ein Psalm Davids».
# Надписания формульны, поэтому снимаются по словарю их лексики.

SUPER_MARK = {
    "de": r"Psalm|Psalmen|Lied|Gebet|Unterweisung|Kleinod|Dankpsalm|vorzusingen"
          r"|Chor|Korah|Davids|Salomos|Asaphs|Mose|Jeduthun|Saiten|Fl[\u00f6o]ten",
    "fr": r"Cantique|Psaume|Pri[e\u00e8]re|David|Salomon|Asaph|chantres|degr[\u00e9e]s"
          r"|Mo[i\u00ef]se|Jeduthun|Cor[\u00e9e]|Michtam|Maskil|Hymne|Lamentation|harpe"
          r"|Colombe|luths|fl[u\u00fb]tes|instruments",
    # Riveduta: «Per il Capo de’ musici. Salmo di Davide.» — те же формулы.
    "it": r"Salmo|Capo de[’']|musici|Davide|Asaf|Core|Salomone|Mos[\u00e8e]|Canto|Cantico"
          r"|Inno|Preghiera|Maschil|Mictam|fanciulle|strumenti|Ghittith|Neghinoth"
          r"|Scemineth|Jeduthun|Iedutun|Sciuscian|Mahalath|Alamoth|flauti|cetra",
}
SUPER_RE = {l: re.compile(rf"^\s*[^.:]{{0,110}}?(?:{m})[^.:]{{0,110}}?[.:]\s*")
            for l, m in SUPER_MARK.items()}
# Reina-Valera набирает первое слово самого псалма прописными: «JEHOVÁ es mi
# pastor». Это надёжнее словаря — надписание кончается там, где начинается
# слово в верхнем регистре.
SPA_BODY = re.compile(r"[\u00a1\u00bf(\"']*\b[A-Z\u00c1\u00c9\u00cd\u00d3\u00da\u00d1\u00dc]{2,}\b")


def strip_superscription(lang, hebrew, text, has_super, offset):
    if lang == "ko":
        return KO_SUPER.sub("", text)
    if lang not in ("de", "fr", "es", "it") or not has_super:
        return text
    if lang == "fr" and offset:
        return text                      # \u043d\u0430\u0434\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u043d\u0443\u043c\u0435\u0440\u043e\u0432\u0430\u043d\u043e \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u043e
    if lang == "es":
        m = SPA_BODY.search(text)
        return text[m.start():].strip() if m and m.start() else text
    out = text
    # Riveduta набирает до четырёх формул подряд: «Per il Capo de’ musici. Dei
    # figliuoli di Core. Per voci di fanciulle. Canto.»
    for _ in range(5):
        m = SUPER_RE[lang].match(out)
        if not m or len(out) - m.end() < 25:
            break
        out = out[m.end():]
    return out


# Bíblia Livre: два огреха набора. В Пс 119 перед первым стихом каждой строфы
# стоит название буквы («Nun :Tua palavra…»), а местоимение после дефиса
# оторвано пробелом — с любой стороны: «considerando -as», «dá- la» (Ин 14:27).
# Оба чинятся только у pt.
PT_STROPHE = re.compile(r"^\s*[^\s:]{1,12}\s*:\s*")
PT_PRONOUNS = r"(o|a|os|as|lo|la|los|las|no|na|nos|nas|lhe|lhes|me|te|se|vos)\b"
PT_CLITIC = re.compile(r"(\w)(?: -|- )" + PT_PRONOUNS)


# 개역한글 на eBible: надписание псалма — в скобках в начале первого стиха;
# пробел перед «!» и «?»; кавычки набраны машинописно, `так'; имена мест — в
# квадратных скобках; и кое-где в стих вклеен следующий с пометкой
# «[ (Numbers 1:55) …». В корпус такие стихи не попадают, но чистится всё.
KO_SUPER = re.compile(r"^\s*\([^)]*\)\s*")
KO_MERGED = re.compile(r"\[\s*\([A-Za-z0-9 ]+\d+:\d+\)\s*")


def tidy(lang, p, verse, text):
    if lang == "ko":
        text = KO_MERGED.sub("", text)
        text = text.replace("[", "").replace("]", "")
        text = re.sub(r"\s+([!?])", r"\1", text)
        return text.replace("`", "\u2018").replace("'", "\u2019").strip()
    if lang != "pt":
        return text
    if p["book"] == "PSA" and p["psalm"][0] == 119 and verse % 8 == 1:
        text = PT_STROPHE.sub("", text)
    return PT_CLITIC.sub(r"\1-\2", text)


TAIL = re.compile(r"[,;:\u2014\u2013-]+$")


def finish(text):
    """Карточка не должна обрываться на запятой или двоеточии."""
    t = text.strip()
    if TAIL.search(t):
        t = TAIL.sub("", t).rstrip() + "."
    return t


def label(lang, books, p, a, b):
    name = BOOK_OVERRIDE.get(lang, {}).get(p["book"]) or books.get(p["book"], p["book"])
    c1, v1 = locate(lang, p, a)
    _, v2 = locate(lang, p, b)
    vv = str(v1) if v1 == v2 else f"{v1}\u2013{v2}"
    return f"{name} {c1}:{vv}"


def build(lang, data, supers):
    ed = EDITIONS[lang]
    verses, books = data[lang]["verses"], data[lang]["books"]
    cards, contexts, missing = [], {}, []
    for p in P:
        if lang in ("ru", "en"):
            contexts[p["id"]] = p[lang]
        elif lang in ("es", "fr", "de"):
            contexts[p["id"]] = T[p["id"]][lang]
        else:
            contexts[p["id"]] = T_MORE[p["id"]][lang]
        for i, (a, b) in enumerate(slices(p)):
            parts, seen = [], set()
            for v in range(a, b + 1):
                c, vv = locate(lang, p, v)
                if (c, vv) in seen:
                    continue        # издание склеило два еврейских стиха в один
                seen.add((c, vv))
                t = verses.get(p["book"], {}).get(str(c), {}).get(str(vv), "")
                if not t:
                    missing.append(f"{p['id']} {p['book']} {c}:{vv}")
                t = tidy(lang, p, v, t)
                if v == 1 and p["book"] == "PSA":
                    t = strip_superscription(lang, p["psalm"][0], t,
                                             p["psalm"][0] in supers,
                                             SEGOND_OFFSET.get(p["psalm"][0], 0))
                parts.append(t)
            cards.append({
                "id": f"{p['id']}#{i}",
                "p": p["id"],
                "th": p["theme"],
                "r": label(lang, books, p, a, b),
                "t": finish(" ".join(x for x in parts if x)),
            })
    return {
        "schema": 1,
        "lang": lang,
        "edition": {"id": ed["id"], "name": ed["name"],
                    "license": ed.get("license", "Public Domain"), "source": "ebible.org"},
        "counts": {"cards": len(cards), "passages": len(contexts)},
        "cards": cards,
        "contexts": contexts,
    }, missing


# ── проверки ──────────────────────────────────────────────────────────────

RESIDUE = re.compile(r"\\|strong=|\|[a-z]+=|\\w\*")


def check(bundles):
    bad = []
    for lang, b in bundles.items():
        for c in b["cards"]:
            # Порог низкий намеренно: Ин 11:35 — самый короткий стих Евангелий
            # («Jesus wept.») — есть в корпусе. Ловим огрызки, а не короткие стихи.
            if len(c["t"]) < 8:
                bad.append((lang, c["id"], f"огрызок: {c['t']!r}"))
            elif RESIDUE.search(c["t"]):
                bad.append((lang, c["id"], "остатки разметки: " + c["t"][:60]))
            elif TAIL.search(c["t"]):
                bad.append((lang, c["id"], "оборван: " + c["t"][-40:]))
            if not c["r"] or c["r"].split()[0] == c["r"]:
                pass
    # одинаковый состав карточек во всех языках
    ids = {lang: [c["id"] for c in b["cards"]] for lang, b in bundles.items()}
    base = ids["en"]
    for lang, v in ids.items():
        if v != base:
            bad.append((lang, "—", "состав карточек расходится с английским"))
    return bad


def main():
    refresh = "--refresh" in sys.argv
    data = load(refresh)
    supers = set(data["en"].get("supers", {}).get("PSA", []))
    print(f"псалмов с надписанием (по WEB): {len(supers)}")
    os.makedirs(OUT, exist_ok=True)
    bundles, allmissing = {}, []
    for lang in EDITIONS:
        b, missing = build(lang, data, supers)
        bundles[lang] = b
        allmissing += [(lang, m) for m in missing]

    bad = check(bundles)
    if allmissing:
        print(f"НЕТ ТЕКСТА: {len(allmissing)}")
        for x in allmissing[:10]:
            print("  ", x)
    if bad:
        print(f"ПРОБЛЕМЫ: {len(bad)}")
        for x in bad[:15]:
            print("  ", x)
    if allmissing or bad:
        sys.exit(1)

    # Приложение читает не bundle/, а свою копию в ресурсах пакета. Раньше её
    # переносили руками, и она отставала молча: корпус пересобран, а на экране
    # прежний текст — заметить это можно только глазами и только на том языке,
    # куда посмотрел. Пишем сразу в оба места: расходиться им нельзя.
    resources = os.path.join(HERE, "LampadaCore", "Sources", "LampadaCore", "Resources")

    total = 0
    for lang, b in bundles.items():
        blob = json.dumps(b, ensure_ascii=False, separators=(",", ":"))
        path = os.path.join(OUT, f"lampada-{lang}.json")
        for destination in (path, os.path.join(resources, f"lampada-{lang}.json")):
            with open(destination, "w", encoding="utf-8") as f:
                f.write(blob)
        size = os.path.getsize(path)
        total += size
        print(f"  bundle/lampada-{lang}.json  {b['counts']['cards']} карточек  "
              f"{size/1024:6.0f} КБ  {b['edition']['name']}")
    print(f"\nвсего {total/1024:.0f} КБ на {len(bundles)} языков; "
          "все Public Domain, кроме Bíblia Livre (CC BY 4.0)")
    print(f"те же файлы записаны в {os.path.relpath(resources, HERE)}")


if __name__ == "__main__":
    main()
