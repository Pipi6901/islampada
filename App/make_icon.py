#!/usr/bin/env python3
"""Собирает иконку приложения из фирменной лампы.

ПОЧЕМУ КАТАЛОГ ЗДЕСЬ, А НЕ В ПАКЕТЕ. Остальная графика живёт в ресурсах
`LampadaUI`, но иконке там не место: она обязана попасть в корень бандла
приложения вместе с ключом `CFBundleIconName`, а из ресурсного бандла пакета
туда не попадает. Без неё загрузка в App Store Connect падает сразу четырьмя
ошибками — нет 120×120, нет 152×152, нет ключа.

Формат каталога — «одна картинка на все размеры»: кладём 1024×1024, остальное
Xcode нарезает сам. Прозрачности в иконке быть не должно, скруглять углы тоже
не надо — это делает система.
"""

import json
import pathlib

from PIL import Image, ImageDraw, ImageFilter

SIZE = 1024

HERE = pathlib.Path(__file__).parent
LAMP = HERE.parent / "art" / "hero.png"
ASSETS = HERE / "Lampada" / "Assets.xcassets"


class Variant:
    """Один вариант иконки.

    `name` совпадает с `AppIcon.alternateName` в модели — по этой же строке
    `setAlternateIconName` находит набор в каталоге. Основная называется
    `AppIcon`, потому что на неё смотрит `ASSETCATALOG_COMPILER_APPICON_NAME`.
    """

    def __init__(self, name, top, bottom, glow=None, lamp_tint=None):
        self.name = name
        self.top = top
        self.bottom = bottom
        # Тёплый свет от фитиля. `None` — на светлом фоне свечение не читается
        # и только пачкает фон.
        self.glow = glow
        # Перекрасить лампу. Нужно там, где фон светлый: исходная лампа сама
        # светлая и на пергаменте попросту пропадает.
        self.lamp_tint = lamp_tint


# Градиенты взяты из палитр наборов, чтобы иконка и экран читались как одно
# целое. Основная — «Ночь», тот же набор, что стоит в приложении по умолчанию.
VARIANTS = [
    Variant("AppIcon", (0x30, 0x27, 0x39), (0x1E, 0x18, 0x1C), glow=(255, 176, 82)),
    Variant("night", (0x14, 0x10, 0x18), (0x0B, 0x09, 0x10), glow=(150, 130, 210)),
]

# Иконки из готовых изображений: те же лики, что человек ставит фоном стиха,
# и отдельное пламя. Рисовать их рецептом нельзя — это живопись, а не градиент,
# поэтому здесь только кадрирование и лёгкое затемнение к краям.
#
# Имена совпадают с `AppIcon.alternateName`: по этой строке `setAlternateIconName`
# ищет набор в каталоге.
PICTURES = ["christ", "paul", "david", "fresco", "flame"]

PICTURE_DIR = HERE.parent / "art" / "icons"

# Готовые иконки (1.0.2): нарисованы сразу иконкой, во весь квадрат, с
# залитыми углами. Кадрировать и затемнять их нельзя — виньетка легла бы
# поверх собственного света рисунка. Только привести к 1024.
READY = ["vitrage", "cross", "christmas", "easter", "dove"]


def background(variant: Variant) -> Image.Image:
    column = Image.new("RGB", (1, SIZE))
    for y in range(SIZE):
        t = y / (SIZE - 1)
        column.putpixel((0, y), tuple(
            int(variant.top[i] + (variant.bottom[i] - variant.top[i]) * t) for i in range(3)))
    return column.resize((SIZE, SIZE), Image.BICUBIC)


def glow(base: Image.Image, colour) -> Image.Image:
    """Тёплый свет от фитиля.

    Без него лампа на тёмном фоне выглядит вырезанной и наклеенной: горящий
    фитиль обязан что-то освещать вокруг себя.
    """
    layer = Image.new("RGB", (SIZE, SIZE), (0, 0, 0))
    draw = ImageDraw.Draw(layer)
    x, y, r = int(SIZE * 0.70), int(SIZE * 0.46), 190
    draw.ellipse([x - r, y - r, x + r, y + r], fill=colour)
    layer = layer.filter(ImageFilter.GaussianBlur(radius=120))
    return Image.blend(base, Image.blend(base, layer, 1.0), 0.30)


