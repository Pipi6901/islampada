#!/usr/bin/env python3
"""Собирает готовую быструю команду с нашим действием и подписывает её.

ПОДПИСЬ ОБЯЗАТЕЛЬНА. iOS отказывается импортировать неподписанные команды —
дословно: «Импорт неподписанных быстрых команд не поддерживается». Прежней
лазейки с «Ненадёжными быстрыми командами» в настройках больше нет. Подписываем
через `shortcuts sign` из macOS; режим `anyone` нужен, чтобы файл открылся не
только на этом компьютере.

iCloud-ССЫЛКУ ОТСЮДА НЕ ПОЛУЧИТЬ. Ссылку вида `icloud.com/shortcuts/<id>`
выдаёт Apple в момент, когда командой делятся с устройства. Подписанный файл —
то, из чего эта ссылка делается: занести его на iPhone, открыть, «Добавить»,
затем «Поделиться» → «Скопировать ссылку iCloud».

Идентификатор действия не выдуман: он вынут из базы «Команд» на симуляторе
после того, как действие добавили в команду вручную.
"""

import pathlib
import plistlib
import subprocess
import uuid

BUNDLE_ID = "com.astonio.lampada"
INTENT = "ShowPauseIntent"
APP_NAME = "Lampada"


def action(identifier: str, parameters: dict) -> dict:
    return {
        "WFWorkflowActionIdentifier": identifier,
        "WFWorkflowActionParameters": {"UUID": str(uuid.uuid4()), **parameters},
    }


def build() -> dict:
    pause = action(
        f"{BUNDLE_ID}.{INTENT}",
        {
            "AppIntentDescriptor": {
                "AppIntentIdentifier": INTENT,
                "BundleIdentifier": BUNDLE_ID,
                "Name": APP_NAME,
            }
        },
    )
    # Системное «Открыть приложение» отсюда убрано. Оно стояло вторым, пока
    # возврат делали им, — но до него дело не доходило: «Команды» убивали наше
    # действие по таймауту раньше. Теперь возврат делает само приложение по
    # адресу соцсети, а адрес берётся из параметра «Приложение» нашего действия.
    #
    # Параметр остаётся пустым: подставить его заранее нельзя, соцсеть выбирает
    # человек. Пустым он и работает — паузу покажет, — но возвращать будет
    # некуда, и приложение об этом прямо говорит на экране паузы.
    return {
        "WFWorkflowActions": [pause],
        "WFWorkflowClientVersion": "2605.0.5",
        "WFWorkflowMinimumClientVersion": 900,
        "WFWorkflowMinimumClientVersionString": "900",
        "WFWorkflowImportQuestions": [],
        "WFWorkflowTypes": [],
        "WFQuickActionSurfaces": [],
        "WFWorkflowHasOutputFallback": False,
        "WFWorkflowHasShortcutInputVariables": False,
        "WFWorkflowInputContentItemClasses": [
            "WFAppStoreAppContentItem",
            "WFArticleContentItem",
            "WFContactContentItem",
            "WFDateContentItem",
            "WFEmailAddressContentItem",
            "WFGenericFileContentItem",
            "WFImageContentItem",
            "WFiTunesProductContentItem",
            "WFLocationContentItem",
            "WFDCMapsLinkContentItem",
            "WFAVAssetContentItem",
            "WFPDFContentItem",
            "WFPhoneNumberContentItem",
            "WFRichTextContentItem",
            "WFSafariWebPageContentItem",
            "WFStringContentItem",
            "WFURLContentItem",
        ],
    }


def sign(unsigned: pathlib.Path, signed: pathlib.Path) -> None:
    # `shortcuts sign` шумит в stderr предупреждениями рантайма ObjC — они не
    # относятся к делу, поэтому смотрим на код возврата и на файл, а не на вывод.
    result = subprocess.run(
        ["shortcuts", "sign", "--mode", "anyone",
         "--input", str(unsigned), "--output", str(signed)],
        capture_output=True,
    )
    if result.returncode != 0 or not signed.exists():
        raise SystemExit(f"подписать не удалось: {result.stderr.decode()[:400]}")


if __name__ == "__main__":
    here = pathlib.Path(__file__).parent
    unsigned = here / "build" / "Пауза Lampada.unsigned.shortcut"
    signed = here / "Пауза Lampada.shortcut"
    unsigned.parent.mkdir(exist_ok=True)
    unsigned.write_bytes(plistlib.dumps(build(), fmt=plistlib.FMT_BINARY))
    sign(unsigned, signed)
    print(f"собрано и подписано: {signed} ({signed.stat().st_size} байт)")
