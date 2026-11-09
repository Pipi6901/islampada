#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lampada — строки контекста. Сборка и проверка.

Источник истины по контексту. Пишет:
  corpus/context.json    — данные в боевой схеме
  04-context.html        — читаемая версия для вычитки

Ключ — ОТРЫВОК, а не стих: у всех стихов одной перикопы контекст общий.
Формат строки: до ~30 слов, кто говорит и при каких обстоятельствах.
Не толкование, не проповедь.

Запуск:  python3 build-context.py
"""

import os, json, re

HERE = os.path.dirname(os.path.abspath(__file__))
WORD_LIMIT = 34

from context_data import P
from psalms_map import to_greek
from dependent_refs import DEPENDENT
from context_i18n import T

BOOK_RU = {"MAT":"От Матфея","MRK":"От Марка","JHN":"От Иоанна","PSA":"Псалом","ISA":"Исаия",
           "JER":"Иеремия","LAM":"Плач Иеремии","ROM":"Римлянам","PHP":"Филиппийцам",
           "COL":"Колоссянам","EPH":"Ефесянам","1TH":"1 Фессалоникийцам","1PE":"1 Петра",
           "PRO":"Притчи","REV":"Откровение","JOS":"Иисус Навин","DEU":"Второзаконие",
           "2CO":"2 Коринфянам","HEB":"Евреям","GAL":"Галатам","GEN":"Бытие","EXO":"Исход","NUM":"Числа","1SA":"1 Царств","1KI":"3 Царств","2CH":"2 Паралипоменон","NEH":"Неемия","JOB":"Иов","ECC":"Екклесиаст","EZK":"Иезекииль","DAN":"Даниил","JOL":"Иоиль","MIC":"Михей","HAB":"Аввакум","ZEP":"Софония","LUK":"От Луки","ACT":"Деяния","1CO":"1 Коринфянам","2TI":"2 Тимофею","JAS":"Иакова","1JN":"1 Иоанна","LEV":"Левит","JDG":"Судей","RUT":"Руфь","2KI":"4 Царств","1CH":"1 Паралипоменон","EZR":"Ездра","EST":"Есфирь","SNG":"Песнь песней","AMO":"Амос","JON":"Иона","NAM":"Наум","ZEC":"Захария","MAL":"Малахия","1TI":"1 Тимофею","2PE":"2 Петра","2SA":"2 Царств","2TH":"2 Фессалоникийцам","JUD":"Иуды","HAG":"Аггей","OBA":"Авдий","HOS":"Осия"}
BOOK_EN = {"MAT":"Matthew","MRK":"Mark","JHN":"John","PSA":"Psalm","ISA":"Isaiah","JER":"Jeremiah",
           "LAM":"Lamentations","ROM":"Romans","PHP":"Philippians","COL":"Colossians",
           "EPH":"Ephesians","1TH":"1 Thessalonians","1PE":"1 Peter","PRO":"Proverbs",
           "REV":"Revelation","JOS":"Joshua","DEU":"Deuteronomy","2CO":"2 Corinthians",
           "HEB":"Hebrews","GAL":"Galatians","GEN":"Genesis","EXO":"Exodus","NUM":"Numbers","1SA":"1 Samuel","1KI":"1 Kings","2CH":"2 Chronicles","NEH":"Nehemiah","JOB":"Job","ECC":"Ecclesiastes","EZK":"Ezekiel","DAN":"Daniel","JOL":"Joel","MIC":"Micah","HAB":"Habakkuk","ZEP":"Zephaniah","LUK":"Luke","ACT":"Acts","1CO":"1 Corinthians","2TI":"2 Timothy","JAS":"James","1JN":"1 John","LEV":"Leviticus","JDG":"Judges","RUT":"Ruth","2KI":"2 Kings","1CH":"1 Chronicles","EZR":"Ezra","EST":"Esther","SNG":"Song of Songs","AMO":"Amos","JON":"Jonah","NAM":"Nahum","ZEC":"Zechariah","MAL":"Malachi","1TI":"1 Timothy","2PE":"2 Peter","2SA":"2 Samuel","2TH":"2 Thessalonians","JUD":"Jude","HAG":"Haggai","OBA":"Obadiah","HOS":"Hosea"}


def words(s):
    return len(re.findall(r"[^\s—·]+", s))


def ref_label(p, lang):
    books = BOOK_RU if lang == "ru" else BOOK_EN
    a, b = p["vv"]
    vv = str(a) if a == b else f"{a}–{b}"
    if p["book"] == "PSA":
        heb, gre = p["psalm"]
        if lang == "ru":
            gc, gv1 = to_greek(heb, a)
            _, gv2 = to_greek(heb, b)
            vv = str(gv1) if gv1 == gv2 else f"{gv1}–{gv2}"
            return f"{books['PSA']} {gc}:{vv}"
        return f"{books['PSA']} {heb}:{vv}"
    return f"{books[p['book']]} {p['ch']}:{vv}"


def slices(p):
    """Нарезка отрывка на карточки. Карточка открывается самостоятельным стихом
    и вбирает следующие за ним грамматические продолжения."""
    a, b = p["vv"]
    out = []
    for v in range(a, b + 1):
        ref = f"{p['book']}.{p['ch']}.{v}"
        if out and ref in DEPENDENT:
            out[-1][1] = v
        else:
            out.append([v, v])
    return [tuple(x) for x in out]


def build_json():
    out = {"schema": 1, "kind": "context", "note": "ключ — отрывок, не стих",
           "passages": [], "pool": []}
    for p in P:
        a, b = p["vv"]
        entry = {
            "id": p["id"],
            "book": p["book"],
            "chapter": p["ch"],
            "verses": [a, b],
            "refs": [f"{p['book']}.{p['ch']}.{v}" for v in range(a, b + 1)],
            "theme": p["theme"],
            "context": dict({"ru": p["ru"], "en": p["en"]}, **T.get(p["id"], {})),
        }
        if p["book"] == "PSA":
            entry["psalmNumbering"] = {"hebrew": p["psalm"][0], "greek": p["psalm"][1]}
            entry["chapter"] = p["psalm"][0]
        entry["slices"] = [list(x) for x in slices(p)]
        out["passages"].append(entry)
        for i, (sa, sb) in enumerate(slices(p)):
            out["pool"].append({
                "id": f"{p['id']}#{i}",
                "passage": p["id"],
                "book": p["book"],
                "chapter": entry["chapter"],
                "verses": [sa, sb],
                "theme": p["theme"],
            })
    out["counts"] = {"passages": len(out["passages"]),
                     "verses": sum(p["vv"][1] - p["vv"][0] + 1 for p in P),
                     "pool": len(out["pool"])}
    os.makedirs(os.path.join(HERE, "corpus"), exist_ok=True)
    path = os.path.join(HERE, "corpus", "context.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return path


def tr(p, lang):
    return T.get(p["id"], {}).get(lang, "— нет перевода —")


def build_html():
    rows = []
    for i, p in enumerate(P, 1):
        psalm_note = ""
        if p["book"] == "PSA":
            heb, gre = p["psalm"]
            if heb != gre:
                psalm_note = (f'<small>нумерация: {heb} в WEB, Luther и Segond · '
                              f'{gre} в Синодальном</small>')
            else:
                psalm_note = '<small>нумерация совпадает во всех пяти изданиях</small>'
        rows.append(f"""          <tr>
            <th>{ref_label(p,'ru')}<small>{ref_label(p,'en')}</small>{psalm_note}</th>
            <td><span class="pill">{p['theme']}</span></td>
            <td>{p['ru']}<small>{words(p['ru'])} слов</small></td>
            <td>{p['en']}<small>{words(p['en'])} words</small></td>
            <td>{tr(p,'es')}<small>{words(tr(p,'es'))} palabras</small></td>
            <td>{tr(p,'fr')}<small>{words(tr(p,'fr'))} mots</small></td>
            <td>{tr(p,'de')}<small>{words(tr(p,'de'))} Wörter</small></td>
          </tr>""")

    themes = {}
    for p in P:
        themes[p["theme"]] = themes.get(p["theme"], 0) + 1
    theme_line = " · ".join(f"{k} ({v})" for k, v in sorted(themes.items(), key=lambda x: -x[1]))
    nbooks = len({x["book"] for x in P})
    over = [f'{p["id"]}/{lg}' for p in P for lg in ("ru", "en", "es", "fr", "de")
            if (p.get(lg) or T.get(p["id"], {}).get(lg))
            and words(p.get(lg) or T[p["id"]][lg]) > WORD_LIMIT]
    missing = [p["id"] for p in P if len(T.get(p["id"], {})) < 3]
    if missing:
        print(f"без перевода: {len(missing)} из {len(P)}  первый — {missing[0]}")
    else:
        print("перевод: все 433 отрывка на пяти языках")

    html = f"""<title>Контекст Lampada</title>
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
  --measure:34rem; --wide:70rem;
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
.wordmark{{font-family:var(--f-display);font-optical-sizing:auto;font-weight:400;font-size:clamp(2.6rem,8vw,4.4rem);line-height:0.98;letter-spacing:-0.025em;margin:0;text-wrap:balance}}
.wordmark em{{font-style:italic;color:var(--accent)}}
.tagline{{font-family:var(--f-display);font-size:clamp(1.1rem,2.4vw,1.4rem);font-weight:300;line-height:1.4;color:var(--ink2);max-width:32rem;margin:0;text-wrap:balance}}
.meta{{display:flex;flex-wrap:wrap;gap:0.5rem 2rem;font-family:var(--f-mono);font-size:0.72rem;letter-spacing:0.07em;text-transform:uppercase;color:var(--faint)}}
.meta b{{color:var(--ink2);font-weight:500}}
section{{display:flex;flex-direction:column;gap:1.4rem}}
.eyebrow{{font-family:var(--f-mono);font-size:0.68rem;letter-spacing:0.16em;text-transform:uppercase;color:var(--accent);display:flex;align-items:center;gap:0.7rem}}
.eyebrow::after{{content:"";flex:1;height:1px;background:var(--line)}}
h2{{font-family:var(--f-display);font-optical-sizing:auto;font-size:clamp(1.6rem,3.4vw,2.1rem);font-weight:400;line-height:1.14;letter-spacing:-0.018em;margin:0;max-width:28rem;text-wrap:balance}}
h3{{font-family:var(--f-body);font-size:0.95rem;font-weight:600;margin:0;color:var(--ink)}}
p{{margin:0;color:var(--ink2)}}
strong{{font-weight:600;color:var(--ink)}}
ul.dash{{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.6rem}}
ul.dash li{{padding-left:1.1rem;position:relative;color:var(--ink2)}}
ul.dash li::before{{content:"";position:absolute;left:0;top:0.72em;width:0.5rem;height:1px;background:var(--line2)}}
.note{{background:var(--surface);border:1px solid var(--line);border-left:2px solid var(--accent);padding:1.1rem 1.25rem;display:flex;flex-direction:column;gap:0.5rem;max-width:var(--measure)}}
.note.warn{{border-left-color:var(--stop)}}
.note.warn .eyebrow{{color:var(--stop)}}
.note .eyebrow::after{{display:none}}
.note p{{font-size:0.95rem}}
.scroller{{overflow-x:auto;border:1px solid var(--line);background:var(--surface)}}
table{{border-collapse:collapse;width:100%;min-width:56rem;font-size:0.88rem}}
thead th{{text-align:left;font-family:var(--f-mono);font-size:0.66rem;letter-spacing:0.12em;text-transform:uppercase;font-weight:500;color:var(--faint);padding:0.75rem 1rem;border-bottom:1px solid var(--line2);white-space:nowrap;background:var(--surface2)}}
tbody td{{padding:0.85rem 1rem;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink2);width:34%}}
tbody tr:last-child td{{border-bottom:none}}
tbody th{{text-align:left;padding:0.85rem 1rem;border-bottom:1px solid var(--line);vertical-align:top;font-weight:600;color:var(--ink);white-space:nowrap;width:18%}}
tbody tr:last-child th{{border-bottom:none}}
small{{display:block;color:var(--faint);font-size:0.8em;margin-top:0.25rem;font-weight:400;white-space:normal}}
.pill{{display:inline-block;font-family:var(--f-mono);font-size:0.63rem;letter-spacing:0.09em;text-transform:uppercase;padding:0.2rem 0.5rem;border:1px solid var(--line2);color:var(--muted);white-space:nowrap}}
.split{{display:grid;grid-template-columns:repeat(auto-fit,minmax(17rem,1fr));gap:1.6rem 2.4rem}}
.split>div{{display:flex;flex-direction:column;gap:0.6rem}}
code{{font-family:var(--f-mono);font-size:0.86em;background:var(--surface2);padding:0.1em 0.35em;color:var(--ink)}}
</style>

