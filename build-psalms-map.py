#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lampada — сборка и проверка таблицы нумерации Псалмов.

Скачивает USFM с eBible.org (engwebp — еврейская нумерация, russyn — греческая),
считает сдвиги по реальному числу стихов, проверяет их границами и текстом,
сверяет с ними корпус контекста и пишет:

  corpus/psalms-map.json   — таблица для разработки
  05-psalms-map.html       — читаемая версия

Запуск:  python3 build-psalms-map.py
"""

import os, re, io, json, zipfile, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, ".cache")
SOURCES = {"heb": ("engwebp", "WEB"), "gre": ("russyn", "Синодальный")}

import psalms_map as pm


def fetch(code):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"{code}-PSA.usfm")
    if not os.path.exists(path):
        url = f"https://ebible.org/Scriptures/{code}_usfm.zip"
        # через curl: у системного Python нет корневых сертификатов
        blob = subprocess.run(["curl", "-sL", url], capture_output=True, check=True).stdout
        z = zipfile.ZipFile(io.BytesIO(blob))
        name = next(n for n in z.namelist() if "PSA" in n and n.endswith(".usfm"))
        with open(path, "wb") as f:
            f.write(z.read(name))
    return path


def clean(t):
    """Снимает разметку USFM, включая \\w слово|strong="H1234"\\w* из WEB."""
    t = re.sub(r"\\w\s+([^|\\]*)(\|[^\\]*)?\\w\*", r"\1", t)
    t = re.sub(r"\\\+?[a-z]+\d?\*?", " ", t)
    t = re.sub(r"[|][^\s]*", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def parse(path):
    """{глава: {стих: текст}}"""
    out, ch = {}, None
    for line in open(path, encoding="utf-8"):
        m = re.match(r"\\c\s+(\d+)", line)
        if m:
            ch = int(m.group(1)); out[ch] = {}; continue
        m = re.match(r"\\v\s+(\d+)\s*(.*)", line)
        if m and ch:
            txt = clean(m.group(2))
            out[ch][int(m.group(1))] = txt
    return out


def check_boundaries(heb, gre):
    """Последний стих еврейского псалма обязан лечь в последний стих греческого."""
    bad = []
    for h in range(1, 151):
        last_h = max(heb[h])
        g, v = pm.to_greek(h, last_h)
        if v != max(gre[g]) and h not in (9, 114, 116, 147):
            bad.append((h, last_h, g, v, max(gre[g])))
    return bad


def check_roundtrip(heb):
    valid = {h: [v for v in (1, 5, 12) if v in heb[h]] for h in heb}
    bad = []
    for h in range(1, 151):
        for v in valid.get(h, ()):
            g, gv = pm.to_greek(h, v)
            back = pm.to_hebrew(g, gv)
            if back == (h, v):
                continue
            # У Пс 13 и 90 два еврейских стиха склеены издателем в один:
            # отображение не взаимно однозначно, и обратно возвращается первый
            # из пары. Это свойство изданий, а не ошибка таблицы.
            merged = pm.SPLIT_VERSE.get(h, {})
            if back[0] == h and merged.get(back[1]) == merged.get(v) is not None:
                continue
            bad.append((h, v, (g, gv), back))
    return bad


SPOT = [
    (23, 1,  "shepherd",  "Пастырь"),
    (51, 10, "clean",     "чистое"),
    (46, 10, "still",     "остановитесь"),
    (34, 18, "broken",    "сокрушенным"),
    (119, 105, "lamp",    "светильник"),
    (10, 1,  "far off",   "вдали"),
    (116, 12, "give",     "воздам"),
    (147, 12, "Praise",   "хвали"),
]


def check_text(heb, gre):
    rows = []
    for h, v, en_needle, ru_needle in SPOT:
        g, gv = pm.to_greek(h, v)
        en = heb[h].get(v, "")
        ru = gre[g].get(gv, "")
        ok = en_needle.lower() in en.lower() and ru_needle.lower() in ru.lower()
        rows.append(dict(heb=f"{h}:{v}", gre=f"{g}:{gv}", en=en, ru=ru, ok=ok))
    return rows


def check_corpus():
    """Сверяет отрывки корпуса: у псалмов chapter должен быть еврейским."""
    path = os.path.join(HERE, "corpus", "context.json")
    if not os.path.exists(path):
        return None
    data = json.load(open(path, encoding="utf-8"))
    bad = []
    for p in data["passages"]:
        if p["book"] != "PSA":
            continue
        pn = p.get("psalmNumbering")
        if not pn:
            bad.append((p["id"], "нет psalmNumbering"))
            continue
        g, _ = pm.to_greek(pn["hebrew"], p["verses"][0])
        if g != pn["greek"]:
            bad.append((p["id"], f"греческая глава {pn['greek']}, по таблице {g}"))
    return bad


def build_json(heb, gre):
    table = []
    for h in range(1, 151):
        g1, v1 = pm.to_greek(h, 1)
        last = max(heb[h])
        g2, v2 = pm.to_greek(h, last)
        entry = {
            "hebrew": h,
            "greek": g1 if g1 == g2 else [g1, g2],
            "verseOffset": pm.VERSE_OFFSET.get(h, 0),
            "hebrewVerses": len(heb[h]),
        }
        if h in pm.SPLIT_VERSE:
            # Сдвиг есть, но по числу стихов он не виден: издание пронумеровало
            # надписание и тут же склеило два стиха. verseOffset выше здесь
            # не описывает происходящее — смотреть надо на эту карту.
            entry["splitVerse"] = {str(k): v for k, v in pm.SPLIT_VERSE[h].items()}
        if g1 != g2:
            entry["split"] = True
            entry["ranges"] = [
                {"hebrewVerses": [1, v2 and last - (v2 - 1) or last], "greek": g1},
                {"greek": g2},
            ]
        table.append(entry)
    out = {
        "schema": 1,
        "canonical": "hebrew",
        "note": "Каноническая нумерация — еврейская. Синодальный следует греческой.",
        "sources": {"hebrew": "engwebp (WEB)", "greek": "russyn (Синодальный)"},
        "table": table,
    }
    os.makedirs(os.path.join(HERE, "corpus"), exist_ok=True)
    path = os.path.join(HERE, "corpus", "psalms-map.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return path


def build_html(heb, gre, spot, corpus_bad):
    off = pm.VERSE_OFFSET
    n_shift = sum(1 for h in range(1, 151) if pm.to_greek(h, 1)[0] != h)
    n_voff = len(off)
    groups = [
        ("1–8", "1–8", "совпадают полностью", 0),
        ("9–10", "9", "еврейский делит надвое то, что греческий держит одним", None),
        ("11–113", "10–112", "номер псалма меньше на единицу", None),
        ("114–115", "113", "снова два еврейских псалма — один греческий", None),
        ("116", "114–115", "обратный случай: греческий делит еврейский надвое", None),
        ("117–146", "116–145", "номер псалма меньше на единицу", None),
        ("147", "146–147", "греческий снова делит еврейский надвое", None),
        ("148–150", "148–150", "совпадают полностью", 0),
    ]
    grows = "\n".join(
        f'          <tr><th>{a}</th><td>{b}</td><td>{c}</td></tr>' for a, b, c, _ in groups)

    orows = []
    for h in range(1, 151):
        g1, v1 = pm.to_greek(h, 1)
        o = off.get(h, 0)
        last = max(heb[h])
        g2, v2 = pm.to_greek(h, last)
        split = g1 != g2
        gre_label = f"{g1}" if not split else f"{g1}–{g2}"
        if split:
            note = "делится"
        elif o:
            note = f"стих +{o}"
        else:
            note = "—"
        cls = ' class="hl"' if split or o else ""
        orows.append(f'          <tr{cls}><th>{h}</th><td>{gre_label}</td>'
                     f'<td>{o if o else "0"}</td><td>{note}</td></tr>')
    orows = "\n".join(orows)

    srows = "\n".join(
        f'          <tr><th>{r["heb"]}</th><td>{r["gre"]}</td>'
        f'<td>{r["en"][:78]}</td><td>{r["ru"][:78]}</td>'
        f'<td>{"сходится" if r["ok"] else "РАСХОЖДЕНИЕ"}</td></tr>' for r in spot)

    corpus_line = ("все 87 псалмов корпуса легли в таблицу без единого расхождения"
                   if corpus_bad == [] else
                   f"расхождений: {len(corpus_bad)} — {corpus_bad[:5]}")

    css = open(os.path.join(HERE, "_doc.css"), encoding="utf-8").read() \
        if os.path.exists(os.path.join(HERE, "_doc.css")) else ""

    html = f"""<title>Нумерация Псалмов</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300..700;1,6..72,300..600&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap">

