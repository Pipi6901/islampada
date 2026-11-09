#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lampada — сборка и валидация метаданных App Store.
Пишет metadata/<locale>.txt и проверяет лимиты символов App Store Connect.

Позиционирование:
  база — виджет со стихом на всех поверхностях телефона;
  УТП  — «пауза перед лентой»: стих встречает в момент открытия соцсети.
  Функция опциональна и включается одним тапом на онбординге.

Запуск:  python3 build-metadata.py
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "metadata")

# Лимиты App Store Connect (символы)
LIMITS = {
    "name": 30,
    "subtitle": 30,
    "keywords": 100,
    "promo": 170,
    "description": 4000,
    "whatsnew": 4000,
    "sub_group": 30,
    "sub_name": 30,
    # Google Play, для второй платформы
    "play_title": 30,
    "play_short": 80,
}

COMMON = {
    "bundle_id": "com.astonio.misbah",
    "sku": "LAMPADA-IOS-001",
    "primary_category": "Reference",
    "secondary_category": "Lifestyle",
    "age_rating": "4+",
    "copyright": "2026 Lampada",
    "support_url": "https://pmoffice.space/lampada-support.html",
    "marketing_url": "https://pmoffice.space/lampada-support.html",
    "privacy_url": "https://pmoffice.space/lampada-privacy.html",
    "min_ios": "17.0",
}

L = {}

# ─────────────────────────────────────────────────────────── EN ──
L["en-US"] = {
    "language": "English (U.S.) — основная локаль",
    # Замерено через Astro (US, iphone), популярность/сложность:
    #   bible verse widget 67/65 · widget 70/83 · bible widget 57/63
    #   widgets 61/82 · bible widgets 29/52 — множественное число вдвое реже
    # Поэтому в названии единственное число, множественное вынесено в keywords.
    "name": "Bible Verse Widget: Lampada",
    # offline 64/80 и widgets 61/82 — два самых частотных слова, которых нет в
    # названии. Плюс lock и screen: «bible lock screen» 24/69.
    # 05.11: ушли из облака клонов. «Bible Verse Widget: X» — больше 50
    # приложений, по сложным словам (lock screen 44/73, widgets 60/80, offline
    # 61/80) мы вне выдачи. В подзаголовок — ниши, где конкуренция ниже и
    # продукт правда отличается: standby 36/39 (уже 241-е из одного поля
    # ключей), wallpapers + jesus → jesus wallpaper 31/11, psalms 31/21. Прежние
    # слова подзаголовка ушли в ключи; ради места убран god 46/77 — не взять.
    "subtitle": "StandBy, wallpapers & psalms",
    # Ни одного повтора из названия и подзаголовка. Отброшены по данным:
    #   prayer 53/71 и catholic 52/60 — частотно, но молитвенника и
    #     католического канона у нас нет: трафик отскочит и утянет конверсию
    #   kjv 30/80, niv 25/50, esv 28/51 — этих переводов в приложении нет
    #   anxiety 7/64 и faith 8/60 — низкая частота при высокой сложности
    # Взяты лучшие отношения: psalms 18/21, standby 12/38, verses 27/52,
    # quotes 32/56, и частотные wallpapers 69/80, sleep 63/81, god 53/74.
    # 27.10: sleep → grief. Реальные ранги Astro: по своему же названию мы 243-и
    # (возраст и оценки, не текст), sleep 63/81 не взять и он ведёт ищущих
    # приложения для сна; grief 17/11 — тема приложения, конкуренции почти нет.
    "keywords": "lock,screen,widgets,offline,daily,verses,quotes,scripture,devotional,christian,jesus,grief,christ",
    # 05.11: промотекст про стих дня, а не про паузу — в онбординге 1.0.2
    # главное теперь стих на экране и уведомлением. Меняется без новой версии.
    "promo": "Today's verse on your Lock Screen, Home Screen and StandBy, and as a notification at the time you choose. No account, no ads, works offline.",
    "sub_group": "Lampada Pro",
    "sub_week": "Lampada Pro · Weekly",
    "sub_month": "Lampada Pro · Monthly",
    "sub_year": "Lampada Pro · Yearly",
    "shots": [
        "Scripture on your Lock Screen",
        "The pause before the scroll",
        "Every widget size, every screen",
        "Your nightstand, at rest",
        "Make it look like yours",
        "Choose what you need today",
        "Wallpaper that changes itself",
    ],
    "description": """Your phone is the thing you look at most. Lampada puts the Word there: on the screens you already look at, and, if you want it, in the one moment you would rather not be scrolling.

Not another app to open. A verse on your Lock Screen, on your Home Screen, and on your nightstand while the phone charges. Nothing to remember. It is simply there, every time you glance down.

THE PAUSE BEFORE THE SCROLL
Switch it on in Places, in a few taps. From then on, the moment you open a social app, a verse meets you first. Not a feed to browse instead: a real pause, at the exact moment you would have started scrolling. Entirely optional, and off unless you ask for it.

WHERE THE WORD APPEARS
- Lock Screen: a short verse beside the clock, in three widget shapes
- Home Screen: three widget sizes, small to large
- StandBy: your phone becomes a bedside display while charging
- Control Centre: a button that opens today's verse (iOS 18)
- Wallpaper: save a verse image and set it as your background

A THOUSAND VERSES, EIGHT EDITIONS
World English Bible, Luther 1912, Louis Segond 1910, Reina-Valera, Bíblia Livre, Riveduta 1927, 개역한글 (Korean Revised Version) and the Russian Synodal translation. All of it inside the app, all of it offline.

CHOOSE WHAT YOU NEED TODAY
Anxiety. Grief. Gratitude. Forgiveness. Doubt. Starting something hard. Sleepless nights. Sixteen states in all: pick the ones that matter right now, and the verses follow.

CONTEXT, NOT JUST A LINE
Hundreds of passages carry one line telling you who is speaking and when. Not commentary. Just enough that the words are not left floating free.

MADE TO BE LOOKED AT
Typography and colour, never stock photos. Eight colour sets, twelve pictures, nine typefaces. Set them separately for the app, for the widgets and for the Lock Screen.

QUIET BY DESIGN
No account. No sign-up. No ads, ever. Works completely offline. The widget never spins, never fails, never asks you for anything.

FREE
The Lock Screen widget, the Home Screen widget, the Control Centre button, daily verses, the pause before the scroll, sharing without a watermark, four colour sets and one picture.

LAMPADA PRO
StandBy, every picture, all eight colour sets, every typeface and a choice of app icons.

Lampada Pro is an auto-renewing subscription and comes in three lengths: one week, one month, and one year with the first 7 days free. The price for your region is shown in the app before you confirm. Payment is charged to your Apple Account, and the subscription renews automatically unless you turn auto-renewal off at least 24 hours before the current period ends. Manage or cancel it any time in your Apple Account settings.

Terms of Use (EULA): https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
Privacy Policy: https://pmoffice.space/lampada-privacy.html

"Your word is a lamp to my feet, and a light for my path." Psalm 119:105

Scripture text: World English Bible, Luther 1912, Louis Segond 1910, Reina-Valera, Riveduta 1927, 개역한글 and the Russian Synodal translation, all in the public domain. Bíblia Livre © Diego Santos, Mario Sérgio, Marco Teles, CC BY 4.0 (creativecommons.org/licenses/by/4.0); final punctuation adjusted.""",
    "whatsnew": """Five new app icons: Stained glass, Cross, Christmas, Easter and Dove. The Dove is free for everyone.

Four new pictures for your verse: Galilee, Star, Gethsemane and Cross.

Lampada now speaks Portuguese, Italian and Korean, with the Bíblia Livre, the Riveduta 1927 and the 개역한글 (Korean Revised Version).

More accurate context notes on several verses, plus small fixes.""",
}

