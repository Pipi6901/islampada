# Первая сборка: от нуля до TestFlight

Порядок важен: каждый шаг даёт то, что нужно следующему. Компилировать Swift на
Windows нельзя, поэтому сборка идёт в облаке (Codemagic). Всё, что в `<угловых скобках>`, —
твои значения.

**Важно:** пока в коде тексты, аяты и картинки от Библии. Первая сборка по этой инструкции проверяет
инфраструктуру (подпись, App Store Connect, Codemagic, подписки), а не готовый продукт. В стор такую сборку
отправлять нельзя.

Отмечай `[x]`, когда шаг сделан.

## 0. Решить заранее

- [ ] **Чей Apple Developer-аккаунт.** Оригинал живёт на аккаунте команды Astonio (куратора).
  Приложение публикуется под тем аккаунтом, где куплена программа ($99/год). Если под
  куратором — нужна роль **Admin** или **App Manager** в App Store Connect и доступ к
  Certificates, Identifiers & Profiles (роль Admin). Если под своим — купи Apple Developer Program.
- [ ] **Рабочее имя приложения** (в макетах «Nur», позже поменяем).
- [ ] **Bundle ID**, обратная запись домена: `com.<команда>.<имя>`, например `com.astonio.nur`.
  Дальше: виджет `<bundle>.widgets`, App Group `group.<bundle>`, подписки `<bundle>.weekly|monthly|yearly`.
  Менять после первой сборки больно, выбирай сразу.

## 1. Apple Developer: идентификаторы
developer.apple.com → Account → Certificates, Identifiers & Profiles → Identifiers.

- [ ] **App Group:** `+` → App Groups → `group.<bundle>`.
- [ ] **App ID приложения:** `+` → App IDs → App → Bundle ID `<bundle>` (Explicit).
  Включи capabilities: **App Groups** (выбери группу) и **Push Notifications**.
- [ ] **App ID виджета:** `<bundle>.widgets` (Explicit), capability **App Groups** (та же группа).
- [ ] Запиши **Team ID** (Account → Membership details), 10 символов.

Без группы в обоих App ID сборка пройдёт, но виджет молча покажет настройки по умолчанию.

## 2. App Store Connect: создать приложение
appstoreconnect.apple.com → Apps → `+` → New App.

- [ ] Platform iOS, Name (уникальное в сторе; пока рабочее), Primary Language, Bundle ID = `<bundle>`, SKU любой (`nur-001`).
- [ ] После создания: App Information → скопируй **Apple ID** (число, ~10 цифр). Это `APP_STORE_APPLE_ID`.
- [ ] Agreements, Tax, and Banking: должен быть принят **Paid Apps Agreement**, заполнены банк и налоги.
  Без этого подписки не заработают. Принять соглашение может только владелец аккаунта (Account Holder).
  Если Apple просит принять обновлённое Program License Agreement — тоже он: пока не принято, сборки не загружаются.

## 3. App Store Connect: API-ключ для Codemagic
Users and Access → Integrations → App Store Connect API → Team Keys → `+`.

- [ ] Имя `Codemagic`, роль **App Manager**. Скачай `.p8` (скачивается один раз!), запиши **Key ID** и **Issuer ID**.
- [ ] Файл `.p8` не клади в репозиторий и не присылай в чаты. Храни в менеджере паролей.

## 4. Сертификат подписи
Нужен distribution-сертификат и его приватный ключ. У аккаунта лимит **3 distribution-сертификата**,
не выпускай новые без нужды.

- Если сертификат команды уже есть (его ключ у куратора) — попроси у куратора значение `CERTIFICATE_PRIVATE_KEY`.
- Если нет — сгенерируй ключ и положи его в Codemagic (шаг 5):
  ```bash
  ssh-keygen -t rsa -b 2048 -m PEM -f nur_cert_key -q -N ""
  ```
  Содержимое файла `nur_cert_key` целиком (с `-----BEGIN` и `-----END`) — это `CERTIFICATE_PRIVATE_KEY`.
  Сборка сама выпустит сертификат с этим ключом (`--create` в `codemagic.yaml`).

## 5. Codemagic
codemagic.io → Add application → GitHub → `Pipi6901/islampada` → тип проекта «Other / codemagic.yaml».

- [ ] Teams → Integrations → **App Store Connect** → Add key: Issuer ID, Key ID, `.p8`.
  Имя интеграции должно совпадать с `app_store_connect:` в `codemagic.yaml` посимвольно (сейчас `Astonio`).
  Поменяй имя в yaml или назови интеграцию так же.
- [ ] Applications → твоё приложение → Environment variables → группа **`app_store_vars`** (секретные):
  - `CERTIFICATE_PRIVATE_KEY` — из шага 4;
  - `GA_MP_SECRET` — секрет Measurement Protocol из GA4 (можно пока пустым: пульс виджета молчит, сборка проходит).
  Группа создаётся именно у этого приложения (группы в Codemagic по-апповые).
