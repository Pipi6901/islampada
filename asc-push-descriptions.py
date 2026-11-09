#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Заливка описаний из build-metadata.py в App Store Connect.

Зачем отдельный скрипт, а не MCP-сервер asc-mcp: у него внутри проверка,
что версия в PREPARE_FOR_SUBMISSION или DEVELOPER_REJECTED. После отказа
ревью версия висит в REJECTED — Apple такое править разрешает, сервер нет.

Заливает одно поле: описание, а с --whatsnew — «Что нового». Названия и
ключевые слова не трогает. Подпись JWT делает openssl, лишних библиотек не нужно.

Запуск:
    python3 asc-push-descriptions.py              # залить описания
    python3 asc-push-descriptions.py --whatsnew   # залить «Что нового»
    python3 asc-push-descriptions.py --dry-run    # только показать, что зальёт
"""

import base64
import importlib.util
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

API = "https://api.appstoreconnect.apple.com/v1"
APP_ID = "6807549676"

KEY_ID = os.environ.get("ASC_KEY_ID", "JSXJ364L48")
ISSUER_ID = os.environ.get("ASC_ISSUER_ID", "57034376-aee7-484e-86f5-3d9d56417d6a")
KEY_PATH = os.environ.get(
    "ASC_PRIVATE_KEY_PATH",
    os.path.expanduser("~/Downloads/AuthKey_JSXJ364L48.p8"),
)

HERE = os.path.dirname(os.path.abspath(__file__))


def b64u(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


def der_to_raw(der: bytes) -> bytes:
    """Подпись ECDSA от openssl приходит в DER, а JWT хочет r||s по 32 байта."""
    assert der[0] == 0x30, "ожидалась DER SEQUENCE"
    i = 2 if der[1] < 0x80 else 3 + (der[1] & 0x7F) - 1
    out = b""
    for _ in range(2):
        assert der[i] == 0x02, "ожидался DER INTEGER"
        length = der[i + 1]
        val = der[i + 2 : i + 2 + length].lstrip(b"\x00")
        out += val.rjust(32, b"\x00")
        i += 2 + length
    return out


def token() -> str:
    """JWT ES256 на 15 минут — потолок, который принимает App Store Connect."""
    if not os.path.exists(KEY_PATH):
        sys.exit(f"не найден приватный ключ: {KEY_PATH}")
    header = {"alg": "ES256", "kid": KEY_ID, "typ": "JWT"}
    payload = {
        "iss": ISSUER_ID,
        "iat": int(time.time()),
        "exp": int(time.time()) + 900,
        "aud": "appstoreconnect-v1",
    }
    signing_input = ".".join(
        b64u(json.dumps(p, separators=(",", ":")).encode()) for p in (header, payload)
    )
    der = subprocess.run(
        ["openssl", "dgst", "-sha256", "-sign", KEY_PATH],
        input=signing_input.encode(),
        capture_output=True,
        check=True,
    ).stdout
    return f"{signing_input}.{b64u(der_to_raw(der))}"


def call(method: str, path: str, jwt: str, body: dict | None = None) -> dict:
    req = urllib.request.Request(
        path if path.startswith("http") else f"{API}{path}",
        method=method,
        data=json.dumps(body).encode() if body else None,
        headers={
            "Authorization": f"Bearer {jwt}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        raise SystemExit(f"{method} {path} → HTTP {e.code}\n{detail}") from None


def metadata() -> dict:
    spec = importlib.util.spec_from_file_location(
        "bm", os.path.join(HERE, "build-metadata.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.L


def main() -> None:
    dry = "--dry-run" in sys.argv
    key, field = ("whatsnew", "whatsNew") if "--whatsnew" in sys.argv else ("description", "description")
    locales = metadata()

    jwt = token()

    # Правится только версия, которая ещё не в магазине: после выхода новой
    # версии первой в списке может оказаться живая, а её текст менять нельзя.
    versions = call("GET", f"/apps/{APP_ID}/appStoreVersions?limit=10", jwt)
    editable = [v for v in versions["data"]
                if v["attributes"]["appVersionState"] not in ("READY_FOR_SALE", "REPLACED_WITH_NEW_VERSION", "REMOVED_FROM_SALE")]
    if not editable:
        sys.exit("нет версии, которую можно править")
    version = editable[0]
    state = version["attributes"]["appVersionState"]
    print(f"версия {version['attributes']['versionString']}  состояние {state}")

    listing = call(
        "GET",
        f"/appStoreVersions/{version['id']}/appStoreVersionLocalizations?limit=50",
        jwt,
    )
    ids = {row["attributes"]["locale"]: row["id"] for row in listing["data"]}

    for locale, data in locales.items():
        if locale not in ids:
            print(f"!! {locale}: локали нет в этой версии, пропускаю")
            continue
        text = data[key]
        note = ""
        if key == "description":
            note = f", ссылка EULA {'есть' if 'stdeula' in text else 'ОТСУТСТВУЕТ'}"
        print(f"{'—' if dry else '→'} {locale}: {len(text)} симв.{note}")
        if dry:
            continue
        call(
            "PATCH",
            f"/appStoreVersionLocalizations/{ids[locale]}",
            jwt,
            {
                "data": {
                    "type": "appStoreVersionLocalizations",
                    "id": ids[locale],
                    "attributes": {field: text},
                }
            },
        )
        print(f"   залито")

    if not dry:
        print("\nготово. Проверь текст в ASC перед отправкой версии на ревью.")


if __name__ == "__main__":
    main()