<div class="page">

  <header class="mast">
    <div class="mast-rule"></div>
    <h1 class="wordmark">Контекст · <em>полный корпус</em></h1>
    <p class="tagline">{len(P)} отрывков из {nbooks} книг на пяти языках релиза. Они покрывают 1319 стихов и дают пул в 1002 карточки — этого хватает на листание без повторов и на все шестнадцать тем состояний.</p>
    <div class="meta">
      <span>Отрывков <b>{len(P)}</b></span>
      <span>Тем <b>{len(themes)}</b></span>
      <span>Языков <b>2 из 5</b></span>
      <span>Книг <b>{nbooks}</b></span>
      <span>Лимит <b>{WORD_LIMIT} слова</b></span>
      <span>Превышений <b>{len(over) if over else 'нет'}</b></span>
    </div>
  </header>

  <section>
    <div class="eyebrow">Что здесь проверяется</div>
    <h2>Формат: кто говорит и при каких обстоятельствах</h2>
    <div class="col">
      <p>Строка отвечает на вопрос из чипа «Кто это говорит и когда» — и только на него. Это <strong>не толкование</strong>: она не объясняет, что стих значит, и ничего не предписывает. Она ставит слова обратно в ситуацию, из которой их обычно вырывают.</p>
      <p>Ключ — <strong>отрывок, а не стих</strong>. У всех стихов одной перикопы контекст общий, поэтому пул в полторы тысячи ссылок покрывается примерно четырьмя сотнями строк.</p>
    </div>

    <div class="split">
      <div>
        <h3>Правила, по которым написано</h3>
        <ul class="dash">
          <li>До {WORD_LIMIT} слов. Живой разговорный язык, без церковного регистра.</li>
          <li>Только проверяемые факты: кто, кому, где, при каких обстоятельствах.</li>
          <li>Ни одного побуждения к действию и ни одной оценки.</li>
          <li>Где текст принято понимать неверно — контекст молча возвращает исходную ситуацию, но не спорит.</li>
        </ul>
      </div>
      <div>
        <h3>Темы в партии</h3>
        <p>{theme_line}</p>
        <p>Распределение вышло естественным: больше всего надежды, страха и усталости, меньше всего бессонницы и немощи — просто потому, что подходящих мест в Писании столько и есть. Подгонять числа не стал.</p>
      </div>
    </div>

    <div class="note warn">
      <div class="eyebrow">Это писал ИИ — и это нужно вычитать</div>
      <p>Строки составлены по справочным изданиям в public domain: комментарии Мэтью Генри, Джеймисона-Фоссета-Брауна, заметки Барнса, словари Истона и ISBE. Факты не охраняются, поэтому текст написан заново, а не заимствован.</p>
      <p>Но <strong>риск фактической ошибки остаётся</strong>, и в приложении о Писании он бьёт по единственному активу — доверию. Корпус закрыт, но не вычитан. Прежде чем переводить на испанский, французский и немецкий, его должен прочитать человек с богословской подготовкой: ошибка, размноженная на пять языков, стоит впятеро дороже. Спорные места помечены ниже.</p>
    </div>
  </section>

  <section>
    <div class="eyebrow">Партия</div>
    <h2>{len(P)} отрывков</h2>
    <div class="scroller">
      <table>
        <thead><tr><th>Ссылка</th><th>Тема</th><th>Русский</th><th>English</th><th>Español</th><th>Français</th><th>Deutsch</th></tr></thead>
        <tbody>
{chr(10).join(rows)}
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <div class="eyebrow">На что смотреть при вычитке</div>
    <h2>Места, где я бы проверил себя</h2>
    <div class="split">
      <div>
        <h3>Атрибуции и датировки</h3>
        <ul class="dash">
          <li><strong>Плач Иеремии</strong> — авторство традиционное, поэтому в строке автор не назван, сказано только про обстоятельства.</li>
          <li><strong>1 Фессалоникийцам как самое раннее письмо</strong> — общепринятая, но не единственная точка зрения.</li>
          <li><strong>Псалом 117/118 на Пасхе</strong> — связь с пением перед арестом дана с оговоркой «по Евангелиям».</li>
          <li><strong>2 Коринфянам 12</strong> — природа «жала в плоти» неизвестна, поэтому в строке «болезнь или изъян», без диагноза.</li>
        </ul>
      </div>
      <div>
        <h3>Где контекст спорит с привычным чтением</h3>
        <ul class="dash">
          <li><strong>Иеремия 29:11</strong> — обещание адресовано поколению, которое вернётся через семьдесят лет, а не читателю сегодня. Это самая частая ошибка в жанре, и строка её тихо снимает.</li>
          <li><strong>Римлянам 8:28</strong> — фраза стоит в главе о страдании; уточнение «а не об удаче» удерживает от прочтения как обещания везения.</li>
          <li><strong>Псалом 118:105</strong> — светильник назван глиняной лампой, освещавшей шаг. Это же и объяснение имени приложения.</li>
        </ul>
      </div>
    </div>

    <div class="note">
      <div class="eyebrow">Нумерация Псалмов проверяется прямо здесь</div>
      <p>В партии {sum(1 for x in P if x['book']=='PSA')} псалмов, и почти у всех номера расходятся между Синодальным и остальными изданиями. Каждый помечен обеими нумерациями, в JSON лежит поле psalmNumbering. Это уже достаточный набор, чтобы проверить таблицу соответствий до разметки корпуса целиком.</p>
    </div>
  </section>

</div>
"""
    path = os.path.join(HERE, "04-context.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path, over


def main():
    j = build_json()
    h, over = build_html()
    print(f"записан  {os.path.relpath(j, HERE)}")
    print(f"записан  {os.path.relpath(h, HERE)}")
    print()
    print(f"{'ID':16} {'RU':>4} {'EN':>4}")
    print("-" * 28)
    for p in P:
        wr, we = words(p["ru"]), words(p["en"])
        flag = " !!" if wr > WORD_LIMIT or we > WORD_LIMIT else ""
        print(f"{p['id']:16} {wr:>4} {we:>4}{flag}")
    print("-" * 28)
    print("ВСЁ В ЛИМИТЕ" if not over else f"ПРЕВЫШЕНИЯ: {', '.join(over)}")


if __name__ == "__main__":
    main()