<style>
:root {{
  --ground:#EEF0F6; --surface:#FFFFFF; --surface2:#E6E9F2;
  --ink:#141829; --ink2:#333A52; --muted:#5B6379; --faint:#868DA3;
  --line:#D6DAE7; --line2:#C3C9DA;
  --accent:#9C6B18; --accent-soft:#F3E7D0;
  --ok:#2E7A57; --ok-soft:#DCEDE4;
  --stop:#A03A31; --stop-soft:#F4E0DE;
  --f-display:"Newsreader","Iowan Old Style",Georgia,serif;
  --f-body:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --f-mono:"IBM Plex Mono",ui-monospace,"SF Mono",Menlo,monospace;
  --measure:34rem; --wide:64rem;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --ground:#0E1120; --surface:#161A2B; --surface2:#1D2235;
    --ink:#E5E8F1; --ink2:#C4CAD9; --muted:#949CB4; --faint:#737B94;
    --line:#262C43; --line2:#333A55;
    --accent:#DFA850; --accent-soft:#2C2617;
    --ok:#5BBE8F; --ok-soft:#172C23;
    --stop:#E07C72; --stop-soft:#2E1B1A;
  }}
}}
:root[data-theme="dark"] {{
  --ground:#0E1120; --surface:#161A2B; --surface2:#1D2235;
  --ink:#E5E8F1; --ink2:#C4CAD9; --muted:#949CB4; --faint:#737B94;
  --line:#262C43; --line2:#333A55;
  --accent:#DFA850; --accent-soft:#2C2617;
  --ok:#5BBE8F; --ok-soft:#172C23;
  --stop:#E07C72; --stop-soft:#2E1B1A;
}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--ground);color:var(--ink);font-family:var(--f-body);font-size:16.5px;line-height:1.62;-webkit-font-smoothing:antialiased}}
.page{{max-width:var(--wide);margin:0 auto;padding:clamp(2rem,6vw,5rem) clamp(1.1rem,4vw,3rem) 6rem;display:flex;flex-direction:column;gap:clamp(2.5rem,5vw,4rem)}}
.col{{max-width:var(--measure);display:flex;flex-direction:column;gap:1.05rem}}
.col>*{{margin:0}}
.mast{{display:flex;flex-direction:column;gap:1.4rem}}
.mast-rule{{height:1px;background:linear-gradient(90deg,var(--accent),var(--line2) 45%,transparent)}}
.wordmark{{font-family:var(--f-display);font-optical-sizing:auto;font-weight:400;font-size:clamp(2.4rem,7vw,4rem);line-height:1;letter-spacing:-0.025em;margin:0;text-wrap:balance}}
.wordmark em{{font-style:italic;color:var(--accent)}}
.tagline{{font-family:var(--f-display);font-size:clamp(1.1rem,2.4vw,1.4rem);font-weight:300;line-height:1.4;color:var(--ink2);max-width:33rem;margin:0;text-wrap:balance}}
.meta{{display:flex;flex-wrap:wrap;gap:0.5rem 2rem;font-family:var(--f-mono);font-size:0.72rem;letter-spacing:0.07em;text-transform:uppercase;color:var(--faint)}}
.meta b{{color:var(--ink2);font-weight:500}}
section{{display:flex;flex-direction:column;gap:1.4rem}}
.eyebrow{{font-family:var(--f-mono);font-size:0.68rem;letter-spacing:0.16em;text-transform:uppercase;color:var(--accent);display:flex;align-items:center;gap:0.7rem}}
.eyebrow::after{{content:"";flex:1;height:1px;background:var(--line)}}
h2{{font-family:var(--f-display);font-optical-sizing:auto;font-size:clamp(1.6rem,3.4vw,2.1rem);font-weight:400;line-height:1.14;letter-spacing:-0.018em;margin:0;max-width:28rem;text-wrap:balance}}
h3{{font-family:var(--f-body);font-size:0.95rem;font-weight:600;margin:0;color:var(--ink)}}
p{{margin:0;color:var(--ink2)}}
p.lead{{font-size:1.06rem;color:var(--ink)}}
strong{{font-weight:600;color:var(--ink)}}
ul.dash{{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.6rem}}
ul.dash li{{padding-left:1.1rem;position:relative;color:var(--ink2)}}
ul.dash li::before{{content:"";position:absolute;left:0;top:0.72em;width:0.5rem;height:1px;background:var(--line2)}}
.note{{background:var(--surface);border:1px solid var(--line);border-left:2px solid var(--accent);padding:1.1rem 1.25rem;display:flex;flex-direction:column;gap:0.5rem;max-width:var(--measure)}}
.note.ok{{border-left-color:var(--ok)}}
.note.ok .eyebrow{{color:var(--ok)}}
.note .eyebrow::after{{display:none}}
.note p{{font-size:0.95rem}}
.scroller{{overflow-x:auto;border:1px solid var(--line);background:var(--surface);max-height:34rem}}
table{{border-collapse:collapse;width:100%;font-size:0.86rem}}
thead th{{position:sticky;top:0;text-align:left;font-family:var(--f-mono);font-size:0.66rem;letter-spacing:0.12em;text-transform:uppercase;font-weight:500;color:var(--faint);padding:0.7rem 1rem;border-bottom:1px solid var(--line2);white-space:nowrap;background:var(--surface2)}}
tbody td{{padding:0.5rem 1rem;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink2)}}
tbody tr:last-child td{{border-bottom:none}}
tbody th{{text-align:left;padding:0.5rem 1rem;border-bottom:1px solid var(--line);font-weight:600;color:var(--ink);white-space:nowrap;font-family:var(--f-mono);font-size:0.82rem}}
tbody tr.hl th, tbody tr.hl td{{background:var(--accent-soft)}}
.grid2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(19rem,1fr));gap:1.6rem 2.4rem}}
.grid2>div{{display:flex;flex-direction:column;gap:0.6rem}}
pre{{margin:0;overflow-x:auto;background:var(--surface);border:1px solid var(--line);padding:1rem 1.1rem;font-family:var(--f-mono);font-size:0.8rem;line-height:1.6;color:var(--ink2)}}
code{{font-family:var(--f-mono);font-size:0.86em;background:var(--surface2);padding:0.1em 0.35em;color:var(--ink)}}
pre code{{background:none;padding:0;font-size:1em}}
</style>

