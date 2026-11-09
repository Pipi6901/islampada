# -*- coding: utf-8 -*-
"""Достаёт строки интерфейса из исходной таблицы Lampada (git-версия Strings.swift).

Нужен один раз, чтобы собрать основу для новых строк Misbah: из пяти колонок
оригинала (ru, en, de, fr, es) оставляются ru и en, остальные пишутся заново.
Результат — tools/i18n/base_strings.json.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def swift_literals(text, start):
    """Читает подряд идущие строковые литералы Swift после `[` и до закрывающей `]`."""
    out = []
    i = start
    n = len(text)
    while i < n:
        c = text[i]
        if c == '"':
            i += 1
            buf = []
            while text[i] != '"':
                if text[i] == "\\":
                    nxt = text[i + 1]
                    if nxt == "u":
                        j = text.index("}", i)
                        buf.append(chr(int(text[i + 3:j], 16)))
                        i = j + 1
                        continue
                    buf.append({"n": "\n", "t": "\t", '"': '"', "\\": "\\", "'": "'"}[nxt])
                    i += 2
                    continue
                buf.append(text[i])
                i += 1
            out.append("".join(buf))
            i += 1
        elif c == "]":
            return out, i
        elif c == "/" and text[i:i + 2] == "//":
            i = text.index("\n", i)
        else:
            i += 1
    raise ValueError("не нашли конец массива")


def main():
    src = subprocess.run(
        ["git", "-C", ROOT, "show", "c2814f4:LampadaCore/Sources/LampadaCore/Strings.swift"],
        capture_output=True, check=True).stdout.decode("utf-8")
    table_start = src.index("private static let table")
    table_end = src.index("extension L10n", table_start)
    body = src[table_start:table_end]
    rows = {}
    for m in re.finditer(r"\n\s*\.(\w+): \[", body):
        key = m.group(1)
        lits, _ = swift_literals(body, m.end())
        rows[key] = lits
    # ключи перечисления
    enum_start = src.index("public enum Key")
    enum_body = src[enum_start:src.index("// Порядок в строке", enum_start)]
    keys = []
    for line in enum_body.splitlines():
        line = line.strip()
        if line.startswith("case "):
            keys += [k.strip() for k in line[5:].split(",") if k.strip()]
    missing = [k for k in keys if k not in rows]
    extra = [k for k in rows if k not in keys]
    print("ключей в перечислении:", len(keys), "строк в таблице:", len(rows),
          "без строки:", missing, "лишние:", extra)
    bad = {k: len(v) for k, v in rows.items() if len(v) != 5}
    print("строки не из пяти значений:", bad)
    # темы
    t0 = src.index("static let themes")
    themes = {}
    for m in re.finditer(r'\n\s*"([^"]+)": \[', src[t0:t0 + 3000]):
        lits, _ = swift_literals(src[t0:], m.end())
        themes[m.group(1)] = lits
    json.dump({"keys": keys, "rows": rows, "themes": themes},
              open(os.path.join(ROOT, "tools", "i18n", "base_strings.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("тем:", len(themes))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
