# -*- coding: utf-8 -*-
"""Собирает юридические страницы Misbah: по одной странице на документ, внутри три
языковых блока (en, ru, ar) и переключатель. Язык выбирается по `navigator.language`
или по `?lang=ru` в адресе (так в App Store Connect можно дать каждой локализации
свою ссылку на одну и ту же страницу); без JavaScript остаётся английский.

Источники — фрагменты в `tools/legal/{en,ru,ar}/{privacy,terms,support}.html`, результат —
`docs/legal/misbah/misbah-{privacy,terms,support}.html`: самодостаточные UTF-8 файлы без
внешних ресурсов, которые кладутся в корень сайта.

Запуск:
    python tools/legal/build_legal.py                       # почта поддержки по умолчанию
    python tools/legal/build_legal.py --email help@example  # другая почта
    python tools/legal/build_legal.py --final               # и проверить, что заглушек не осталось
"""
import argparse
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "docs", "legal", "misbah")

# Почта поддержки, как у остальных приложений команды (pmoffice.space).
DEFAULT_EMAIL = "help@pmoffice.space"

LANGS = [("en", "English"), ("ru", "Русский"), ("ar", "العربية")]

PAGES = {
    "privacy": {
        "title": {"en": "Misbah — Privacy Policy", "ru": "Misbah — политика конфиденциальности",
                  "ar": "Misbah — سياسة الخصوصية"},
        "desc": {"en": "How the Misbah app handles your data.",
                 "ru": "Как приложение Misbah обращается с вашими данными.",
                 "ar": "كيف يتعامل تطبيق Misbah مع بياناتك."},
    },
    "terms": {
        "title": {"en": "Misbah — Terms of Use", "ru": "Misbah — условия использования",
                  "ar": "Misbah — شروط الاستخدام"},
        "desc": {"en": "Terms of use of the Misbah app.",
                 "ru": "Условия использования приложения Misbah.",
                 "ar": "شروط استخدام تطبيق Misbah."},
    },
    "support": {
        "title": {"en": "Misbah — Support", "ru": "Misbah — поддержка", "ar": "Misbah — الدعم"},
        "desc": {"en": "Help and answers for the Misbah app.",
                 "ru": "Помощь и ответы по приложению Misbah.",
                 "ar": "مساعدة وإجابات عن تطبيق Misbah."},
    },
}

CSS = """
  body{font:16px/1.6 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;max-width:720px;margin:40px auto;padding:0 20px;color:#1b2a2c}
  h1{font-size:28px}h2{font-size:20px;margin-top:32px}h3{font-size:17px;margin-top:24px}a{color:#0f7a6b}
  .lang{display:flex;gap:8px;margin:0 0 24px}
  .lang button{font:inherit;font-size:14px;padding:6px 14px;border-radius:999px;border:1px solid #9bb3b0;background:transparent;color:inherit;cursor:pointer}
  .lang button[aria-pressed=true]{background:#0f7a6b;border-color:#0f7a6b;color:#fff}
  section[data-lang]{display:none}
  section[data-lang].on{display:block}
  html[dir=rtl] body{font-family:-apple-system,"Segoe UI",Tahoma,"Noto Naskh Arabic",Arial,sans-serif}
  @media(prefers-color-scheme:dark){body{background:#0f1a1c;color:#dfe8e8}a{color:#5fd0b4}.lang button{border-color:#4c6663}}
"""

JS = """
(function(){
  var langs=%(langs)s, titles=%(titles)s;
  var q=(location.search.match(/[?&]lang=([a-z]{2})/)||[])[1];
  var nav=(navigator.language||'en').slice(0,2).toLowerCase();
  var cur=langs.indexOf(q)>=0?q:(langs.indexOf(nav)>=0?nav:'en');
  function set(l){
    document.documentElement.lang=l;
    document.documentElement.dir=(l==='ar'?'rtl':'ltr');
    [].forEach.call(document.querySelectorAll('section[data-lang]'),function(s){
      s.classList.toggle('on',s.getAttribute('data-lang')===l);
    });
    [].forEach.call(document.querySelectorAll('[data-set-lang]'),function(b){
      b.setAttribute('aria-pressed',b.getAttribute('data-set-lang')===l?'true':'false');
    });
    document.title=titles[l];
  }
  [].forEach.call(document.querySelectorAll('[data-set-lang]'),function(b){
    b.addEventListener('click',function(){set(b.getAttribute('data-set-lang'));});
  });
  set(cur);
})();
"""


def read(path):
    with io.open(path, encoding="utf-8") as f:
        return f.read().strip()


def build(page, email, links=None, embed=False):
    meta = PAGES[page]
    links = links or {}
    sections = []
    for code, _ in LANGS:
        body = read(os.path.join(HERE, code, page + ".html")).replace("{{EMAIL}}", email)
        for target in PAGES:
            if target in links:
                body = body.replace(f'href="misbah-{target}.html"', f'href="{links[target]}"')
        attrs = f'data-lang="{code}" lang="{code}"' + (' dir="rtl"' if code == "ar" else "")
        cls = ' class="on"' if code == "en" else ""
        sections.append(f"<section {attrs}{cls}>\n{body}\n</section>")
    buttons = "".join(
        f'<button type="button" data-set-lang="{c}" aria-pressed="{"true" if c == "en" else "false"}">{n}</button>'
        for c, n in LANGS)
    titles = {c: meta["title"][c] for c, _ in LANGS}
    js = JS % {"langs": json.dumps([c for c, _ in LANGS]),
               "titles": json.dumps(titles, ensure_ascii=False)}
    # Во встроенном виде (Google Sites) ссылки открываются в новой вкладке: внутри окна
    # встраивания Google и почтовые ссылки не откроются.
    base = '<base target="_blank">' + chr(10) if embed else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{meta['title']['en']}</title>
<meta name="description" content="{meta['desc']['en']}">
{base}<style>{CSS}</style>
</head>
<body>
<nav class="lang" aria-label="Language">{buttons}</nav>
{chr(10).join(sections)}
<script>{js}</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", default=DEFAULT_EMAIL)
    ap.add_argument("--final", action="store_true", help="упасть, если остались заглушки")
    ap.add_argument("--out-dir", default=OUT, help="куда писать страницы")
    ap.add_argument("--embed", action="store_true", help="вариант для встраивания в Google Sites")
    for page in PAGES:
        ap.add_argument(f"--link-{page}", help=f"адрес страницы «{page}» для ссылок между страницами")
    args = ap.parse_args()

    stale = re.compile(r"Lampada|Psalm|Bible|Библи[яиюе]|Христ|Иисус|Colour|Centre", re.I)
    problems = []
    links = {page: getattr(args, f"link_{page}") for page in PAGES if getattr(args, f"link_{page}")}
    os.makedirs(args.out_dir, exist_ok=True)
    for page in PAGES:
        html = build(page, args.email, links, args.embed)
        for m in stale.finditer(html):
            problems.append(f"{page}: след прежнего приложения или британское написание: {m.group(0)}")
        if args.final and "{{" in html:
            problems.append(f"{page}: остались заглушки {{{{...}}}}")
        path = os.path.join(args.out_dir, f"misbah-{page}.html")
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print(f"  {os.path.relpath(path, ROOT)}  {len(html.encode('utf-8')) / 1024:5.1f} КБ")
    if problems:
        print("ПРОБЛЕМЫ:")
        for p in problems:
            print("  ", p)
        sys.exit(1)


if __name__ == "__main__":
    main()