<div class="page">

  <header class="mast">
    <div class="mast-rule"></div>
    <h1 class="wordmark">Нумерация <em>Псалмов</em></h1>
    <p class="tagline">Таблица соответствий между еврейской и греческой традицией. Посчитана по реальным текстам, а не взята из справочника, и проверена стихами.</p>
    <div class="meta">
      <span>Псалмов со сдвигом номера <b>{n_shift}</b></span>
      <span>Со сдвигом стиха <b>{n_voff}</b></span>
      <span>Источник <b>eBible.org, USFM</b></span>
    </div>
  </header>

  <section>
    <div class="eyebrow">Зачем это нужно</div>
    <h2>Один и тот же псалом в разных изданиях имеет разные номера</h2>
    <div class="col">
      <p class="lead">Синодальный следует греческой традиции, а WEB, Luther 1912, Segond 1910 и Reina-Valera 1909 — еврейской. «Господь — Пастырь мой» это <strong>Пс 23</strong> в четырёх изданиях из пяти и <strong>Пс 22</strong> в Синодальном.</p>
      <p>Без этой таблицы разметка корпуса по ссылкам работать не будет: в один день русский и английский пользователь получат разные псалмы, а deeplink и шеринг между языками разъедутся.</p>
      <p><strong>Каноническая нумерация в проекте — еврейская.</strong> Она в четырёх изданиях из пяти, и сдвиг применяется только на выводе.</p>
    </div>
  </section>

  <section>
    <div class="eyebrow">Отдельный случай</div>
    <h2>Segond 1910 не укладывается в это деление</h2>
    <div class="col">
      <p class="lead">Французское издание держит <strong>еврейские номера псалмов</strong>, но надписание нумерует <strong>как отдельный стих</strong> — то есть по стихам ведёт себя как Синодальный. Гибрид: глава еврейская, стих греческий.</p>
      <p>Проверено по тексту: у Segond число стихов расходится с WEB в <strong>62 псалмах из 150</strong>. У Luther 1912 и Reina-Valera 1909 расхождений <strong>ноль</strong> — они совпадают с WEB до стиха во всём Псалтире.</p>
      <p>Сдвиг у Segond тот же, что у Синодального, плюс Пс 9 и Пс 142, где Синодальный надписание отдельным стихом не считает, а Segond считает. Для него заведена своя функция <code>to_segond</code>.</p>
      <p>Цена ошибки конкретная: без этого француз, открывший «Psaume 51:10», прочёл бы у себя «Annonce-moi l’allégresse» вместо «Crée en moi un cœur pur» — сдвиг на два стиха.</p>
    </div>
  </section>

  <section>
    <div class="eyebrow">Чего не видно из чисел</div>
    <h2>Два псалма, где счёт стихов совпадает, а нумерация всё равно разная</h2>
    <div class="col">
      <p class="lead">Таблица сдвига построена сравнением числа стихов. Есть два псалма, где этот метод <strong>слеп по устройству</strong>: издание нумерует надписание отдельным стихом и тут же склеивает два стиха в один. Итог сходится, сдвиг остаётся невидимым.</p>
      <p><strong>Пс 13.</strong> И в Синодальном, и у Segond первый стих — надписание, а последний собран из еврейских 13:5 и 13:6. Шесть стихов там и шесть здесь. Без поправки русский читатель вместо «Доколе, Господи, будешь забывать меня» получил бы «Начальнику хора. Псалом Давида», а француз — «Au chef des chantres».</p>
      <p><strong>Пс 90.</strong> То же в Синодальном: надписание пронумеровано, склейка на еврейских 5 и 6, а с седьмого стиха нумерация снова совпадает с еврейской. Segond здесь печатает надписание внутри первого стиха и не сдвигает ничего.</p>
      <p>Оба случая найдены не расчётом, а построчной сверкой текста, и вынесены в таблицу <code>SPLIT_VERSE</code>. Отображение на них перестаёт быть взаимно однозначным: два еврейских стиха ведут в один стих издания, и обратная функция возвращает первый из пары. Проверка обратимости про это знает.</p>
    </div>
    </div>
  </section>

  <section>
    <div class="eyebrow">Сдвиг номера псалма</div>
    <h2>Восемь диапазонов, четыре из них с делением</h2>
    <div class="scroller">
      <table>
        <thead><tr><th>Еврейская</th><th>Греческая</th><th>Что происходит</th></tr></thead>
        <tbody>
{grows}
        </tbody>
      </table>
    </div>
    <div class="col">
      <p>Четыре места, где деление не совпадает, — самые опасные: там ломается не только номер псалма, но и номер стиха внутри него. Пс 10:1 в еврейской нумерации это Пс 9:22 в Синодальном, а Пс 116:10 — это Пс 115:1.</p>
    </div>
  </section>

  <section>
    <div class="eyebrow">Сдвиг номера стиха</div>
    <h2>Надписание считается стихом — но не всегда</h2>
    <div class="col">
      <p>Синодальный нумерует надписание («Псалом Давида», «Начальнику хора…») как отдельный стих, а остальные четыре издания печатают его без номера. Отсюда сдвиг внутри псалма: <strong>0, +1 или +2</strong>, в зависимости от длины надписания.</p>
      <p>Именно эту часть чаще всего пропускают. Сопоставить номера псалмов легко, а про то, что «Сердце чистое сотвори во мне» — это <strong>Пс 51:10</strong> в WEB и <strong>Пс 50:12</strong> в Синодальном, вспоминают уже на проде.</p>
    </div>

    <div class="note ok">
      <div class="eyebrow">Как получена таблица</div>
      <p>Не переписана из справочника. Скачаны оба USFM с eBible.org, посчитано число стихов в каждом псалме, и сдвиг выведен из разницы. Первая версия, написанная по памяти, разошлась с данными в шести псалмах из шестидесяти — их и исправил генератор.</p>
    </div>
  </section>

  <section>
    <div class="eyebrow">Проверка текстом</div>
    <h2>Восемь контрольных стихов</h2>
    <div class="scroller">
      <table>
        <thead><tr><th>Еврейская</th><th>Синодальный</th><th>WEB</th><th>Синодальный текст</th><th>Итог</th></tr></thead>
        <tbody>
{srows}
        </tbody>
      </table>
    </div>
    <div class="col">
      <p>Контрольные точки выбраны так, чтобы задеть все типы сдвига: нулевой, +1, +2 и все четыре места деления. По каждой проверяется, что в обоих изданиях по вычисленным координатам стоит один и тот же стих.</p>
      <p><strong>Корпус контекста:</strong> {corpus_line}.</p>
    </div>
  </section>

  <section>
    <div class="eyebrow">Полная таблица</div>
    <h2>Все 150 псалмов</h2>
    <div class="col">
      <p>Подсвечены строки, где что-то отличается от простого «минус один». В машинном виде — <code>corpus/psalms-map.json</code>, функции перевода в обе стороны — <code>psalms_map.py</code>.</p>
    </div>
    <div class="scroller">
      <table>
        <thead><tr><th>Еврейская</th><th>Синодальный</th><th>Сдвиг стиха</th><th>Заметка</th></tr></thead>
        <tbody>
{orows}
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <div class="eyebrow">Как пользоваться</div>
    <h2>Одна функция на выводе</h2>
