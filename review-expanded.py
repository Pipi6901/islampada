#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lampada — материал для вычитки расширенных диапазонов.

Печатает отрывок целиком: строку контекста и каждую карточку с русским текстом
по Синодальному (нумерация псалмов пересчитывается). Вычитывать нужно две вещи:
контекст должен покрывать ВЕСЬ диапазон, и каждая карточка должна читаться
самостоятельно.

Запуск:  python3 review-expanded.py <номер партии>
"""
import sys, json, os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from context_data import P
from psalms_map import to_greek
from expand import EXPAND

spec = importlib.util.spec_from_file_location("bc", os.path.join(HERE, "build-context.py"))
bc = importlib.util.module_from_spec(spec); spec.loader.exec_module(bc)
RU = json.load(open(os.path.join(HERE, ".cache/rus-text.json")))

MORE = {"psa-46-1","psa-107-1","psa-116-1","psa-119-71","psa-9-9","psa-68-6",
        "psa-127-2","psa-19-1","psa-139-14","psa-145-18","psa-37-4","psa-34-8"}
EXPANDED = [p for p in P if p["id"] in set(EXPAND) | MORE]

# порядок: сначала псалмы, потом остальное в каноническом порядке файла
psalms = [p for p in EXPANDED if p["book"] == "PSA"]
rest   = [p for p in EXPANDED if p["book"] != "PSA"]
ORDER  = psalms + rest
BATCHES = [(0, 40), (40, 80), (80, 122), (122, 160), (160, len(ORDER))]


def ru_text(p, v):
    if p["book"] == "PSA":
        c, gv = to_greek(p["psalm"][0], v)
        return RU["PSA"].get(str(c), {}).get(str(gv), "— нет текста —")
    return RU.get(p["book"], {}).get(str(p["ch"]), {}).get(str(v), "— нет текста —")


def main(n):
    a, b = BATCHES[n - 1]
    chunk = ORDER[a:b]
    print(f"ПАРТИЯ {n} — отрывки {a+1}–{b} из {len(ORDER)}\n" + "=" * 78)
    for p in chunk:
        sl = bc.slices(p)
        print(f"\n[{p['id']}]  {bc.ref_label(p,'ru')}  ({bc.ref_label(p,'en')})  · тема: {p['theme']}")
        print(f"  КОНТЕКСТ: {p['ru']}")
        print(f"  карточек: {len(sl)}")
        for i, (x, y) in enumerate(sl):
            rng = str(x) if x == y else f"{x}–{y}"
            txt = " / ".join(ru_text(p, v) for v in range(x, y + 1))
            print(f"    {i}) {rng}: {txt}")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
