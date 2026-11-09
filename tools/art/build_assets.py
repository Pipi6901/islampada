# -*- coding: utf-8 -*-
"""Собирает графику Misbah: фоны-картинки, иконки приложения, арт онбординга.

Исходники лежат в art-src/ (картинки, сгенерированные в Pencil: фоны 9:16 и фонарь).
Недостающее — орнаментальные фоны и часть иконок — рисуется здесь же процедурно: так
оно не зависит от лимитов генератора, чётко на любом размере и без людей и животных.

Пишет:
  LampadaCore/Sources/LampadaUI/Resources/Media.xcassets   фоны, плитки иконок, арт онбординга
  App/Misbah/Assets.xcassets                              иконки приложения (основная и альтернативные)
  LampadaCore/Sources/LampadaCore/VerseScene.swift         параметры фонов, посчитанные по картинкам
  блок `VerseScene.focus` в LampadaCore/Sources/LampadaUI/Background.swift

Запуск: python tools/art/build_assets.py
"""
import json
import math
import os
import random
import re
import shutil
import sys

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "art-src")
MEDIA = os.path.join(ROOT, "LampadaCore", "Sources", "LampadaUI", "Resources", "Media.xcassets")
APPICONS = os.path.join(ROOT, "App", "Misbah", "Assets.xcassets")

random.seed(11)
LIGHT_TEXT = 0xEEECE6
DARK_TEXT = 0x201C1A


def rgb(h):
    return ((h >> 16) & 255, (h >> 8) & 255, h & 255)


def vgrad(w, h, top, bottom):
    t = np.linspace(0, 1, h)[:, None, None]
    a = np.array(rgb(top)).reshape(1, 1, 3)
    b = np.array(rgb(bottom)).reshape(1, 1, 3)
    arr = (a * (1 - t) + b * t) * np.ones((1, w, 1))
    return Image.fromarray(arr.astype("uint8"), "RGB").convert("RGBA")


def rgrad(w, h, center, radius, inner, outer):
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.clip(np.sqrt((xx - center[0]) ** 2 + (yy - center[1]) ** 2) / radius, 0, 1)[..., None]
    a = np.array(rgb(inner)).reshape(1, 1, 3)
    b = np.array(rgb(outer)).reshape(1, 1, 3)
    arr = a * (1 - d) + b * d
    return Image.fromarray(arr.astype("uint8"), "RGB").convert("RGBA")


def glow(size, center, radius, color, strength):
    w, h = size
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt((xx - center[0]) ** 2 + (yy - center[1]) ** 2) / radius
    a = np.clip(1 - d, 0, 1) ** 2 * strength
    layer = np.zeros((h, w, 4), dtype="uint8")
    layer[..., :3] = rgb(color)
    layer[..., 3] = (a * 255).astype("uint8")
    return Image.fromarray(layer, "RGBA")


def star_points(cx, cy, r, rot=0.0, ratio=0.765):
    pts = []
    for k in range(16):
        ang = math.radians(rot + k * 22.5)
        rr = r if k % 2 == 0 else r * ratio
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    return pts


def star_field(size, s, fill, line, line_w, inner=None, diamond=None, scale=2, offset=(0, 0)):
    """Узор из восьмиконечных звёзд, касающихся вершинами, и ромбов между ними."""
    W, H = size[0] * scale, size[1] * scale
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    S = s * scale
    cols, rows = int(W / S) + 3, int(H / S) + 3
    ox, oy = offset[0] * scale, offset[1] * scale
    for j in range(-1, rows):
        for i in range(-1, cols):
            cx, cy = i * S + ox, j * S + oy
            pts = star_points(cx, cy, S / 2)
            d.polygon(pts, fill=fill)
            d.line(pts + [pts[0]], fill=line, width=max(1, int(line_w * scale)), joint="curve")
            if inner:
                d.polygon(star_points(cx, cy, S / 4, rot=22.5), fill=inner)
            if diamond:
                mx, my = cx + S / 2, cy + S / 2
                q = S * 0.17
                d.polygon([(mx - q, my), (mx, my - q), (mx + q, my), (mx, my + q)], fill=diamond)
    return img.resize(size, Image.LANCZOS)


def petal(cx, cy, length, width, angle, steps=40):
    pts = []
    for k in range(steps):
        t = 2 * math.pi * k / steps
        x = (length / 2) * (1 + math.cos(t)) / 2 * 2 * math.cos(0)  # вытянутый эллипс вдоль луча
        px = (length / 2) * math.cos(t) + length / 2
        py = (width / 2) * math.sin(t)
        ca, sa = math.cos(angle), math.sin(angle)
        pts.append((cx + px * ca - py * sa, cy + px * sa + py * ca))
    return pts