# ─────────────────────────────────────────────────── EN-GB / EN-AU ──
# 27.10, Astro. en-GB — язык витрины по умолчанию в ~20 странах (Великобритания,
# Ирландия, Скандинавия, Восточная Европа, Турция, Индия, Африка, Филиппины) и
# второй индексируемый почти во всей Европе и Латинской Америке. GB проще US:
# bible verse widget 45/23 против 67/75, без своей локали уже 66-е место.
# en-AU — Австралия и Новая Зеландия, где en-GB индексируется тоже, поэтому
# поля ключей GB и AU не пересекаются. Текст описания — тот же, что у en-US.
L["en-GB"] = {
    **L["en-US"],
    "language": "English (U.K.)",
    # 07.11: в Великобритании мы вне выдачи по всем 121 ключу, даже по hope
    # 27/11 и comfort 27/7 из этого же поля — дело в установках, не в словах.
    # Раз терять нечего, подзаголовок — под самые лёгкие частотные запросы:
    # verse of the day 32/23, standby 30/17. В ключи — peace 28/15,
    # gratitude 33/19, reflection 27/23; убраны god 39/58 и anxiety 40/52,
    # devotional ушёл в en-AU (поля GB и AU не пересекаются).
    "subtitle": "Verse of the Day & StandBy",
    # offline — ради «offline bible» в Индии, Нигерии, Кении, Филиппинах.
    # holy 46/36 не взят: тянет «holy bible», а полного текста Библии нет.
    "keywords": "hope,grief,comfort,psalms,peace,gratitude,reflection,wallpaper,christian,jesus,quotes,offline,verses",
}
L["en-AU"] = {
    **L["en-US"],
    "language": "English (Australia)",
    # 07.11: comfort 46/13 — самое выгодное слово Австралии, hope 24/9,
    # standby 25/13. Прежний «Home & Lock Screen» (home screen 33/58) не брал.
    "subtitle": "Comfort, Hope & StandBy",
    # hope, comfort, verses, offline, peace, gratitude приходят из en-GB.
    "keywords": "spiritual,christ,faith,affirmations,encouragement,forgiveness,proverbs,daily,devotional,aesthetic",
}

# ─────────────────────────────────────────────────── EN-CA / FR-CA ──
# 27.10, Astro (ca). Витрина Канады — English (Canada) + French (Canada); до
# этого не было ни того ни другого, и Канада видела en-US. Обе локали
# индексируются в одной витрине, поэтому их поля ключей не пересекаются.
# bible widget 49/50 — уже 18-е место; hope 49/36 и comfort 39/15 здесь
# сильнее, чем где-либо; lock screen 36/42, christ 38/17, standby 25/15.
# Французские запросы в CA почти пустые (5), кроме verset du jour 31/17 (105-е).
L["en-CA"] = {
    **L["en-US"],
    "language": "English (Canada)",
    "subtitle": "Hope & Comfort on Lock Screen",
    # 07.11: + grief 23/5 и quotes 35/23; убраны god 32/49, aesthetic 38/52 и
    # home (дублировал «Lock Screen» подзаголовка по смыслу, не по слову).
    "keywords": "christian,jesus,christ,daily,devotional,scripture,standby,affirmations,wallpapers,grief,quotes",
}

# ─────────────────────────────────────────────────────────── ES ──
L["es-ES"] = {
    # Только Испания: Латинскую Америку Apple показывает на es-MX (таблица App
    # Store localizations), поэтому для неё отдельная локаль ниже.
    "language": "Español (España)",
    # Astro (es): biblia 65/46 · citas 63/71 · widget 60/58 · diario 59/58
    # widgets 56/54 · esperanza 39/42 · fondos 27/55 · salmos 15/17
    # «oración» отброшена: молитвенника нет. «reina valera» 8/43 — наше издание.
    # 27.10, Astro (es): «citas» в Испании — запись на приём и свидания
    # (citas diarias 5), «sin conexión» 26/67 не взять. frases 27, fe 32,
    # jesus 24, devocional diario 25, ansiedad 16. Ключи без ударений: Astro
    # меряет «frases biblicas» 34 против 5 у «frases bíblicas».
    "name": "Biblia Widget: Frases de Fe",
    # 05.11 предлагали «Versículo del día y fondos», 07.11 откатили: Испания
    # растёт и так (frases de fe — 2-е место), а растущее не трогаем.
    "subtitle": "Versículo diario y fondos",
    "keywords": "esperanza,dios,jesus,ansiedad,biblicas,pantalla,devocional,reina,valera,salmos,lampada,evangelio,paz",
    "promo": "El versículo del día en tu pantalla de bloqueo, de inicio y en StandBy, y como notificación a la hora que elijas. Sin cuenta, sin anuncios, funciona sin conexión.",
    "sub_group": "Lampada Pro",
    "sub_week": "Lampada Pro · Semanal",
    "sub_month": "Lampada Pro · Mensual",
    "sub_year": "Lampada Pro · Anual",
    "shots": [
        "La Palabra en tu pantalla de bloqueo",
        "La pausa antes de deslizar",
        "Todos los tamaños, todas las pantallas",
        "Tu mesita de noche, en reposo",
        "Que se vea como tú",
        "Elige lo que necesitas hoy",
        "Un fondo que cambia solo",
    ],
    "description": """El teléfono es lo que más miras. Lampada pone ahí la Palabra: en las pantallas que ya miras y, si tú quieres, en el único momento en que preferirías no estar deslizando.

No es otra aplicación que abrir. Un versículo en la pantalla de bloqueo, en la de inicio y en tu mesita de noche mientras el teléfono carga. No hay que acordarse de nada: simplemente está ahí cada vez que bajas la mirada.

LA PAUSA ANTES DE DESLIZAR
Se activa en Lugares, con unos pocos toques. A partir de ahí, en el momento en que abres una red social, un versículo te recibe primero. No es otro muro que mirar: es una pausa real, justo donde ibas a empezar a deslizar. Es opcional y está desactivado si no lo pides.

DÓNDE APARECE LA PALABRA
- Pantalla de bloqueo: un versículo corto junto al reloj, en tres formas de widget
- Pantalla de inicio: tres tamaños de widget, de pequeño a grande
- StandBy: tu teléfono se convierte en pantalla de mesilla mientras carga
- Centro de control: un botón que abre el versículo de hoy (iOS 18)
- Fondo: guarda una imagen con el versículo y ponla de fondo

MIL VERSÍCULOS, OCHO TRADUCCIONES
Reina-Valera, World English Bible, Lutherbibel 1912, Louis Segond 1910, Bíblia Livre, Riveduta 1927, 개역한글 (coreano) y la traducción sinodal rusa. Todo dentro de la app y todo sin conexión.

ELIGE LO QUE NECESITAS HOY
Ansiedad. Pérdida. Gratitud. Perdón. Duda. Un comienzo difícil. Noches en vela. Dieciséis estados en total: marca los tuyos y los versículos se ajustarán.

CONTEXTO, NO SOLO UNA LÍNEA
Cientos de pasajes llevan una línea que dice quién habla y cuándo. No es comentario. Lo justo para que las palabras no queden en el aire.

HECHO PARA MIRARSE
Tipografía y color, nunca fotos de banco de imágenes. Ocho juegos de color, doce imágenes, nueve tipografías. Se ajustan por separado para la app, los widgets y la pantalla de bloqueo.

SILENCIOSO POR DISEÑO
Sin cuenta. Sin registro. Sin anuncios, nunca. Funciona totalmente sin conexión. El widget no da vueltas, no falla y no te pide nada.

GRATIS
El widget de la pantalla de bloqueo, el de inicio, el botón del centro de control, los versículos diarios, la pausa antes de deslizar, compartir sin marca de agua, cuatro juegos de color y una imagen.

LAMPADA PRO
StandBy, todas las imágenes, los ocho juegos de color, todas las tipografías e iconos de app a elegir.

Lampada Pro es una suscripción de renovación automática y se ofrece en tres duraciones: una semana, un mes y un año con los primeros 7 días gratis. El precio de tu región se muestra en la app antes de confirmar. El cobro se hace en tu cuenta de Apple y la suscripción se renueva sola salvo que desactives la renovación al menos 24 horas antes de que termine el periodo en curso. Puedes gestionarla o cancelarla cuando quieras en los ajustes de tu cuenta de Apple.

Condiciones de uso (EULA): https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
Política de privacidad: https://pmoffice.space/lampada-privacy.html

«Lámpara es a mis pies tu palabra, y lumbrera a mi camino». Salmo 119:105

Textos bíblicos: Reina-Valera, World English Bible, Lutherbibel 1912, Louis Segond 1910, Riveduta 1927, 개역한글, traducción sinodal rusa, todos de dominio público. Bíblia Livre © Diego Santos, Mario Sérgio, Marco Teles, CC BY 4.0 (creativecommons.org/licenses/by/4.0); puntuación final ajustada.""",
    "whatsnew": """Cinco iconos nuevos para la app: Vitral, Cruz, Navidad, Pascua y Paloma. La Paloma es gratis para todos.

Cuatro imágenes nuevas para tu versículo: Galilea, Estrella, Getsemaní y Cruz.

Lampada ya habla portugués, italiano y coreano, con la Bíblia Livre, la Riveduta 1927 y la 개역한글.

Notas de contexto más precisas en varios versículos y pequeñas correcciones.""",
}

