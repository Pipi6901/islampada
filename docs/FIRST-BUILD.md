# Первая сборка Misbah: от репозитория до TestFlight

Код, тексты, картинки и тесты готовы (см. `README.md`). Компилировать Swift на Windows нельзя, поэтому
каждый коммит проверяет GitHub Actions на macOS (`.github/workflows/ci.yml`: тесты пакета, сборка пакета под
iOS, сборка приложения вместе с виджетом), а настоящая сборка для TestFlight идёт в Codemagic.

Идентификаторы в коде уже стоят свои:

| Что | Значение |
|---|---|
| Bundle ID приложения | `com.astonio.misbah` |
| Bundle ID виджета | `com.astonio.misbah.widgets` |
| App Group | `group.com.astonio.misbah` |
| Team ID | `VG9U7V4AAL` |
| Apple ID приложения в App Store Connect | `6832716134` |
| Entitlement в RevenueCat | `misbah_pro` |

Отмечай `[x]`, когда шаг сделан. Порядок важен: каждый шаг даёт то, что нужно следующему.

## 1. Apple Developer — проверить, что заведено

developer.apple.com → Account → Certificates, Identifiers & Profiles → Identifiers.

- [ ] App Group `group.com.astonio.misbah`.
- [ ] App ID `com.astonio.misbah` — capabilities **App Groups** (эта группа) и **Push Notifications**.
- [ ] App ID `com.astonio.misbah.widgets` — capability **App Groups** (та же группа).

Без группы в обоих App ID сборка пройдёт, но виджет молча покажет настройки по умолчанию.

## 2. App Store Connect

- [ ] Приложение создано (имя **Misbah**, bundle `com.astonio.misbah`).
- [ ] Agreements, Tax, and Banking: принят **Paid Apps Agreement**, заполнены банк и налоги. Принять его может только
  владелец аккаунта (Account Holder). Пока не принято Program License Agreement (если Apple просит), сборки не загружаются.
- [ ] Users and Access → Integrations → App Store Connect API → ключ `Codemagic`, роль **App Manager**; `.p8` скачивается один раз —
  в менеджер паролей, не в репозиторий и не в чаты.

## 3. Codemagic

codemagic.io → Add application → GitHub → `Pipi6901/islampada` → «Other / codemagic.yaml».

- [ ] Teams → Integrations → App Store Connect: ключ из шага 2. Имя интеграции должно совпадать с `app_store_connect:` в
  `codemagic.yaml` посимвольно (сейчас `Astonio`).
- [ ] Environment variables → группа **`app_store_vars`** у ЭТОГО приложения (группы в Codemagic по-апповые):
  `CERTIFICATE_PRIVATE_KEY` (приватный ключ distribution-сертификата команды; у аккаунта лимит 3 сертификатов,
  новых не выпускать) и `GA_MP_SECRET` (можно пустым: пульс виджета молчит, сборка проходит).
- [ ] Версия Xcode: в `codemagic.yaml` стоит `xcode: latest` — первая сборка не споткнётся о версию, которой нет у Codemagic.
  Когда сборка пройдёт, можно прибить номер (например `27.1`: только с SDK iOS 27.1 приложение на iPhone Duo идёт край в край).

## 4. Firebase (аналитика и рассылки; для первой сборки не блокирует)

Без `GoogleService-Info.plist` приложение запускается, а Firebase просто не поднимается (аналитики и рассылок нет).
Когда понадобятся:

- [ ] console.firebase.google.com → новый проект (Analytics включить) → Add app → iOS → `com.astonio.misbah`.
- [ ] Скачай `GoogleService-Info.plist`, положи в `App/Misbah/`, закоммить и запушь.
- [ ] Рассылки: Project settings → Cloud Messaging → загрузи APNs-ключ (Apple Developer → Keys → APNs, `.p8`).

## 4а. Политика, условия, поддержка (обязательно до отправки на ревью)

Три страницы на en, ru и ar лежат в `docs/legal/misbah/misbah-{privacy,terms,support}.html`; исходники текстов — `tools/legal/`.
Страница сама выбирает язык по устройству, а `?lang=ru` или `?lang=ar` в адресе открывает нужный язык.

- [x] Почта поддержки в страницах — `help@pmoffice.space` (задана в `tools/legal/build_legal.py`, `DEFAULT_EMAIL`). Сменить:
  `python tools/legal/build_legal.py --email <почта> --final` и перезалить файлы. Если есть почтовый адрес юрлица, добавить его
  в раздел «Контакты» фрагментов `tools/legal/{en,ru,ar}/privacy.html` и `terms.html` и пересобрать.
- [ ] Залить файлы в корень сайта. Сейчас в коде стоит `https://pmoffice.space/misbah-privacy.html`
  (`LampadaCore/Sources/LampadaCore/Legal.swift`); если сайт другой — поправить там. Заливку делает человек со своим доступом:
  `curl -sS --ssl-reqd --max-time 120 -u '<ЛОГИН>' -T docs/legal/misbah/misbah-privacy.html ftp://<хост>.beget.tech/misbah-privacy.html`
  (так же `misbah-terms.html` и `misbah-support.html`; хост — часть логина до `_` плюс `.beget.tech`; пароль curl спросит сам,
  в команду и в репозиторий его не писать; сертификат выдан на `*.beget.tech`, поэтому адрес должен быть именно такой и без `-k`).
