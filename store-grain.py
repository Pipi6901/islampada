#!/usr/bin/env python3
"""Плёночное зерно поверх выгруженных кадров витрины.

Зерно накладывается здесь, а не в .pen, потому что рендерер Pencil у картиночных
заливок игнорирует и альфа-канал, и режим смешивания: слой ложится непрозрачным
и поднимает чёрный на два десятка уровней. Считать зерно на готовом PNG и точнее,
и повторяемо — кадр пересобирается одной командой после каждого экспорта.

    python3 store-grain.py store-screenshots/ru

Берёт PNG, выгруженные из Pencil, добавляет зерно и кладёт рядом JPEG, а
исходный PNG удаляет. Повторный запуск ничего не найдёт и не испортит: PNG в
папке уже нет. Чтобы пересобрать кадр — выгрузи его из Pencil заново.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

# Сила зерна в уровнях яркости: в чистом чёрном и в чистом белом его почти нет,
# как на плёнке, а в полутонах — максимум.
FLOOR = 3.4
PEAK = 9.0

# Доля крупного зерна. Один белый шум читается как цифровой дизеринг, поэтому
# к нему подмешивается слой вдвое крупнее — крупинки начинают слипаться.
COARSE = 0.24

SEED = 4242


def grain(shape: tuple[int, int], rng: np.random.Generator) -> np.ndarray:
    h, w = shape
    fine = rng.normal(0.0, 1.0, (h, w))
    half = ((rng.normal(0.0, 1.0, (h // 2 + 1, w // 2 + 1)) * 40) + 128).clip(0, 255).astype(np.uint8)
    coarse = np.asarray(Image.fromarray(half).resize((w, h), Image.BILINEAR), dtype=np.float64)
    coarse = (coarse - 128.0) / 40.0
    mixed = (1.0 - COARSE) * fine + COARSE * coarse
    smoothed = Image.fromarray(((mixed * 40) + 128).clip(0, 255).astype(np.uint8), mode="L")
    smoothed = smoothed.filter(ImageFilter.GaussianBlur(0.35))
    return (np.asarray(smoothed, dtype=np.float64) - 128.0) / 40.0


def apply(path: Path, rng: np.random.Generator) -> Path:
    img = Image.open(path).convert("RGB")
    a = np.asarray(img, dtype=np.float64)
    lum = a.mean(axis=2) / 255.0
    amp = FLOOR + PEAK * (1.0 - np.abs(2.0 * lum - 1.0))
    out = a + (grain(a.shape[:2], rng) * amp)[:, :, None]
    # JPEG, а не PNG: зерно ломает сжатие, и кадр в PNG весит около пяти мегабайт.
    # Тридцать пять таких файлов раздували репозиторий быстрее, чем весь остальной
    # код. На качестве это не сказывается — 4:4:4 без даунсемплинга цвета.
    jpg = path.with_suffix(".jpg")
    Image.fromarray(out.clip(0, 255).astype(np.uint8)).save(
        jpg, quality=95, subsampling=0, optimize=True
    )
    path.unlink()
    return jpg


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "store-screenshots/ru")
    files = sorted(root.glob("*.png"))
    if not files:
        print(f"нет PNG в {root}", file=sys.stderr)
        return 1
    rng = np.random.default_rng(SEED)
    for f in files:
        print(apply(f, rng).name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