# ─────────────────────────────────────────────────────────── ES-MX ──
# 27.10, Astro (mx/ar/co). Язык витрины всей Латинской Америки и второй
# индексируемый в США; до этого Латинская Америка видела английскую страницу,
# хотя приложение внутри испанское. MX: biblia 71/60, esperanza 56/21,
# versículo del día 48/36, ansiedad 42/41, biblia widget 40/39 (144-е место),
# frases biblicas 34/19, escritura 30/21. «Lampada» в названии не стоит
# (популярность 5) — бренд в ключах, место отдано под «versículo del día».
L["es-MX"] = {
    **L["es-ES"],
    "language": "Español (México) — вся Латинская Америка",
    # «Biblia: Versículo del Día» занято чужим приложением (409 от ASC при
    # создании локали 27.10) — те же слова в обратном порядке свободны.
    "name": "Versículo del Día: Biblia",
    # 05.11 предлагали «Frases bíblicas y esperanza» (esperanza 55/19), 07.11
    # откатили: до выхода правки Мексика выросла сама — 25 → 49 ключей в
    # выдаче, versículo del día 71 → 8, biblia widget 180 → 52. Эти места
    # держат как раз «widget» и «fondos» из подзаголовка — растущее не трогаем.
    "subtitle": "Widget, fondos y frases de fe",
    "keywords": "biblicas,escritura,esperanza,ansiedad,dios,jesus,reina,valera,pantalla,devocional,lampada,salmos,paz",
}

# ─────────────────────────────────────────────────────────── FR ──
L["fr-FR"] = {
    "language": "Français (France, Québec, Belgique, Suisse, Afrique francophone)",
    # Astro (fr): bible 69/60 · widget 68/68 · widgets 53/68
    # verset du jour 49/50 · christ 37/44 · quotidien 20/54
    # «Bible Widget : Verset du Jour» занято другим аккаунтом — порядок слов
    # перевёрнут, набор слов тот же. «prière» 17/68 отброшена.
    "name": "Verset du Jour : Bible Widget",
    # 27.10, Astro (fr): fond d'écran 66/68 — в метаданных его не было; hors
    # ligne 6/74 ничего не давал. catholique убран: канона и литургии нет,
    # обещание было бы ложным. louis segond 17/46 — наш перевод.
    "subtitle": "Fond d'écran chrétien, widgets",
    "keywords": "christ,dieu,louis,segond,biblique,citations,versets,psaumes,quotidien,évangile,jésus,lampada,paix",
    "promo": "Le verset du jour sur l'écran verrouillé, l'écran d'accueil et en StandBy, et en notification à l'heure choisie. Sans compte, sans pub, fonctionne hors ligne.",
    "sub_group": "Lampada Pro",
    "sub_week": "Lampada Pro · Hebdo",
    "sub_month": "Lampada Pro · Mensuel",
    "sub_year": "Lampada Pro · Annuel",
    "shots": [
        "La Parole sur votre écran verrouillé",
        "La pause avant le défilement",
        "Toutes les tailles, tous les écrans",
        "Votre table de chevet, au repos",
        "À votre image",
        "Choisissez ce dont vous avez besoin",
        "Un fond d'écran qui change seul",
    ],
    "description": """Le téléphone est ce que vous regardez le plus. Lampada y met la Parole : sur les écrans que vous regardez déjà et, si vous le voulez, dans le seul moment où vous préféreriez ne pas faire défiler.

Pas une application de plus à ouvrir. Un verset sur l'écran verrouillé, sur l'écran d'accueil et sur votre table de nuit pendant que le téléphone charge. Rien à retenir : il est simplement là, chaque fois que vous baissez les yeux.

LA PAUSE AVANT LE DÉFILEMENT
S'active dans Endroits, en quelques touches. Dès lors, au moment où vous ouvrez un réseau social, un verset vous accueille d'abord. Pas un autre fil à parcourir : une vraie pause, exactement là où vous auriez commencé à faire défiler. Entièrement facultatif, et désactivé tant que vous ne le demandez pas.

OÙ LA PAROLE APPARAÎT
- Écran verrouillé : un verset court près de l'horloge, en trois formes de widget
- Écran d'accueil : trois tailles de widget, de petite à grande
- StandBy : votre téléphone devient un écran de chevet pendant la charge
- Centre de contrôle : un bouton qui ouvre le verset du jour (iOS 18)
- Fond d'écran : enregistrez une image de verset et mettez-la en fond

MILLE VERSETS, HUIT TRADUCTIONS
Louis Segond 1910, World English Bible, Lutherbibel 1912, Reina-Valera, Bíblia Livre, Riveduta 1927, 개역한글 (coréen) et la traduction synodale russe. Tout est dans l'application, tout fonctionne hors ligne.

CHOISISSEZ CE QUI COMPTE AUJOURD'HUI
Anxiété. Deuil. Gratitude. Pardon. Doute. Un début difficile. Nuits sans sommeil. Seize états en tout : cochez les vôtres, et les versets suivront.

LE CONTEXTE, PAS SEULEMENT UNE LIGNE
Des centaines de passages portent une ligne indiquant qui parle et quand. Pas un commentaire. Juste assez pour que les mots ne restent pas en l'air.

FAIT POUR ÊTRE REGARDÉ
Typographie et couleur, jamais de photos de banque d'images. Huit jeux de couleurs, douze images, neuf polices. Réglables séparément pour l'application, les widgets et l'écran verrouillé.

SILENCIEUX PAR CONCEPTION
Pas de compte. Pas d'inscription. Jamais de publicité. Fonctionne entièrement hors ligne. Le widget ne tourne jamais, ne tombe jamais en panne et ne vous demande rien.

GRATUIT
Le widget de l'écran verrouillé, celui de l'écran d'accueil, le bouton du centre de contrôle, les versets du jour, la pause avant le défilement, le partage sans filigrane, quatre jeux de couleurs et une image.

LAMPADA PRO
StandBy, toutes les images, les huit jeux de couleurs, toutes les polices et des icônes d'application au choix.

Lampada Pro est un abonnement à renouvellement automatique, proposé en trois durées : une semaine, un mois et un an avec les 7 premiers jours offerts. Le prix applicable à votre région s'affiche dans l'app avant la confirmation. Le paiement est débité de votre compte Apple et l'abonnement se renouvelle automatiquement, sauf désactivation au moins 24 heures avant la fin de la période en cours. Vous pouvez le gérer ou le résilier à tout moment dans les réglages de votre compte Apple.

Conditions d'utilisation (CLUF) : https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
Politique de confidentialité : https://pmoffice.space/lampada-privacy.html

« Ta parole est une lampe à mes pieds, et une lumière sur mon sentier. » Psaume 119:105

Textes bibliques : Louis Segond 1910, World English Bible, Lutherbibel 1912, Reina-Valera, Riveduta 1927, 개역한글, traduction synodale russe, tous dans le domaine public. Bíblia Livre © Diego Santos, Mario Sérgio, Marco Teles, CC BY 4.0 (creativecommons.org/licenses/by/4.0) ; ponctuation finale ajustée.""",
    "whatsnew": """Cinq nouvelles icônes pour l'app : Vitrail, Croix, Noël, Pâques et Colombe. La Colombe est gratuite pour tous.

Quatre nouvelles images pour votre verset : Galilée, Étoile, Gethsémani et Croix.

Lampada parle désormais portugais, italien et coréen, avec la Bíblia Livre, la Riveduta 1927 et la 개역한글.

Des notes de contexte plus justes sur plusieurs versets, et quelques corrections.""",
}

# fr-CA: текст и название — как у fr-FR; «lampada» в ключах не нужен — он
# уже в названии en-CA, которое в Канаде индексируется тоже.
L["fr-CA"] = {
    **L["fr-FR"],
    "language": "Français (Canada)",
    "keywords": "dieu,citations,psaumes,louis,segond,biblique,versets,évangile,paix,espoir,quotidien,parole,proverbes",
}