- [ ] Проверь версию Xcode: в `codemagic.yaml` стоит `xcode: 27.1`. Если Codemagic её не знает, сборка не стартует.
  Тогда поставь доступную из списка Codemagic (например `26.0`). Для iPhone Duo нужна 27.1, для первой сборки не критично.

## 6. Подставить свои идентификаторы в код
В папке репозитория:

```bash
python tools/set-ids.py --bundle <bundle> --team <TEAMID> --apple-id <число>
python tools/set-ids.py --bundle <bundle> --team <TEAMID> --apple-id <число> --apply
```

Первая команда только показывает, что поменяет. Вторая применяет. Заменятся bundle ID, App Group, Team ID и
Apple ID в `codemagic.yaml`, `make_project.py`, entitlements и Swift-коде. Если Apple ID ещё не известен, запусти без `--apple-id`.

## 7. Firebase (обязательно: без него приложение упадёт на запуске)
В проекте оригинала файл `GoogleService-Info.plist` удалён.

- [ ] console.firebase.google.com → новый проект (Analytics включить) → Add app → iOS → Bundle ID `<bundle>`.
- [ ] Скачай `GoogleService-Info.plist`, положи в `App/Lampada/`, закоммить.
- [ ] Для уведомлений: Project settings → Cloud Messaging → загрузи APNs-ключ (Apple Developer → Keys → APNs, `.p8`).
  Можно отложить: на первую сборку и TestFlight не блокирует.

## 8. RevenueCat (покупки)
app.revenuecat.com → новый проект → Add app → App Store.

- [ ] Bundle ID `<bundle>`; загрузи **In-App Purchase key** (App Store Connect → Users and Access → Integrations →
  In-App Purchase → `+`, `.p8`) и App Store Connect API key из шага 3.
- [ ] Entitlement с идентификатором **`lampada_pro`** (так названо в коде, `Purchases+Lampada.swift`).
  Позже можно переименовать в коде и панели одновременно.
- [ ] Продукты: `<bundle>.weekly`, `.monthly`, `.yearly` и `.yearly.welcome` (после шага 9). Привяжи к entitlement.
- [ ] Offering `default` с пакетами Weekly, Monthly, Annual и пакетом `welcome`.
- [ ] API Keys → скопируй **Public app-specific key** (`appl_...`) и вставь в `App/Lampada/LampadaApp.swift`
  вместо пустой строки `revenueCatKey`. Ключ публичный, в git его класть можно. Ключ с префиксом `test_` в Release роняет приложение.

## 9. Подписки в App Store Connect
Приложение → Monetization → Subscriptions.

- [ ] Группа подписок. Три авто-возобновляемых: `<bundle>.weekly`, `.monthly`, `.yearly`; цены $2.99 / $5.99 / $24.99 (как в оригинале).
- [ ] Intro offer «7 days free» только на годовой.
- [ ] Локализация названий, скриншот пейволла для ревью.
- [ ] Статус «Ready to Submit» нужен до того, как их увидит RevenueCat в тесте.

## 10. Запуск сборки
- [ ] Закоммить и запушь изменения (шаги 6–8).
- [ ] Codemagic → Start new build → workflow `ios-testflight`, ветка `main`.
  Шаги по `codemagic.yaml`: генерация проекта, тесты пакета, подпись, номер сборки, SPM, `.ipa`, публикация в TestFlight.
  Первая сборка идёт 30–60 минут (скачиваются Firebase и RevenueCat).
- [ ] App Store Connect → TestFlight: через 10–30 минут после публикации сборка обрабатывается. Добавь себя во внутренние тестеры
  (Users and Access → у тебя должна быть роль, TestFlight → Internal Testing → `+`).
- [ ] На iPhone: приложение TestFlight → установить.

## Типичные отказы
| Что видишь | Причина |
|---|---|
| Сборка не стартует, «xcode 27.1 not found» | Версии нет в Codemagic — шаг 5, поправь `xcode:` |
| «No matching profiles found» | Нет интеграции ASC, имя не совпало, или App ID не создан (шаги 1, 5) |
| Падает на упаковке `.ipa` | Нет профиля виджета: нужен App ID `<bundle>.widgets` с группой |
| Загрузка сборки отклонена из-за соглашения | Не принят Program License Agreement / Paid Apps Agreement (шаг 2, делает владелец аккаунта) |
| Приложение падает на запуске | Нет `GoogleService-Info.plist` (шаг 7) или ключ RevenueCat `test_` в Release |
| Виджет показывает настройки по умолчанию | App Group не прописан в обоих App ID |
| «Maximum number of certificates reached» | Уже 3 distribution-сертификата — используй существующий ключ (шаг 4) |
| Покупки пустые | Подписки не Ready to Submit, нет Paid Apps Agreement, продукты не привязаны в RevenueCat |

## Что делать после первой сборки
Метаданные для стора (`build-metadata.py` под Коран), App Privacy, политика конфиденциальности и поддержка,
скриншоты из `design/`, ASO в Astro. Отдельный план: `docs/RESKIN-PLAN.md`.
