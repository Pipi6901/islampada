# -*- coding: utf-8 -*-
"""Сборка корпуса Misbah: арабский оригинал + переводы, по файлу на язык.

На выходе (в ресурсы пакета LampadaCore):
    corpus-en.json  — карточки с переводом Pickthall + арабский текст
    corpus-ru.json  — карточки с переводом Саблукова + арабский текст
    corpus-ar.json  — карточки, где основной текст — сам арабский оригинал

ТЕКСТЫ НЕ ПРАВЯТСЯ. Каждая карточка — это стихи из исходных файлов Tanzil, склеенные
через пробел. Сборка проверяет это обратной сверкой: текст карточки должен совпасть с
исходником посимвольно (кроме склейки диапазона), иначе сборка падает.

Исходники (corpus-src/, скачаны с tanzil.net скриптом fetch_sources.py):
    quran-uthmani.txt  — арабский (Uthmani), Tanzil, CC BY 3.0: копировать только дословно,
                         сохранять указание источника и ссылку на tanzil.net
    en.pickthall.txt   — Marmaduke Pickthall (1930, ум. 1936): общественное достояние
    ru.sablukov.txt    — Гордий Саблуков (1878, ум. 1880): общественное достояние

Запуск:  python tools/corpus/build_corpus.py [--report]
"""

import json
import os
import re
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "corpus-src")
OUT = os.path.join(ROOT, "LampadaCore", "Sources", "LampadaCore", "Resources")

sys.path.insert(0, HERE)
import selection  # noqa: E402
import surah_names  # noqa: E402
import notes  # noqa: E402

EDITIONS = {
    "en": dict(id="en.pickthall", name="Pickthall", full="Marmaduke Pickthall, 1930",
               license="Public Domain", source="tanzil.net"),
    "ru": dict(id="ru.sablukov", name="Саблуков", full="Гордий Саблуков, 1878",
               license="Public Domain", source="tanzil.net"),
    "ar": dict(id="quran-uthmani", name="القرآن الكريم", full="Tanzil Quran Text (Uthmani)",
               license="CC BY 3.0 — Tanzil Project, tanzil.net", source="tanzil.net"),
}
ARABIC_CREDIT = "CC BY 3.0 — Tanzil Project, tanzil.net"


def load_verses(path):
    verses = {}
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line or line.startswith("#"):
            continue
        s, a, t = line.split("|", 2)
        verses[(int(s), int(a))] = t.strip()
    return verses


def load_meta():
    root = ET.parse(os.path.join(SRC, "quran-data.xml")).getroot()
    meta = {}
    for el in root.iter("sura"):
        i = int(el.attrib["index"])
        meta[i] = dict(ayas=int(el.attrib["ayas"]), name_ar=el.attrib["name"],
                       type=el.attrib["type"])
    return meta


def label(lang, meta, sura, a, b):
    num = f"{a}" if a == b else f"{a}–{b}"
    if lang == "ru":
        return f"{surah_names.RU[sura - 1]} {sura}:{num}"
    if lang == "en":
        return f"{surah_names.EN[sura - 1]} {sura}:{num}"
    return f"{meta[sura]['name_ar']} {sura}:{num}"


def clean(text):
    """Только пробелы: ни слова, ни знака не трогаем."""
    return re.sub(r"\s+", " ", text).strip()


TAIL = re.compile(r"[,;:—–-]+$")


def finish(text, lang):
    """Знак в конце. Переводы кончают аят так, как удобно внутри суры: запятой, точкой с
    запятой, двоеточием. Карточка с таким концом выглядит оборванной, и такой знак меняется
    на точку (в исходниках он не трогается). Арабский текст не меняется никогда."""
    if lang == "ar":
        return text
    return TAIL.sub("", text).rstrip() + "." if TAIL.search(text) else text