# ─────────────────────────────────────────────────────────── DE ──
L["de-DE"] = {
    "language": "Deutsch (Deutschland, Österreich, Schweiz)",
    # Astro (de): bibel 66/54 · widget 62/64 · hintergrundbilder 61/65
    # offline 61/69 · widgets 57/62 · jesus 36/46 · hintergrund 37/57
    # «gebet» 19/62 отброшено: молитвенника нет.
    "name": "Bibel Widget: Vers des Tages",
    # 27.10, Astro (de): lockscreen 33/47 в подзаголовок, offline уходит в
    # ключи. luther + «Bibel» из названия собирают «luther bibel» 30/21 — наш
    # Luther 1912. losung убран: Herrnhuter Losungen в приложении нет.
    "subtitle": "Lockscreen & Hintergrundbilder",
    "keywords": "luther,offline,widgets,jesus,gott,christlich,sperrbildschirm,zitate,hintergrund,sprüche,lampada",
    "promo": "Der Vers des Tages auf Sperrbildschirm, Home-Bildschirm und in StandBy und als Mitteilung zur gewählten Zeit. Ohne Konto, ohne Werbung, auch offline.",
    "sub_group": "Lampada Pro",
    "sub_week": "Lampada Pro · Wöchentlich",
    "sub_month": "Lampada Pro · Monatlich",
    "sub_year": "Lampada Pro · Jährlich",
    "shots": [
        "Das Wort auf deinem Sperrbildschirm",
        "Die Pause vor dem Scrollen",
        "Jede Widget-Größe, jeder Bildschirm",
        "Dein Nachttisch, zur Ruhe gekommen",
        "Ganz nach deinem Geschmack",
        "Wähle, was du heute brauchst",
        "Ein Hintergrund, der sich selbst wechselt",
    ],
    "description": """Das Handy ist das, worauf du am häufigsten schaust. Lampada legt das Wort genau dorthin: auf die Bildschirme, auf die du ohnehin schaust, und, wenn du willst, in den einen Moment, in dem du lieber nicht scrollen würdest.

Keine weitere App zum Öffnen. Ein Vers auf dem Sperrbildschirm, auf dem Home-Bildschirm und auf deinem Nachttisch, während das Handy lädt. Du musst an nichts denken — er ist einfach da, jedes Mal, wenn du hinunterblickst.

DIE PAUSE VOR DEM SCROLLEN
Wird unter „Orte“ mit wenigen Tippen aktiviert. Von da an empfängt dich in dem Moment, in dem du eine Social-App öffnest, zuerst ein Vers. Kein Feed als Ersatz, sondern eine echte Pause genau dort, wo du zu scrollen begonnen hättest. Vollkommen optional und aus, solange du nicht danach fragst.

WO DAS WORT ERSCHEINT
- Sperrbildschirm: ein kurzer Vers neben der Uhr, in drei Widget-Formen
- Home-Bildschirm: drei Widget-Größen, von klein bis groß
- StandBy: dein Handy wird beim Laden zum Nachttischdisplay
- Kontrollzentrum: eine Taste, die den heutigen Vers öffnet (ab iOS 18)
- Hintergrundbild: Vers-Bild sichern und als Hintergrund einstellen

TAUSEND VERSE, ACHT ÜBERSETZUNGEN
Lutherbibel 1912, World English Bible, Louis Segond 1910, Reina-Valera, Bíblia Livre, Riveduta 1927, 개역한글 (koreanisch) und die russische Synodalübersetzung. Alles in der App, alles offline.

WÄHLE, WAS HEUTE ZÄHLT
Unruhe. Verlust. Dankbarkeit. Vergebung. Zweifel. Ein schwerer Anfang. Schlaflose Nächte. Sechzehn Zustände insgesamt: markiere deine, und die Verse richten sich danach.

KONTEXT, NICHT NUR EINE ZEILE
Hunderte Stellen tragen eine Zeile dazu, wer spricht und wann. Keine Auslegung. Gerade so viel, dass die Worte nicht in der Luft hängen.

ZUM ANSCHAUEN GEMACHT
Schrift und Farbe, keine Stockfotos. Acht Farbsets, zwölf Bilder, neun Schriften. Getrennt einstellbar für die App, für die Widgets und für den Sperrbildschirm.

STILL VON GRUND AUF
Kein Konto. Keine Anmeldung. Niemals Werbung. Funktioniert vollständig offline. Das Widget dreht sich nie, fällt nie aus und verlangt nichts von dir.

KOSTENLOS
Das Sperrbildschirm-Widget, das Home-Bildschirm-Widget, die Taste im Kontrollzentrum, die Tagesverse, die Pause vor dem Scrollen, das Teilen ohne Wasserzeichen, vier Farbsets und ein Bild.

LAMPADA PRO
StandBy, alle Bilder, alle acht Farbsets, alle Schriften und App-Symbole zur Auswahl.

Lampada Pro ist ein Abo mit automatischer Verlängerung und wird in drei Laufzeiten angeboten: eine Woche, ein Monat und ein Jahr mit den ersten 7 Tagen gratis. Der für deine Region geltende Preis steht in der App, bevor du bestätigst. Die Zahlung läuft über deinen Apple-Account, und das Abo verlängert sich automatisch, sofern du die Verlängerung nicht mindestens 24 Stunden vor Ende des laufenden Zeitraums deaktivierst. Verwalten oder kündigen kannst du es jederzeit in den Einstellungen deines Apple-Accounts.

Nutzungsbedingungen (EULA): https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
Datenschutzrichtlinie: https://pmoffice.space/lampada-privacy.html

„Dein Wort ist meines Fußes Leuchte und ein Licht auf meinem Wege." Psalm 119,105

Bibeltexte: Lutherbibel 1912, World English Bible, Louis Segond 1910, Reina-Valera, Riveduta 1927, 개역한글, russische Synodalübersetzung, alle gemeinfrei. Bíblia Livre © Diego Santos, Mario Sérgio, Marco Teles, CC BY 4.0 (creativecommons.org/licenses/by/4.0); Satzzeichen am Versende angepasst.""",
    "whatsnew": """Fünf neue App-Symbole: Buntglas, Kreuz, Weihnachten, Ostern und Taube. Die Taube ist für alle kostenlos.

Vier neue Bilder für deinen Vers: Galiläa, Stern, Gethsemane und Kreuz.

Lampada spricht jetzt auch Portugiesisch, Italienisch und Koreanisch, mit der Bíblia Livre, der Riveduta 1927 und der 개역한글.

Genauere Kontextzeilen bei einigen Versen und kleine Korrekturen.""",
}

