#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Заменяет идентификаторы оригинала (Lampada) на свои.

Запуск (сначала без --apply: покажет, что поменяет):
    python tools/set-ids.py --bundle com.example.nur --team ABCDE12345 --apple-id 1234567890
    python tools/set-ids.py ... --apply

--bundle    основной bundle ID приложения; виджет получит суффикс .widgets,
            App Group станет group.<bundle>, продукты подписок — <bundle>.weekly и т. д.
--team      Team ID из Apple Developer (Membership).
--apple-id  числовой Apple ID приложения из App Store Connect (App Information).
            Можно не указывать, пока приложение не создано: останется старый.
"""
import argparse, pathlib, sys

OLD_BUNDLE = "com.astonio.lampada"
OLD_GROUP = "group.com.astonio.lampada"
OLD_TEAM = "VG9U7V4AAL"
OLD_APPLE_ID = "6807549676"
ROOT = pathlib.Path(__file__).resolve().parent.parent
EXT = {".swift", ".py", ".yaml", ".yml", ".plist", ".entitlements", ".xcstrings", ".md", ".html"}
SKIP = {".git", "design", "docs", "tools", "node_modules", ".cache"}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", required=True)
    ap.add_argument("--team", required=True)
    ap.add_argument("--apple-id")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    if a.bundle == OLD_BUNDLE:
        sys.exit("bundle совпадает с оригиналом")

    pairs = [(OLD_GROUP, "group." + a.bundle), (OLD_BUNDLE, a.bundle), (OLD_TEAM, a.team)]
    if a.apple_id:
        pairs.append((OLD_APPLE_ID, a.apple_id))

    changed = 0
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix not in EXT or SKIP & set(p.relative_to(ROOT).parts):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new = text
        for old, rep in pairs:
            new = new.replace(old, rep)
        if new != text:
            changed += 1
            print(("правлю  " if a.apply else "будет:  ") + str(p.relative_to(ROOT)))
            if a.apply:
                p.write_text(new, encoding="utf-8", newline="")
    print(f"\nфайлов: {changed}" + ("" if a.apply else " (пробный прогон, добавь --apply)"))


if __name__ == "__main__":
    main()
