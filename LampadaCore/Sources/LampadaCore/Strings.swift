import Foundation

/// Строки интерфейса на пяти языках релиза.
///
/// Таблица в коде, а не `.strings`-файлы, по одной причине: язык интерфейса
/// здесь выбирает человек в настройках приложения, а не система. Стандартный
/// механизм локализации подставляет язык устройства и заставляет держать
/// отдельный `Bundle` на каждый `lproj`; здесь же достаточно словаря, который
/// к тому же виден на ревью целиком и не может «потерять ключ» в рантайме.
///
/// Порядок значений в каждой строке всегда один: ru, en, de, fr, es. Языки,
/// добавленные позже, — отдельными словарями в своих файлах: дописывать
/// шестое и седьмое значение в каждую из сотен строк значило бы перетряхнуть
/// весь файл ради двух столбцов.
public struct L10n: Sendable, Hashable {
    public let locale: AppLocale

    public init(_ locale: AppLocale) {
        self.locale = locale
    }

    public subscript(_ key: Key) -> String {
        let row = L10n.table[key] ?? ["", "", "", "", ""]
        let value = switch locale {
        case .ru: row[0]
        case .en: row[1]
        case .de: row[2]
        case .fr: row[3]
        case .es: row[4]
        case .pt: L10n.portuguese[key] ?? ""
        case .it: L10n.italian[key] ?? ""
        case .ko: L10n.korean[key] ?? ""
        }
        guard value.isEmpty else { return value }
        // Пустая строка означает недостающий перевод: показываем русский, а не
        // пустоту. Заметить это на глаз проще, чем дыру в интерфейсе. Новым
        // языкам — английский: русский посреди португальского не прочтёт никто.
        switch locale {
        case .pt, .it, .ko: return row[1]
        case .ru, .en, .de, .fr, .es: return row[0]
        }
    }

    /// Подстановка чисел: «Сейчас 3 из 7».
    public func callAsFunction(_ key: Key, _ arguments: CVarArg...) -> String {
        String(format: self[key], arguments: arguments)
    }

    /// Число со словом в нужной форме: «1 день», «22 дня», «45 дней».
    ///
    /// В корейском множественного числа нет, а счётное слово пишется слитно
    /// с числом и иногда после существительного: «45일», «글꼴 8개». Поэтому
    /// корейская форма одна, и место числа в ней отмечено решёткой.
    ///
    /// Формы лежат в строке таблицы через вертикальную черту: у русского три
    /// (1, 2–4, 5–20), у остальных две. Французский и бразильский
    /// португальский, в отличие от прочих, ставят единственное число и для нуля.
    public func count(_ number: Int, _ key: Key) -> String {
        if locale == .ko {
            return self[key].replacingOccurrences(of: "#", with: String(number))
        }
        let forms = self[key].split(separator: "|").map(String.init)
        let index: Int
        switch locale {
        case .ru:
            let ones = number % 10, tens = number % 100
            index = ones == 1 && tens != 11 ? 0
                : (2...4).contains(ones) && !(12...14).contains(tens) ? 1 : 2
        case .fr, .pt:
            index = number <= 1 ? 0 : 1
        case .en, .de, .es, .it, .ko:
            index = number == 1 ? 0 : 1
        }
        return "\(number) \(forms[min(index, forms.count - 1)])"
    }

    public enum Key: String, Sendable, Hashable, CaseIterable {
        // Онбординг
        case epigraph, heroTitle, heroSubtitle, heroAction, heroEditions
        case languageTitle, languageSubtitle, next
        case themesTitle, themesSubtitle, themesEmpty, themesPicked
        case widgetTitle, widgetSubtitle, widgetAction, widgetLater
        case pauseEyebrow, pauseTitle, pauseSubtitle, pauseAction, pauseWait
        case pauseClose, pauseNoApp
        // Онбординг v3 (1.0.2) — блок «Онбординг v3» в макете. Прежние ключи
        // выше оставлены: по ним ещё живут старые экраны макета.
        case obVerseEyebrow, obVerseCta, obVerseTrust
        case goalTitle, goalLead, goalHint
        case goalComfort, goalComfortSub, goalDaily, goalDailySub
        case goalFeed, goalFeedSub, goalBeauty, goalBeautySub
        case obThemesTitle, obThemesSub, obThemesCounter
        case obTimeEyebrow, obTimeTitle, obTimeSub, obTimeLater
        case obFeedTitle, obFeedSub, obFeedInsight
        case feedUnderOne, feedOneToTwo, feedTwoToFour, feedOverFour
        case obLookEyebrow, obLookTitle, obLookSub
        case obFirstTitle, obFirstSub, obFirstCta, obFirstSentTitle, obFirstSentSub
        case obIconEyebrow, obIconTitle, obIconSub, obIconKeep
        case obWidgetEyebrow, obWidgetTitle, obWidgetSub, obWidgetCta, obWidgetLater
        case obDoneEyebrow, obDoneTitle, obDoneFooter
        case obWhyLead, obWhyNumber, obWhyQuestion, obWhySource, obWhyCta
        // Слова к числам — формы через «|», см. `count(_:_:)`
        case versesUnit, daysUnit, fontsUnit, iconsUnit
        // Пейволл: общий и четыре ветки онбординга
        case pwTitle, pwTitleGeneric, pwSub
        case pwComfortEyebrow, pwComfortTitle, pwComfortSub
        case pwDailyEyebrow, pwDailyTitle, pwDailySub, chipDailyVerse
        case pwFeedEyebrow, pwFeedTitle, pwFeedSub
        case pwBeautyTitle, pwBeautySub, pwBeautySubNoPick
        case unlockStandBy, unlockWallpaper, unlockSets
        case unlockPictures, unlockFonts, unlockIcons
        case planWeek, planMonth, planYear
        case planWeekNote, planMonthNote, planYearNote
        case pwTrialCta, pwSubscribeCta, pwAfterTrial, pwCancelAnytime
        case pwHowTrial, pwRestore, pwTerms, pwPrivacy
        case standByLocked, proEndedTitle, proEndedBody, proEndedCta
        // Вкладки
        // Шаги инструкций. Названия системных пунктов взяты так, как они
        // называются в самой iOS на каждом языке: человек сверяет их глазами
        // с экраном, и вольный перевод отправил бы его искать несуществующее.
        case stepLock1, stepLock1Hint, stepLock2
        case stepLock2Hint, stepLock3, stepLock3Hint
        case stepHome1, stepHome1Hint, stepHome2
        case stepHome2Hint, stepHome3, stepHome3Hint
        case stepControl1, stepControl1Hint, stepControl2
        case stepControl2Hint, stepControl3, stepControl3Hint
        case stepStandBy1, stepStandBy1Hint, stepStandBy2
        case stepStandBy2Hint, stepStandBy3, stepStandBy3Hint
        case stepWatch1, stepWatch1Hint, stepWatch2
        case stepWatch2Hint, stepWatch3, stepWatch3Hint
        case stepWallpaper1, stepWallpaper1Hint, stepWallpaper2
        case stepWallpaper2Hint, stepWallpaper3, stepWallpaper3Hint
        case stepPause1, stepPause1Hint, stepPause2
        case stepPause2Hint, stepPause3, stepPause3Hint
        case back, notNow, continueAction, openShortcuts, installShortcut, manageSubscription
        // Обучающий тур
        case coachSwipe, coachAreas, coachAppStyle, coachSwitchToWidgets, coachWidgetStyle
        case coachPlaces, coachMarkDone, coachSkip, coachNext, coachDone
        // Фоны-изображения
        case sceneShepherd, sceneClouds, scenePastel, sceneOldBook
        case sceneFresco, sceneChrist, scenePaul, sceneDavid
        case sceneGalilee, sceneStar, sceneGethsemane, sceneCross
        case colourSets, imageSets
        case tabToday
        // Иконки приложения
        case appIconTitle
        case iconDefault, iconNight, iconFlame
        case iconVitrage, iconCross, iconChristmas, iconEaster, iconDove
        // Виджет: подпись в галерее виджетов iOS
        case widgetDisplayName, widgetDescription
        case controlDisplayName, controlDescription
        // Доступность
        case depthHint
        // Поверхности: названия, заголовки шторок, заметки и кнопки.
        // Сами шаги инструкций пока только по-русски — см. Surface.steps.
        case surfaceLock, surfaceHome, surfaceControl, surfaceWallpaper, surfacePause
        case howLock, howHome, howControl, howStandBy, howWatch, howWallpaper
        case noteAuto, noteSecondRelease, noteManual
        case ctaLock, ctaHome, ctaControl, ctaStandBy, ctaWatch, ctaWallpaper, ctaPause
        case areaApp, areaWidgets, areaLock
        // Наборы стилей
        case styleLavender, styleNight, styleParchment, styleAmber
        case styleInk, styleDawn, styleOpal, styleCoal
        // Размеры виджета и варианты на экране блокировки
        case sizeSmall, sizeMedium, sizeLarge
        case lengthShort, lengthFull, alignLeading, alignCenter
        // Форматы картинки для шеринга
        case formatStory, formatSquare, formatWallpaper
        // Сегодня
        case backToDaily, share, contextPill
        // Места
        case placesTitle, placesProgress, groupScreens, groupMoment
        // Вид
        case lookTitle, preview, size, font, languageAndEdition, systemFont
        case verseLength, alignment, lockColorNote, appIcon
        // Поделиться
        case shareTitle, sendAction, wordmark
        // Шторки
        case context, understood, close, openSettings, markDone
        // Пейволл
        case paywallTitle, subscribe, restore, paywallLegal
        case perkSurfaces, perkStyles, perkIcons
        // Образцы стихов в онбординге. Взяты из самих изданий, а не переведены
        // руками: в приложении про Писание выдуманная цитата недопустима.
        case demoVerse, demoReference, pauseVerse, pauseReference
        // Уведомления: шаг онбординга, строка в «Местах», сами пуши
        case obNotifyEyebrow, notifyNow
        // Онбординг: разрешение на отслеживание (ATT)
        case obTrackEyebrow, obTrackTitle, obTrackSub, obTrackCta
        case dailyVerseTitle, dailyVerseOn, dailyVerseOff, dailyVerseSub, dailyVerseTime
        case notifyDenied
        case comeback3Title, comeback3Body, comeback7Title, comeback7Body
        case widgetGoneTitle, widgetGoneBody
        case secondHomeTitle, secondHomeBody, secondLockTitle, secondLockBody
        // Причина отмены триала
        case cancelTitle, cancelSub, cancelSkip, cancelThanks, cancelSend
        case reasonPrice, reasonUnused, reasonFreeEnough, reasonNotWhat, reasonJustLooking, reasonOther
        // Скидка после закрытого пейволла
        case welcomeEyebrow, welcomeTitle, welcomeSub, welcomeTerms, welcomeCta, welcomeNo
        // Пейволл с замка
        case pwPickedEyebrow
        // Аналитика
        case analyticsTitle, analyticsNote
        // «Что нового» после обновления и согласие на новости (4.5.4)
        case wnIconsEyebrow, wnIconsTitle, wnIconsSub, wnFree, wnSkip
        case wnPicturesEyebrow, wnPicturesTitle, wnPicturesSub, wnSetPicture, wnUnlockPicture
        case wnDailyTitle, wnDailySub, wnDailyCta, wnDone
        case promoTitle, promoSub, promoPlacesSub
        // Оценка в App Store
        case rateApp
        // Скрытое: токен уведомлений для пробной рассылки
        case pushTokenCopied
        // Ошибка
        case corpusFailedTitle, corpusFailedHint
    }