# ─────────────────────────────────────────────── PT-BR / PT-PT / IT ──
# 07.11: новые языки (docs/new-languages.md). Внутри приложения один
# португальский — бразильский, с Bíblia Livre; витрин две. Тексты описаний
# переведены с en-US/es-ES, факты те же.
# 07.11, Astro (br): versículo do dia 49/45, bíblia widget 39/41, frases
# bíblicas 41/54, papel de parede 57/63, palavra do dia 33/51, palavra de deus
# 25/23, devocional 49/50, tela de bloqueio 37/61, standby 21/13. «Bíblia
# Sagrada» 74/71 не взять. «Versículo do Dia: Bíblia» занято другим аккаунтом
# (409 при создании локали) — взяли имя издания: Bíblia Livre ещё и читается
# как «свободная Библия». «almeida» 24/11 не берём: у нас не Алмейда.
# «católica» тоже: канона и литургии нет.
L["pt-BR"] = {
    "language": "Português (Brasil)",
    "name": "Versículo do Dia: Bíblia Livre",
    "subtitle": "Widget e frases bíblicas",
    "keywords": "papel,parede,palavra,deus,salmos,devocional,tela,bloqueio,standby,paz,ansiedade,luto,offline,lampada",
    "promo": "O versículo do dia na Tela Bloqueada, na Tela de Início e no StandBy, e como notificação no horário que você escolher. Sem conta, sem anúncios, funciona offline.",
    "sub_group": "Lampada Pro",
    "sub_week": "Lampada Pro · Semanal",
    "sub_month": "Lampada Pro · Mensal",
    "sub_year": "Lampada Pro · Anual",
    "shots": [
        "A Palavra na sua Tela Bloqueada",
        "A pausa antes do feed",
        "Todos os tamanhos, todas as telas",
        "Sua mesa de cabeceira, em repouso",
        "Deixe com a sua cara",
        "Escolha do que você precisa hoje",
        "Imagem de fundo que muda sozinha",
    ],
    "description": """O celular é o que você mais olha. Lampada coloca a Palavra ali: nas telas que você já olha e, se quiser, naquele único momento em que você preferiria não estar rolando o feed.

Não é mais um app para abrir. Um versículo na Tela Bloqueada, na Tela de Início e na mesa de cabeceira enquanto o celular carrega. Nada para lembrar. Ele simplesmente está lá, toda vez que você baixa os olhos.

A PAUSA ANTES DO FEED
Você ativa em “Lugares”, com poucos toques. A partir daí, no momento em que você abre uma rede social, um versículo vem primeiro ao seu encontro. Não é outro feed para percorrer: é uma pausa de verdade, bem na hora em que você começaria a rolar a tela. Totalmente opcional e desativada, a menos que você peça.

ONDE A PALAVRA APARECE
- Tela Bloqueada: um versículo curto ao lado do relógio, em três formatos de widget
- Tela de Início: três tamanhos de widget, do pequeno ao grande
- StandBy: o celular vira uma tela de cabeceira enquanto carrega
- Central de Controle: um botão que abre o versículo de hoje (iOS 18)
- Imagem de fundo: salve uma imagem com o versículo e use-a como fundo da tela

MIL VERSÍCULOS, OITO TRADUÇÕES
Bíblia Livre, World English Bible, Lutherbibel 1912, Louis Segond 1910, Reina-Valera, Riveduta 1927, 개역한글 (coreana) e a tradução sinodal russa. Tudo dentro do app, tudo offline.

ESCOLHA DO QUE VOCÊ PRECISA HOJE
Ansiedade. Perda. Gratidão. Perdão. Dúvida. Começar algo difícil. Noites sem dormir. São dezesseis estados de espírito ao todo: escolha os que importam agora, e os versículos acompanham.

CONTEXTO, NÃO SÓ UMA FRASE
Centenas de passagens trazem uma linha dizendo quem está falando e quando. Não é comentário. Só o suficiente para que as palavras não fiquem soltas no ar.

FEITO PARA SER VISTO
Tipografia e cor, nunca fotos de banco de imagens. Oito conjuntos de cores, doze imagens, nove fontes. Tudo isso se ajusta separadamente para o app, para os widgets e para a Tela Bloqueada.

SILENCIOSO DE PROPÓSITO
Sem conta. Sem cadastro. Sem anúncios, nunca. Funciona totalmente offline. O widget nunca fica carregando, nunca falha, nunca pede nada a você.

GRÁTIS
O widget da Tela Bloqueada, o widget da Tela de Início, o botão da Central de Controle, os versículos diários, a pausa antes do feed, compartilhar sem marca d’água, quatro conjuntos de cores e uma imagem.

LAMPADA PRO
StandBy, todas as imagens, os oito conjuntos de cores, todas as fontes e ícones do app à sua escolha.

Lampada Pro é uma assinatura com renovação automática e tem três durações: uma semana, um mês e um ano com os primeiros 7 dias grátis. O preço para o seu país ou região aparece no app antes de você confirmar. O pagamento é cobrado na sua Conta Apple, e a assinatura é renovada automaticamente, a menos que você desative a renovação automática pelo menos 24 horas antes do fim do período atual. Gerencie ou cancele quando quiser nos ajustes da sua Conta Apple.

Termos de Uso (EULA): https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
Política de Privacidade: https://pmoffice.space/lampada-privacy.html

“Tua palavra é lâmpada para meus pés e luz para meu caminho.” Salmo 119:105

Textos bíblicos: World English Bible, Lutherbibel 1912, Louis Segond 1910, Reina-Valera, Riveduta 1927, 개역한글 e a tradução sinodal russa, todos em domínio público. Bíblia Livre © Diego Santos, Mario Sérgio, Marco Teles, CC BY 4.0 (creativecommons.org/licenses/by/4.0); pontuação final ajustada.""",
    "whatsnew": """Agora em português: o app inteiro e mil versículos da Bíblia Livre, também nos widgets e na Tela Bloqueada.

Cinco ícones novos: Vitral, Cruz, Natal, Páscoa e Pomba. A Pomba é grátis para todos.

Quatro imagens novas para o seu versículo: Galileia, Estrela, Getsêmani e Cruz.

Também chegaram o italiano e o coreano.

E pequenas correções.""",
}

# 07.11, Astro (pt): рынок маленький, почти всё — популярность 5. Живые
# запросы: bíblia sagrada 67/45 (в подзаголовке), biblia 59/45, widget 57/52,
# ansiedade 30/46, papel de parede 28/43, devocional 27/21. Лексика
# европейская: ecrã, ecrã de bloqueio, telemóvel. Приложение внутри — то же
# бразильское pt.
L["pt-PT"] = {
    "language": "Português (Portugal)",
    "name": "Versículo do Dia: Bíblia Livre",
    "subtitle": "Widget da Bíblia Sagrada",
    "keywords": "devocional,ansiedade,papel,parede,ecrã,bloqueio,frases,bíblicas,salmos,palavra,deus,lampada",
    "promo": "O versículo do dia no ecrã bloqueado, no ecrã principal e no StandBy, e como notificação à hora que escolheres. Sem conta, sem anúncios, funciona offline.",
    "sub_group": "Lampada Pro",
    "sub_week": "Lampada Pro · Semanal",
    "sub_month": "Lampada Pro · Mensal",
    "sub_year": "Lampada Pro · Anual",
    "shots": [
        "A Palavra no teu ecrã bloqueado",
        "A pausa antes do feed",
        "Todos os tamanhos, todos os ecrãs",
        "A tua mesa de cabeceira, em repouso",
        "Ao teu estilo",
        "Escolhe aquilo de que precisas hoje",
        "Um fundo de ecrã que muda sozinho",
    ],
    "description": """O telemóvel é aquilo para onde mais olhas. Lampada põe lá a Palavra: nos ecrãs para onde já olhas e, se quiseres, naquele único momento em que preferias não estar a percorrer o feed.

Não é mais uma app para abrir. Um versículo no ecrã bloqueado, no ecrã principal e na mesa de cabeceira enquanto o telemóvel carrega. Nada para te lembrares. Está simplesmente lá, sempre que baixas os olhos.

A PAUSA ANTES DO FEED
Ativa-a em “Lugares”, com poucos toques. A partir daí, no momento em que abres uma rede social, é um versículo que te recebe primeiro. Não é outro feed para percorrer: é uma pausa a sério, exatamente no instante em que ias começar a deslizar o ecrã. Totalmente opcional e desativada, a não ser que a peças.

ONDE A PALAVRA APARECE
- Ecrã bloqueado: um versículo curto junto ao relógio, em três formatos de widget
- Ecrã principal: três tamanhos de widget, do pequeno ao grande
- StandBy: o telemóvel transforma-se num ecrã de cabeceira enquanto carrega
- Centro de controlo: um botão que abre o versículo de hoje (iOS 18)
- Fundo de ecrã: guarda uma imagem com o versículo e define-a como fundo

MIL VERSÍCULOS, OITO TRADUÇÕES
Bíblia Livre, World English Bible, Lutherbibel 1912, Louis Segond 1910, Reina-Valera, Riveduta 1927, 개역한글 (coreana) e a tradução sinodal russa. Tudo dentro da app, tudo offline.

ESCOLHE AQUILO DE QUE PRECISAS HOJE
Ansiedade. Perda. Gratidão. Perdão. Dúvida. Começar algo difícil. Noites em branco. Dezasseis estados de espírito ao todo: escolhe os que importam agora e os versículos acompanham.

CONTEXTO, NÃO APENAS UMA FRASE
Centenas de passagens trazem uma linha que diz quem está a falar e quando. Não é um comentário. Apenas o suficiente para que as palavras não fiquem soltas no ar.

FEITO PARA SER VISTO
Tipografia e cor, nunca fotografias de banco de imagens. Oito conjuntos de cores, doze imagens, nove tipos de letra. Configura-os separadamente para a app, para os widgets e para o ecrã bloqueado.

SILENCIOSO DE PROPÓSITO
Sem conta. Sem registo. Sem anúncios, nunca. Funciona totalmente offline. O widget nunca fica a carregar, nunca falha, nunca te pede nada.

GRATUITO
O widget do ecrã bloqueado, o widget do ecrã principal, o botão do Centro de controlo, os versículos diários, a pausa antes do feed, partilhar sem marca de água, quatro conjuntos de cores e uma imagem.

LAMPADA PRO
StandBy, todas as imagens, os oito conjuntos de cores, todos os tipos de letra e ícones da app à escolha.

Lampada Pro é uma subscrição com renovação automática e está disponível em três durações: uma semana, um mês e um ano com os primeiros 7 dias grátis. O preço para o teu país ou região é apresentado na app antes de confirmares. O pagamento é cobrado na tua Conta Apple e a subscrição renova-se automaticamente, a menos que desatives a renovação automática pelo menos 24 horas antes do fim do período em curso. Podes geri-la ou cancelá-la a qualquer momento nas definições da tua Conta Apple.

Termos de Utilização (EULA): https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
Política de Privacidade: https://pmoffice.space/lampada-privacy.html

“Tua palavra é lâmpada para meus pés e luz para meu caminho.” Salmo 119:105

Textos bíblicos: World English Bible, Lutherbibel 1912, Louis Segond 1910, Reina-Valera, Riveduta 1927, 개역한글 e a tradução sinodal russa, todos em domínio público. Bíblia Livre © Diego Santos, Mario Sérgio, Marco Teles, CC BY 4.0 (creativecommons.org/licenses/by/4.0); pontuação final ajustada.""",
    "whatsnew": """Agora em português: a app inteira e mil versículos da Bíblia Livre, também nos widgets e no ecrã bloqueado.

Cinco ícones novos: Vitral, Cruz, Natal, Páscoa e Pomba. A Pomba é gratuita para todos.

Quatro imagens novas para o teu versículo: Galileia, Estrela, Getsêmani e Cruz.

Chegaram também o italiano e o coreano.

E pequenas correções.""",
}