def tinted(lamp: Image.Image, colour) -> Image.Image:
    """Перекрашивает лампу в заданный цвет, сохраняя её светотень.

    Не заливка силуэта: плоское пятно теряет и фитиль, и блик на боку. Яркость
    исходного пикселя остаётся множителем, поэтому объём никуда не девается —
    меняется только тон.
    """
    grey = lamp.convert("L")
    # Множитель от 0.55 в тенях до 1.0 в светах: ниже тени ушли бы в чёрный и
    # лампа стала бы плоским пятном.
    bands = [grey.point(lambda level, v=value: int(v * (0.55 + 0.45 * level / 255)))
             for value in colour]
    bands.append(lamp.getchannel("A"))
    return Image.merge("RGBA", bands)


def build(variant: Variant) -> Image.Image:
    icon = background(variant)
    if variant.glow:
        icon = glow(icon, variant.glow)
    lamp = Image.open(LAMP).convert("RGBA")
    # Обрезаем прозрачные поля: иначе доля лампы в кадре зависит от того, сколько
    # пустоты оставил рендер, и подбирать масштаб пришлось бы на глаз.
    lamp = lamp.crop(lamp.getbbox())
    scale = (SIZE * 0.74) / max(lamp.size)
    lamp = lamp.resize((int(lamp.width * scale), int(lamp.height * scale)), Image.LANCZOS)
    if variant.lamp_tint:
        lamp = tinted(lamp, variant.lamp_tint)
    icon.paste(lamp,
               ((SIZE - lamp.width) // 2, (SIZE - lamp.height) // 2 + int(SIZE * 0.02)),
               lamp)
    return icon


def from_picture(name: str) -> Image.Image:
    """Иконка из готового изображения.

    Прозрачности в иконке быть не должно, поэтому кладём на непрозрачный холст.
    Виньетка нужна не для красоты: на маленьком размере светлые края сливаются
    с обоями рабочего стола, и силуэт иконки теряется.
    """
    src = Image.open(PICTURE_DIR / f"{name}.jpg").convert("RGB")
    side = min(src.size)
    left, top = (src.width - side) // 2, (src.height - side) // 2
    icon = src.crop((left, top, left + side, top + side)).resize((SIZE, SIZE), Image.LANCZOS)

    vignette = Image.new("L", (SIZE, SIZE), 0)
    draw = ImageDraw.Draw(vignette)
    inset = int(SIZE * 0.06)
    draw.ellipse((-inset, -inset, SIZE + inset, SIZE + inset), fill=255)
    vignette = vignette.filter(ImageFilter.GaussianBlur(SIZE * 0.13))
    return Image.composite(icon, Image.new("RGB", (SIZE, SIZE), (12, 10, 16)), vignette)


def ready(name: str) -> Image.Image:
    return Image.open(PICTURE_DIR / f"{name}.png").convert("RGB").resize((SIZE, SIZE), Image.LANCZOS)


def write(name: str, image: Image.Image) -> None:
    out = ASSETS / f"{name}.appiconset"
    out.mkdir(parents=True, exist_ok=True)
    image.save(out / f"{name}.png")
    (out / "Contents.json").write_text(json.dumps({
        "images": [{"filename": f"{name}.png", "idiom": "universal",
                    "platform": "ios", "size": "1024x1024"}],
        "info": {"author": "xcode", "version": 1},
    }, indent=2), encoding="utf-8")
    print(f"иконка собрана: {out / f'{name}.png'}")


if __name__ == "__main__":
    for variant in VARIANTS:
        write(variant.name, build(variant))
    for name in PICTURES:
        write(name, from_picture(name))
    for name in READY:
        write(name, ready(name))
    # Наборы, которых в списках больше нет, оставлять нельзя: Xcode соберёт их
    # в бандл, а `setAlternateIconName` про них не знает — мёртвый вес.
    keep = {v.name for v in VARIANTS} | set(PICTURES) | set(READY)
    for stale in ASSETS.glob("*.appiconset"):
        if stale.stem not in keep:
            for f in stale.iterdir():
                f.unlink()
            stale.rmdir()
            print(f"удалён устаревший набор: {stale.name}")
    (ASSETS / "Contents.json").write_text(
        json.dumps({"info": {"author": "xcode", "version": 1}}, indent=2), encoding="utf-8")