    // Порядок в строке: ru, en, de, fr, es
    private static let table: [Key: [String]] = [
        .epigraph: ["«Светильник ноге моей»", "“A lamp to my feet”", "„Eine Leuchte für meinen Fuß“", "« Une lampe à mes pieds »", "«Lámpara a mis pies»"],
        .heroTitle: ["Слово там, куда ты и так смотришь", "The Word where you already look", "Das Wort dort, wohin du ohnehin schaust", "La Parole là où tu regardes déjà", "La Palabra donde ya miras"],
        .heroSubtitle: ["Экран блокировки, рабочий стол, часы, тумбочка у кровати. Ничего не надо помнить — стих просто есть.",
                        "Lock screen, home screen, watch, bedside table. Nothing to remember — the verse is simply there.",
                        "Sperrbildschirm, Home-Bildschirm, Uhr, Nachttisch. Nichts zu merken — der Vers ist einfach da.",
                        "Écran verrouillé, écran d’accueil, montre, table de nuit. Rien à retenir — le verset est là.",
                        "Pantalla de bloqueo, inicio, reloj, mesita de noche. Nada que recordar: el versículo está ahí."],
        .heroAction: ["Зажечь", "Light it", "Anzünden", "Allumer", "Encender"],
        .heroEditions: ["Синодальный · WEB · Segond · Luther · Reina-Valera", "WEB · Синодальный · Luther · Segond · Reina-Valera", "Luther · WEB · Синодальный · Segond · Reina-Valera", "Segond · WEB · Синодальный · Luther · Reina-Valera", "Reina-Valera · WEB · Синодальный · Luther · Segond"],
        .languageTitle: ["На каком языке", "Which language", "In welcher Sprache", "Dans quelle langue", "En qué idioma"],
        .languageSubtitle: ["Перевод можно поменять позже в настройках", "You can change the translation later in settings", "Die Übersetzung lässt sich später ändern", "La traduction se change plus tard dans les réglages", "La traducción se cambia luego en ajustes"],
        .next: ["Дальше", "Next", "Weiter", "Suivant", "Siguiente"],
        .themesTitle: ["Что тебе сейчас нужно", "What do you need right now", "Was brauchst du gerade", "De quoi as-tu besoin maintenant", "Qué necesitas ahora"],
        .themesSubtitle: ["Отметь одно или несколько. Стихи пойдут за ними", "Pick one or several. The verses will follow", "Wähle eins oder mehrere. Die Verse folgen dem", "Coche un ou plusieurs. Les versets suivront", "Marca uno o varios. Los versículos irán tras ellos"],
        .themesEmpty: ["Можно ничего не выбирать — тогда весь корпус", "Choose nothing and you get everything", "Nichts wählen heißt: alles zeigen", "Ne rien choisir, c’est tout recevoir", "Sin elegir nada, se muestra todo"],
        .themesPicked: ["Выбрано %d из %d", "%d of %d selected", "%d von %d gewählt", "%d sur %d sélectionnés", "%d de %d elegidos"],
        .widgetTitle: ["Поставь виджет", "Add the widget", "Widget hinzufügen", "Ajoute le widget", "Pon el widget"],
        .widgetSubtitle: ["Экран блокировки — самое видное место в телефоне. Бесплатно, навсегда",
                          "The lock screen is the most visible place on your phone. Free, forever",
                          "Der Sperrbildschirm ist der sichtbarste Ort im Telefon. Kostenlos, für immer",
                          "L’écran verrouillé est l’endroit le plus vu du téléphone. Gratuit, pour toujours",
                          "La pantalla de bloqueo es el lugar más visible del teléfono. Gratis, para siempre"],
        .widgetAction: ["Показать как", "Show me how", "Zeig mir wie", "Montre-moi comment", "Muéstrame cómo"],
        .widgetLater: ["Поставлю позже", "I’ll do it later", "Später", "Plus tard", "Más tarde"],
        .pauseEyebrow: ["Только у нас", "Only here", "Nur bei uns", "Seulement ici", "Solo aquí"],
        .pauseTitle: ["Пауза перед лентой", "A pause before the feed", "Pause vor dem Feed", "Une pause avant le fil", "Pausa antes del feed"],
        .pauseSubtitle: ["Открываешь соцсеть — первым тебя встречает стих. Не лента вместо ленты, а секунда там, где ты собирался листать",
                         "You open a social app and a verse meets you first. Not another feed — one second where you were about to scroll",
                         "Du öffnest eine App, und zuerst begegnet dir ein Vers. Kein zweiter Feed, sondern eine Sekunde vor dem Scrollen",
                         "Tu ouvres un réseau et un verset t’accueille. Pas un autre fil, une seconde avant de faire défiler",
                         "Abres una red y primero te recibe un versículo. No otro feed: un segundo antes de deslizar"],
        .pauseAction: ["Включить", "Turn on", "Einschalten", "Activer", "Activar"],
        .pauseWait: ["Подожди секунду", "Wait a second", "Warte kurz", "Attends une seconde", "Espera un segundo"],
        .pauseClose: ["Закрыть", "Close", "Schließen", "Fermer", "Cerrar"],
        .pauseNoApp: ["В автоматизации не выбрано приложение. Откройте её в «Командах» и укажите его в действии «Пауза со стихом» — тогда кнопка будет возвращать сразу туда", "No app is chosen in the automation. Open it in Shortcuts and set one in the “Pause with a verse” action — then the button will take you straight back", "In der Automation ist keine App gewählt. Öffne sie in „Kurzbefehle“ und wähle eine in der Aktion „Pause mit einem Vers“ — dann führt die Taste direkt zurück", "Aucune app n’est choisie dans l’automatisation. Ouvrez-la dans Raccourcis et indiquez-en une dans l’action « Pause avec un verset » : le bouton vous y ramènera directement", "En la automatización no hay ninguna app elegida. Ábrela en Atajos e indícala en la acción «Pausa con un versículo»: así el botón te llevará de vuelta"],
        .backToDaily: ["к стиху дня", "back to today’s verse", "zum Vers des Tages", "au verset du jour", "al versículo del día"],
        .share: ["Поделиться", "Share", "Teilen", "Partager", "Compartir"],
        .contextPill: ["Кто это говорит и когда", "Who says this, and when", "Wer sagt das, und wann", "Qui parle, et quand", "Quién lo dice, y cuándo"],
        .placesTitle: ["Места", "Places", "Orte", "Endroits", "Lugares"],
        .placesProgress: ["Сейчас %d из %d — чем больше, тем чаще Слово попадается на глаза",
                          "%d of %d — the more places, the more often the Word catches your eye",
                          "%d von %d — je mehr Orte, desto öfter fällt das Wort ins Auge",
                          "%d sur %d — plus il y a d’endroits, plus la Parole se rappelle à toi",
                          "%d de %d — cuantos más lugares, más veces aparece la Palabra"],
        .groupScreens: ["На экранах", "On screens", "Auf Bildschirmen", "Sur les écrans", "En pantallas"],
        .groupMoment: ["В моменте", "In the moment", "Im Moment", "Sur le moment", "En el momento"],
        .lookTitle: ["Вид", "Look", "Aussehen", "Apparence", "Aspecto"],
        .preview: ["Предпросмотр", "Preview", "Vorschau", "Aperçu", "Vista previa"],
        .size: ["Размер", "Size", "Größe", "Taille", "Tamaño"],
        .font: ["Шрифт", "Font", "Schrift", "Police", "Fuente"],
        .systemFont: ["Системный", "System", "System", "Système", "Del sistema"],
        .languageAndEdition: ["Язык и перевод", "Language and translation", "Sprache und Übersetzung", "Langue et traduction", "Idioma y traducción"],
        .verseLength: ["Длина стиха", "Verse length", "Verslänge", "Longueur du verset", "Longitud del versículo"],
        .alignment: ["Выравнивание", "Alignment", "Ausrichtung", "Alignement", "Alineación"],
        .lockColorNote: ["Цвет здесь задаёт iOS — виджет подстраивается под обои",
                         "iOS sets the color here — the widget adapts to your wallpaper",
                         "Die Farbe bestimmt iOS — das Widget passt sich dem Hintergrund an",
                         "La couleur est fixée par iOS — le widget s’adapte au fond d’écran",
                         "El color lo fija iOS: el widget se adapta al fondo"],
        .appIcon: ["Иконка приложения", "App icon", "App-Symbol", "Icône de l’app", "Icono de la app"],
        .shareTitle: ["Поделиться", "Share", "Teilen", "Partager", "Compartir"],
        .sendAction: ["Отправить", "Send", "Senden", "Envoyer", "Enviar"],
        .wordmark: ["Подпись Lampada", "Lampada mark", "Lampada-Signatur", "Signature Lampada", "Firma Lampada"],
        .context: ["Контекст", "Context", "Kontext", "Contexte", "Contexto"],
        .understood: ["Понятно", "Got it", "Verstanden", "Compris", "Entendido"],
        .close: ["Закрыть", "Close", "Schließen", "Fermer", "Cerrar"],
        .openSettings: ["Открыть настройки", "Open Settings", "Einstellungen öffnen", "Ouvrir Réglages", "Abrir Ajustes"],
        .markDone: ["Отметить, что готово", "Mark as done", "Als erledigt markieren", "Marquer comme fait", "Marcar como hecho"],
        .paywallTitle: ["Стих везде, где ты смотришь", "The verse everywhere you look", "Der Vers überall, wohin du schaust", "Le verset partout où tu regardes", "El versículo donde mires"],
        .subscribe: ["Оформить", "Subscribe", "Abonnieren", "S’abonner", "Suscribirse"],
        .restore: ["Восстановить покупки", "Restore purchases", "Käufe wiederherstellen", "Restaurer les achats", "Restaurar compras"],
        .paywallLegal: ["Подписка продлевается автоматически. Отменить можно в настройках Apple ID.",
                        "The subscription renews automatically. Cancel any time in your Apple ID settings.",
                        "Das Abo verlängert sich automatisch. Kündigung in den Apple-ID-Einstellungen.",
                        "L’abonnement se renouvelle automatiquement. Résiliation dans les réglages Apple ID.",
                        "La suscripción se renueva automáticamente. Cancela en los ajustes de Apple ID."],
        .perkSurfaces: ["StandBy и обои со стихом", "StandBy and verse wallpapers", "StandBy und Vers-Hintergründe", "StandBy et fonds d’écran avec verset", "StandBy y fondos con versículo"],
        .perkStyles: ["Все наборы стилей для приложения, виджетов и локскрина", "Every style set for the app, widgets and lock screen", "Alle Stilsets für App, Widgets und Sperrbildschirm", "Tous les styles pour l’app, les widgets et l’écran verrouillé", "Todos los estilos para la app, widgets y bloqueo"],
        .perkIcons: ["Иконки приложения на выбор", "A choice of app icons", "App-Symbole zur Auswahl", "Des icônes d’app au choix", "Iconos de app a elegir"],
        .areaApp: ["Приложение", "App", "App", "Application", "Aplicación"],
        .areaWidgets: ["Виджеты", "Widgets", "Widgets", "Widgets", "Widgets"],
        .areaLock: ["Блокировка", "Lock screen", "Sperrbildschirm", "Écran verrouillé", "Bloqueo"],
        .styleLavender: ["Лаванда", "Lavender", "Lavendel", "Lavande", "Lavanda"],
        .styleNight: ["Ночь", "Night", "Nacht", "Nuit", "Noche"],
        .styleParchment: ["Пергамент", "Parchment", "Pergament", "Parchemin", "Pergamino"],
        .styleAmber: ["Янтарь", "Amber", "Bernstein", "Ambre", "Ámbar"],
        .styleInk: ["Тушь", "Ink", "Tusche", "Encre", "Tinta"],
        .styleDawn: ["Заря", "Dawn", "Morgenrot", "Aurore", "Alba"],
        .styleOpal: ["Опал", "Opal", "Opal", "Opale", "Ópalo"],
        .styleCoal: ["Уголь", "Coal", "Kohle", "Charbon", "Carbón"],
        .sizeSmall: ["Малый", "Small", "Klein", "Petit", "Pequeño"],
        .sizeMedium: ["Средний", "Medium", "Mittel", "Moyen", "Mediano"],
        .sizeLarge: ["Большой", "Large", "Groß", "Grand", "Grande"],
        .lengthShort: ["Короткая", "Short", "Kurz", "Courte", "Corta"],
        .lengthFull: ["Полная", "Full", "Vollständig", "Complète", "Completa"],
        .alignLeading: ["По левому краю", "Left", "Linksbündig", "À gauche", "A la izquierda"],
        .alignCenter: ["По центру", "Centred", "Zentriert", "Centré", "Centrado"],
        .formatStory: ["Сторис", "Story", "Story", "Story", "Historia"],
        .formatSquare: ["Квадрат", "Square", "Quadrat", "Carré", "Cuadrado"],
        .formatWallpaper: ["Обои", "Wallpaper", "Hintergrund", "Fond d’écran", "Fondo"],
        .surfaceLock: ["Экран блокировки", "Lock screen", "Sperrbildschirm", "Écran verrouillé", "Pantalla de bloqueo"],
        .surfaceHome: ["Рабочий стол", "Home screen", "Home-Bildschirm", "Écran d’accueil", "Pantalla de inicio"],
        .surfaceControl: ["Пункт управления", "Control Centre", "Kontrollzentrum", "Centre de contrôle", "Centro de control"],
        .surfaceWallpaper: ["Обои", "Wallpaper", "Hintergrund", "Fond d’écran", "Fondo de pantalla"],
        .surfacePause: ["Пауза перед лентой", "Pause before the feed", "Pause vor dem Feed", "Pause avant le fil", "Pausa antes del feed"],
        .howLock: ["Виджет на экран блокировки", "Widget on the lock screen", "Widget auf dem Sperrbildschirm", "Widget sur l’écran verrouillé", "Widget en la pantalla de bloqueo"],
        .howHome: ["Виджет на рабочий стол", "Widget on the home screen", "Widget auf dem Home-Bildschirm", "Widget sur l’écran d’accueil", "Widget en la pantalla de inicio"],
        .howControl: ["Кнопка в Пункте управления", "Button in Control Centre", "Schaltfläche im Kontrollzentrum", "Bouton dans le Centre de contrôle", "Botón en el Centro de control"],
        .howStandBy: ["Виджет в StandBy", "Widget in StandBy", "Widget in StandBy", "Widget dans StandBy", "Widget en StandBy"],
        .howWatch: ["Циферблат на Apple Watch", "Complication on Apple Watch", "Zifferblatt auf der Apple Watch", "Cadran sur l’Apple Watch", "Esfera en el Apple Watch"],
        .howWallpaper: ["Обои со стихом", "Wallpaper with a verse", "Hintergrund mit Vers", "Fond d’écran avec un verset", "Fondo con un versículo"],
        .noteAuto: ["Виджет отметится в «Местах» сам", "The widget will tick itself in Places", "Das Widget markiert sich in „Orte“ selbst", "Le widget se cochera dans « Endroits »", "El widget se marcará solo en «Lugares»"],
        .noteSecondRelease: ["Появится во втором релизе", "Coming in the second release", "Kommt im zweiten Release", "Arrive dans la deuxième version", "Llegará en la segunda versión"],
        .noteManual: ["Отметьте в «Местах», когда закончите", "Tick it in Places when you are done", "Markieren Sie es in „Orte“, wenn Sie fertig sind", "Cochez-le dans « Endroits » une fois terminé", "Márcalo en «Lugares» cuando termines"],
        .ctaLock: ["Поставить на экран блокировки", "Put it on the lock screen", "Auf den Sperrbildschirm setzen", "Mettre sur l’écran verrouillé", "Ponerlo en la pantalla de bloqueo"],
        .ctaHome: ["Добавить на рабочий стол", "Add to the home screen", "Zum Home-Bildschirm hinzufügen", "Ajouter à l’écran d’accueil", "Añadir a la pantalla de inicio"],
        .ctaControl: ["Добавить в Пункт управления", "Add to Control Centre", "Zum Kontrollzentrum hinzufügen", "Ajouter au Centre de contrôle", "Añadir al Centro de control"],
        .ctaStandBy: ["Включить в StandBy", "Turn on in StandBy", "In StandBy aktivieren", "Activer dans StandBy", "Activar en StandBy"],
        .ctaWatch: ["Показать на Apple Watch", "Show on Apple Watch", "Auf der Apple Watch zeigen", "Afficher sur l’Apple Watch", "Mostrar en el Apple Watch"],
        .ctaWallpaper: ["Поставить обои", "Set the wallpaper", "Hintergrund einrichten", "Définir le fond d’écran", "Poner el fondo"],
        .ctaPause: ["Включить паузу перед лентой", "Turn on the pause before the feed", "Pause vor dem Feed aktivieren", "Activer la pause avant le fil", "Activar la pausa antes del feed"],
        .appIconTitle: ["Иконка приложения", "App icon", "App-Symbol", "Icône de l’app", "Icono de la app"],
        .iconDefault: ["Основная", "Default", "Standard", "Par défaut", "Predeterminado"],
        .iconNight: ["Ночь", "Night", "Nacht", "Nuit", "Noche"],
        .iconFlame: ["Пламя", "Flame", "Flamme", "Flamme", "Llama"],
        .iconVitrage: ["Витраж", "Stained glass", "Buntglas", "Vitrail", "Vitral"],
        .iconCross: ["Крест", "Cross", "Kreuz", "Croix", "Cruz"],
        .iconChristmas: ["Рождество", "Christmas", "Weihnachten", "Noël", "Navidad"],
        .iconEaster: ["Пасха", "Easter", "Ostern", "Pâques", "Pascua"],
        .iconDove: ["Голубь", "Dove", "Taube", "Colombe", "Paloma"],
        .widgetDisplayName: ["Стих дня", "Verse of the day", "Vers des Tages", "Verset du jour", "Versículo del día"],
        .controlDisplayName: ["Стих дня", "Verse of the day", "Vers des Tages", "Verset du jour", "Versículo del día"],
        .controlDescription: ["Кнопка в Пункте управления: открывает сегодняшний стих", "A Control Centre button that opens today\u{2019}s verse", "Eine Taste im Kontrollzentrum, die den heutigen Vers öffnet", "Un bouton du centre de contrôle qui ouvre le verset du jour", "Un botón del centro de control que abre el versículo de hoy"],
        .widgetDescription: ["Слово на каждый день там, где вы и так смотрите", "A word for every day, where you already look", "Ein Wort für jeden Tag – dort, wo Sie ohnehin hinsehen", "Une parole chaque jour, là où vous regardez déjà", "Una palabra cada día, donde ya miras"],
        .depthHint: ["Сейчас показан %d-й стих от сегодняшнего", "Showing verse %d back from today", "Aktuell der %d. Vers vor heute", "Actuellement le %d\u{00A0}e verset avant aujourd’hui", "Ahora el versículo %d antes de hoy"],
        .stepLock1: ["Зажмите экран блокировки", "Touch and hold the Lock Screen", "Halten Sie den Sperrbildschirm gedrückt", "Touchez l’écran verrouillé et maintenez", "Mantén pulsada la pantalla de bloqueo"],
        .stepLock1Hint: ["пока не появится кнопка «Настроить»", "until the Customize button appears", "bis die Taste „Anpassen“ erscheint", "jusqu’à l’apparition du bouton « Personnaliser »", "hasta que aparezca el botón «Personalizar»"],
        .stepLock2: ["Нажмите «Настроить», затем «Экран блокировки»", "Tap Customize, then Lock Screen", "Tippen Sie auf „Anpassen“, dann „Sperrbildschirm“", "Touchez « Personnaliser », puis « Écran verrouillé »", "Toca «Personalizar» y luego «Pantalla de bloqueo»"],
        .stepLock2Hint: ["откроется редактор", "the editor opens", "der Editor öffnet sich", "l’éditeur s’ouvre", "se abre el editor"],
        .stepLock3: ["Добавьте виджет Lampada под часами", "Add the Lampada widget below the clock", "Fügen Sie das Lampada-Widget unter der Uhr hinzu", "Ajoutez le widget Lampada sous l’horloge", "Añade el widget Lampada bajo el reloj"],
        .stepLock3Hint: ["выберите прямоугольный размер", "choose the rectangular size", "wählen Sie die rechteckige Größe", "choisissez la taille rectangulaire", "elige el tamaño rectangular"],
        .stepHome1: ["Зажмите свободное место на рабочем столе", "Touch and hold an empty area of the Home Screen", "Halten Sie eine freie Stelle auf dem Home-Bildschirm gedrückt", "Touchez une zone vide de l’écran d’accueil et maintenez", "Mantén pulsada una zona vacía de la pantalla de inicio"],
        .stepHome1Hint: ["иконки начнут покачиваться", "the icons start to jiggle", "die Symbole beginnen zu wackeln", "les icônes se mettent à bouger", "los iconos empiezan a moverse"],
        .stepHome2: ["Нажмите «+» в левом верхнем углу", "Tap + in the top-left corner", "Tippen Sie oben links auf „+“", "Touchez « + » en haut à gauche", "Toca «+» en la esquina superior izquierda"],
        .stepHome2Hint: ["откроется галерея виджетов", "the widget gallery opens", "die Widget-Galerie öffnet sich", "la galerie de widgets s’ouvre", "se abre la galería de widgets"],
        .stepHome3: ["Найдите Lampada и выберите размер", "Find Lampada and pick a size", "Suchen Sie Lampada und wählen Sie eine Größe", "Trouvez Lampada et choisissez une taille", "Busca Lampada y elige un tamaño"],
        .stepHome3Hint: ["средний помещает стих целиком", "the medium one fits the whole verse", "die mittlere fasst den ganzen Vers", "la moyenne contient le verset entier", "el mediano cabe el versículo entero"],
        .stepControl1: ["Откройте Пункт управления и нажмите «+»", "Open Control Center and tap +", "Öffnen Sie das Kontrollzentrum und tippen Sie auf „+“", "Ouvrez le centre de contrôle et touchez « + »", "Abre el centro de control y toca «+»"],
        .stepControl1Hint: ["нужна iOS 18: кнопка добавляется в режиме правки", "iOS 18 required: add it in editing mode", "iOS 18 nötig: im Bearbeitungsmodus hinzufügen", "iOS 18 requise : à ajouter en mode édition", "requiere iOS 18: se añade en modo edición"],
        .stepControl2: ["Нажмите «Добавить элемент управления»", "Tap Add a Control", "Tippen Sie auf „Steuerelement hinzufügen“", "Touchez « Ajouter une commande »", "Toca «Añadir un control»"],
        .stepControl2Hint: ["откроется список", "a list opens", "eine Liste öffnet sich", "une liste s’ouvre", "se abre una lista"],
        .stepControl3: ["Найдите Lampada в списке", "Find Lampada in the list", "Suchen Sie Lampada in der Liste", "Trouvez Lampada dans la liste", "Busca Lampada en la lista"],
        .stepControl3Hint: ["кнопка встанет туда, куда её поставите", "the button goes wherever you place it", "die Taste landet dort, wo Sie sie ablegen", "le bouton se place où vous le déposez", "el botón queda donde lo coloques"],
        .stepStandBy1: ["Положите телефон на зарядку боком", "Put the phone on a charger on its side", "Legen Sie das iPhone quer auf das Ladegerät", "Posez le téléphone en charge, à l’horizontale", "Pon el teléfono a cargar de lado"],
        .stepStandBy1Hint: ["экран перейдёт в режим StandBy", "the screen switches to StandBy", "der Bildschirm wechselt in den StandBy-Modus", "l’écran passe en mode StandBy", "la pantalla pasa al modo StandBy"],
        .stepStandBy2: ["Пролистайте до правой панели", "Swipe to the right-hand panel", "Wischen Sie zur rechten Ansicht", "Faites défiler jusqu’au panneau de droite", "Desliza hasta el panel derecho"],
        .stepStandBy2Hint: ["там живут виджеты", "that is where the widgets live", "dort wohnen die Widgets", "c’est là que vivent les widgets", "ahí viven los widgets"],
        .stepStandBy3: ["Зажмите панель и добавьте Lampada", "Touch and hold the panel, then add Lampada", "Halten Sie die Ansicht gedrückt und fügen Sie Lampada hinzu", "Maintenez le panneau et ajoutez Lampada", "Mantén pulsado el panel y añade Lampada"],
        .stepStandBy3Hint: ["виджет будет виден всю ночь", "the widget stays visible all night", "das Widget bleibt die ganze Nacht sichtbar", "le widget reste visible toute la nuit", "el widget se ve toda la noche"],
        .stepWatch1: ["Дождитесь второго релиза", "Wait for the second release", "Warten Sie auf das zweite Release", "Attendez la deuxième version", "Espera a la segunda versión"],
        .stepWatch1Hint: ["приложение для часов ещё не вышло", "the watch app is not out yet", "die App für die Uhr ist noch nicht erschienen", "l’app pour la montre n’est pas encore sortie", "la app para el reloj aún no ha salido"],
        .stepWatch2: ["Обновите Lampada, когда оно появится", "Update Lampada when it arrives", "Aktualisieren Sie Lampada, sobald sie da ist", "Mettez Lampada à jour dès sa sortie", "Actualiza Lampada cuando llegue"],
        .stepWatch2Hint: ["мы сообщим об этом в приложении", "we will say so in the app", "wir sagen in der App Bescheid", "nous vous le dirons dans l’app", "te lo diremos en la app"],
        .stepWatch3: ["Добавьте расширение на циферблат", "Add the complication to your watch face", "Fügen Sie die Komplikation zum Zifferblatt hinzu", "Ajoutez la complication au cadran", "Añade la complicación a la esfera"],
        .stepWatch3Hint: ["стих будет виден при подъёме руки", "the verse shows when you raise your wrist", "der Vers erscheint beim Anheben des Handgelenks", "le verset apparaît quand vous levez le poignet", "el versículo aparece al levantar la muñeca"],
        .stepWallpaper1: ["Сохраните обои со стихом", "Save the wallpaper with the verse", "Sichern Sie den Hintergrund mit dem Vers", "Enregistrez le fond d’écran avec le verset", "Guarda el fondo con el versículo"],
        .stepWallpaper1Hint: ["кнопка «Поделиться» → «Сохранить в Фото»", "Share → Save Image", "„Teilen“ → „Bild sichern“", "« Partager » → « Enregistrer l’image »", "«Compartir» → «Guardar imagen»"],
        .stepWallpaper2: ["Откройте Настройки → Обои", "Open Settings → Wallpaper", "Öffnen Sie „Einstellungen“ → „Hintergrundbild“", "Ouvrez « Réglages » → « Fond d’écran »", "Abre «Ajustes» → «Fondo de pantalla»"],
        .stepWallpaper2Hint: ["нажмите «Добавить обои»", "tap Add New Wallpaper", "tippen Sie auf „Neues Hintergrundbild hinzufügen“", "touchez « Ajouter un fond d’écran »", "toca «Añadir fondo de pantalla»"],
        .stepWallpaper3: ["Выберите «Фото» и сохранённое изображение", "Choose Photos and the saved image", "Wählen Sie „Fotos“ und das gesicherte Bild", "Choisissez « Photos » et l’image enregistrée", "Elige «Fotos» y la imagen guardada"],
        .stepWallpaper3Hint: ["стих будет меняться раз в день", "the verse changes once a day", "der Vers wechselt einmal am Tag", "le verset change une fois par jour", "el versículo cambia una vez al día"],
        .stepPause1: ["Откройте «Команды» → «Автоматизация»", "Open Shortcuts → Automation", "Öffnen Sie „Kurzbefehle“ → „Automation“", "Ouvrez « Raccourcis » → « Automatisation »", "Abre «Atajos» → «Automatización»"],
        .stepPause1Hint: ["приложение уже стоит на вашем телефоне", "the app is already on your phone", "die App ist bereits auf Ihrem iPhone", "l’app est déjà sur votre téléphone", "la app ya está en tu teléfono"],
        .stepPause2: ["Создайте автоматизацию «Приложение» → «Открыто»", "Create an App automation → Is Opened", "Erstellen Sie eine Automation „App“ → „Wird geöffnet“", "Créez une automatisation « App » → « Est ouverte »", "Crea una automatización «App» → «Se abre»"],
        .stepPause2Hint: ["выберите соцсети, которые открываете чаще всего", "pick the social apps you open most", "wählen Sie die sozialen Apps, die Sie am häufigsten öffnen", "choisissez les réseaux que vous ouvrez le plus", "elige las redes que abres más a menudo"],
        .stepPause3: ["Добавьте действие «Пауза со стихом»", "Add the Verse pause action", "Fügen Sie die Aktion „Pause mit Vers“ hinzu", "Ajoutez l’action « Pause avec un verset »", "Añade la acción «Pausa con versículo»"],
        .stepPause3Hint: ["в поле действия выберите ту же соцсеть — в неё вас и вернёт", "in the action’s field pick the same app — that is where it returns you", "wählen Sie im Feld der Aktion dieselbe App — dorthin bringt sie Sie zurück", "dans le champ de l’action, choisissez la même app — c’est là qu’elle vous ramène", "en el campo de la acción elige la misma app: ahí te devolverá"],
        .continueAction: ["Продолжить", "Continue", "Weiter", "Continuer", "Continuar"],
        .openShortcuts: ["Открыть «Команды»", "Open Shortcuts", "„Kurzbefehle“ öffnen", "Ouvrir « Raccourcis »", "Abrir «Atajos»"],
        .installShortcut: ["Поставить готовую команду", "Add the ready shortcut", "Fertigen Kurzbefehl laden", "Installer le raccourci prêt", "Añadir el atajo listo"],
        .obVerseEyebrow: ["СТИХ НА СЕГОДНЯ", "VERSE FOR TODAY", "VERS FÜR HEUTE", "VERSET DU JOUR", "VERSÍCULO DE HOY"],
        .obVerseCta: ["Хочу видеть его чаще", "I want to see it more often", "Ich will ihn öfter sehen", "Je veux le voir plus souvent", "Quiero verlo más a menudo"],
        .obVerseTrust: ["Без аккаунта · без рекламы · работает офлайн",
                        "No account · no ads · works offline",
                        "Ohne Konto · ohne Werbung · offline nutzbar",
                        "Sans compte · sans pub · fonctionne hors ligne",
                        "Sin cuenta · sin anuncios · funciona sin conexión"],
        // Тексты онбординга v3 и пейволлов веток — утверждены 01.11 (ru).
        .goalTitle: ["Что тебе сейчас нужнее?", "What do you need most right now?", "Was brauchst du gerade am meisten?", "De quoi as-tu le plus besoin maintenant ?", "¿Qué necesitas más ahora?"],
        .goalLead: ["Одно — под это подберём стихи, экран и Pro",
                    "Pick one — we will fit the verses, the screen and Pro to it",
                    "Eins davon — danach richten wir Verse, Bildschirm und Pro aus",
                    "Un seul choix — on y adapte les versets, l’écran et Pro",
                    "Elige una: a ella ajustaremos los versículos, la pantalla y Pro"],
        .goalHint: ["Остальное откроется потом — в «Местах»", "Everything else opens up later, in Places", "Alles andere findest du später unter „Orte“", "Le reste s’ouvrira plus tard, dans « Endroits »", "Lo demás se abrirá luego, en «Lugares»"],
        .goalComfort: ["Утешение, когда тяжело", "Comfort when it is hard", "Trost, wenn es schwer ist", "Du réconfort quand c’est dur", "Consuelo cuando cuesta"],
        .goalComfortSub: ["стихи под то, что на сердце", "verses for what is on your heart", "Verse zu dem, was dich bewegt", "des versets pour ce que tu as sur le cœur", "versículos para lo que llevas en el corazón"],
        .goalDaily: ["Помнить о вере каждый день", "Remember my faith every day", "Jeden Tag an den Glauben denken", "Me souvenir de ma foi chaque jour", "Recordar la fe cada día"],
        .goalDailySub: ["один стих в выбранное время", "one verse at the time you choose", "ein Vers zur gewählten Zeit", "un verset à l’heure choisie", "un versículo a la hora que elijas"],
        .goalFeed: ["Меньше листать ленту", "Scroll the feed less", "Weniger im Feed scrollen", "Moins faire défiler le fil", "Deslizar menos el feed"],
        .goalFeedSub: ["стих раньше соцсетей", "a verse before social media", "ein Vers vor den sozialen Medien", "un verset avant les réseaux", "un versículo antes de las redes"],
        .goalBeauty: ["Красиво на телефоне", "Something beautiful on my phone", "Schön auf dem Telefon", "Du beau sur mon téléphone", "Algo bonito en el teléfono"],
        .goalBeautySub: ["свой вид стиха и иконка", "your own verse style and icon", "eigener Look für Vers und Symbol", "ton style de verset et ton icône", "tu estilo de versículo y tu icono"],
        .obThemesTitle: ["Что сейчас на сердце?", "What is on your heart right now?", "Was bewegt dich gerade?", "Qu’as-tu sur le cœur en ce moment ?", "¿Qué llevas ahora en el corazón?"],
        .obThemesSub: ["Отметь — и стих на экране будет об этом",
                       "Pick it, and the verse on your screen will speak to it",
                       "Wähle es aus — und der Vers auf dem Bildschirm spricht davon",
                       "Coche-le, et le verset à l’écran en parlera",
                       "Márcalo y el versículo de la pantalla hablará de ello"],
        .obThemesCounter: ["Выбрано %d · нашли %@", "%d selected · %@ for you", "%d gewählt · %@ für dich", "%d choisi(s) · %@ pour toi", "%d elegidos · %@ para ti"],
        .obTimeEyebrow: ["КАЖДЫЙ ДЕНЬ", "EVERY DAY", "JEDEN TAG", "CHAQUE JOUR", "CADA DÍA"],
        .obTimeTitle: ["Во сколько присылать стих?", "When should the verse arrive?", "Wann soll der Vers kommen?", "À quelle heure t’envoyer le verset ?", "¿A qué hora te enviamos el versículo?"],
        .obTimeSub: ["Один стих в одно и то же время, без рекламы. Первый придёт прямо сейчас — на следующем шаге",
                     "One verse at the same time each day, no ads. The first one arrives right now, on the next step",
                     "Ein Vers, jeden Tag zur selben Zeit, ohne Werbung. Der erste kommt gleich — im nächsten Schritt",
                     "Un verset à la même heure, sans pub. Le premier arrive tout de suite, à l’étape suivante",
                     "Un versículo a la misma hora, sin anuncios. El primero llega ahora mismo, en el siguiente paso"],
        .obTimeLater: ["Решу позже", "I will decide later", "Entscheide ich später", "Je déciderai plus tard", "Lo decidiré luego"],
        .obFeedTitle: ["Сколько в день уходит на ленту?", "How much of your day goes to the feed?", "Wie viel Zeit am Tag geht an den Feed?", "Combien de temps par jour pour le fil ?", "¿Cuánto tiempo al día se va en el feed?"],
        .obFeedSub: ["Примерно — ответ останется на телефоне", "Roughly — the answer stays on your phone", "Ungefähr — die Antwort bleibt auf dem Telefon", "À peu près — la réponse reste sur ton téléphone", "Más o menos: la respuesta se queda en tu teléfono"],
        .obFeedInsight: ["≈ %@ в году. Стих их не вернёт — но встретит тебя раньше ленты, каждый раз, когда берёшь телефон",
                         "≈ %@ a year. A verse won’t give them back — but it will meet you before the feed, every time you pick up your phone",
                         "≈ %@ im Jahr. Ein Vers holt sie nicht zurück — aber er begegnet dir vor dem Feed, jedes Mal, wenn du das Telefon nimmst",
                         "≈ %@ par an. Un verset ne te les rendra pas, mais il t’accueillera avant le fil, chaque fois que tu prends ton téléphone",
                         "≈ %@ al año. Un versículo no te los devolverá, pero te recibirá antes del feed cada vez que cojas el teléfono"],
        .feedUnderOne: ["Меньше часа", "Under an hour", "Weniger als eine Stunde", "Moins d’une heure", "Menos de una hora"],
        .feedOneToTwo: ["1–2 часа", "1–2 hours", "1–2 Stunden", "1 à 2 heures", "1–2 horas"],
        .feedTwoToFour: ["2–4 часа", "2–4 hours", "2–4 Stunden", "2 à 4 heures", "2–4 horas"],
        .feedOverFour: ["Больше 4 часов", "Over 4 hours", "Mehr als 4 Stunden", "Plus de 4 heures", "Más de 4 horas"],
        .obLookEyebrow: ["СВОЙ ВИД", "YOUR LOOK", "DEIN LOOK", "TON STYLE", "TU ESTILO"],
        .obLookTitle: ["Каким будет стих?", "How should your verse look?", "Wie soll dein Vers aussehen?", "À quoi ressemblera ton verset ?", "¿Cómo será tu versículo?"],
        .obLookSub: ["Цвет или картинка — так он будет выглядеть на экране блокировки и в виджетах",
                     "A colour or a picture — this is how it will look on your lock screen and in widgets",
                     "Farbe oder Bild — so sieht er auf dem Sperrbildschirm und in Widgets aus",
                     "Une couleur ou une image — c’est ainsi qu’il apparaîtra sur l’écran verrouillé et dans les widgets",
                     "Un color o una imagen: así se verá en la pantalla de bloqueo y en los widgets"],
        .obFirstTitle: ["Первый стих — прямо сейчас", "Your first verse, right now", "Dein erster Vers — jetzt gleich", "Ton premier verset, tout de suite", "Tu primer versículo, ahora mismo"],
        .obFirstSub: ["Нажми — и он придёт уведомлением, так же, как будет приходить каждый день",
                      "Tap, and it arrives as a notification — just as it will every day",
                      "Tippe — und er kommt als Mitteilung, so wie jeden Tag",
                      "Touche, et il arrive en notification, comme il arrivera chaque jour",
                      "Toca y llegará como notificación, igual que llegará cada día"],
        .obFirstCta: ["Прислать первый стих", "Send my first verse", "Ersten Vers schicken", "Envoyer mon premier verset", "Enviar mi primer versículo"],
        .obFirstSentTitle: ["Первый стих уже пришёл ↑", "Your first verse is here ↑", "Dein erster Vers ist da ↑", "Ton premier verset est arrivé ↑", "Tu primer versículo ya llegó ↑"],
        .obFirstSentSub: ["Так он будет приходить каждый день в %@ — время меняется в «Местах». Это тот же стих, что на экране сейчас",
                          "It will come like this every day at %@ — change the time in Places. It is the same verse as on your screen now",
                          "So kommt er jeden Tag um %@ — die Uhrzeit änderst du unter „Orte“. Es ist derselbe Vers wie jetzt auf dem Bildschirm",
                          "Il arrivera ainsi chaque jour à %@ — l’heure se change dans « Endroits ». C’est le même verset qu’à l’écran maintenant",
                          "Llegará así cada día a las %@: la hora se cambia en «Lugares». Es el mismo versículo que ves ahora en pantalla"],
        .obIconEyebrow: ["ТВОЯ LAMPADA", "YOUR LAMPADA", "DEINE LAMPADA", "TA LAMPADA", "TU LAMPADA"],
        .obIconTitle: ["Какой будет иконка?", "Which icon will it be?", "Welches Symbol soll es sein?", "Quelle icône choisir ?", "¿Qué icono quieres?"],
        .obIconSub: ["Меняется сразу — загляни на рабочий стол. Платные включатся с Pro",
                     "It changes right away — take a look at your home screen. Paid ones switch on with Pro",
                     "Es ändert sich sofort — schau auf den Home-Bildschirm. Die kostenpflichtigen gibt es mit Pro",
                     "Elle change tout de suite — regarde ton écran d’accueil. Les payantes s’activent avec Pro",
                     "Cambia al instante: mira tu pantalla de inicio. Los de pago se activan con Pro"],
        .obIconKeep: ["Оставить основную", "Keep the main one", "Hauptsymbol behalten", "Garder l’icône principale", "Dejar el principal"],
        .obWidgetEyebrow: ["ГЛАВНОЕ МЕСТО", "THE MAIN SPOT", "DER WICHTIGSTE ORT", "L’ENDROIT CLÉ", "EL LUGAR CLAVE"],
        .obWidgetTitle: ["Теперь — на экран блокировки", "Now, onto the lock screen", "Jetzt auf den Sperrbildschirm", "Maintenant, sur l’écran verrouillé", "Ahora, a la pantalla de bloqueo"],
        .obWidgetSub: ["Три касания — и стих будет там при каждом взгляде на телефон",
                       "Three taps, and the verse is there every time you glance at your phone",
                       "Drei Tipps — und der Vers ist bei jedem Blick aufs Telefon da",
                       "Trois touches, et le verset sera là à chaque coup d’œil au téléphone",
                       "Tres toques y el versículo estará ahí cada vez que mires el teléfono"],
        .obWidgetCta: ["Показать, как поставить", "Show me how", "Zeig mir, wie", "Montre-moi comment", "Muéstrame cómo"],
        .obWidgetLater: ["Поставлю позже", "I will add it later", "Mache ich später", "Je le ferai plus tard", "Lo pondré después"],
        .obDoneEyebrow: ["✓ ВИДЖЕТ НА МЕСТЕ", "✓ WIDGET IN PLACE", "✓ WIDGET IST DA", "✓ WIDGET EN PLACE", "✓ WIDGET EN SU SITIO"],
        .obDoneTitle: ["Готово — стих уже на экране", "Done — the verse is on your screen", "Fertig — der Vers ist auf dem Bildschirm", "C’est fait — le verset est à l’écran", "Listo: el versículo ya está en tu pantalla"],
        .obDoneFooter: ["Он будет встречать тебя каждый раз, когда берёшь телефон", "It will greet you every time you pick up your phone", "Er begrüßt dich jedes Mal, wenn du das Telefon nimmst", "Il t’accueillera chaque fois que tu prends ton téléphone", "Te recibirá cada vez que cojas el teléfono"],
        .obWhyLead: ["В этом году ты возьмёшь телефон", "This year you will pick up your phone", "Dieses Jahr nimmst du dein Telefon", "Cette année, tu prendras ton téléphone", "Este año cogerás el teléfono"],
        .obWhyNumber: ["35 000 раз", "35,000 times", "35 000 Mal", "35 000 fois", "35 000 veces"],
        .obWhyQuestion: ["Сколько из них начнутся со Слова?", "How many will start with the Word?", "Wie viele davon beginnen mit dem Wort?", "Combien commenceront par la Parole ?", "¿Cuántas empezarán con la Palabra?"],
        .obWhySource: ["В среднем телефон разблокируют 96 раз в день — за год набегает около 35 000",
                       "On average a phone is unlocked 96 times a day — about 35,000 a year",
                       "Im Schnitt wird ein Telefon 96-mal am Tag entsperrt — rund 35 000 im Jahr",
                       "En moyenne, un téléphone est déverrouillé 96 fois par jour — environ 35 000 par an",
                       "De media, un teléfono se desbloquea 96 veces al día: unas 35 000 al año"],
        .obWhyCta: ["Пусть каждый", "Let every one", "Jede einzelne", "Que chacune", "Que todas"],
        .versesUnit: ["стих|стиха|стихов", "verse|verses", "Vers|Verse", "verset|versets", "versículo|versículos"],
        .daysUnit: ["день|дня|дней", "day|days", "Tag|Tage", "jour|jours", "día|días"],
        .fontsUnit: ["шрифт|шрифта|шрифтов", "typeface|typefaces", "Schrift|Schriften", "police|polices", "tipografía|tipografías"],
        .iconsUnit: ["иконка|иконки|иконок", "icon|icons", "Symbol|Symbole", "icône|icônes", "icono|iconos"],
        .pwTitle: ["Пусть светильник не гаснет", "Let the lamp keep burning", "Lass das Licht nicht erlöschen", "Que la lampe ne s’éteigne pas", "Que la lámpara no se apague"],
        .pwTitleGeneric: ["Зажечь весь телефон", "Light up the whole phone", "Das ganze Telefon erleuchten", "Illuminer tout le téléphone", "Enciende todo el teléfono"],
        .pwSub: ["Lampada живёт без рекламы и без инвесторов — только на тех, кто ей пользуется. Подписка — это масло в светильнике",
                 "Lampada runs with no ads and no investors — only on the people who use it. A subscription is the oil in the lamp",
                 "Lampada lebt ohne Werbung und ohne Investoren — nur von denen, die sie nutzen. Ein Abo ist das Öl in der Lampe",
                 "Lampada vit sans pub et sans investisseurs — seulement grâce à ceux qui s’en servent. L’abonnement, c’est l’huile de la lampe",
                 "Lampada vive sin anuncios ni inversores: solo de quienes la usan. La suscripción es el aceite de la lámpara"],
        .pwComfortEyebrow: ["ПОД ТО, ЧТО НА СЕРДЦЕ", "FOR WHAT IS ON YOUR HEART", "FÜR DAS, WAS DICH BEWEGT", "POUR CE QUE TU AS SUR LE CŒUR", "PARA LO QUE LLEVAS DENTRO"],
        .pwComfortTitle: ["Слово рядом, когда тяжело", "The Word close by when it is hard", "Das Wort ist nah, wenn es schwer ist", "La Parole tout près quand c’est dur", "La Palabra cerca cuando cuesta"],
        .pwComfortSub: ["Ночью — на тумбочке в StandBy, днём — на экране блокировки, в картинке, которая успокаивает",
                        "At night on your nightstand in StandBy, by day on your lock screen, in a picture that calms",
                        "Nachts auf dem Nachttisch in StandBy, tagsüber auf dem Sperrbildschirm — in einem Bild, das zur Ruhe bringt",
                        "La nuit sur la table de chevet en StandBy, le jour sur l’écran verrouillé, dans une image qui apaise",
                        "De noche en la mesita con StandBy, de día en la pantalla de bloqueo, en una imagen que calma"],
        .pwDailyEyebrow: ["КАЖДЫЙ ДЕНЬ В %@", "EVERY DAY AT %@", "JEDEN TAG UM %@", "CHAQUE JOUR À %@", "CADA DÍA A LAS %@"],
        .pwDailyTitle: ["Стих везде, куда ты смотришь", "The verse wherever you look", "Der Vers überall, wohin du schaust", "Le verset partout où tu regardes", "El versículo donde mires"],
        .pwDailySub: ["Ты берёшь телефон 35 000 раз в год. С Pro стих встречает тебя и на тумбочке, и на обоях",
                      "You pick up your phone 35,000 times a year. With Pro the verse meets you on the nightstand and on your wallpaper too",
                      "Du nimmst dein Telefon 35 000 Mal im Jahr. Mit Pro begegnet dir der Vers auch auf dem Nachttisch und im Hintergrundbild",
                      "Tu prends ton téléphone 35 000 fois par an. Avec Pro, le verset t’accueille aussi sur la table de chevet et en fond d’écran",
                      "Coges el teléfono 35 000 veces al año. Con Pro, el versículo te recibe también en la mesita y en el fondo de pantalla"],
        .chipDailyVerse: ["Стих дня", "Verse of the day", "Vers des Tages", "Verset du jour", "Versículo del día"],
        .pwFeedEyebrow: ["ПАУЗА — БЕСПЛАТНО НАВСЕГДА", "THE PAUSE IS FREE FOREVER", "DIE PAUSE BLEIBT KOSTENLOS", "LA PAUSE, GRATUITE POUR TOUJOURS", "LA PAUSA, GRATIS PARA SIEMPRE"],
        .pwFeedTitle: ["Меньше ленты — больше Слова", "Less feed, more Word", "Weniger Feed, mehr Wort", "Moins de fil, plus de Parole", "Menos feed, más Palabra"],
        .pwFeedSub: ["Пауза перед соцсетями остаётся бесплатной. Pro — чтобы стих был на всех экранах и выглядел так, как тебе хочется",
                     "The pause before social media stays free. Pro puts the verse on every screen, looking the way you like",
                     "Die Pause vor sozialen Medien bleibt kostenlos. Mit Pro ist der Vers auf allen Bildschirmen — so, wie es dir gefällt",
                     "La pause avant les réseaux reste gratuite. Pro met le verset sur tous les écrans, avec le style que tu veux",
                     "La pausa antes de las redes sigue siendo gratis. Pro pone el versículo en todas las pantallas, con el aspecto que quieras"],
        .pwBeautyTitle: ["Сделай его своим", "Make it yours", "Mach ihn zu deinem", "Fais-le tien", "Hazlo tuyo"],
        .pwBeautySub: ["Иконка и картинка, которые ты выбрал, включатся с Pro. А с ними — все наборы и картинки, %@ и %@",
                       "The icon and picture you chose switch on with Pro. And with them, every colour set and picture, %@ and %@",
                       "Symbol und Bild, die du gewählt hast, gibt es mit Pro. Dazu alle Farbsets und Bilder, %@ und %@",
                       "L’icône et l’image que tu as choisies s’activent avec Pro. Et avec elles, tous les jeux et images, %@ et %@",
                       "El icono y la imagen que elegiste se activan con Pro. Y con ellos, todos los juegos e imágenes, %@ y %@"],
        .pwBeautySubNoPick: ["С Pro — все наборы и картинки, %@ и %@", "With Pro: every colour set and picture, %@ and %@", "Mit Pro: alle Farbsets und Bilder, %@ und %@", "Avec Pro : tous les jeux et images, %@ et %@", "Con Pro: todos los juegos e imágenes, %@ y %@"],
        .unlockStandBy: ["StandBy", "StandBy", "StandBy", "StandBy", "StandBy"],
        .unlockWallpaper: ["Обои", "Wallpaper", "Hintergrund", "Fond d’écran", "Fondo"],
        .unlockSets: ["Все наборы", "All colour sets", "Alle Farbsets", "Tous les jeux", "Todos los juegos"],
        .unlockPictures: ["Все картинки", "All pictures", "Alle Bilder", "Toutes les images", "Todas las imágenes"],
        .unlockFonts: ["Шрифты", "Typefaces", "Schriften", "Polices", "Tipografías"],
        .unlockIcons: ["Иконки", "App icons", "App-Symbole", "Icônes d’app", "Iconos de app"],
        .planWeek: ["Неделя", "Week", "Woche", "Semaine", "Semana"],
        .planMonth: ["Месяц", "Month", "Monat", "Mois", "Mes"],
        .planYear: ["Год", "Year", "Jahr", "An", "Año"],
        .planWeekNote: ["в неделю", "per week", "pro Woche", "par semaine", "por semana"],
        .planMonthNote: ["в месяц", "per month", "pro Monat", "par mois", "por mes"],
        .planYearNote: ["7 дней бесплатно", "7 days free", "7 Tage gratis", "7 jours offerts", "7 días gratis"],
        .pwTrialCta: ["Начать 7 дней бесплатно", "Start 7 days free", "7 Tage gratis starten", "Commencer 7 jours offerts", "Empezar 7 días gratis"],
        .pwSubscribeCta: ["Подписаться за %@", "Subscribe for %@", "Für %@ abonnieren", "S’abonner pour %@", "Suscribirse por %@"],
        .pwAfterTrial: ["Потом %@ в год · отменить можно в любой момент",
                        "Then %@ a year · cancel anytime",
                        "Danach %@ pro Jahr · jederzeit kündbar",
                        "Puis %@ par an · résiliable à tout moment",
                        "Luego %@ al año · cancela cuando quieras"],
        .pwCancelAnytime: ["Отменить можно в любой момент",
                           "Cancel anytime",
                           "Jederzeit kündbar",
                           "Résiliable à tout moment",
                           "Cancela cuando quieras"],
        .pwHowTrial: ["Как работает пробный период", "How the free trial works", "So funktioniert die Testphase", "Comment marche l’essai", "Cómo funciona la prueba"],
        // Раньше в этой подписи стояло «· Условия», хотя кнопка только
        // восстанавливала покупки: ссылки на условия на экране не было вовсе.
        .pwRestore: ["Восстановить покупки", "Restore purchases", "Käufe wiederherstellen", "Restaurer les achats", "Restaurar compras"],
        .pwTerms: ["Условия использования", "Terms of Use", "Nutzungsbedingungen", "Conditions d’utilisation", "Condiciones de uso"],
        .pwPrivacy: ["Конфиденциальность", "Privacy Policy", "Datenschutz", "Confidentialité", "Privacidad"],
        // Подпись на закрытом StandBy. Места там на две строки мелким кеглем,
        // поэтому коротко и без глагола там, где язык позволяет.
        .standByLocked: ["StandBy — в Lampada Pro",
                         "StandBy comes with Lampada Pro",
                         "StandBy gibt es mit Lampada Pro",
                         "StandBy est inclus dans Lampada Pro",
                         "StandBy viene con Lampada Pro"],
        // Лист после конца подписки. Безлично: в онбординге приложение на «ты»,
        // в инструкциях на «вы», а этот лист видят и те, и другие.
        .proEndedTitle: ["Подписка закончилась",
                         "Your subscription has ended",
                         "Das Abo ist abgelaufen",
                         "L’abonnement a pris fin",
                         "La suscripción ha terminado"],
        .proEndedBody: ["Оформление вернулось к бесплатному. StandBy, платные наборы, картинки, шрифты и иконки снова откроются с Lampada Pro.",
                        "The look is back to the free version. StandBy and the Pro colour sets, pictures, typefaces and icons return with Lampada Pro.",
                        "Das Aussehen ist wieder kostenlos. StandBy sowie die Pro-Farbsets, -Bilder, -Schriften und -Symbole gibt es wieder mit Lampada Pro.",
                        "L’apparence est revenue à la version gratuite. StandBy et les couleurs, images, polices et icônes Pro reviennent avec Lampada Pro.",
                        "El aspecto ha vuelto a la versión gratuita. StandBy y los colores, imágenes, tipografías e iconos Pro vuelven con Lampada Pro."],
        .proEndedCta: ["Вернуть Lampada Pro",
                       "Get Lampada Pro back",
                       "Lampada Pro zurückholen",
                       "Retrouver Lampada Pro",
                       "Recuperar Lampada Pro"],
        .coachSwipe: ["Листайте вверх — придёт другой стих. Тап по дате вернёт сегодняшний",
                      "Swipe up for another verse. Tap the date to come back to today’s",
                      "Nach oben wischen für einen anderen Vers. Tippen Sie auf das Datum, um zum heutigen zurückzukehren",
                      "Balayez vers le haut pour un autre verset. Touchez la date pour revenir à celui du jour",
                      "Desliza hacia arriba para otro versículo. Toca la fecha para volver al de hoy"],
        .coachAreas: ["Три места, где стих попадается на глаза: сам экран, виджеты и экран блокировки. Каждое настраивается отдельно",
                      "Three places the verse meets you: the app, widgets and the lock screen. Each is set up separately",
                      "Drei Orte, an denen der Vers Ihnen begegnet: die App, Widgets und der Sperrbildschirm. Jeder wird getrennt eingestellt",
                      "Trois endroits où le verset vous croise : l’app, les widgets et l’écran verrouillé. Chacun se règle à part",
                      "Tres lugares donde el versículo te encuentra: la app, los widgets y la pantalla de bloqueo. Cada uno se ajusta aparte"],
        .coachAppStyle: ["Выберите цвет или картинку — так будет выглядеть само приложение",
                         "Pick a colour or a picture — that is how the app itself will look",
                         "Wählen Sie eine Farbe oder ein Bild — so wird die App selbst aussehen",
                         "Choisissez une couleur ou une image — c’est ainsi que l’app apparaîtra",
                         "Elige un color o una imagen: así se verá la app"],
        .coachSwitchToWidgets: ["Теперь переключитесь на «Виджеты»",
                                "Now switch to Widgets",
                                "Wechseln Sie nun zu „Widgets“",
                                "Passez maintenant à « Widgets »",
                                "Ahora cambia a «Widgets»"],
        .coachWidgetStyle: ["У виджетов оформление своё. Выберите цвет или картинку и для них",
                            "Widgets have a look of their own. Pick a colour or a picture for them too",
                            "Widgets haben ein eigenes Aussehen. Wählen Sie auch für sie eine Farbe oder ein Bild",
                            "Les widgets ont leur propre apparence. Choisissez aussi une couleur ou une image pour eux",
                            "Los widgets tienen su propio aspecto. Elige también un color o una imagen para ellos"],
        .coachPlaces: ["Тапните по плитке — покажу, как поставить стих в это место",
                       "Tap a tile and I will show you how to put the verse there",
                       "Tippen Sie auf eine Kachel — ich zeige, wie der Vers dorthin kommt",
                       "Touchez une tuile et je montre comment y mettre le verset",
                       "Toca una tarjeta y te muestro cómo poner ahí el versículo"],
        .coachMarkDone: ["А переключателем отметьте, что поставили",
                         "And flip the switch once you have done it",
                         "Und mit dem Schalter markieren Sie, dass es erledigt ist",
                         "Et cochez l’interrupteur une fois que c’est fait",
                         "Y marca el interruptor cuando lo hayas hecho"],
        .coachSkip: ["Пропустить", "Skip", "Überspringen", "Passer", "Omitir"],
        .coachNext: ["Дальше", "Next", "Weiter", "Suivant", "Siguiente"],
        .coachDone: ["Готово", "Done", "Fertig", "Terminé", "Listo"],
        .manageSubscription: ["Подписка", "Subscription", "Abonnement", "Abonnement", "Suscripción"],
        .back: ["Назад", "Back", "Zurück", "Retour", "Atrás"],
        .notNow: ["Не сейчас", "Not now", "Nicht jetzt", "Pas maintenant", "Ahora no"],
        .sceneShepherd: ["Пастырь", "The Shepherd", "Der Hirte", "Le Berger", "El Pastor"],
        .sceneClouds: ["Облака", "Clouds", "Wolken", "Nuages", "Nubes"],
        .scenePastel: ["Пастель", "Pastel", "Pastell", "Pastel", "Pastel"],
        .sceneOldBook: ["Старая книга", "Old book", "Altes Buch", "Vieux livre", "Libro antiguo"],
        .sceneFresco: ["Ночная фреска", "Night fresco", "Nachtfresko", "Fresque nocturne", "Fresco nocturno"],
        .sceneChrist: ["Спаситель", "The Saviour", "Der Erlöser", "Le Sauveur", "El Salvador"],
        .scenePaul: ["Апостол Павел", "Saint Paul", "Apostel Paulus", "Saint Paul", "San Pablo"],
        .sceneDavid: ["Царь Давид", "King David", "König David", "Le roi David", "Rey David"],
        .sceneGalilee: ["Галилея", "Galilee", "Galiläa", "Galilée", "Galilea"],
        .sceneStar: ["Звезда", "Star", "Stern", "Étoile", "Estrella"],
        .sceneGethsemane: ["Гефсимания", "Gethsemane", "Gethsemane", "Gethsémani", "Getsemaní"],
        .sceneCross: ["Крест", "Cross", "Kreuz", "Croix", "Cruz"],
        .colourSets: ["Цвет", "Colour", "Farbe", "Couleur", "Color"],
        .imageSets: ["Изображение", "Image", "Bild", "Image", "Imagen"],
        .tabToday: ["Сегодня", "Today", "Heute", "Aujourd’hui", "Hoy"],
        .demoVerse: ["ибо у Бога не останется бессильным никакое слово.", "For nothing spoken by God is impossible.", "Denn bei Gott ist kein Ding unmöglich.", "Car rien n’est impossible à Dieu.", "Porque ninguna cosa es imposible para Dios."],
        .demoReference: ["От Луки 1:37", "Luke 1:37", "Lukas 1:37", "Luc 1:37", "San Lucas 1:37"],
        .pauseVerse: ["А Мария сохраняла все слова сии, слагая в сердце Своем.", "But Mary kept all these sayings, pondering them in her heart.", "Maria aber behielt alle diese Worte und bewegte sie in ihrem Herzen.", "Marie gardait toutes ces choses, et les repassait dans son cœur.", "Mas María guardaba todas estas cosas, confiriéndolas en su corazón."],
        .pauseReference: ["От Луки 2:19", "Luke 2:19", "Lukas 2:19", "Luc 2:19", "San Lucas 2:19"],
        // Тексты уведомлений, скидки, листа отмены — утверждены 27.10.
        .obNotifyEyebrow: ["СТИХ ДНЯ", "VERSE OF THE DAY", "VERS DES TAGES", "VERSET DU JOUR", "VERSÍCULO DEL DÍA"],
        .obTrackEyebrow: ["ОДИН ВОПРОС", "ONE QUESTION", "EINE FRAGE", "UNE QUESTION", "UNA PREGUNTA"],
        .obTrackTitle: ["Сейчас iPhone спросит про отслеживание", "Your iPhone is about to ask about tracking",
                        "Gleich fragt dein iPhone nach Tracking", "Ton iPhone va te poser une question sur le suivi",
                        "Tu iPhone te va a preguntar por el rastreo"],
        .obTrackSub: ["Lampada находит людей через рекламу в Instagram и Facebook. Если разрешишь, мы узнаем, какая реклама привела тебя, — и перестанем платить за ту, что не работает. Стихи и твои ответы туда не уходят. Ответ можно поменять в Настройках iPhone",
                      "Lampada finds people through ads on Instagram and Facebook. If you allow it, we learn which ad brought you here — and stop paying for the ones that don’t work. Your verses and answers are never shared. You can change this in iPhone Settings",
                      "Lampada findet Menschen über Werbung auf Instagram und Facebook. Wenn du es erlaubst, sehen wir, welche Anzeige dich hergebracht hat — und zahlen nicht mehr für die, die nichts bringen. Verse und deine Antworten werden nicht weitergegeben. Ändern kannst du das in den iPhone-Einstellungen",
                      "Lampada se fait connaître grâce à des pubs sur Instagram et Facebook. Si tu l’autorises, nous saurons quelle pub t’a amené ici — et nous arrêterons de payer pour celles qui ne marchent pas. Les versets et tes réponses ne sont jamais partagés. Tu peux changer ce choix dans les Réglages de l’iPhone",
                      "Lampada llega a la gente con anuncios en Instagram y Facebook. Si lo permites, sabremos qué anuncio te trajo aquí y dejaremos de pagar por los que no funcionan. Los versículos y tus respuestas no se comparten. Puedes cambiarlo en Ajustes del iPhone"],
        .obTrackCta: ["Продолжить", "Continue", "Weiter", "Continuer", "Continuar"],
        .notifyNow: ["сейчас", "now", "jetzt", "maintenant", "ahora"],
        .dailyVerseTitle: ["Стих дня в уведомлении", "Verse of the day as a notification", "Vers des Tages als Mitteilung", "Verset du jour en notification", "Versículo del día como notificación"],
        .dailyVerseOn: ["Каждый день в %@", "Every day at %@", "Täglich um %@", "Chaque jour à %@", "Cada día a las %@"],
        .dailyVerseOff: ["Выключено", "Off", "Aus", "Désactivé", "Desactivado"],
        .dailyVerseSub: ["Тот же стих, что на «Сегодня», — в выбранное время",
                         "The same verse as on Today, at the time you choose",
                         "Derselbe Vers wie unter „Heute“, zur gewählten Zeit",
                         "Le même verset que dans Aujourd’hui, à l’heure choisie",
                         "El mismo versículo que en Hoy, a la hora que elijas"],
        .dailyVerseTime: ["Время", "Time", "Uhrzeit", "Heure", "Hora"],
        .notifyDenied: ["Уведомления для Lampada выключены в настройках iPhone",
                        "Notifications for Lampada are turned off in iPhone Settings",
                        "Mitteilungen für Lampada sind in den iPhone-Einstellungen aus",
                        "Les notifications de Lampada sont coupées dans les Réglages de l’iPhone",
                        "Las notificaciones de Lampada están desactivadas en los Ajustes del iPhone"],
        .comeback3Title: ["Стих на сегодня уже ждёт", "Today’s verse is waiting", "Der Vers für heute wartet", "Le verset du jour t’attend", "El versículo de hoy te espera"],
        .comeback3Body: ["Минута тишины — и одна строка, которая останется с тобой на весь день.",
                         "One quiet minute — and a line to carry with you all day.",
                         "Eine stille Minute — und ein Satz, der dich durch den Tag begleitet.",
                         "Une minute de calme — et une phrase à garder toute la journée.",
                         "Un minuto de calma y una frase que te acompañe todo el día."],
        .comeback7Title: ["Неделя без стиха", "A week without a verse", "Eine Woche ohne Vers", "Une semaine sans verset", "Una semana sin versículo"],
        .comeback7Body: ["Поставь его на экран блокировки — и он будет встречать тебя сам, без приложения.",
                         "Put it on your lock screen and it will greet you on its own — no app needed.",
                         "Leg ihn auf den Sperrbildschirm — dann begrüßt er dich von selbst, ohne App.",
                         "Mets-le sur l’écran verrouillé : il t’accueillera tout seul, sans ouvrir l’app.",
                         "Ponlo en la pantalla de bloqueo y te recibirá solo, sin abrir la app."],
        .widgetGoneTitle: ["Стих пропал с экрана?", "Has your verse left the screen?", "Ist dein Vers vom Bildschirm verschwunden?", "Ton verset a quitté l’écran ?", "¿Tu versículo se fue de la pantalla?"],
        .widgetGoneBody: ["Виджета Lampada давно не видно. Вернуть его — двадцать секунд.",
                          "The Lampada widget hasn’t shown up for a while. Putting it back takes twenty seconds.",
                          "Das Lampada-Widget war länger nicht zu sehen. Zurückholen dauert zwanzig Sekunden.",
                          "Le widget Lampada ne s’affiche plus depuis un moment. Le remettre prend vingt secondes.",
                          "Hace tiempo que no aparece el widget de Lampada. Volver a ponerlo lleva veinte segundos."],
        .analyticsTitle: ["Помогать улучшать Lampada", "Help improve Lampada", "Lampada verbessern helfen", "Aider à améliorer Lampada", "Ayudar a mejorar Lampada"],
        .rateApp: ["Оценить Lampada", "Rate Lampada", "Lampada bewerten", "Noter Lampada", "Calificar Lampada"],
        .pushTokenCopied: ["Токен уведомлений скопирован", "Push token copied", "Push-Token kopiert",
                           "Jeton de notification copié", "Token de notificaciones copiado"],
        .analyticsNote: ["Анонимная статистика: что выбирают в начале, какие экраны открывают и где застревают. Без текста стихов.",
                         "Anonymous stats: what people choose at the start, which screens they open and where they get stuck. No verse text.",
                         "Anonyme Statistik: was zu Beginn gewählt wird, welche Bildschirme geöffnet werden und wo es hakt. Ohne Verstexte.",
                         "Statistiques anonymes : ce qu’on choisit au début, quels écrans on ouvre et où l’on bloque. Sans le texte des versets.",
                         "Estadísticas anónimas: qué se elige al principio, qué pantallas se abren y dónde se atasca la gente. Sin el texto de los versículos."],
        .secondHomeTitle: ["Стих уже на экране блокировки", "Your verse is on the lock screen", "Dein Vers ist auf dem Sperrbildschirm", "Ton verset est sur l’écran verrouillé", "Tu versículo está en la pantalla de bloqueo"],
        .secondHomeBody: ["Поставь его и на рабочий стол — будет перед глазами весь день. Двадцать секунд.",
                          "Add it to your Home Screen too — it stays in sight all day. Twenty seconds.",
                          "Leg ihn auch auf den Home-Bildschirm — dann ist er den ganzen Tag im Blick. Zwanzig Sekunden.",
                          "Ajoute-le aussi à l’écran d’accueil : il restera sous tes yeux toute la journée. Vingt secondes.",
                          "Ponlo también en la pantalla de inicio: estará a la vista todo el día. Veinte segundos."],
        .secondLockTitle: ["Стих уже на рабочем столе", "Your verse is on the Home Screen", "Dein Vers ist auf dem Home-Bildschirm", "Ton verset est sur l’écran d’accueil", "Tu versículo está en la pantalla de inicio"],
        .secondLockBody: ["Поставь его и на экран блокировки — увидишь, даже не разблокируя телефон.",
                          "Add it to your lock screen too — you’ll see it without even unlocking.",
                          "Leg ihn auch auf den Sperrbildschirm — du siehst ihn, ohne zu entsperren.",
                          "Ajoute-le aussi à l’écran verrouillé : tu le verras sans même déverrouiller.",
                          "Ponlo también en la pantalla de bloqueo: lo verás sin desbloquear."],
        .cancelTitle: ["Пробная неделя отменена", "Your free week is cancelled", "Deine Gratiswoche ist gekündigt", "Ta semaine gratuite est annulée", "Tu semana gratis está cancelada"],
        .cancelSub: ["Доступ остаётся до конца недели. Подскажи, что не так, — можно отметить несколько.",
                     "You keep access until the week ends. What didn’t work? You can pick more than one.",
                     "Der Zugang bleibt bis zum Ende der Woche. Was hat nicht gepasst? Du kannst mehreres auswählen.",
                     "Tu gardes l’accès jusqu’à la fin de la semaine. Qu’est-ce qui n’a pas marché ? Tu peux en choisir plusieurs.",
                     "Mantienes el acceso hasta que termine la semana. ¿Qué no funcionó? Puedes elegir varias."],
        .cancelSend: ["Отправить", "Send", "Senden", "Envoyer", "Enviar"],
        .cancelSkip: ["Пропустить", "Skip", "Überspringen", "Passer", "Omitir"],
        .cancelThanks: ["Спасибо — это правда помогает", "Thank you — this really helps", "Danke — das hilft wirklich", "Merci, ça aide vraiment", "Gracias, de verdad ayuda"],
        .reasonPrice: ["Дорого", "Too expensive", "Zu teuer", "Trop cher", "Demasiado caro"],
        .reasonUnused: ["Редко открываю", "I rarely use it", "Ich nutze es kaum", "Je l’utilise peu", "Casi no lo uso"],
        .reasonFreeEnough: ["Хватает бесплатного", "The free version is enough", "Die Gratisversion reicht mir", "La version gratuite me suffit", "Me basta la versión gratuita"],
        .reasonNotWhat: ["Не то, что нужно", "Not what I was looking for", "Nicht das, was ich suche", "Pas ce que je cherchais", "No es lo que buscaba"],
        .reasonJustLooking: ["Хотелось просто посмотреть", "I just wanted to look around", "Wollte nur reinschauen", "Je voulais juste regarder", "Solo quería echar un vistazo"],
        .reasonOther: ["Другое", "Something else", "Etwas anderes", "Autre chose", "Otra cosa"],
        .welcomeEyebrow: ["ПОДАРОК К НАЧАЛУ", "A WELCOME GIFT", "EIN WILLKOMMENSGESCHENK", "UN CADEAU DE BIENVENUE", "UN REGALO DE BIENVENIDA"],
        .welcomeTitle: ["Первый год Pro — за %@", "Your first year of Pro for %@", "Dein erstes Pro-Jahr für %@", "Ta première année Pro pour %@", "Tu primer año de Pro por %@"],
        .welcomeSub: ["Вместо %@. Все фоны, наборы и шрифты, StandBy и обои",
                      "Instead of %@. Every background, colour set and font, StandBy and wallpapers",
                      "Statt %@. Alle Hintergründe, Farbsets und Schriften, StandBy und Hintergrundbilder",
                      "Au lieu de %@. Tous les fonds, couleurs et polices, StandBy et fonds d’écran",
                      "En lugar de %@. Todos los fondos, colores y fuentes, StandBy y fondos de pantalla"],
        .welcomeTerms: ["Оплата сразу за первый год, дальше %@ в год. Продлевается автоматически — отменить можно в настройках Apple ID",
                        "Paid once for the first year, then %@ a year. Renews automatically — cancel any time in your Apple ID settings",
                        "Einmalig für das erste Jahr, danach %@ pro Jahr. Verlängert sich automatisch — jederzeit in den Apple-ID-Einstellungen kündbar",
                        "Payé en une fois pour la première année, puis %@ par an. Renouvellement automatique — résiliable à tout moment dans les réglages de l’identifiant Apple",
                        "Un pago por el primer año y después %@ al año. Se renueva automáticamente: cancela cuando quieras en los ajustes de tu Apple ID"],
        .welcomeCta: ["Забрать за %@", "Get it for %@", "Für %@ holen", "En profiter pour %@", "Obtener por %@"],
        .welcomeNo: ["Нет, спасибо", "No, thanks", "Nein, danke", "Non merci", "No, gracias"],
        // «Что нового» в 1.0.2 — макет 05.11, тексты утверждены 08.11.
        .wnIconsEyebrow: ["НОВОЕ В LAMPADA", "NEW IN LAMPADA", "NEU IN LAMPADA", "NOUVEAU DANS LAMPADA", "NOVEDADES EN LAMPADA"],
        .wnIconsTitle: ["Пять новых иконок", "Five new icons", "Fünf neue Symbole", "Cinq nouvelles icônes", "Cinco iconos nuevos"],
        .wnIconsSub: ["Голубь — бесплатно, для всех: тапни, и он уже на рабочем столе. Остальные четыре — с Pro",
                      "The Dove is free for everyone: tap it and it’s on your home screen. The other four come with Pro",
                      "Die Taube ist für alle kostenlos: antippen, und sie ist auf dem Home-Bildschirm. Die anderen vier gibt es mit Pro",
                      "La Colombe est gratuite pour tous : touche-la et elle est sur ton écran d’accueil. Les quatre autres sont avec Pro",
                      "La Paloma es gratis para todos: tócala y ya está en tu pantalla de inicio. Los otros cuatro, con Pro"],
        .wnFree: ["бесплатно", "free", "kostenlos", "gratuite", "gratis"],
        .wnSkip: ["Пропустить", "Skip", "Überspringen", "Passer", "Omitir"],
        .wnPicturesEyebrow: ["НОВЫЕ КАРТИНКИ", "NEW PICTURES", "NEUE BILDER", "NOUVELLES IMAGES", "IMÁGENES NUEVAS"],
        .wnPicturesTitle: ["Четыре новые картинки", "Four new pictures", "Vier neue Bilder", "Quatre nouvelles images", "Cuatro imágenes nuevas"],
        .wnPicturesSub: ["Фон для стиха в приложении, виджетах и на обоях. Тапни — посмотришь со своим стихом",
                         "A background for your verse in the app, widgets and wallpaper. Tap to see it with your verse",
                         "Ein Hintergrund für deinen Vers in der App, in Widgets und als Hintergrundbild. Tippe, um ihn mit deinem Vers zu sehen",
                         "Un fond pour ton verset dans l’app, les widgets et en fond d’écran. Touche pour le voir avec ton verset",
                         "Un fondo para tu versículo en la app, los widgets y el fondo de pantalla. Tócalo para verlo con tu versículo"],
        .wnSetPicture: ["Поставить фоном", "Use as background", "Als Hintergrund nehmen", "Mettre en fond", "Poner de fondo"],
        .wnUnlockPicture: ["Включить с Pro", "Unlock with Pro", "Mit Pro freischalten", "Débloquer avec Pro", "Desbloquear con Pro"],
        .wnDailyTitle: ["Пусть стих приходит сам", "Let the verse come to you", "Lass den Vers zu dir kommen", "Laisse le verset venir à toi", "Deja que el versículo venga a ti"],
        .wnDailySub: ["Одно уведомление в день, в %@ — тот же стих, что у тебя на экране. Без рекламы. Время меняется в «Местах»",
                      "One notification a day at %@ — the same verse as on your screen. No ads. Change the time in Places",
                      "Eine Mitteilung am Tag um %@ — derselbe Vers wie auf deinem Bildschirm. Ohne Werbung. Die Uhrzeit änderst du unter „Orte“",
                      "Une notification par jour à %@ — le même verset qu’à ton écran. Sans pub. L’heure se change dans « Endroits »",
                      "Una notificación al día a las %@: el mismo versículo que en tu pantalla. Sin anuncios. La hora se cambia en «Lugares»"],
        .wnDailyCta: ["Присылать стих каждый день", "Send me a verse every day", "Jeden Tag einen Vers schicken", "M’envoyer un verset chaque jour", "Enviarme un versículo cada día"],
        .wnDone: ["Готово", "Done", "Fertig", "Terminé", "Listo"],
        .promoTitle: ["Новости и обновления", "News and updates", "Neuigkeiten und Updates", "Nouveautés et mises à jour", "Novedades y actualizaciones"],
        .promoSub: ["Иногда — о новых иконках, картинках и предложениях. Выключить можно в «Местах»",
                    "Now and then — new icons, pictures and offers. Turn it off any time in Places",
                    "Ab und zu — neue Symbole, Bilder und Angebote. Jederzeit abschaltbar unter „Orte“",
                    "De temps en temps — nouvelles icônes, images et offres. À désactiver quand tu veux dans « Endroits »",
                    "De vez en cuando: iconos, imágenes y ofertas nuevas. Se apaga cuando quieras en «Lugares»"],
        .promoPlacesSub: ["Новинки и предложения", "New features and offers", "Neues und Angebote", "Nouveautés et offres", "Novedades y ofertas"],
        .pwPickedEyebrow: ["ТВОЙ ВЫБОР", "YOUR PICK", "DEINE WAHL", "TON CHOIX", "TU ELECCIÓN"],
        .corpusFailedTitle: ["Не удалось прочитать корпус", "Could not read the corpus", "Korpus konnte nicht gelesen werden", "Impossible de lire le corpus", "No se pudo leer el corpus"],
        .corpusFailedHint: ["Переустановите приложение", "Reinstall the app", "App neu installieren", "Réinstallez l’application", "Reinstala la aplicación"],
    ]
}