# 07.11, Astro (it): bibbia 57/23, la bibbia 45/23, versetto del giorno
# 27/15, bibbia widget 29/13, vangelo 32/13, parola del giorno 35/40, frase
# del giorno 26/41, sfondi 56/53, widget 65/57, ansia 36/39, standby 25/19.
# «Bibbia: Versetto del Giorno» занято (John Harvey) — слова переставлены.
# «Vangelo» только в ключах: литургического «Vangelo del giorno» у нас нет.
# «lampada» по-итальянски — просто «лампа» (25/35, мы уже 63-и).
L["it"] = {
    "language": "Italiano",
    "name": "Versetto del Giorno: Bibbia",
    "subtitle": "Widget e sfondi cristiani",
    "keywords": "parola,frase,vangelo,salmi,standby,pace,ansia,speranza,gesù,dio,citazioni,lampada,offline",
    "promo": "Il versetto del giorno sulla schermata di blocco, sulla schermata Home e in StandBy, e come notifica all’ora che scegli. Senza account né pubblicità, funziona offline.",
    "sub_group": "Lampada Pro",
    "sub_week": "Lampada Pro · Settimanale",
    "sub_month": "Lampada Pro · Mensile",
    "sub_year": "Lampada Pro · Annuale",
    "shots": [
        "La Parola sulla schermata di blocco",
        "La pausa prima del feed",
        "Ogni dimensione, ogni schermata",
        "Il tuo comodino, a riposo",
        "A modo tuo",
        "Scegli ciò di cui hai bisogno oggi",
        "Uno sfondo che cambia da solo",
    ],
    "description": """Il telefono è la cosa che guardi di più. Lampada ci mette la Parola: sugli schermi che guardi già e, se lo vuoi, in quell’unico momento in cui preferiresti non scorrere il feed.

Non un’altra app da aprire. Un versetto sulla schermata di blocco, sulla schermata Home e sul comodino mentre il telefono è in carica. Niente da ricordare. È semplicemente lì, ogni volta che abbassi lo sguardo.

LA PAUSA PRIMA DEL FEED
Si attiva in «Luoghi», con pochi tocchi. Da quel momento, quando apri un social, ad accoglierti c’è prima un versetto. Non un altro feed da sfogliare: una pausa vera, proprio nell’istante in cui avresti iniziato a scorrere. Del tutto facoltativa, e disattivata finché non la chiedi tu.

DOVE APPARE LA PAROLA
- Schermata di blocco: un versetto breve accanto all’orologio, in tre forme di widget
- Schermata Home: tre dimensioni di widget, dalla piccola alla grande
- StandBy: il telefono diventa un display da comodino mentre è in carica
- Centro di Controllo: un pulsante che apre il versetto di oggi (iOS 18)
- Sfondo: salva un’immagine con il versetto e impostala come sfondo

MILLE VERSETTI, OTTO TRADUZIONI
Riveduta 1927, World English Bible, Lutherbibel 1912, Louis Segond 1910, Reina-Valera, Bíblia Livre, 개역한글 (coreana) e la traduzione sinodale russa. Tutto dentro l’app, tutto offline.

SCEGLI CIÒ DI CUI HAI BISOGNO OGGI
Ansia. Lutto. Gratitudine. Perdono. Dubbio. Iniziare qualcosa di difficile. Notti insonni. Sedici stati d’animo in tutto: scegli quelli che contano adesso, e i versetti ti seguono.

CONTESTO, NON SOLO UNA RIGA
Centinaia di passi riportano una riga che ti dice chi sta parlando e quando. Non è un commento. Quanto basta perché le parole non restino sospese nel vuoto.

FATTO PER ESSERE GUARDATO
Tipografia e colore, mai foto di repertorio. Otto set di colori, dodici immagini, nove font. Si impostano separatamente per l’app, per i widget e per la schermata di blocco.

SILENZIOSO PER SCELTA
Nessun account. Nessuna registrazione. Nessuna pubblicità, mai. Funziona completamente offline. Il widget non resta mai in caricamento, non si blocca mai, non ti chiede mai niente.

GRATIS
Il widget della schermata di blocco, il widget della schermata Home, il pulsante del Centro di Controllo, i versetti del giorno, la pausa prima del feed, la condivisione senza filigrana, quattro set di colori e un’immagine.

LAMPADA PRO
StandBy, tutte le immagini, tutti e otto i set di colori, tutti i font e le icone dell’app a scelta.

Lampada Pro è un abbonamento a rinnovo automatico ed è disponibile in tre durate: una settimana, un mese e un anno con i primi 7 giorni gratis. Il prezzo per il tuo Paese o la tua regione viene mostrato nell’app prima che tu confermi. Il pagamento viene addebitato sul tuo Account Apple e l’abbonamento si rinnova automaticamente, a meno che tu non disattivi il rinnovo automatico almeno 24 ore prima della fine del periodo in corso. Puoi gestirlo o annullarlo in qualsiasi momento nelle impostazioni del tuo Account Apple.

Termini d’uso (EULA): https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
Informativa sulla privacy: https://pmoffice.space/lampada-privacy.html

«La tua parola è una lampada al mio piè ed una luce sul mio sentiero». Salmo 119:105

Testi biblici: Riveduta 1927, World English Bible, Lutherbibel 1912, Louis Segond 1910, Reina-Valera, 개역한글 e la traduzione sinodale russa, tutti di pubblico dominio. Bíblia Livre © Diego Santos, Mario Sérgio, Marco Teles, CC BY 4.0 (creativecommons.org/licenses/by/4.0); punteggiatura finale adattata.""",
    "whatsnew": """Ora in italiano: l’app intera e mille versetti della Riveduta 1927, anche nei widget e sulla schermata di blocco.

Cinque nuove icone: Vetrata, Croce, Natale, Pasqua e Colomba. La Colomba è gratis per tutti.

Quattro nuove immagini per il tuo versetto: Galilea, Stella, Getsemani e Croce.

Sono arrivati anche il portoghese e il coreano.

E qualche piccola correzione.""",
}