def build():
    ar = load_verses(os.path.join(SRC, "quran-uthmani.txt"))
    en = load_verses(os.path.join(SRC, "en.pickthall.txt"))
    ru = load_verses(os.path.join(SRC, "ru.sablukov.txt"))
    meta = load_meta()
    for name, d in (("ar", ar), ("en", en), ("ru", ru)):
        assert len(d) == 6236, f"{name}: {len(d)} аятов вместо 6236"
        assert set(d) == set(ar), f"{name}: набор аятов расходится с арабским"
    for s in range(1, 115):
        assert max(a for (x, a) in ar if x == s) == meta[s]["ayas"], f"сура {s}: число аятов"

    cards = {"en": [], "ru": [], "ar": []}
    used_notes = {}
    for theme, sura, a, b in selection.passages():
        key = notes.passage_key(sura, a, b)
        used_notes[key] = (sura, a, b)
        parts = {lang: finish(clean(" ".join(src[(sura, x)] for x in range(a, b + 1))), lang)
                 for lang, src in (("en", en), ("ru", ru), ("ar", ar))}
        cid = f"{sura}-{a}" + ("" if a == b else f"-{b}")
        for lang in ("en", "ru", "ar"):
            card = {"id": cid, "p": key, "th": theme,
                    "r": label(lang, meta, sura, a, b), "t": parts[lang]}
            if lang != "ar":
                card["a"] = parts["ar"]
            cards[lang].append(card)

    bundles = {}
    for lang, ed in EDITIONS.items():
        contexts = {k: notes.context(lang, k, v, meta) for k, v in used_notes.items()}
        bundles[lang] = {
            "schema": 2,
            "lang": lang,
            "edition": {"id": ed["id"], "name": ed["name"], "license": ed["license"],
                        "source": ed["source"]},
            "arabicCredit": ARABIC_CREDIT,
            "counts": {"cards": len(cards[lang]), "passages": len(contexts)},
            "cards": cards[lang],
            "contexts": contexts,
        }
    return bundles, (ar, en, ru)


def verify(bundles, sources):
    """Обратная сверка: карточка == исходник, во всех языках один состав."""
    ar, en, ru = sources
    base = [c["id"] for c in bundles["en"]["cards"]]
    problems = []
    for lang, b in bundles.items():
        if [c["id"] for c in b["cards"]] != base:
            problems.append(f"{lang}: состав карточек расходится")
        src = {"en": en, "ru": ru, "ar": ar}[lang]
        for c in b["cards"]:
            s, a, *rest = (int(x) for x in c["id"].split("-"))
            e = rest[0] if rest else a
            expected = finish(clean(" ".join(src[(s, x)] for x in range(a, e + 1))), lang)
            if c["t"] != expected:
                problems.append(f"{lang} {c['id']}: текст не совпал с исходником")
            if lang != "ar":
                exp_ar = clean(" ".join(ar[(s, x)] for x in range(a, e + 1)))
                if c.get("a") != exp_ar:
                    problems.append(f"{lang} {c['id']}: арабский не совпал с исходником")
            if len(c["t"]) < 8:
                problems.append(f"{lang} {c['id']}: слишком короткий текст")
            if c["t"][-1] in ",;:—–-":
                problems.append(f"{lang} {c['id']}: оборван на «{c['t'][-1]}»")
            if "|" in c["t"] or "<" in c["t"]:
                problems.append(f"{lang} {c['id']}: служебные символы")
            if c["id"] not in {x["id"] for x in b["cards"]}:
                problems.append("?")
        for c in b["cards"]:
            if c["p"] not in b["contexts"]:
                problems.append(f"{lang} {c['id']}: нет контекста {c['p']}")
        themes = {c["th"] for c in b["cards"]}
        if themes != set(selection.THEMES):
            problems.append(f"{lang}: набор состояний {themes ^ set(selection.THEMES)}")
    return problems


def main():
    bundles, sources = build()
    problems = verify(bundles, sources)
    if problems:
        print("ПРОБЛЕМЫ:", len(problems))
        for p in problems[:40]:
            print("  ", p)
        sys.exit(1)
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for lang, b in bundles.items():
        path = os.path.join(OUT, f"corpus-{lang}.json")
        blob = json.dumps(b, ensure_ascii=False, separators=(",", ":"))
        with open(path, "w", encoding="utf-8") as f:
            f.write(blob)
        size = os.path.getsize(path)
        total += size
        print(f"  corpus-{lang}.json  {b['counts']['cards']} карточек  {size / 1024:6.0f} КБ")
    print(f"всего {total / 1024:.0f} КБ; записано в {os.path.relpath(OUT, ROOT)}")
    if "--report" in sys.argv:
        en = bundles["en"]["cards"]
        for c in en:
            print(f"{c['th'][:6]:6} {c['r']:22} {len(c['t']):4}  {c['t'][:70]}")


if __name__ == "__main__":
    main()