def hue_shift(img, deg):
    hsv = img.convert("RGB").convert("HSV")
    h, s, v = hsv.split()
    h = h.point(lambda x: int((x + deg / 360 * 255) % 255))
    return Image.merge("HSV", (h, s, v)).convert("RGB")


def lanczos_up(img, size):
    out = img.resize(size, Image.LANCZOS)
    return out.filter(ImageFilter.UnsharpMask(radius=1.4, percent=60, threshold=3))


def cover(img, size, focus=(0.5, 0.5)):
    """Масштаб «cover» с обрезкой вокруг точки фокуса."""
    w, h = img.size
    scale = max(size[0] / w, size[1] / h)
    nw, nh = int(math.ceil(w * scale)), int(math.ceil(h * scale))
    big = lanczos_up(img, (nw, nh))
    x = int(min(max(focus[0] * nw - size[0] / 2, 0), nw - size[0]))
    y = int(min(max(focus[1] * nh - size[1] / 2, 0), nh - size[1]))
    return big.crop((x, y, x + size[0], y + size[1]))


# ── запись каталогов ────────────────────────────────────────────────────────

def write_imageset(name, filename, image, fmt="JPEG", quality=88):
    d = os.path.join(MEDIA, f"{name}.imageset")
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    image = image.convert("RGB") if fmt == "JPEG" else image
    image.save(os.path.join(d, filename), fmt, quality=quality) if fmt == "JPEG" \
        else image.save(os.path.join(d, filename), fmt)
    contents = {
        "images": [{"filename": filename, "idiom": "universal", "scale": "1x"},
                   {"idiom": "universal", "scale": "2x"}, {"idiom": "universal", "scale": "3x"}],
        "info": {"author": "xcode", "version": 1},
        "properties": {"preserves-vector-representation": False},
    }
    json.dump(contents, open(os.path.join(d, "Contents.json"), "w", encoding="utf-8"), indent=2)


def write_appicon(name, image):
    d = os.path.join(APPICONS, f"{name}.appiconset")
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    image.convert("RGB").resize((1024, 1024), Image.LANCZOS).save(os.path.join(d, f"{name}.png"), "PNG")
    contents = {"images": [{"filename": f"{name}.png", "idiom": "universal",
                            "platform": "ios", "size": "1024x1024"}],
                "info": {"author": "xcode", "version": 1}}
    json.dump(contents, open(os.path.join(d, "Contents.json"), "w", encoding="utf-8"), indent=2)


# ── фоны ────────────────────────────────────────────────────────────────────