# 07.11, Astro (kr): 성경 72/43, 성경 위젯 27/17, 오늘의 말씀 28/23, 큐티 46/38,
# 개역한글 30/19 (наше издание), 스탠바이 33/21, 위로 34/13, 예수님 27/5,
# 배경화면 64/53, 잠금화면 37/54. «성경 위젯: 오늘의 말씀» занято — слова
# переставлены. 기도 41/35, 교회 41/21 и 성경책 57/35 не берём: молитв,
# церкви и полного текста Библии в приложении нет.
L["ko"] = {
    "language": "한국어",
    "name": "오늘의 말씀: 성경 위젯",
    "subtitle": "개역한글 · 잠금화면 · 스탠바이",
    "keywords": "성경구절,큐티,묵상,위로,예수님,기독교,배경화면,감사,시편,매일,구절,평안,소망,하나님,크리스천,말씀카드,홈화면,오프라인,불안,lampada",
    "promo": "오늘의 말씀을 잠금 화면, 홈 화면, 스탠바이에서 만나고, 원하는 시간에 알림으로도 받아 보세요. 계정도 광고도 없고, 오프라인에서도 작동해요.",
    "sub_group": "Lampada Pro",
    "sub_week": "Lampada Pro · 주간",
    "sub_month": "Lampada Pro · 월간",
    "sub_year": "Lampada Pro · 연간",
    "shots": [
        "잠금 화면 위의 말씀",
        "스크롤 전, 잠시 멈춤",
        "모든 위젯 크기, 모든 화면",
        "고요한 머리맡",
        "나만의 스타일로",
        "오늘 필요한 말씀을 골라 보세요",
        "스스로 바뀌는 배경화면",
    ],
    "description": """하루 중 가장 많이 보는 건 휴대폰이에요. Lampada는 바로 그곳에 말씀을 담아요. 이미 늘 보는 화면에, 그리고 원한다면 스크롤하지 않았으면 하는 바로 그 순간에도요.

열어야 할 앱이 하나 더 생기는 게 아니에요. 잠금 화면과 홈 화면에, 충전하는 동안에는 머리맡에 말씀 한 구절이 있어요. 기억해야 할 것도 없어요. 휴대폰을 내려다볼 때마다 그냥 그 자리에 있어요.

스크롤 전, 잠시 멈춤
‘장소’에서 몇 번만 탭하면 켤 수 있어요. 그다음부터는 소셜 앱을 여는 순간 말씀 한 구절이 먼저 반겨 줘요. 대신 둘러볼 또 하나의 피드가 아니라, 스크롤을 시작하려던 바로 그 순간에 찾아오는 진짜 멈춤이에요. 완전히 선택 사항이고, 직접 켜기 전에는 꺼져 있어요.

말씀이 보이는 곳
- 잠금 화면: 시계 옆의 짧은 말씀, 세 가지 형태의 위젯
- 홈 화면: 소형부터 대형까지 세 가지 크기의 위젯
- 스탠바이: 충전하는 동안 휴대폰이 머리맡 디스플레이가 돼요
- 제어 센터: 오늘의 말씀을 여는 버튼(iOS 18)
- 배경화면: 말씀 이미지를 저장해 배경화면으로 설정할 수 있어요

천 개의 말씀, 여덟 가지 역본
개역한글, World English Bible, Lutherbibel 1912, Louis Segond 1910, Reina-Valera, Bíblia Livre, Riveduta 1927, 러시아 시노달 역본. 모두 앱 안에 담겨 있고, 모두 오프라인으로 읽을 수 있어요.

오늘 필요한 말씀을 골라 보세요
불안. 상실. 감사. 용서. 의심. 어려운 일의 시작. 잠 못 드는 밤. 모두 열여섯 가지 마음 상태가 있어요. 지금 중요한 것을 고르면 그에 맞는 말씀이 찾아와요.

구절만이 아니라 맥락까지
수백 개의 구절에는 누가, 언제 한 말인지 알려 주는 설명 한 줄이 붙어 있어요. 주석은 아니에요. 말씀이 맥락 없이 떠다니지 않을 만큼만 담았어요.

보기 좋게 만든 디자인
스톡 사진 대신 타이포그래피와 색으로 만들었어요. 색상 세트 여덟 가지, 이미지 열두 가지, 서체 아홉 가지. 앱, 위젯, 잠금 화면에 각각 따로 설정할 수 있어요.

처음부터 조용하게
계정도, 가입도 필요 없어요. 광고는 앞으로도 절대 없어요. 완전히 오프라인으로 작동해요. 위젯은 로딩 표시가 도는 일도, 오류가 나는 일도, 무언가를 요구하는 일도 없어요.

무료
잠금 화면 위젯, 홈 화면 위젯, 제어 센터 버튼, 매일의 말씀, 스크롤 전 잠시 멈춤, 워터마크 없는 공유, 색상 세트 네 가지와 이미지 한 가지.

Lampada Pro
스탠바이, 모든 이미지, 색상 세트 여덟 가지 전부, 모든 서체, 그리고 앱 아이콘 선택.

Lampada Pro는 자동 갱신 구독으로, 1주, 1개월, 그리고 처음 7일이 무료인 1년, 이렇게 세 가지 기간이 있어요. 해당 지역의 가격은 구매를 확인하기 전에 앱에 표시돼요. 결제 금액은 Apple 계정으로 청구되고, 현재 기간이 끝나기 최소 24시간 전에 자동 갱신을 끄지 않으면 구독이 자동으로 갱신돼요. 언제든지 Apple 계정 설정에서 구독을 관리하거나 취소할 수 있어요.

이용약관(EULA): https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
개인정보 처리방침: https://pmoffice.space/lampada-privacy.html

“주의 말씀은 내 발에 등이요 내 길에 빛이니이다” 시편 119:105

성경 본문: 개역한글, World English Bible, Lutherbibel 1912, Louis Segond 1910, Reina-Valera, Riveduta 1927, 러시아 시노달 역본은 모두 퍼블릭 도메인이에요. Bíblia Livre © Diego Santos, Mario Sérgio, Marco Teles, CC BY 4.0 (creativecommons.org/licenses/by/4.0); 구절 끝의 문장 부호를 조정했어요.""",
    "whatsnew": """이제 한국어를 지원해요. 앱 화면 전체와 개역한글 말씀 천 구절을 위젯과 잠금 화면에서도 볼 수 있어요.

새 아이콘 다섯 개: 스테인드글라스, 십자가, 성탄절, 부활절, 비둘기. 비둘기는 모두에게 무료예요.

말씀 배경으로 쓸 새 그림 네 점: 갈릴리, 별, 겟세마네, 십자가.

포르투갈어와 이탈리아어도 추가됐어요.

그 밖에 자잘한 문제를 고쳤어요.""",
}

# ─────────────────────────────────────────────────────────── RU ──
L["ru"] = {
    "language": "Русский (диаспора: Германия, Израиль, США, Казахстан, Балтия)",
    # Astro (ru): виджеты 63/63 · обои 57/67 · виджет 53/68 · библия 52/41
    # офлайн 40/68 · бог 31/51 · евангелие 28/44 · цитаты 25/39 · стихи 24/21
    # «библия» здесь редкий случай: высокая частота при низкой сложности.
    "name": "Библия: виджеты и стих дня",
    "subtitle": "Обои и стихи, работает офлайн",
    "keywords": "бог,евангелие,цитаты,псалмы,вера,иисус,христос,православие,завет,экран,блокировки,lampada,заставка",
    "promo": "Слово на каждом экране. И, если захотите, стих, который встречает вас в момент открытия соцсети: пауза перед лентой.",
    "sub_group": "Lampada Pro",
    "sub_week": "Lampada Pro · Неделя",
    "sub_month": "Lampada Pro · Месяц",
    "sub_year": "Lampada Pro · Год",
    "shots": [
        "Слово на экране блокировки",
        "Пауза перед лентой",
        "Все размеры, все экраны",
        "Тумбочка у кровати, в покое",
        "Чтобы выглядело по-твоему",
        "Выберите, что нужно сегодня",
        "Обои, которые меняются сами",
    ],
    "description": """Телефон — то, на что вы смотрите чаще всего. Lampada кладёт Слово именно туда: на экраны, куда вы и так смотрите, и, если захотите, в ту единственную минуту, когда лучше бы не листать.

Это не ещё одно приложение, которое надо открывать. Стих на экране блокировки, на рабочем столе и на тумбочке, пока телефон заряжается. Помнить ни о чём не нужно — он просто есть каждый раз, когда вы опускаете глаза.

ПАУЗА ПЕРЕД ЛЕНТОЙ
Включается в «Местах», в несколько касаний. Дальше в момент, когда вы открываете соцсеть, первым вас встречает стих. Не другая лента взамен — настоящая пауза ровно там, где вы начали бы листать. Функция необязательная и выключена, пока вы сами её не попросите.

ГДЕ ПОЯВЛЯЕТСЯ СЛОВО
- Экран блокировки: короткий стих рядом с часами, в трёх формах виджета
- Рабочий стол: три размера виджета, от маленького до большого
- StandBy: телефон становится прикроватным экраном на зарядке
- Пункт управления: кнопка, открывающая стих дня (нужна iOS 18)
- Обои: сохраните картинку со стихом и поставьте её фоном

ТЫСЯЧА СТИХОВ, ВОСЕМЬ ИЗДАНИЙ
Синодальный перевод, World English Bible, Lutherbibel 1912, Louis Segond 1910, Reina-Valera, Bíblia Livre, Riveduta 1927 и 개역한글 (корейский). Всё внутри приложения и всё офлайн.

ВЫБЕРИТЕ ТО, ЧТО СЕЙЧАС
Тревога. Утрата. Благодарность. Прощение. Сомнение. Начало трудного дела. Бессонные ночи. Всего шестнадцать состояний: отметьте свои — стихи подберутся под них.

КОНТЕКСТ, А НЕ ПРОСТО СТРОКА
У сотен отрывков есть одна строка о том, кто это говорит и когда. Не толкование. Ровно столько, чтобы слова не повисли в воздухе.

СДЕЛАНО, ЧТОБЫ НА ЭТО СМОТРЕЛИ
Шрифт и цвет, никаких стоковых фотографий. Восемь наборов цвета, двенадцать картинок, девять шрифтов. Настраиваются отдельно для приложения, для виджетов и для экрана блокировки.

ТИХОЕ ПО УСТРОЙСТВУ
Без аккаунта. Без регистрации. Без рекламы — никогда. Работает полностью офлайн. Виджет не крутит спиннер, не отваливается и ничего у вас не просит.

БЕСПЛАТНО
Виджет на экране блокировки, виджет на рабочем столе, кнопка в Пункте управления, стих дня, пауза перед лентой, публикация без водяного знака, четыре набора цвета и одна картинка.

LAMPADA PRO
StandBy, все картинки, все восемь наборов цвета, все шрифты и иконки приложения на выбор.

Lampada Pro — подписка с автопродлением, есть три срока: неделя, месяц и год с первыми 7 днями бесплатно. Цена для вашего региона показана в приложении до подтверждения. Оплата списывается с аккаунта Apple, подписка продлевается сама, если не отключить автопродление не позже чем за 24 часа до конца текущего срока. Управлять ею и отменить можно в любой момент в настройках аккаунта Apple.

Условия использования (EULA): https://www.apple.com/legal/internet-services/itunes/dev/stdeula/
Политика конфиденциальности: https://pmoffice.space/lampada-privacy.html

«Слово Твоё — светильник ноге моей и свет стезе моей». Псалом 118:105

Тексты Писания: Синодальный перевод, World English Bible, Lutherbibel 1912, Louis Segond 1910, Reina-Valera, Riveduta 1927, 개역한글 — в общественном достоянии. Bíblia Livre © Diego Santos, Mario Sérgio, Marco Teles, CC BY 4.0 (creativecommons.org/licenses/by/4.0); знаки в конце стиха исправлены.""",
    "whatsnew": """Пять новых иконок приложения: Витраж, Крест, Рождество, Пасха и Голубь. Голубь — бесплатно для всех.

Четыре новые картинки для стиха: Галилея, Звезда, Гефсимания и Крест.

Lampada теперь говорит на португальском, итальянском и корейском — с переводами Bíblia Livre, Riveduta 1927 и 개역한글.

Уточнили пояснения к нескольким стихам и исправили мелкие ошибки.""",
}