- [ ] Проверить: `https://pmoffice.space/misbah-privacy.html`, `-terms.html`, `-support.html` открываются по HTTPS без входа,
  в каждой видны три языковые кнопки.
- [ ] В App Store Connect: Privacy Policy URL — `…/misbah-privacy.html`; Support URL — `…/misbah-support.html` (для локализаций
  ru и ar-SA можно добавить `?lang=ru` и `?lang=ar`).
- [ ] Политику юридически никто не проверял: это адаптация. Она должна совпадать с анкетой App Privacy и с реально
  подключёнными SDK (Firebase, RevenueCat); Amplitude и Meta в первой сборке выключены и в тексте не упомянуты —
  включишь их, поправь фрагменты и анкету.

## 5. RevenueCat

app.revenuecat.com → новый проект → Add app → App Store.

- [ ] Bundle ID `com.astonio.misbah`; загрузи **In-App Purchase key** (ASC → Users and Access → Integrations → In-App Purchase)
  и API-ключ из шага 2.
- [ ] Entitlement **`misbah_pro`** (так названо в коде, `Purchases+Misbah.swift`).
- [ ] Продукты `com.astonio.misbah.weekly`, `.monthly`, `.yearly`, а для скидки после пейволла `.yearly.welcome`;
  привязать к entitlement.
- [ ] Offering `default` с пакетами Weekly, Monthly, Annual и пакетом `welcome`.
- [ ] API Keys → **Public app-specific key** (`appl_…`) вставить в `App/Misbah/MisbahApp.swift` вместо пустой строки
  `revenueCatKey`. Ключ публичный, в git его класть можно. Ключ с префиксом `test_` в Release роняет приложение.
  Пока ключ пустой, платный экран остаётся витриной: показывает состав Pro, но продать ничего не может.

## 6. Подписки в App Store Connect

Приложение → Monetization → Subscriptions.

- [ ] Группа подписок; три авто-возобновляемых — `weekly`, `monthly`, `yearly` (идентификаторы как в шаге 5).
- [ ] Цены и пробный период — по принятому решению (бесплатный пробный период только на годовой). В коде цены не зашиты:
  показывается то, что отдаёт RevenueCat.
- [ ] Локализации названий (en, ru, ar), скриншот пейволла для ревью. Статус «Ready to Submit».

## 7. Запуск сборки

- [ ] Codemagic → Start new build → workflow `ios-testflight`, ветка `main`. Шаги: генерация проекта, тесты пакета, подпись,
  номер сборки, пакеты SPM, `.ipa`, публикация в TestFlight. Первая сборка идёт 30–60 минут (скачиваются Firebase и RevenueCat).
- [ ] ASC → TestFlight: через 10–30 минут сборка обработается. Добавь себя во внутренние тестеры.

## 8. Что проверить на iPhone в первой сборке

1. Онбординг на русском, английском и арабском (Настройки iPhone → Основные → Язык и регион, потом открыть приложение
   или сменить язык кнопкой на первом экране). Арабский интерфейс должен зеркалиться целиком.
2. Экран «Сегодня»: арабский над переводом, огласовки и знаки чтения не пропадают, длинный аят уменьшается ступенями,
   листание вверх меняет аят.
3. «Вид» → «Показывать арабский текст» выключается и включается; выбор фона-картинки и набора цвета; смена иконки.
4. Виджеты: экран блокировки (прямоугольный: перевод, у арабского — оригинал), рабочий стол (малый — перевод, средний и
   большой — оригинал и перевод), StandBy, кнопка в Пункте управления.
5. Первое уведомление в онбординге: арабская строка выше перевода.
6. Поделиться: три формата (сторис, квадрат, обои) с арабским и без.
7. Экран «Язык и перевод»: видно уведомление Tanzil и ссылку `tanzil.net`.

## Типичные отказы

| Что видишь | Причина |
|---|---|
| Сборка не стартует, «xcode … not found» | Прибитой версии нет в Codemagic — верни `xcode: latest` (шаг 3) |
| «No matching profiles found» | Нет интеграции ASC, имя не совпало или App ID не создан (шаги 1, 3) |
| Падает на упаковке `.ipa` | Нет профиля виджета: нужен App ID `com.astonio.misbah.widgets` с группой |
| Загрузка отклонена из-за соглашения | Не принят Program License Agreement / Paid Apps Agreement (шаг 2) |
| Приложение падает на запуске | Ключ RevenueCat с префиксом `test_` в Release (шаг 5) |
| Виджет показывает настройки по умолчанию | App Group не прописан в обоих App ID |
| «Maximum number of certificates reached» | Уже 3 distribution-сертификата — используй существующий ключ |
| Покупки пустые | Подписки не Ready to Submit, нет Paid Apps Agreement, продукты не привязаны в RevenueCat |
| Нет аналитики и рассылок | Нет `GoogleService-Info.plist` (шаг 4) |

## Перед публикацией в стор

Метаданные App Store (en-US, ru, ar-SA), App Privacy, политика конфиденциальности и поддержка, скриншоты из `design/`,
вычитка отбора аятов и строк контекста мусульманином (см. `docs/TRANSLATIONS.md`, раздел «Состояние»). Отдельный план — `docs/RESKIN-PLAN.md`.