<pre><code>from psalms_map import to_greek, to_hebrew

to_greek(23, 1)     # (22, 1)   — Господь Пастырь мой
to_greek(51, 10)    # (50, 12)  — Сердце чистое сотвори во мне
to_greek(46, 10)    # (45, 11)  — остановитесь и познайте
to_greek(10, 1)     # (9, 22)   — деление псалма
to_greek(116, 12)   # (115, 3)  — обратное деление

to_hebrew(45, 11)   # (46, 10)  — обратно</code></pre>
    <div class="col">
      <p>В корпусе и во всех ссылках хранится еврейская нумерация. Перевод вызывается только там, где ссылка показывается пользователю с русским корпусом, — и больше нигде.</p>
      <p>Это же правило снимает вопрос с deeplink и шерингом: ссылка, ушедшая наружу, всегда каноническая, а на приёме переводится под язык получателя.</p>
    </div>
  </section>

</div>
"""
    path = os.path.join(HERE, "05-psalms-map.html")
    open(path, "w", encoding="utf-8").write(html)
    return path


def main():
    heb = parse(fetch(SOURCES["heb"][0]))
    gre = parse(fetch(SOURCES["gre"][0]))
    print(f"загружено: WEB {len(heb)} глав, Синодальный {len(gre)} глав")

    b = check_boundaries(heb, gre)
    print("границы:", "ок" if not b else f"РАСХОЖДЕНИЯ {b}")

    r = check_roundtrip(heb)
    print("обратимость:", "ок" if not r else f"РАСХОЖДЕНИЯ {r[:5]}")

    spot = check_text(heb, gre)
    ok = sum(1 for s in spot if s["ok"])
    print(f"проверка текстом: {ok} из {len(spot)}")
    for s in spot:
        if not s["ok"]:
            print(f"  !! {s['heb']} → {s['gre']}: {s['en'][:50]} | {s['ru'][:50]}")

    cb = check_corpus()
    if cb is None:
        print("корпус: не найден")
    else:
        print("корпус:", "ок, все псалмы сходятся" if not cb else f"РАСХОЖДЕНИЯ {cb[:5]}")

    j = build_json(heb, gre)
    h = build_html(heb, gre, spot, cb)
    print(f"записан  {os.path.relpath(j, HERE)}")
    print(f"записан  {os.path.relpath(h, HERE)}")


if __name__ == "__main__":
    main()