def check(label, value, key):
    limit = LIMITS[key]
    n = len(value)
    mark = "OK " if n <= limit else "!! "
    return f"{mark}{label}: {n}/{limit}", n <= limit


def main():
    os.makedirs(OUT, exist_ok=True)
    all_ok = True
    report = []

    for loc, d in L.items():
        lines = []
        w = lines.append
        w("=" * 78)
        w(f"LAMPADA — метаданные App Store · локаль {loc}")
        w(d["language"])
        w("=" * 78)
        w("")
        w("ПОЗИЦИОНИРОВАНИЕ")
        w("  База : виджет со стихом на всех поверхностях телефона.")
        w("  УТП  : «пауза перед лентой» — стих встречает при открытии соцсети.")
        w("         Опционально, включается одним тапом на онбординге.")
        w("")
        w(f"BUNDLE ID       {COMMON['bundle_id']}")
        w(f"SKU             {COMMON['sku']}")
        w(f"КАТЕГОРИИ       {COMMON['primary_category']} (основная) / "
          f"{COMMON['secondary_category']} (вторая)")
        w(f"ВОЗРАСТ         {COMMON['age_rating']}")
        w(f"МИН. iOS        {COMMON['min_ios']}")
        w(f"COPYRIGHT       {COMMON['copyright']}")
        w(f"URL ПОДДЕРЖКИ   {COMMON['support_url']}")
        w(f"URL МАРКЕТИНГ   {COMMON['marketing_url']}")
        w(f"URL ПРИВАТНОСТЬ {COMMON['privacy_url']}")
        w("")

        checks = [
            ("НАЗВАНИЕ (App Name)", d["name"], "name"),
            ("ПОДЗАГОЛОВОК (Subtitle)", d["subtitle"], "subtitle"),
            ("КЛЮЧЕВЫЕ СЛОВА (Keywords)", d["keywords"], "keywords"),
            ("ПРОМО-ТЕКСТ (Promotional Text)", d["promo"], "promo"),
            ("ОПИСАНИЕ (Description)", d["description"], "description"),
            ("ЧТО НОВОГО (What's New)", d["whatsnew"], "whatsnew"),
            ("ПОДПИСКА — группа", d["sub_group"], "sub_group"),
            ("ПОДПИСКА — неделя", d["sub_week"], "sub_name"),
            ("ПОДПИСКА — месяц", d["sub_month"], "sub_name"),
            ("ПОДПИСКА — год", d["sub_year"], "sub_name"),
        ]

        for label, val, key in checks:
            line, ok = check(label, val, key)
            all_ok = all_ok and ok
            report.append(f"{loc:6} {line}")
            w("-" * 78)
            w(f"{label}  [{len(val)}/{LIMITS[key]}]")
            w("-" * 78)
            w(val)
            w("")

        w("-" * 78)
        w(f"ПОДПИСКИ (группа «{d['sub_group']}»)")
        w("-" * 78)
        w("Пробный период 7 дней — только на годовой: триал на всех тарифах")
        w("сразу уводит на недельный, и годовой перестаёт продаваться.")
        w("")
        w(f"Недельная: {d['sub_week']}   com.astonio.misbah.weekly   $2.99")
        w(f"Месячная:  {d['sub_month']}   com.astonio.misbah.monthly  $5.99")
        w(f"Годовая:   {d['sub_year']}   com.astonio.misbah.yearly   $24.99 + 7 дней")
        w("")
        w("Пожизненная покупка com.astonio.misbah.lifetime остаётся в каталоге,")
        w("но на пейволле не показывается и в описании не упоминается.")
        w("")
        w("-" * 78)
        w("ПОДПИСИ К СКРИНШОТАМ (7 экранов; первые два видны без листания)")
        w("-" * 78)
        for i, s in enumerate(d["shots"], 1):
            w(f"{i}. {s}")
        w("")
        w("-" * 78)
        w("GOOGLE PLAY (для второй платформы)")
        w("-" * 78)
        play_title = d["name"]
        play_short = d["subtitle"]
        w(f"Заголовок [{len(play_title)}/{LIMITS['play_title']}]: {play_title}")
        w(f"Краткое описание [{len(play_short)}/{LIMITS['play_short']}]: {play_short}")
        w("Полное описание: то же, что Description выше.")
        w("")

        path = os.path.join(OUT, f"{loc}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"записан  metadata/{loc}.txt")

        # Голое описание без отчёта — чтобы вставлять в App Store Connect
        # руками, когда API недоступен. В общем файле выше описание лежит
        # среди рамок и заголовков, и выделить ровно его мышью неудобно.
        bare = os.path.join(OUT, f"description-{loc}.txt")
        with open(bare, "w", encoding="utf-8") as f:
            f.write(d["description"])

    print()
    print("ПРОВЕРКА ЛИМИТОВ")
    print("-" * 50)
    for r in report:
        print(r)
    print("-" * 50)
    print("ВСЁ В ЛИМИТАХ" if all_ok else "ЕСТЬ ПРЕВЫШЕНИЯ — СМОТРИ СТРОКИ С !!")

    # Из-за отсутствия этих двух ссылок ревью отклонило первую подачу: у
    # приложения с автопродляемой подпиской они обязаны быть в описании на
    # странице App Store (правило 3.1.2). Потерять их при следующей правке
    # текста легко — заметно это станет только через отказ и потерянные сутки.
    print()
    print("ССЫЛКИ В ОПИСАНИИ (правило 3.1.2)")
    print("-" * 50)
    links_ok = True
    for loc, d in L.items():
        for label, needle in (("EULA", "stdeula"),
                              ("политика", COMMON["privacy_url"])):
            found = needle in d["description"]
            links_ok = links_ok and found
            print(f"{loc:6} {'OK ' if found else '!! '}{label}")
    print("-" * 50)
    print("ССЫЛКИ НА МЕСТЕ" if links_ok else "ССЫЛОК НЕ ХВАТАЕТ — РЕВЬЮ ОТКЛОНИТ")


if __name__ == "__main__":
    main()
