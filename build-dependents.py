#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lampada — расчёт списка стихов, которые не могут открывать карточку.

Карточка обязана читаться целиком НА ВСЕХ языках релиза. Поэтому стих
считается продолжением, если он начинается со строчной буквы хотя бы в одном
из изданий: значит там это середина фразы, и в отрыве он читается обрывком.

Издания и что они дают:
    en  engwebp     World English Bible          — 127 продолжений
    ru  russyn      Синодальный                  — 258
    de  deu1912     Lutherbibel 1912             — 166
    fr  fraLSG      Louis Segond 1910            —  74
    es  spaRV1909   Reina-Valera 1909            —   0

ВНИМАНИЕ по Reina-Valera: там каждый стих набран с заглавной буквы независимо
от синтаксиса. Ноль в этой колонке — свойство вёрстки издания, а НЕ признак
того, что все испанские стихи самостоятельны. Проверять список по RV нельзя.

Нумерация псалмов: Синодальный по греческой традиции (to_greek), Segond по
еврейским главам с греческим сдвигом стиха (to_segond), Luther и RV совпадают
с WEB. Подробности в psalms_map.py.

Тексты берутся из локального кэша .cache/bundle-*.json, который наполняет
build-bundle.py. Запуск:  python3 build-dependents.py
"""

import os, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from context_data import P
from psalms_map import to_greek, to_segond

EDITIONS = ["en", "ru", "de", "fr", "es"]
LEAD = "“«‘\"'¿¡([—- "


def load():
    out = {}
    for e in EDITIONS:
        path = os.path.join(HERE, ".cache", f"bundle-{e}.json")
        if not os.path.exists(path):
            sys.exit(f"нет кэша {path} — сначала запустите build-bundle.py")
        out[e] = json.load(open(path, encoding="utf-8"))["verses"]
    return out


def verse(ed, texts, p, v):
    if p["book"] == "PSA":
        h = p["psalm"][0]
        if ed == "ru":
            c, vv = to_greek(h, v)
        elif ed == "fr":
            c, vv = to_segond(h, v)
        else:
            c, vv = h, v
        return texts[ed]["PSA"].get(str(c), {}).get(str(vv), "")
    return texts[ed].get(p["book"], {}).get(str(p["ch"]), {}).get(str(v), "")


def is_continuation(s):
    s = s.lstrip(LEAD)
    return bool(s) and s[0].islower()


def main():
    texts = load()
    dep, per = set(), {e: 0 for e in EDITIONS}
    for p in P:
        for v in range(p["vv"][0] + 1, p["vv"][1] + 1):
            ref = f"{p['book']}.{p['ch']}.{v}"
            for e in EDITIONS:
                if is_continuation(verse(e, texts, p, v)):
                    per[e] += 1
                    dep.add(ref)
    body = json.dumps(sorted(dep), indent=4, ensure_ascii=False)
    body = "{" + body[1:-1] + "}"
    with open(os.path.join(HERE, "dependent_refs.py"), "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Список продолжений. Сгенерирован build-dependents.py, руками не править.\n\n')
        f.write("Стих здесь, если хотя бы в одном издании релиза он начинается со строчной\n")
        f.write("буквы, то есть является серединой фразы. Такой стих не открывает карточку,\n")
        f.write("а прирастает к предыдущей.\n\n")
        f.write("По изданиям: " + ", ".join(f"{e} {n}" for e, n in per.items()) + ".\n")
        f.write("У Reina-Valera ноль потому, что издание набирает каждый стих с заглавной;\n")
        f.write('это свойство вёрстки, а не признак самостоятельности.\n"""\n\n')
        f.write("DEPENDENT = " + body + "\n")
    print("по изданиям:", per)
    print("всего продолжений:", len(dep))


if __name__ == "__main__":
    main()
