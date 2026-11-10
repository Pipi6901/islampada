# -*- coding: utf-8 -*-
"""Заливает юридические страницы Misbah на сайт по FTP через TLS и проверяет их по HTTPS.

Запускает человек со своим доступом: пароль спрашивается здесь же (ввод скрыт) и нигде не
сохраняется, в аргументах и в репозитории его нет. Сертификат хостинга выдан на `*.beget.tech`,
поэтому подключаться надо к хосту `<часть логина до "_">.beget.tech`, и проверка сертификата
включена (никаких `-k`).

    python tools/legal/upload.py <ЛОГИН>
    python tools/legal/upload.py <ЛОГИН> --host другой.beget.tech --site https://pmoffice.space

Перед заливкой при необходимости пересоберите страницы: `python tools/legal/build_legal.py`.
После заливки у хостинга бывает кэш: если страница выглядит старой, подождите несколько минут.
"""
import argparse
import ftplib
import getpass
import os
import ssl
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PAGES_DIR = os.path.join(ROOT, "docs", "legal", "misbah")
NAMES = ["misbah-privacy.html", "misbah-terms.html", "misbah-support.html"]


def upload(host, login, password, paths, remote_dir=""):
    ftp = ftplib.FTP_TLS(host, timeout=60, context=ssl.create_default_context())
    try:
        ftp.login(login, password)
        ftp.prot_p()  # данные тоже по TLS, а не только управляющий канал
        if remote_dir:
            ftp.cwd(remote_dir)
        for path in paths:
            name = os.path.basename(path)
            with open(path, "rb") as f:
                ftp.storbinary("STOR " + name, f)
            print("залито:", name, flush=True)
    finally:
        try:
            ftp.quit()
        except Exception:
            ftp.close()


def _fetch(url):
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.status, response.read().decode("utf-8", "replace")


def check(site, names, email):
    """Каждая страница открывается по HTTPS без предупреждений, в ней три языка и актуальная почта."""
    ok = True
    for name in names:
        url = f"{site.rstrip('/')}/{name}"
        try:
            status, body = _fetch(url)
        except Exception as error:
            ok = False
            if isinstance(getattr(error, "reason", error), ssl.SSLError):
                print("HTTPS НЕ РАБОТАЕТ: сертификат сайта не подходит к домену —", url)
                print("   Включите SSL-сертификат для домена в панели хостинга (Let's Encrypt):")
                print("   без него Safari и ревьюер App Store увидят предупреждение вместо страницы.")
                try:
                    _, plain = _fetch("http://" + url.split("://", 1)[1])
                    print("   По HTTP страница", "есть." if "data-lang" in plain else "другая или её нет.")
                except Exception as plain_error:
                    print("   По HTTP:", plain_error)
            else:
                print("НЕ ОТКРЫВАЕТСЯ:", url, "—", error)
            continue
        fresh = all(part in body for part in (email, 'data-lang="ru"', 'data-lang="ar"'))
        print(status, f"{len(body.encode('utf-8')) / 1024:.1f} КБ",
              "актуальная" if fresh else "СТАРАЯ ВЕРСИЯ ИЛИ НЕ ТА СТРАНИЦА", url)
        ok = ok and status == 200 and fresh
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("login", nargs="?", help="логин FTP; без него только проверка страниц на сайте")
    ap.add_argument("--host", help="FTP-хост; по умолчанию <часть логина до _>.beget.tech")
    ap.add_argument("--site", default="https://pmoffice.space", help="адрес сайта для проверки")
    ap.add_argument("--email", default="help@pmoffice.space", help="почта, которая должна быть в страницах")
    ap.add_argument("--remote-dir", default="", help="папка на сервере; по умолчанию корень (он же корень сайта)")
    args = ap.parse_args()

    if args.login:
        host = args.host or args.login.split("_")[0] + ".beget.tech"
        paths = [os.path.join(PAGES_DIR, n) for n in NAMES]
        missing = [p for p in paths if not os.path.exists(p)]
        if missing:
            sys.exit("нет файлов, соберите: python tools/legal/build_legal.py — " + ", ".join(missing))
        password = getpass.getpass(f"Пароль FTP для {args.login} (ввод скрыт, нигде не сохраняется): ")
        upload(host, args.login, password, paths, args.remote_dir)
        del password
    sys.exit(0 if check(args.site, NAMES, args.email) else 1)


if __name__ == "__main__":
    main()
