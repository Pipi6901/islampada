# -*- coding: utf-8 -*-
"""Перекрашивает цветовые константы 0xRRGGBB в Swift-коде: фиолетовый -> изумрудный и
тёмный сине-зелёный. Правило то же, что в макете (design/): оттенки сиреневого и
фиолетового (225-345 градусов) уходят в изумруд (светлые и насыщенные) или в тёмный
сине-зелёный (тёмные и приглушённые); нейтральные чёрные, белые и тёплые не трогаются.

Запуск: python tools/art/recolor_swift.py [--apply] файл.swift ...
"""
import colorsys
import re
import sys


def conv(rgb):
    r, g, b = ((rgb >> 16) & 255) / 255, ((rgb >> 8) & 255) / 255, (rgb & 255) / 255
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    H = h * 360
    if s < 0.05 and (l > 0.93 or l < 0.04):
        return rgb
    nh = None
    ns = s
    if 225 <= H <= 345:
        if s >= 0.3 and l >= 0.45:
            nh, ns = 158, max(s, 0.5)
        elif s >= 0.3:
            nh, ns = 182, s * 0.9
        else:
            nh, ns = 190, min(0.26, s * 1.8 + 0.05)
    elif l < 0.3 and 0.04 <= s < 0.25:
        nh, ns = 190, max(s, 0.15)
    if nh is None:
        return rgb
    r2, g2, b2 = colorsys.hls_to_rgb(nh / 360, l, ns)
    return (round(r2 * 255) << 16) | (round(g2 * 255) << 8) | round(b2 * 255)


def main():
    apply = "--apply" in sys.argv
    for path in [a for a in sys.argv[1:] if not a.startswith("--")]:
        text = open(path, encoding="utf-8").read()
        changes = []

        def sub(m):
            old = int(m.group(1), 16)
            new = conv(old)
            if new != old:
                changes.append((old, new))
            return f"0x{new:06X}" if new != old else m.group(0)

        out = re.sub(r"0x([0-9A-Fa-f]{6})\b", sub, text)
        print(f"{path}: {len(changes)} цветов")
        if apply and changes:
            open(path, "w", encoding="utf-8", newline="").write(out)


if __name__ == "__main__":
    main()
