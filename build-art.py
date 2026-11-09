#!/usr/bin/env python3
"""Раскладывает графику онбординга v3, новые фоны и плитки иконок по ресурсам.

Источники — в `art/`: картинки онбординга в `art/onboarding/`, фоны 9:16 в
`art/backgrounds/`, иконки приложения в `art/icons/`. Пишет в
`LampadaCore/Sources/LampadaUI/Resources/Media.xcassets`. Сами наборы иконок
для системы собирает `App/make_icon.py`.

`art/backgrounds/` в git не попадает (см. `.gitignore`): исходники фонов 9:16
лежат только на маке, где их генерировали, а в сборку идут готовые варианты
из каталога. Перегенерировать фоны можно только там.

ПОЧЕМУ АПСКЕЙЛ. Grok отдаёт фон в 688×1504, а приложению нужен высокий
вариант 1320×2868 — в нём фон стоит на весь экран. Перегенерация в большем
размере дала бы другую картинку, а эти уже утверждены. Поэтому Lanczos и лёгкая
резкость поверх: на живописи без мелкого шрифта разница с родным размером на
телефоне не видна.

Квадратный и широкий варианты режутся из того же кадра вокруг сюжета — точка
та же, что `VerseScene.focus` в коде: лодка, звезда, сад и крест стоят не по
центру, и срез по середине выбросил бы их из кадра.
"""

import json
import pathlib

from PIL import Image, ImageFilter

HERE = pathlib.Path(__file__).parent
ART = HERE / "art"
MEDIA = HERE / "LampadaCore" / "Sources" / "LampadaUI" / "Resources" / "Media.xcassets"

# Фон: имя в коде, исходник, точка сюжета по высоте (доля от верха).
SCENES = [
    ("galilee", "Галилея", 0.80),
    ("star", "Звезда", 0.55),
    ("gethsemane", "Гефсимания", 0.70),
    ("cross", "Крест", 0.72),
]

# Размеры вариантов — те же, что у прежних фонов: `SceneBackground.Variant`
# считает пропорции по ним.
TALL = (1320, 2868)
SQUARE = (1092, 1092)
WIDE = (1092, 510)


def sharpened(image: Image.Image, size) -> Image.Image:
    return image.resize(size, Image.LANCZOS).filter(
        ImageFilter.UnsharpMask(radius=1.6, percent=45, threshold=2))


def crop_around(image: Image.Image, aspect: float, focus_y: float) -> Image.Image:
    """Самый большой кадр с пропорцией `aspect`, где сюжет как можно ближе к
    середине, а края не выходят за картинку."""
    width = image.width
    height = round(width / aspect)
    if height > image.height:
        height = image.height
        width = round(height * aspect)
    left = (image.width - width) // 2
    top = round(focus_y * image.height - height / 2)
    top = max(0, min(image.height - height, top))
    return image.crop((left, top, left + width, top + height))


def write_imageset(name: str, image: Image.Image, ext: str = "jpg", quality: int = 86) -> None:
    folder = MEDIA / f"{name}.imageset"
    folder.mkdir(parents=True, exist_ok=True)
    for stale in folder.glob(f"{name}.*"):
        stale.unlink()
    path = folder / f"{name}.{ext}"
    if ext == "jpg":
        image.convert("RGB").save(path, quality=quality, optimize=True, progressive=True)
    else:
        image.save(path, optimize=True)
    (folder / "Contents.json").write_text(json.dumps({
        "images": [
            {"filename": path.name, "idiom": "universal", "scale": "1x"},
            {"idiom": "universal", "scale": "2x"},
            {"idiom": "universal", "scale": "3x"},
        ],
        "info": {"author": "xcode", "version": 1},
    }, indent=2), encoding="utf-8")
    print(f"{name}: {image.width}×{image.height}")


def scenes() -> None:
    for name, source, focus in SCENES:
        src = Image.open(ART / "backgrounds" / f"{source}-9x16.png").convert("RGB")
        for variant, size in (("tall", TALL), ("square", SQUARE), ("wide", WIDE)):
            frame = crop_around(src, size[0] / size[1], focus)
            write_imageset(f"bg-{name}-{variant}", sharpened(frame, size))


def onboarding() -> None:
    folder = ART / "onboarding"
    # Иконки целей стоят плиткой 48 pt — на @3x это 144 пикселя.
    for goal in ("comfort", "daily", "feed", "beauty"):
        src = Image.open(folder / f"goal-{goal}.png").convert("RGB")
        write_imageset(f"goal-{goal}", src.resize((192, 192), Image.LANCZOS), quality=90)
    # Плакаты на весь экран, как заставка первого слайда.
    for poster in ("done", "gift"):
        src = Image.open(folder / f"{poster}.png").convert("RGB")
        write_imageset(poster, sharpened(src, (1032, round(1032 * src.height / src.width))))
    # Часы с прозрачными краями — только PNG.
    hourglass = Image.open(folder / "hourglass.png").convert("RGBA")
    write_imageset("hourglass", hourglass.resize((480, 480), Image.LANCZOS), ext="png")


def icon_previews() -> None:
    """Плитки в выборе иконки: экран выбора живёт в пакете и до наборов
    иконок в бандле приложения не дотягивается (см. `AppIcon.previewAsset`)."""
    for name in ("vitrage", "cross", "christmas", "easter", "dove"):
        src = Image.open(ART / "icons" / f"{name}.png").convert("RGB")
        write_imageset(f"icon-{name}", src.resize((512, 512), Image.LANCZOS), quality=88)


if __name__ == "__main__":
    scenes()
    onboarding()
    icon_previews()