def scene_mosaic():
    w, h = 1320, 2868
    base = vgrad(w, h, 0xF4F8F5, 0xD6E7E1)
    pat = star_field((w, h), 165, (255, 255, 255, 80), (63, 139, 130, 130), 2.4,
                     inner=(63, 139, 130, 38), diamond=(63, 139, 130, 60))
    base.alpha_composite(pat)
    base.alpha_composite(glow((w, h), (w // 2, int(h * 0.42)), 1300, 0xFFFFFF, 0.35))
    return base.convert("RGB")


def scene_lattice():
    w, h = 1320, 2868
    base = vgrad(w, h, 0x0F3336, 0x061417)
    base.alpha_composite(glow((w, h), (w // 2, int(h * 0.36)), 1500, 0x1C7A78, 0.55))
    pat = star_field((w, h), 165, (255, 255, 255, 7), (212, 175, 55, 70), 2.2,
                     inner=(212, 175, 55, 16), diamond=(212, 175, 55, 22))
    base.alpha_composite(pat)
    return base.convert("RGB")


SCENES = [
    # key, источник (None — процедурный), точка фокуса на высоком кадре, акцент, цвет подписи
    dict(key="desert", src="scene-desert-src.png", focus=(0.5, 0.80), accent=0x8F6E54),
    dict(key="stars", src="scene-stars-src.png", focus=(0.5, 0.30), accent=0xE8C27A),
    dict(key="dome", src="scene-dome-src.png", focus=(0.5, 0.74), accent=0xE2B866),
    dict(key="lantern", src="scene-lantern-src.png", focus=(0.5, 0.24), accent=0xE8C27A),
    dict(key="garden", src="scene-garden-src.png", focus=(0.5, 0.42), accent=0xC9A24A),
    dict(key="mosaic", src=None, focus=(0.5, 0.5), accent=0x0F6F6A),
    dict(key="lattice", src=None, focus=(0.5, 0.5), accent=0xD4AF37),
]


def srgb_to_lin(a):
    return np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)


def rel_lum(a):
    lin = srgb_to_lin(a)
    return 0.2126 * lin[..., 0] + 0.7152 * lin[..., 1] + 0.0722 * lin[..., 2]


def measure(tall):
    a = np.asarray(tall.convert("RGB")).astype(float) / 255
    h = a.shape[0]
    band = a[int(0.27 * h):int(0.67 * h)]
    lum = rel_lum(band)
    light_text = lum.mean() < 0.22
    text_lum = rel_lum(np.array(rgb(LIGHT_TEXT if light_text else DARK_TEXT)) / 255)
    scrim = 0.0
    for step in range(0, 61):
        alpha = step / 100
        tint = 0.0 if light_text else 1.0
        adj = band * (1 - alpha) + tint * alpha
        l2 = rel_lum(adj)
        if light_text:
            ok = (text_lum + 0.05) / (np.percentile(l2, 92) + 0.05) >= 4.5
        else:
            ok = (np.percentile(l2, 8) + 0.05) / (text_lum + 0.05) >= 4.5
        if ok:
            scrim = alpha
            break
    else:
        scrim = 0.6
    mean_band = tuple(int(x) for x in (band.reshape(-1, 3).mean(0) * 255))
    mean_all = tuple(int(x) for x in (a.reshape(-1, 3).mean(0) * 255))
    to_hex = lambda c: (c[0] << 16) | (c[1] << 8) | c[2]
    return dict(light_text=bool(light_text), scrim=round(scrim, 2),
                background=to_hex(mean_band), second=to_hex(mean_all))


def build_scenes():
    params = {}
    for sc in SCENES:
        key = sc["key"]
        if sc["src"]:
            src = Image.open(os.path.join(SRC, sc["src"])).convert("RGB")
            tall = cover(src, (1320, 2868), sc["focus"])
            # квадрат и полоса режутся вокруг той же точки, что и в приложении
            fx, fy = sc["focus"]
            sq_w = src.width
            sy = int(min(max(fy * src.height - sq_w / 2, 0), src.height - sq_w))
            square = lanczos_up(src.crop((0, sy, sq_w, sy + sq_w)), (1092, 1092))
            wide_h = int(src.width * 510 / 1092)
            wy = int(min(max(fy * src.height - wide_h / 2, 0), src.height - wide_h))
            wide = lanczos_up(src.crop((0, wy, src.width, wy + wide_h)), (1092, 510))
        else:
            tall = scene_mosaic() if key == "mosaic" else scene_lattice()
            square = tall.crop((0, 700, 1320, 2020)).resize((1092, 1092), Image.LANCZOS)
            wide = tall.crop((0, 1100, 1320, 1100 + int(1320 * 510 / 1092))).resize((1092, 510), Image.LANCZOS)
        write_imageset(f"bg-{key}-tall", f"bg-{key}-tall.jpg", tall, quality=86)
        write_imageset(f"bg-{key}-square", f"bg-{key}-square.jpg", square, quality=86)
        write_imageset(f"bg-{key}-wide", f"bg-{key}-wide.jpg", wide, quality=86)
        m = measure(tall)
        m.update(focus=sc["focus"], accent=sc["accent"])
        params[key] = m
        print(f"  фон {key}: светлый текст={m['light_text']} подложка={m['scrim']}")
    return params


def write_scene_swift(params):
    order = [s["key"] for s in SCENES]
    light = [k for k in order if params[k]["light_text"]]
    dark = [k for k in order if not params[k]["light_text"]]
    scrim_lines = "\n".join(f"        case .{k}: {params[k]['scrim']}" for k in order)
    title = {"desert": "sceneDesert", "stars": "sceneStars", "dome": "sceneDome",
             "lantern": "sceneLantern", "garden": "sceneGarden", "mosaic": "sceneMosaic",
             "lattice": "sceneLattice"}
    title_lines = "\n".join(f"        case .{k}: .{title[k]}" for k in order)

    def pal(k):
        p = params[k]
        text = LIGHT_TEXT if p["light_text"] else DARK_TEXT
        return f"        case .{k}: (0x{p['background']:06X}, 0x{p['second']:06X}, 0x{text:06X}, 0x{p['accent']:06X})"

    palette_lines = "\n".join(pal(k) for k in order)
    cases = "\n".join(f"    case {k}" for k in order)
    swift = f'''import Foundation

/// Фон-изображение вместо цветной заливки.
///
/// Выбирается там же, где наборы цвета, и тем же жестом: это второй ряд плиток
/// на экране «Вид». Одно исключает другое — выбрал картинку, цветной набор
/// перестаёт действовать, и наоборот.
///
/// Все сюжеты без людей и животных: пустыня, звёзды, купол мечети, фонарь, сад и
/// два орнамента.
///
/// У каждого фона своя палитра. Она не декоративная: из неё выводятся плашки,
/// линии, приглушённый текст и заливка кнопок — всё то же, что у цветных
/// наборов. Значения посчитаны по самим изображениям (`tools/art/build_assets.py`),
/// а не подобраны на глаз.
///
/// ФАЙЛ СГЕНЕРИРОВАН `tools/art/build_assets.py` — не править руками.
public enum VerseScene: String, Sendable, Hashable, Codable, CaseIterable, Identifiable {{
{cases}

    public var id: String {{ rawValue }}

    /// Имя набора в каталоге. Формат подставляется по месту: `-tall` для экрана
    /// и обоев, `-wide` для среднего виджета и StandBy, `-square` для остальных.
    public var asset: String {{ "bg-\\(rawValue)" }}

    /// Светлый ли текст поверх картинки.
    ///
    /// Определяется самим изображением: тёмная картинка — светлый текст.
    public var prefersLightText: Bool {{
        switch self {{
        case {", ".join("." + k for k in light)}: true
        case {", ".join("." + k for k in dark)}: false
        }}
    }}

    /// Плотность подложки под текстом.
    ///
    /// Ноль означает, что картинка держит текст сама. Значения посчитаны от
    /// яркости в той полосе, где реально лежит аят: подложка доводит контраст до
    /// 4,5:1 — порога, ниже которого текст на светлом участке перестаёт
    /// читаться. Подложка не сплошная, а сгущается только в этой полосе, иначе
    /// картинка гаснет целиком и смысл её теряется.
    public var scrim: Double {{
        switch self {{
{scrim_lines}
        }}
    }}

    /// Полоса, в которой подложка держится на полную силу, в долях высоты
    /// экрана. Совпадает с местом ссылки, аята и плашки контекста.
    public static let textBand: ClosedRange<Double> = 0.27...0.67

    public var titleKey: L10n.Key {{
        switch self {{
{title_lines}
        }}
    }}

    /// Бесплатна только «Пустыня» — самая спокойная. Остальные за подпиской:
    /// это и есть тот платный набор, ради которого фоны затевались.
    public var isPremium: Bool {{ self != .desert }}

    /// Те же четыре цвета, что у цветного набора. `background` здесь не рисуется
    /// (сверху лежит картинка), но задаёт светлоту для плашек и кнопок.
    public var palette: (background: UInt32, second: UInt32, text: UInt32, accent: UInt32) {{
        switch self {{
{palette_lines}
        }}
    }}
}}
'''
    path = os.path.join(ROOT, "LampadaCore", "Sources", "LampadaCore", "VerseScene.swift")
    open(path, "w", encoding="utf-8", newline="\n").write(swift)

    # точки фокуса — в Background.swift
    focus_lines = "\n".join(
        f"        case .{k}: UnitPoint(x: {params[k]['focus'][0]}, y: {params[k]['focus'][1]})" for k in order)
    bg_path = os.path.join(ROOT, "LampadaCore", "Sources", "LampadaUI", "Background.swift")
    text = open(bg_path, encoding="utf-8").read()
    start = text.index("extension VerseScene {")
    end = text.index("/// Затемнение под строкой состояния")
    block = f'''extension VerseScene {{
    /// Где на картинке сюжет. Эта точка остаётся в кадре, когда экран режет
    /// картинку.
    ///
    /// У пустыни и купола сюжет стоит низко (горизонт, силуэт), у звёзд и
    /// фонаря — выше середины. Новый фон без точки фокуса не соберётся — здесь
    /// исчерпывающий перебор, а не значение по умолчанию. Те же точки использует
    /// `tools/art/build_assets.py`, когда режет квадрат и полосу.
    var focus: UnitPoint {{
        switch self {{
{focus_lines}
        }}
    }}
}}

'''
    open(bg_path, "w", encoding="utf-8", newline="").write(text[:start] + block + text[end:])


# ── иконки приложения ───────────────────────────────────────────────────────

def lantern_crop():
    """Квадрат с фонарём из hero-src: сам фонарь, свет вокруг и немного подставки."""
    src = Image.open(os.path.join(SRC, "hero-src.png")).convert("RGB")
    return src.crop((344, 0, 1064, 720))


def add_stars(img, n, seed=3, area=None):
    rnd = random.Random(seed)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    w, h = img.size
    x0, y0, x1, y1 = area or (0, 0, w, h)
    for _ in range(n):
        x, y = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        r = rnd.choice([1.2, 1.6, 2.2, 3.0])
        a = rnd.randint(110, 255)
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 244, 214, a))
    layer = layer.filter(ImageFilter.GaussianBlur(0.6))
    base = img.convert("RGBA")
    base.alpha_composite(layer)
    return base.convert("RGB")


def icon_default():
    return lanczos_up(lantern_crop(), (1024, 1024))


def selective_hue(img, lo, hi, shift_deg):
    """Сдвигает оттенок только у пикселей с оттенком от lo до hi (шкала PIL, 0-255)."""
    hsv = np.asarray(img.convert("RGB").convert("HSV")).copy()
    mask = (hsv[..., 0] >= lo) & (hsv[..., 0] <= hi)
    hsv[..., 0] = np.where(mask, (hsv[..., 0].astype(int) + int(shift_deg / 360 * 255)) % 255, hsv[..., 0])
    return Image.fromarray(hsv, "HSV").convert("RGB")


def icon_night():
    img = selective_hue(icon_default(), 85, 150, 38)
    img = ImageEnhance.Brightness(img).enhance(0.8)
    return add_stars(img, 90, seed=5, area=(0, 0, 1024, 1024))


def icon_star():
    w = 1024
    base = rgrad(w, w, (w // 2, w // 2), 760, 0x1D7C66, 0x082F29)
    base.alpha_composite(glow((w, w), (w // 2, w // 2), 520, 0xE8C27A, 0.38))
    s = 2
    layer = Image.new("RGBA", (w * s, w * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    c = w * s // 2
    outer = star_points(c, c, 390 * s)
    d.polygon(outer, fill=(10, 76, 63, 255))
    d.line(outer + [outer[0]], fill=(226, 184, 102, 255), width=14 * s, joint="curve")
    mid = star_points(c, c, 290 * s, rot=22.5)
    d.line(mid + [mid[0]], fill=(226, 184, 102, 200), width=6 * s, joint="curve")
    inner = star_points(c, c, 170 * s)
    d.polygon(inner, fill=(226, 184, 102, 255))
    d.ellipse((c - 54 * s, c - 54 * s, c + 54 * s, c + 54 * s), fill=(10, 76, 63, 255))
    for k in range(8):
        ang = math.radians(k * 45 + 22.5)
        x, y = c + 450 * s * math.cos(ang), c + 450 * s * math.sin(ang)
        d.ellipse((x - 9 * s, y - 9 * s, x + 9 * s, y + 9 * s), fill=(226, 184, 102, 230))
    base.alpha_composite(layer.resize((w, w), Image.LANCZOS))
    return base.convert("RGB")


def icon_mosaic():
    w = 1024
    base = Image.new("RGBA", (w, w), rgb(0xEFE6CF) + (255,))
    pat = star_field((w, w), 330, (19, 112, 111, 255), (201, 162, 74, 255), 9,
                     inner=(239, 230, 207, 255), diamond=(201, 162, 74, 255), offset=(w // 2 - 165, w // 2 - 165))
    base.alpha_composite(pat)
    base.alpha_composite(glow((w, w), (w // 2, w // 2), 900, 0xFFFFFF, 0.12))
    return base.convert("RGB")


def icon_dawn():
    w = 1024
    img = vgrad(w, w, 0x0E4A57, 0xF2C28B)
    arr = np.asarray(vgrad(w, w, 0x0E4A57, 0x2E7F88)).copy()
    # небо: бирюза сверху, тёплый горизонт у линии дюн
    t = np.linspace(0, 1, w)[:, None, None] ** 1.8
    top = np.array(rgb(0x0E4A57)).reshape(1, 1, 3)
    mid = np.array(rgb(0x4B9AA0)).reshape(1, 1, 3)
    hor = np.array(rgb(0xF6C98F)).reshape(1, 1, 3)
    sky = np.where(t < 0.5, top + (mid - top) * (t / 0.5), mid + (hor - mid) * ((t - 0.5) / 0.5))
    img = Image.fromarray((sky * np.ones((1, w, 1))).astype("uint8"), "RGB").convert("RGBA")
    img.alpha_composite(glow((w, w), (w // 2, 640), 420, 0xFFE7B0, 0.8))
    d = ImageDraw.Draw(img)
    d.ellipse((w // 2 - 120, 520, w // 2 + 120, 760), fill=(255, 238, 200, 255))
    for base_y, amp, phase, color in ((690, 60, 0.4, 0xE9B67C), (780, 80, 1.7, 0xC98F5A),
                                      (880, 70, 3.1, 0x8A5B3C)):
        pts = [(0, w)]
        for x in range(0, w + 8, 8):
            y = base_y + amp * math.sin(x / 190 + phase) + amp * 0.45 * math.sin(x / 83 + phase * 2)
            pts.append((x, y))
        pts.append((w, w))
        d.polygon(pts, fill=rgb(color) + (255,))
    return img.convert("RGB")


def icon_dome():
    w = 1024
    t = np.linspace(0, 1, w)[:, None, None] ** 1.5
    top = np.array(rgb(0x082B36)).reshape(1, 1, 3)
    mid = np.array(rgb(0x1F6E73)).reshape(1, 1, 3)
    hor = np.array(rgb(0xE7B66A)).reshape(1, 1, 3)
    sky = np.where(t < 0.55, top + (mid - top) * (t / 0.55), mid + (hor - mid) * ((t - 0.55) / 0.45))
    img = Image.fromarray((sky * np.ones((1, w, 1))).astype("uint8"), "RGB").convert("RGBA")
    img = add_stars(img.convert("RGB"), 40, seed=9, area=(0, 0, w, 520)).convert("RGBA")
    s = 2
    layer = Image.new("RGBA", (w * s, w * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    col = (6, 26, 33, 255)
    # здание
    d.rectangle((120 * s, 760 * s, 904 * s, 1024 * s), fill=col)
    # купол
    d.pieslice((312 * s, 470 * s, 712 * s, 870 * s), 180, 360, fill=col)
    d.rectangle((312 * s, 670 * s, 712 * s, 780 * s), fill=col)
    # шпиль
    d.rectangle((508 * s, 440 * s, 516 * s, 480 * s), fill=col)
    d.ellipse((502 * s, 424 * s, 522 * s, 444 * s), fill=col)
    # минареты
    for cx in (212, 812):
        d.rectangle(((cx - 22) * s, 360 * s, (cx + 22) * s, 800 * s), fill=col)
        d.polygon([((cx - 34) * s, 360 * s), ((cx + 34) * s, 360 * s), (cx * s, 250 * s)], fill=col)
        d.rectangle(((cx - 34) * s, 470 * s, (cx + 34) * s, 486 * s), fill=col)
    # малые купола
    for cx in (330, 694):
        d.pieslice(((cx - 70) * s, 690 * s, (cx + 70) * s, 830 * s), 180, 360, fill=col)
    img.alpha_composite(layer.resize((w, w), Image.LANCZOS))
    return img.convert("RGB")


def icon_rosette():
    w = 1024
    base = rgrad(w, w, (w // 2, w // 2), 760, 0x0F3D40, 0x051518)
    s = 2
    layer = Image.new("RGBA", (w * s, w * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    c = w * s // 2
    gold = (212, 175, 55, 255)
    for ring, (n, length, width, rot, fill) in enumerate((
            (16, 400, 120, 0, None), (16, 330, 96, 11.25, (20, 110, 108, 70)),
            (8, 230, 80, 0, (212, 175, 55, 40)))):
        for k in range(n):
            ang = math.radians(rot + k * 360 / n)
            pts = petal(c, c, length * s, width * s, ang)
            if fill:
                d.polygon(pts, fill=fill)
            d.line(pts + [pts[0]], fill=gold, width=6 * s, joint="curve")
    for r in (440, 120, 70):
        d.ellipse((c - r * s, c - r * s, c + r * s, c + r * s), outline=gold, width=5 * s)
    d.polygon(star_points(c, c, 60 * s), fill=gold)
    base.alpha_composite(layer.resize((w, w), Image.LANCZOS))
    base.alpha_composite(glow((w, w), (w // 2, w // 2), 420, 0xD4AF37, 0.18))
    return base.convert("RGB")


def icon_light():
    w = 1024
    base = rgrad(w, w, (w // 2, w // 2), 800, 0x1A6A69, 0x051517)
    s = 2
    layer = Image.new("RGBA", (w * s, w * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    c = w * s // 2
    n = 32
    for k in range(n):
        ang = math.radians(k * 360 / n)
        spread = math.radians(1.2 if k % 2 else 2.4)
        length = (470 if k % 2 else 560) * s
        a = int(230 if k % 2 == 0 else 150)
        pts = [(c, c), (c + length * math.cos(ang - spread), c + length * math.sin(ang - spread)),
               (c + length * math.cos(ang + spread), c + length * math.sin(ang + spread))]
        d.polygon(pts, fill=(240, 205, 120, a))
    base.alpha_composite(layer.resize((w, w), Image.LANCZOS))
    base.alpha_composite(glow((w, w), (w // 2, w // 2), 300, 0xFFE7A8, 0.9))
    d2 = ImageDraw.Draw(base)
    d2.ellipse((w // 2 - 70, w // 2 - 70, w // 2 + 70, w // 2 + 70), fill=(255, 244, 214, 255))
    return base.convert("RGB")


ICONS = [("default", icon_default), ("night", icon_night), ("mosaic", icon_mosaic),
         ("star", icon_star), ("dawn", icon_dawn), ("dome", icon_dome),
         ("rosette", icon_rosette), ("light", icon_light)]


def build_icons():
    # старые наборы иконок убираем целиком
    for entry in os.listdir(APPICONS):
        if entry.endswith(".appiconset"):
            shutil.rmtree(os.path.join(APPICONS, entry))
    for key, fn in ICONS:
        img = fn()
        write_appicon("AppIcon" if key == "default" else key, img)
        write_imageset(f"icon-{key}", f"icon-{key}.jpg", img.resize((512, 512), Image.LANCZOS), quality=88)
        print(f"  иконка {key}")


# ── арт онбординга ──────────────────────────────────────────────────────────

def faded_on(bg, crop, center, feather=0.62):
    """Кладёт `crop` на `bg` с радиальным растворением краёв, чтобы не было шва."""
    w, h = crop.size
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    a = np.clip((1 - d) / (1 - feather), 0, 1)
    a = a * a * (3 - 2 * a)
    mask = Image.fromarray((a * 255).astype("uint8"), "L")
    out = bg.convert("RGBA")
    out.paste(crop.convert("RGBA"), (int(center[0] - w / 2), int(center[1] - h / 2)), mask)
    return out


def sparkles(img, n, seed, area, color=(255, 232, 170)):
    rnd = random.Random(seed)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x0, y0, x1, y1 = area
    for _ in range(n):
        x, y = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        r = rnd.choice([2, 3, 4, 6])
        d.ellipse((x - r, y - r, x + r, y + r), fill=color + (rnd.randint(120, 255),))
    layer = layer.filter(ImageFilter.GaussianBlur(1.2))
    out = img.convert("RGBA")
    out.alpha_composite(layer)
    return out


def build_onboarding_art():
    src = Image.open(os.path.join(SRC, "hero-src.png")).convert("RGB")
    lantern = src.crop((352, 0, 1056, 768))  # фонарь, подставка, свет
    # герой: высокий плакат, фонарь в верхней половине
    pw, ph = 1170, 2532
    poster = vgrad(pw, ph, 0x1C4A4C, 0x0B1E21)
    big = lanczos_up(lantern, (int(704 * 1.55), int(768 * 1.55)))
    poster = faded_on(poster, big, (pw // 2, int(ph * 0.30)), feather=0.55)
    poster.alpha_composite(glow((pw, ph), (pw // 2, int(ph * 0.30)), 700, 0xF4B860, 0.22))
    write_imageset("hero", "hero.jpg", poster.convert("RGB"), quality=90)

    # «Готово» и подарок: тот же фонарь на высоком кадре
    dw, dh = 1032, 2256
    done = vgrad(dw, dh, 0x16403F, 0x091A1D)
    big2 = lanczos_up(lantern, (int(704 * 1.35), int(768 * 1.35)))
    done = faded_on(done, big2, (dw // 2, int(dh * 0.36)), feather=0.55)
    done = sparkles(done, 46, 21, (int(dw * 0.18), int(dh * 0.10), int(dw * 0.82), int(dh * 0.46)))
    write_imageset("done", "done.jpg", done.convert("RGB"), quality=88)

    gift = vgrad(dw, dh, 0x1B3F52, 0x0A1B26)
    gift.alpha_composite(glow((dw, dh), (dw // 2, int(dh * 0.36)), 800, 0xE8C27A, 0.28))
    gift = faded_on(gift, big2, (dw // 2, int(dh * 0.36)), feather=0.55)
    ray = Image.new("RGBA", (dw, dh), (0, 0, 0, 0))
    d = ImageDraw.Draw(ray)
    cx, cy = dw // 2, int(dh * 0.36)
    for k in range(24):
        ang = math.radians(k * 15)
        sp = math.radians(2.2)
        L = 900
        d.polygon([(cx, cy), (cx + L * math.cos(ang - sp), cy + L * math.sin(ang - sp)),
                   (cx + L * math.cos(ang + sp), cy + L * math.sin(ang + sp))], fill=(232, 194, 122, 26))
    gift.alpha_composite(ray.filter(ImageFilter.GaussianBlur(3)))
    gift = sparkles(gift, 60, 33, (0, int(dh * 0.05), dw, int(dh * 0.55)), color=(255, 214, 140))
    write_imageset("gift", "gift.jpg", gift.convert("RGB"), quality=88)

    # иконки ответов 4 шт.: фон тот же, что у экрана онбординга
    bgc = 0x1B2B2E

    def goal_from(srcname, box, out):
        im = Image.open(os.path.join(SRC, srcname)).convert("RGB").crop(box)
        im = lanczos_up(im, (384, 384))
        canvas = Image.new("RGBA", (384, 384), rgb(bgc) + (255,))
        canvas = faded_on(canvas, im, (192, 192), feather=0.45)
        write_imageset(out, f"{out}.jpg", canvas.convert("RGB"), quality=90)

    goal_from("goal-comfort-src.png", (454, 214, 954, 714), "goal-comfort")
    goal_from("goal-daily-src.png", (404, 164, 1004, 764), "goal-daily")

    def goal_from_png(path, out, scale=0.82):
        im = Image.open(path).convert("RGBA")
        im = ImageEnhance.Brightness(hue_shift(im.convert("RGB"), 0)).enhance(1.0).convert("RGBA") if False else im
        rgb_im = hue_shift(im.convert("RGB"), 0)
        r, g, b = rgb_im.split()
        a = im.split()[3]
        im2 = Image.merge("RGBA", (r, g, b, a))
        im2 = recolor_purple(im2)
        side = int(384 * scale)
        im2 = im2.resize((side, side), Image.LANCZOS)
        canvas = Image.new("RGBA", (384, 384), rgb(bgc) + (255,))
        canvas.alpha_composite(im2, ((384 - side) // 2, (384 - side) // 2))
        write_imageset(out, f"{out}.jpg", canvas.convert("RGB"), quality=90)

    old = os.path.join(ROOT, "art-src", "old")
    goal_from_png(os.path.join(old, "hourglass.png"), "goal-feed")
    goal_from_png(os.path.join(old, "palette.png"), "goal-beauty")
    hg = recolor_purple(Image.open(os.path.join(old, "hourglass.png")).convert("RGBA"))
    write_imageset("hourglass", "hourglass.png", hg, fmt="PNG")


def recolor_purple(im):
    """Сиреневое и фиолетовое в картинке уходит в бирюзовое и изумрудное."""
    arr = np.asarray(im.convert("RGBA")).astype(float) / 255
    r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]
    mx, mn = arr[..., :3].max(-1), arr[..., :3].min(-1)
    d = mx - mn
    s = np.where(mx == 0, 0, d / np.maximum(mx, 1e-9))
    dd = np.maximum(d, 1e-9)
    h = np.where(mx == r, ((g - b) / dd) % 6, np.where(mx == g, (b - r) / dd + 2, (r - g) / dd + 4)) / 6.0
    m = (h > 0.62) & (h < 0.95) & (s > 0.10)
    h2 = np.where(m, 0.50 - (h - 0.62) * 0.4, h)
    i = np.floor(h2 * 6).astype(int) % 6
    f = h2 * 6 - np.floor(h2 * 6)
    p, q, t = mx * (1 - s), mx * (1 - f * s), mx * (1 - (1 - f) * s)
    out = np.stack([np.choose(i, [mx, q, p, p, t, mx]),
                    np.choose(i, [t, mx, mx, q, p, p]),
                    np.choose(i, [p, p, t, mx, mx, q])], -1)
    out = np.where(m[..., None], out, arr[..., :3])
    res = np.dstack([out, a])
    return Image.fromarray((res * 255).astype("uint8"), "RGBA")


def clean_old_assets():
    keep_prefix = ()
    for name in os.listdir(MEDIA):
        if name.endswith(".imageset") and name.split(".")[0] not in ():
            shutil.rmtree(os.path.join(MEDIA, name))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    old = os.path.join(SRC, "old")
    if not os.path.isdir(old):
        os.makedirs(old)
        for name in ("hourglass", "palette"):
            shutil.copy(os.path.join(MEDIA, f"{name}.imageset", f"{name}.png"), os.path.join(old, f"{name}.png"))
    clean_old_assets()
    params = build_scenes()
    write_scene_swift(params)
    build_icons()
    build_onboarding_art()
    json.dump(params, open(os.path.join(SRC, "scene_params.json"), "w", encoding="utf-8"), indent=1)
    print("готово")


if __name__ == "__main__":
    main()