extension L10n {
    /// Название состояния для чипов в онбординге.
    ///
    /// Состояния лежат в корпусе одинаковыми во всех изданиях — по ним
    /// фильтруется пул, и общий идентификатор здесь правильный. Но показывать
    /// его нельзя: в английской сборке чипы были русскими. Отдельная таблица, а
    /// не ключи в общем перечислении, потому что список задаёт корпус, а не код;
    /// тест сверяет одно с другим.
    public func theme(_ id: String) -> String {
        switch locale {
        case .pt: return L10n.portugueseThemes[id] ?? id
        case .it: return L10n.italianThemes[id] ?? id
        case .ko: return L10n.koreanThemes[id] ?? id
        case .ru, .en, .de, .fr, .es:
            guard let row = L10n.themes[id] else { return id }
            return row[index]
        }
    }

    /// Порядок значений тот же: ru, en, de, fr, es.
    static let themes: [String: [String]] = [
        "бессонница": ["Бессонница", "Sleeplessness", "Schlaflosigkeit", "Insomnie", "Insomnio"],
        "благодарность": ["Благодарность", "Gratitude", "Dankbarkeit", "Gratitude", "Gratitud"],
        "вина": ["Вина", "Guilt", "Schuld", "Culpabilité", "Culpa"],
        "доверие": ["Доверие", "Trust", "Vertrauen", "Confiance", "Confianza"],
        "любовь": ["Любовь", "Love", "Liebe", "Amour", "Amor"],
        "надежда": ["Надежда", "Hope", "Hoffnung", "Espérance", "Esperanza"],
        "начало дела": ["Начало дела", "A new start", "Neuanfang", "Nouveau départ", "Un nuevo comienzo"],
        "немощь": ["Немощь", "Weakness", "Schwäche", "Faiblesse", "Debilidad"],
        "одиночество": ["Одиночество", "Loneliness", "Einsamkeit", "Solitude", "Soledad"],
        "прощение": ["Прощение", "Forgiveness", "Vergebung", "Pardon", "Perdón"],
        "решение": ["Решение", "A decision", "Entscheidung", "Décision", "Decisión"],
        "сомнение": ["Сомнение", "Doubt", "Zweifel", "Doute", "Duda"],
        "страх": ["Страх", "Fear", "Angst", "Peur", "Miedo"],
        "тревога": ["Тревога", "Anxiety", "Unruhe", "Anxiété", "Ansiedad"],
        "усталость": ["Усталость", "Tiredness", "Müdigkeit", "Fatigue", "Cansancio"],
        "утрата": ["Утрата", "Loss", "Verlust", "Deuil", "Pérdida"],
    ]

    /// Номер языка в строке таблицы.
    var index: Int {
        switch locale {
        case .ru: 0
        case .en: 1
        case .de: 2
        case .fr: 3
        case .es: 4
        // У новых языков своих столбцов в таблицах нет — их строки в
        // отдельных словарях. Здесь английский как запасной.
        case .pt, .it, .ko: 1
        }
    }

    /// Название поверхности. Отдельный метод, потому что у StandBy и Apple Watch
    /// переводить нечего — это имена продуктов Apple.
    public func name(_ surface: Surface) -> String {
        surface.titleKey.map { self[$0] } ?? surface.untranslatedTitle
    }

    /// Дата для макета экрана блокировки.
    ///
    /// Число условное — как и 9:41 на всех снимках Apple, — но написано оно
    /// должно быть на языке интерфейса: раньше там стояла строка «вторник,
    /// 3 сентября», и на английском макет получался наполовину русским.
    public var mockDate: String {
        let calendar = Calendar(identifier: .gregorian)
        guard let date = calendar.date(from: DateComponents(year: 2025, month: 9, day: 3))
        else { return "" }
        return date.formatted(
            .dateTime.weekday(.wide).day().month(.wide)
                .locale(Locale(identifier: locale.rawValue))
        )
    }
}
