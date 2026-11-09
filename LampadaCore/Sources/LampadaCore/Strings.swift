import Foundation

/// Строки интерфейса на трёх языках: русский, английский, арабский.
///
/// Таблица в коде, а не `.strings`-файлы, по одной причине: язык интерфейса
/// здесь выбирает человек в настройках приложения, а не система. Стандартный
/// механизм локализации подставляет язык устройства и заставляет держать
/// отдельный `Bundle` на каждый `lproj`; здесь же достаточно словаря, который
/// к тому же виден на ревью целиком и не может «потерять ключ» в рантайме.
///
/// Порядок значений в каждой строке всегда один: ru, en, ar.
///
/// ФАЙЛ СГЕНЕРИРОВАН `tools/i18n/gen_strings.py` — не править руками: правки
/// пропадут при следующей сборке. Образцы аятов (`demoVerse`, `pauseVerse`) берутся
/// из исходников корпуса, а не набираются.
public struct L10n: Sendable, Hashable {
    public let locale: AppLocale

    public init(_ locale: AppLocale) {
        self.locale = locale
    }

    public subscript(_ key: Key) -> String {
        let row = L10n.table[key] ?? ["", "", ""]
        let value = switch locale {
        case .ru: row[0]
        case .en: row[1]
        case .ar: row[2]
        }
        guard value.isEmpty else { return value }
        // Пустая строка означает недостающий перевод: показываем английский, а
        // не пустоту. Заметить это на глаз проще, чем дыру в интерфейсе.
        return row[1]
    }

    /// Подстановка чисел: «Сейчас 3 из 7».
    public func callAsFunction(_ key: Key, _ arguments: CVarArg...) -> String {
        String(format: self[key], arguments: arguments)
    }

    /// Число со словом в нужной форме: «1 день», «22 дня», «45 дней».
    ///
    /// Формы лежат в строке таблицы через вертикальную черту: у русского три
    /// (1, 2–4, 5–20), у английского две, у арабского четыре (1, 2, 3–10, 11 и
    /// больше).
    public func count(_ number: Int, _ key: Key) -> String {
        let forms = self[key].split(separator: "|").map(String.init)
        let index: Int
        switch locale {
        case .ru:
            let ones = number % 10, tens = number % 100
            index = ones == 1 && tens != 11 ? 0
                : (2...4).contains(ones) && !(12...14).contains(tens) ? 1 : 2
        case .ar:
            let tens = number % 100
            index = number == 1 ? 0 : number == 2 ? 1 : (3...10).contains(tens) ? 2 : 3
        case .en:
            index = number == 1 ? 0 : 1
        }
        return "\(number) \(forms[min(index, forms.count - 1)])"
    }

    public enum Key: String, Sendable, Hashable, CaseIterable {
        case epigraph, heroTitle, heroSubtitle, heroAction, heroEditions, languageTitle
        case languageSubtitle, next, themesTitle, themesSubtitle, themesEmpty, themesPicked
        case widgetTitle, widgetSubtitle, widgetAction, widgetLater, pauseEyebrow, pauseTitle
        case pauseSubtitle, pauseAction, pauseWait, pauseClose, pauseNoApp, obVerseEyebrow
        case obVerseCta, obVerseTrust, goalTitle, goalLead, goalHint, goalComfort
        case goalComfortSub, goalDaily, goalDailySub, goalFeed, goalFeedSub, goalBeauty
        case goalBeautySub, obThemesTitle, obThemesSub, obThemesCounter, obTimeEyebrow, obTimeTitle
        case obTimeSub, obTimeLater, obFeedTitle, obFeedSub, obFeedInsight, feedUnderOne
        case feedOneToTwo, feedTwoToFour, feedOverFour, obLookEyebrow, obLookTitle, obLookSub
        case obFirstTitle, obFirstSub, obFirstCta, obFirstSentTitle, obFirstSentSub, obIconEyebrow
        case obIconTitle, obIconSub, obIconKeep, obWidgetEyebrow, obWidgetTitle, obWidgetSub
        case obWidgetCta, obWidgetLater, obDoneEyebrow, obDoneTitle, obDoneFooter, obWhyLead
        case obWhyNumber, obWhyQuestion, obWhySource, obWhyCta, versesUnit, daysUnit
        case fontsUnit, iconsUnit, pwTitle, pwTitleGeneric, pwSub, pwComfortEyebrow
        case pwComfortTitle, pwComfortSub, pwDailyEyebrow, pwDailyTitle, pwDailySub, chipDailyVerse
        case pwFeedEyebrow, pwFeedTitle, pwFeedSub, pwBeautyTitle, pwBeautySub, pwBeautySubNoPick
        case unlockStandBy, unlockWallpaper, unlockSets, unlockPictures, unlockFonts, unlockIcons
        case planWeek, planMonth, planYear, planWeekNote, planMonthNote, planYearNote
        case pwTrialCta, pwSubscribeCta, pwAfterTrial, pwCancelAnytime, pwHowTrial, pwRestore
        case pwTerms, pwPrivacy, standByLocked, proEndedTitle, proEndedBody, proEndedCta
        case stepLock1, stepLock1Hint, stepLock2, stepLock2Hint, stepLock3, stepLock3Hint
        case stepHome1, stepHome1Hint, stepHome2, stepHome2Hint, stepHome3, stepHome3Hint
        case stepControl1, stepControl1Hint, stepControl2, stepControl2Hint, stepControl3, stepControl3Hint
        case stepStandBy1, stepStandBy1Hint, stepStandBy2, stepStandBy2Hint, stepStandBy3, stepStandBy3Hint
        case stepWatch1, stepWatch1Hint, stepWatch2, stepWatch2Hint, stepWatch3, stepWatch3Hint
        case stepWallpaper1, stepWallpaper1Hint, stepWallpaper2, stepWallpaper2Hint, stepWallpaper3, stepWallpaper3Hint
        case stepPause1, stepPause1Hint, stepPause2, stepPause2Hint, stepPause3, stepPause3Hint
        case back, notNow, continueAction, openShortcuts, installShortcut, manageSubscription
        case coachSwipe, coachAreas, coachAppStyle, coachSwitchToWidgets, coachWidgetStyle, coachPlaces
        case coachMarkDone, coachSkip, coachNext, coachDone, colourSets, imageSets
        case tabToday, appIconTitle, iconDefault, iconNight, widgetDisplayName, widgetDescription
        case controlDisplayName, controlDescription, depthHint, surfaceLock, surfaceHome, surfaceControl
        case surfaceWallpaper, surfacePause, howLock, howHome, howControl, howStandBy
        case howWatch, howWallpaper, noteAuto, noteSecondRelease, noteManual, ctaLock
        case ctaHome, ctaControl, ctaStandBy, ctaWatch, ctaWallpaper, ctaPause
        case areaApp, areaWidgets, areaLock, styleNight, styleParchment, styleAmber
        case styleInk, styleDawn, styleOpal, styleCoal, sizeSmall, sizeMedium
        case sizeLarge, lengthShort, lengthFull, alignLeading, alignCenter, formatStory
        case formatSquare, formatWallpaper, backToDaily, share, contextPill, placesTitle
        case placesProgress, groupScreens, groupMoment, lookTitle, preview, size
        case font, languageAndEdition, systemFont, verseLength, alignment, lockColorNote
        case appIcon, shareTitle, sendAction, wordmark, context, understood
        case close, openSettings, markDone, paywallTitle, subscribe, restore
        case paywallLegal, perkSurfaces, perkStyles, perkIcons, demoVerse, demoReference
        case pauseVerse, pauseReference, obNotifyEyebrow, notifyNow, obTrackEyebrow, obTrackTitle
        case obTrackSub, obTrackCta, dailyVerseTitle, dailyVerseOn, dailyVerseOff, dailyVerseSub
        case dailyVerseTime, notifyDenied, comeback3Title, comeback3Body, comeback7Title, comeback7Body
        case widgetGoneTitle, widgetGoneBody, secondHomeTitle, secondHomeBody, secondLockTitle, secondLockBody
        case cancelTitle, cancelSub, cancelSkip, cancelThanks, cancelSend, reasonPrice
        case reasonUnused, reasonFreeEnough, reasonNotWhat, reasonJustLooking, reasonOther, welcomeEyebrow
        case welcomeTitle, welcomeSub, welcomeTerms, welcomeCta, welcomeNo, pwPickedEyebrow
        case analyticsTitle, analyticsNote, wnIconsEyebrow, wnIconsTitle, wnIconsSub, wnFree
        case wnSkip, wnPicturesEyebrow, wnPicturesTitle, wnPicturesSub, wnSetPicture, wnUnlockPicture
        case wnDailyTitle, wnDailySub, wnDailyCta, wnDone, promoTitle, promoSub
        case promoPlacesSub, rateApp, pushTokenCopied, corpusFailedTitle, corpusFailedHint, sceneDesert
        case sceneStars, sceneDome, sceneLantern, sceneGarden, sceneMosaic, sceneLattice
        case iconMosaic, iconStar, iconDawn, iconDome, iconRosette, iconLight
        case styleEmerald, showArabic
    }

    // Порядок в строке: ru, en, ar
    private static let table: [Key: [String]] = [
        .epigraph: ["«Аллах — свет небес и земли»", "“Allah is the Light of the heavens and the earth”", "«اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ»"],
        .heroTitle: ["Аят там, куда ты и так смотришь", "The ayah where you already look", "الآية حيث تنظر أصلًا"],
        .heroSubtitle: ["Экран блокировки, рабочий стол, тумбочка у кровати. Ничего не надо помнить — аят просто есть.", "Lock screen, home screen, bedside table. Nothing to remember — the ayah is simply there.", "شاشة القفل، الشاشة الرئيسية، الطاولة بجانب السرير. لا شيء تتذكره، فالآية حاضرة."],
        .heroAction: ["Зажечь", "Light it", "أضئها"],
        .heroEditions: ["Оригинал на арабском · Pickthall · Саблуков", "Arabic original · Pickthall · Sablukov", "النص العربي · Pickthall · Sablukov"],
        .languageTitle: ["На каком языке", "Which language", "بأي لغة"],
        .languageSubtitle: ["Перевод можно поменять позже в настройках", "You can change the translation later in settings", "يمكنك تغيير الترجمة لاحقًا من الإعدادات"],
        .next: ["Дальше", "Next", "التالي"],
        .themesTitle: ["Что тебе сейчас нужно", "What do you need right now", "ما الذي تحتاجه الآن"],
        .themesSubtitle: ["Отметь одно или несколько. Аяты пойдут за ними", "Pick one or several. The ayat will follow", "اختر واحدًا أو أكثر، وستتبعها الآيات"],
        .themesEmpty: ["Можно ничего не выбирать — тогда будут все аяты", "Choose nothing and you get every ayah", "إن لم تختر شيئًا فستظهر لك كل الآيات"],
        .themesPicked: ["Выбрано %d из %d", "%d of %d selected", "تم اختيار %d من %d"],
        .widgetTitle: ["Поставь виджет", "Add the widget", "أضف الودجت"],
        .widgetSubtitle: ["Экран блокировки — самое видное место в телефоне. Бесплатно, навсегда", "The lock screen is the most visible place on your phone. Free, forever", "شاشة القفل أوضح مكان في هاتفك. مجانًا وللأبد"],
        .widgetAction: ["Показать как", "Show me how", "أرني كيف"],
        .widgetLater: ["Поставлю позже", "I’ll do it later", "سأفعل ذلك لاحقًا"],
        .pauseEyebrow: ["Только у нас", "Only here", "هنا فقط"],
        .pauseTitle: ["Пауза перед лентой", "A pause before the feed", "وقفة قبل التصفح"],
        .pauseSubtitle: ["Открываешь соцсеть — первым тебя встречает аят. Не лента вместо ленты, а секунда там, где ты собирался листать", "You open a social app and an ayah meets you first. Not another feed — one second where you were about to scroll", "تفتح تطبيق تواصل فتستقبلك آية أولًا. لا خلاصة أخرى، بل ثانية قبل أن تبدأ بالتمرير"],
        .pauseAction: ["Включить", "Turn on", "تفعيل"],
        .pauseWait: ["Подожди секунду", "Wait a second", "انتظر لحظة"],
        .pauseClose: ["Закрыть", "Close", "إغلاق"],
        .pauseNoApp: ["В автоматизации не выбрано приложение. Откройте её в «Командах» и укажите его в действии «Пауза с аятом» — тогда кнопка будет возвращать сразу туда", "No app is chosen in the automation. Open it in Shortcuts and set one in the “Pause with an ayah” action — then the button will take you straight back", "لم يُحدَّد تطبيق في الأتمتة. افتحها في «الاختصارات» وحدّد تطبيقًا في إجراء «وقفة مع آية» ليعيدك الزر إليه مباشرة"],
        .obVerseEyebrow: ["АЯТ НА СЕГОДНЯ", "AYAH FOR TODAY", "آية اليوم"],
        .obVerseCta: ["Хочу видеть его чаще", "I want to see it more often", "أريد أن أراها أكثر"],
        .obVerseTrust: ["Без аккаунта · без рекламы · работает офлайн", "No account · no ads · works offline", "بلا حساب · بلا إعلانات · تعمل دون إنترنت"],
        .goalTitle: ["Что тебе сейчас нужнее?", "What do you need most right now?", "ما أحوج ما تحتاجه الآن؟"],
        .goalLead: ["Одно — под это подберём аяты, экран и Pro", "Pick one — we will fit the ayat, the screen and Pro to it", "اختر واحدًا، وسنلائم له الآيات والشاشة وPro"],
        .goalHint: ["Остальное откроется потом — в «Местах»", "Everything else opens up later, in Places", "الباقي يُفتح لاحقًا في «الأماكن»"],
        .goalComfort: ["Утешение, когда тяжело", "Comfort when it is hard", "عزاء حين يشتد الأمر"],
        .goalComfortSub: ["аяты под то, что на сердце", "ayat for what is on your heart", "آيات تلائم ما في قلبك"],
        .goalDaily: ["Помнить об Аллахе каждый день", "Remember Allah every day", "أن أذكر الله كل يوم"],
        .goalDailySub: ["один аят в выбранное время", "one ayah at the time you choose", "آية واحدة في الوقت الذي تختاره"],
        .goalFeed: ["Меньше листать ленту", "Scroll the feed less", "تصفّح أقل"],
        .goalFeedSub: ["аят раньше соцсетей", "an ayah before social media", "آية قبل وسائل التواصل"],
        .goalBeauty: ["Красиво на телефоне", "Something beautiful on my phone", "شيء جميل على هاتفي"],
        .goalBeautySub: ["свой вид аята и иконка", "your own ayah style and icon", "مظهرك الخاص للآية وأيقونتك"],
        .obThemesTitle: ["Что сейчас на сердце?", "What is on your heart right now?", "ما الذي في قلبك الآن؟"],
        .obThemesSub: ["Отметь — и аят на экране будет об этом", "Pick it, and the ayah on your screen will speak to it", "اخترها وستحدّثك الآية على شاشتك عنها"],
        .obThemesCounter: ["Выбрано %d · нашли %@", "%d selected · %@ for you", "اخترت %d · وجدنا %@ لك"],
        .obTimeEyebrow: ["КАЖДЫЙ ДЕНЬ", "EVERY DAY", "كل يوم"],
        .obTimeTitle: ["Во сколько присылать аят?", "When should the ayah arrive?", "متى نرسل الآية؟"],
        .obTimeSub: ["Один аят в одно и то же время, без рекламы. Первый придёт прямо сейчас — на следующем шаге", "One ayah at the same time each day, no ads. The first one arrives right now, on the next step", "آية واحدة في الوقت نفسه كل يوم بلا إعلانات. الأولى تصل الآن في الخطوة التالية"],
        .obTimeLater: ["Решу позже", "I will decide later", "سأقرر لاحقًا"],
        .obFeedTitle: ["Сколько в день уходит на ленту?", "How much of your day goes to the feed?", "كم من يومك يذهب إلى التصفح؟"],
        .obFeedSub: ["Примерно — ответ останется на телефоне", "Roughly — the answer stays on your phone", "تقريبًا، وتبقى الإجابة على هاتفك"],
        .obFeedInsight: ["≈ %@ в году. Аят их не вернёт — но встретит тебя раньше ленты, каждый раз, когда берёшь телефон", "≈ %@ a year. An ayah won’t give them back — but it will meet you before the feed, every time you pick up your phone", "≈ %@ في السنة. لن تعيدها الآية، لكنها ستستقبلك قبل التصفح كلما حملت هاتفك"],
        .feedUnderOne: ["Меньше часа", "Under an hour", "أقل من ساعة"],
        .feedOneToTwo: ["1–2 часа", "1–2 hours", "1–2 ساعة"],
        .feedTwoToFour: ["2–4 часа", "2–4 hours", "2–4 ساعات"],
        .feedOverFour: ["Больше 4 часов", "Over 4 hours", "أكثر من 4 ساعات"],
        .obLookEyebrow: ["СВОЙ ВИД", "YOUR LOOK", "مظهرك"],
        .obLookTitle: ["Каким будет аят?", "How should your ayah look?", "كيف تريد أن تبدو آيتك؟"],
        .obLookSub: ["Цвет или картинка — так он будет выглядеть на экране блокировки и в виджетах", "A colour or a picture — this is how it will look on your lock screen and in widgets", "لون أو صورة: هكذا ستظهر على شاشة القفل وفي الودجت"],
        .obFirstTitle: ["Первый аят — прямо сейчас", "Your first ayah, right now", "آيتك الأولى الآن"],
        .obFirstSub: ["Нажми — и он придёт уведомлением, так же, как будет приходить каждый день", "Tap, and it arrives as a notification — just as it will every day", "المس فتصلك إشعارًا كما ستصلك كل يوم"],
        .obFirstCta: ["Прислать первый аят", "Send my first ayah", "أرسل آيتي الأولى"],
        .obFirstSentTitle: ["Первый аят уже пришёл ↑", "Your first ayah is here ↑", "وصلت آيتك الأولى ↑"],
        .obFirstSentSub: ["Так он будет приходить каждый день в %@ — время меняется в «Местах». Это тот же аят, что на экране сейчас", "It will come like this every day at %@ — change the time in Places. It is the same ayah as on your screen now", "ستصلك هكذا كل يوم عند %@ — يمكن تغيير الوقت في «الأماكن». هي نفس الآية على شاشتك الآن"],
        .obIconEyebrow: ["ТВОЙ MISBAH", "YOUR MISBAH", "مصباحك"],
        .obIconTitle: ["Какой будет иконка?", "Which icon will it be?", "أي أيقونة تريد؟"],
        .obIconSub: ["Меняется сразу — загляни на рабочий стол. Платные включатся с Pro", "It changes right away — take a look at your home screen. Paid ones switch on with Pro", "تتغير فورًا، انظر إلى شاشتك الرئيسية. المدفوعة تعمل مع Pro"],
        .obIconKeep: ["Оставить основную", "Keep the main one", "أبقِ الأساسية"],
        .obWidgetEyebrow: ["ГЛАВНОЕ МЕСТО", "THE MAIN SPOT", "المكان الأهم"],
        .obWidgetTitle: ["Теперь — на экран блокировки", "Now, onto the lock screen", "الآن إلى شاشة القفل"],
        .obWidgetSub: ["Три касания — и аят будет там при каждом взгляде на телефон", "Three taps, and the ayah is there every time you glance at your phone", "ثلاث لمسات وتكون الآية هناك كلما نظرت إلى هاتفك"],
        .obWidgetCta: ["Показать, как поставить", "Show me how", "أرني كيف"],
        .obWidgetLater: ["Поставлю позже", "I will add it later", "سأضيفه لاحقًا"],
        .obDoneEyebrow: ["✓ ВИДЖЕТ НА МЕСТЕ", "✓ WIDGET IN PLACE", "✓ الودجت في مكانه"],
        .obDoneTitle: ["Готово — аят уже на экране", "Done — the ayah is on your screen", "تم، الآية الآن على شاشتك"],
        .obDoneFooter: ["Он будет встречать тебя каждый раз, когда берёшь телефон", "It will greet you every time you pick up your phone", "ستستقبلك كلما حملت هاتفك"],
        .obWhyLead: ["В этом году ты возьмёшь телефон", "This year you will pick up your phone", "هذا العام ستحمل هاتفك"],
        .obWhyNumber: ["35 000 раз", "35,000 times", "35,000 مرة"],
        .obWhyQuestion: ["Сколько из них начнутся с аята?", "How many will start with an ayah?", "كم منها سيبدأ بآية؟"],
        .obWhySource: ["В среднем телефон разблокируют 96 раз в день — за год набегает около 35 000", "On average a phone is unlocked 96 times a day — about 35,000 a year", "في المتوسط يُفتح الهاتف 96 مرة في اليوم، أي نحو 35,000 في السنة"],
        .obWhyCta: ["Пусть каждый", "Let every one", "لتكن كل مرة"],
        .versesUnit: ["аят|аята|аятов", "ayah|ayat", "آية|آيتان|آيات|آية"],
        .daysUnit: ["день|дня|дней", "day|days", "يوم|يومان|أيام|يومًا"],
        .fontsUnit: ["шрифт|шрифта|шрифтов", "typeface|typefaces", "خط|خطان|خطوط|خطًا"],
        .iconsUnit: ["иконка|иконки|иконок", "icon|icons", "أيقونة|أيقونتان|أيقونات|أيقونة"],
        .pwTitle: ["Пусть свет не гаснет", "Let the light keep shining", "لِيَدُم النور"],
        .pwTitleGeneric: ["Зажечь весь телефон", "Light up the whole phone", "أضئ هاتفك كله"],
        .pwSub: ["Misbah живёт без рекламы и без инвесторов — только на тех, кто им пользуется. Подписка помогает ему светить", "Misbah runs with no ads and no investors — only on the people who use it. A subscription helps it keep shining", "يعمل Misbah بلا إعلانات وبلا مستثمرين، ويعتمد على مستخدميه فقط. الاشتراك يساعده على الاستمرار في الإضاءة"],
        .pwComfortEyebrow: ["ПОД ТО, ЧТО НА СЕРДЦЕ", "FOR WHAT IS ON YOUR HEART", "لما في قلبك"],
        .pwComfortTitle: ["Аят рядом, когда тяжело", "An ayah close by when it is hard", "آية قريبة حين يشتد الأمر"],
        .pwComfortSub: ["Ночью — на тумбочке в StandBy, днём — на экране блокировки, в картинке, которая успокаивает", "At night on your nightstand in StandBy, by day on your lock screen, in a picture that calms", "ليلًا على الطاولة في StandBy، ونهارًا على شاشة القفل، في صورة تهدّئ"],
        .pwDailyEyebrow: ["КАЖДЫЙ ДЕНЬ В %@", "EVERY DAY AT %@", "كل يوم عند %@"],
        .pwDailyTitle: ["Аят везде, куда ты смотришь", "The ayah wherever you look", "الآية أينما نظرت"],
        .pwDailySub: ["Ты берёшь телефон 35 000 раз в год. С Pro аят встречает тебя и на тумбочке, и на обоях", "You pick up your phone 35,000 times a year. With Pro the ayah meets you on the nightstand and on your wallpaper too", "تحمل هاتفك 35,000 مرة في السنة. مع Pro تستقبلك الآية على الطاولة وعلى الخلفية أيضًا"],
        .chipDailyVerse: ["Аят дня", "Ayah of the day", "آية اليوم"],
        .pwFeedEyebrow: ["ПАУЗА — БЕСПЛАТНО НАВСЕГДА", "THE PAUSE IS FREE FOREVER", "الوقفة مجانية للأبد"],
        .pwFeedTitle: ["Меньше ленты — больше Корана", "Less feed, more Quran", "تصفّح أقل، قرآن أكثر"],
        .pwFeedSub: ["Пауза перед соцсетями остаётся бесплатной. Pro — чтобы аят был на всех экранах и выглядел так, как тебе хочется", "The pause before social media stays free. Pro puts the ayah on every screen, looking the way you like", "تبقى الوقفة قبل وسائل التواصل مجانية. مع Pro تكون الآية على كل الشاشات بالمظهر الذي تحب"],
        .pwBeautyTitle: ["Сделай его своим", "Make it yours", "اجعلها لك"],
        .pwBeautySub: ["Иконка и картинка, которые ты выбрал, включатся с Pro. А с ними — все наборы и картинки, %@ и %@", "The icon and picture you chose switch on with Pro. And with them, every colour set and picture, %@ and %@", "الأيقونة والصورة اللتان اخترتهما تعملان مع Pro، ومعهما كل مجموعات الألوان والصور، %@ و%@"],
        .pwBeautySubNoPick: ["С Pro — все наборы и картинки, %@ и %@", "With Pro: every colour set and picture, %@ and %@", "مع Pro: كل مجموعات الألوان والصور، %@ و%@"],
        .unlockStandBy: ["StandBy", "StandBy", "StandBy"],
        .unlockWallpaper: ["Обои", "Wallpaper", "الخلفية"],
        .unlockSets: ["Все наборы", "All colour sets", "كل المجموعات"],
        .unlockPictures: ["Все картинки", "All pictures", "كل الصور"],
        .unlockFonts: ["Шрифты", "Typefaces", "الخطوط"],
        .unlockIcons: ["Иконки", "App icons", "الأيقونات"],
        .planWeek: ["Неделя", "Week", "أسبوع"],
        .planMonth: ["Месяц", "Month", "شهر"],
        .planYear: ["Год", "Year", "سنة"],
        .planWeekNote: ["в неделю", "per week", "في الأسبوع"],
        .planMonthNote: ["в месяц", "per month", "في الشهر"],
        .planYearNote: ["7 дней бесплатно", "7 days free", "7 أيام مجانًا"],
        .pwTrialCta: ["Начать 7 дней бесплатно", "Start 7 days free", "ابدأ 7 أيام مجانًا"],
        .pwSubscribeCta: ["Подписаться за %@", "Subscribe for %@", "اشترك بـ %@"],
        .pwAfterTrial: ["Потом %@ в год · отменить можно в любой момент", "Then %@ a year · cancel anytime", "ثم %@ في السنة · يمكنك الإلغاء في أي وقت"],
        .pwCancelAnytime: ["Отменить можно в любой момент", "Cancel anytime", "يمكنك الإلغاء في أي وقت"],
        .pwHowTrial: ["Как работает пробный период", "How the free trial works", "كيف تعمل الفترة التجريبية"],
        .pwRestore: ["Восстановить покупки", "Restore purchases", "استعادة المشتريات"],
        .pwTerms: ["Условия использования", "Terms of Use", "شروط الاستخدام"],
        .pwPrivacy: ["Конфиденциальность", "Privacy Policy", "سياسة الخصوصية"],
        .standByLocked: ["StandBy — в Misbah Pro", "StandBy comes with Misbah Pro", "StandBy ضمن Misbah Pro"],
        .proEndedTitle: ["Подписка закончилась", "Your subscription has ended", "انتهى اشتراكك"],
        .proEndedBody: ["Оформление вернулось к бесплатному. StandBy, платные наборы, картинки, шрифты и иконки снова откроются с Misbah Pro.", "The look is back to the free version. StandBy and the Pro colour sets, pictures, typefaces and icons return with Misbah Pro.", "عاد المظهر إلى النسخة المجانية. تعود StandBy ومجموعات الألوان والصور والخطوط والأيقونات المدفوعة مع Misbah Pro."],
        .proEndedCta: ["Вернуть Misbah Pro", "Get Misbah Pro back", "استعد Misbah Pro"],
        .stepLock1: ["Зажмите экран блокировки", "Touch and hold the Lock Screen", "اضغط مطولًا على شاشة القفل"],
        .stepLock1Hint: ["пока не появится кнопка «Настроить»", "until the Customize button appears", "حتى يظهر زر «تخصيص»"],
        .stepLock2: ["Нажмите «Настроить», затем «Экран блокировки»", "Tap Customize, then Lock Screen", "اضغط «تخصيص» ثم «شاشة القفل»"],
        .stepLock2Hint: ["откроется редактор", "the editor opens", "سيُفتح المحرر"],
        .stepLock3: ["Добавьте виджет Misbah под часами", "Add the Misbah widget below the clock", "أضف ودجت Misbah تحت الساعة"],
        .stepLock3Hint: ["выберите прямоугольный размер", "choose the rectangular size", "اختر الحجم المستطيل"],
        .stepHome1: ["Зажмите свободное место на рабочем столе", "Touch and hold an empty area of the Home Screen", "اضغط مطولًا على مساحة فارغة في الشاشة الرئيسية"],
        .stepHome1Hint: ["иконки начнут покачиваться", "the icons start to jiggle", "ستبدأ الأيقونات بالاهتزاز"],
        .stepHome2: ["Нажмите «+» в левом верхнем углу", "Tap + in the top-left corner", "اضغط «+» في أعلى الشاشة"],
        .stepHome2Hint: ["откроется галерея виджетов", "the widget gallery opens", "سيُفتح معرض الودجت"],
        .stepHome3: ["Найдите Misbah и выберите размер", "Find Misbah and pick a size", "ابحث عن Misbah واختر الحجم"],
        .stepHome3Hint: ["средний помещает аят целиком", "the medium one fits the whole ayah", "الحجم المتوسط يتّسع للآية كاملة"],
        .stepControl1: ["Откройте Пункт управления и нажмите «+»", "Open Control Center and tap +", "افتح مركز التحكم واضغط «+»"],
        .stepControl1Hint: ["нужна iOS 18: кнопка добавляется в режиме правки", "iOS 18 required: add it in editing mode", "يتطلب iOS 18: يُضاف الزر في وضع التحرير"],
        .stepControl2: ["Нажмите «Добавить элемент управления»", "Tap Add a Control", "اضغط «إضافة عنصر تحكم»"],
        .stepControl2Hint: ["откроется список", "a list opens", "ستُفتح قائمة"],
        .stepControl3: ["Найдите Misbah в списке", "Find Misbah in the list", "ابحث عن Misbah في القائمة"],
        .stepControl3Hint: ["кнопка встанет туда, куда её поставите", "the button goes wherever you place it", "سيوضع الزر حيث تضعه"],
        .stepStandBy1: ["Положите телефон на зарядку боком", "Put the phone on a charger on its side", "ضع الهاتف على الشاحن بوضع أفقي"],
        .stepStandBy1Hint: ["экран перейдёт в режим StandBy", "the screen switches to StandBy", "ستنتقل الشاشة إلى وضع StandBy"],
        .stepStandBy2: ["Пролистайте до правой панели", "Swipe to the right-hand panel", "مرّر إلى اللوحة اليمنى"],
        .stepStandBy2Hint: ["там живут виджеты", "that is where the widgets live", "هناك توجد الودجت"],
        .stepStandBy3: ["Зажмите панель и добавьте Misbah", "Touch and hold the panel, then add Misbah", "اضغط مطولًا على اللوحة وأضف Misbah"],
        .stepStandBy3Hint: ["виджет будет виден всю ночь", "the widget stays visible all night", "سيبقى الودجت ظاهرًا طوال الليل"],
        .stepWatch1: ["Дождитесь второго релиза", "Wait for the second release", "انتظر الإصدار الثاني"],
        .stepWatch1Hint: ["приложение для часов ещё не вышло", "the watch app is not out yet", "تطبيق الساعة لم يصدر بعد"],
        .stepWatch2: ["Обновите Misbah, когда оно появится", "Update Misbah when it arrives", "حدّث Misbah عند صدوره"],
        .stepWatch2Hint: ["мы сообщим об этом в приложении", "we will say so in the app", "سنخبرك داخل التطبيق"],
        .stepWatch3: ["Добавьте расширение на циферблат", "Add the complication to your watch face", "أضف المكوّن إلى وجه الساعة"],
        .stepWatch3Hint: ["аят будет виден при подъёме руки", "the ayah shows when you raise your wrist", "تظهر الآية عند رفع معصمك"],
        .stepWallpaper1: ["Сохраните обои с аятом", "Save the wallpaper with the ayah", "احفظ الخلفية مع الآية"],
        .stepWallpaper1Hint: ["кнопка «Поделиться» → «Сохранить в Фото»", "Share → Save Image", "زر «مشاركة» ← «حفظ الصورة»"],
        .stepWallpaper2: ["Откройте Настройки → Обои", "Open Settings → Wallpaper", "افتح الإعدادات ← خلفية الشاشة"],
        .stepWallpaper2Hint: ["нажмите «Добавить обои»", "tap Add New Wallpaper", "اضغط «إضافة خلفية جديدة»"],
        .stepWallpaper3: ["Выберите «Фото» и сохранённое изображение", "Choose Photos and the saved image", "اختر «الصور» ثم الصورة المحفوظة"],
        .stepWallpaper3Hint: ["аят будет меняться раз в день", "the ayah changes once a day", "تتغير الآية مرة في اليوم"],
        .stepPause1: ["Откройте «Команды» → «Автоматизация»", "Open Shortcuts → Automation", "افتح «الاختصارات» ← «الأتمتة»"],
        .stepPause1Hint: ["приложение уже стоит на вашем телефоне", "the app is already on your phone", "التطبيق موجود أصلًا على هاتفك"],
        .stepPause2: ["Создайте автоматизацию «Приложение» → «Открыто»", "Create an App automation → Is Opened", "أنشئ أتمتة «التطبيق» ← «عند الفتح»"],
        .stepPause2Hint: ["выберите соцсети, которые открываете чаще всего", "pick the social apps you open most", "اختر تطبيقات التواصل التي تفتحها أكثر"],
        .stepPause3: ["Добавьте действие «Пауза с аятом»", "Add the “Pause with an ayah” action", "أضف إجراء «وقفة مع آية»"],
        .stepPause3Hint: ["в поле действия выберите ту же соцсеть — в неё вас и вернёт", "in the action’s field pick the same app — that is where it returns you", "في حقل الإجراء اختر التطبيق نفسه، وإليه ستعود"],
        .back: ["Назад", "Back", "رجوع"],
        .notNow: ["Не сейчас", "Not now", "ليس الآن"],
        .continueAction: ["Продолжить", "Continue", "متابعة"],
        .openShortcuts: ["Открыть «Команды»", "Open Shortcuts", "فتح «الاختصارات»"],
        .installShortcut: ["Поставить готовую команду", "Add the ready shortcut", "إضافة الأمر الجاهز"],
        .manageSubscription: ["Подписка", "Subscription", "الاشتراك"],
        .coachSwipe: ["Листайте вверх — придёт другой аят. Тап по дате вернёт сегодняшний", "Swipe up for another ayah. Tap the date to come back to today’s", "مرّر لأعلى لترى آية أخرى. اضغط على التاريخ للعودة إلى آية اليوم"],
        .coachAreas: ["Три места, где аят попадается на глаза: сам экран, виджеты и экран блокировки. Каждое настраивается отдельно", "Three places the ayah meets you: the app, widgets and the lock screen. Each is set up separately", "ثلاثة أماكن تلتقي فيها بالآية: التطبيق والودجت وشاشة القفل. كلٌّ منها يُضبط على حدة"],
        .coachAppStyle: ["Выберите цвет или картинку — так будет выглядеть само приложение", "Pick a colour or a picture — that is how the app itself will look", "اختر لونًا أو صورة، فهكذا سيبدو التطبيق نفسه"],
        .coachSwitchToWidgets: ["Теперь переключитесь на «Виджеты»", "Now switch to Widgets", "انتقل الآن إلى «الودجت»"],
        .coachWidgetStyle: ["У виджетов оформление своё. Выберите цвет или картинку и для них", "Widgets have a look of their own. Pick a colour or a picture for them too", "للودجت مظهر خاص بها. اختر لها لونًا أو صورة أيضًا"],
        .coachPlaces: ["Тапните по плитке — покажу, как поставить аят в это место", "Tap a tile and I will show you how to put the ayah there", "اضغط على بطاقة لأريك كيف تضع الآية هناك"],
        .coachMarkDone: ["А переключателем отметьте, что поставили", "And flip the switch once you have done it", "وبالمفتاح حدّد أنك أنجزت ذلك"],
        .coachSkip: ["Пропустить", "Skip", "تخطٍّ"],
        .coachNext: ["Дальше", "Next", "التالي"],
        .coachDone: ["Готово", "Done", "تم"],
        .colourSets: ["Цвет", "Colour", "اللون"],
        .imageSets: ["Изображение", "Image", "الصورة"],
        .tabToday: ["Сегодня", "Today", "اليوم"],
        .appIconTitle: ["Иконка приложения", "App icon", "أيقونة التطبيق"],
        .iconDefault: ["Основная", "Default", "الأساسية"],
        .iconNight: ["Ночь", "Night", "ليل"],
        .widgetDisplayName: ["Аят дня", "Ayah of the day", "آية اليوم"],
        .widgetDescription: ["Аят на каждый день там, где вы и так смотрите", "An ayah for every day, where you already look", "آية لكل يوم حيث تنظر أصلًا"],
        .controlDisplayName: ["Аят дня", "Ayah of the day", "آية اليوم"],
        .controlDescription: ["Кнопка в Пункте управления: открывает сегодняшний аят", "A Control Centre button that opens today’s ayah", "زر في مركز التحكم يفتح آية اليوم"],
        .depthHint: ["Сейчас показан %d-й аят от сегодняшнего", "Showing ayah %d back from today", "تُعرض الآية رقم %d قبل آية اليوم"],
        .surfaceLock: ["Экран блокировки", "Lock screen", "شاشة القفل"],
        .surfaceHome: ["Рабочий стол", "Home screen", "الشاشة الرئيسية"],
        .surfaceControl: ["Пункт управления", "Control Centre", "مركز التحكم"],
        .surfaceWallpaper: ["Обои", "Wallpaper", "خلفية الشاشة"],
        .surfacePause: ["Пауза перед лентой", "Pause before the feed", "وقفة قبل التصفح"],
        .howLock: ["Виджет на экран блокировки", "Widget on the lock screen", "ودجت على شاشة القفل"],
        .howHome: ["Виджет на рабочий стол", "Widget on the home screen", "ودجت على الشاشة الرئيسية"],
        .howControl: ["Кнопка в Пункте управления", "Button in Control Centre", "زر في مركز التحكم"],
        .howStandBy: ["Виджет в StandBy", "Widget in StandBy", "ودجت في StandBy"],
        .howWatch: ["Циферблат на Apple Watch", "Complication on Apple Watch", "ودجت على ساعة Apple Watch"],
        .howWallpaper: ["Обои с аятом", "Wallpaper with an ayah", "خلفية بآية"],
        .noteAuto: ["Виджет отметится в «Местах» сам", "The widget will tick itself in Places", "سيُحدَّد الودجت تلقائيًا في «الأماكن»"],
        .noteSecondRelease: ["Появится во втором релизе", "Coming in the second release", "سيأتي في الإصدار الثاني"],
        .noteManual: ["Отметьте в «Местах», когда закончите", "Tick it in Places when you are done", "حدّده في «الأماكن» عند الانتهاء"],
        .ctaLock: ["Поставить на экран блокировки", "Put it on the lock screen", "ضعه على شاشة القفل"],
        .ctaHome: ["Добавить на рабочий стол", "Add to the home screen", "أضفه إلى الشاشة الرئيسية"],
        .ctaControl: ["Добавить в Пункт управления", "Add to Control Centre", "أضفه إلى مركز التحكم"],
        .ctaStandBy: ["Включить в StandBy", "Turn on in StandBy", "فعّله في StandBy"],
        .ctaWatch: ["Показать на Apple Watch", "Show on Apple Watch", "اعرضه على Apple Watch"],
        .ctaWallpaper: ["Поставить обои", "Set the wallpaper", "اضبط الخلفية"],
        .ctaPause: ["Включить паузу перед лентой", "Turn on the pause before the feed", "فعّل الوقفة قبل التصفح"],
        .areaApp: ["Приложение", "App", "التطبيق"],
        .areaWidgets: ["Виджеты", "Widgets", "الودجت"],
        .areaLock: ["Блокировка", "Lock screen", "شاشة القفل"],
        .styleNight: ["Ночь", "Night", "ليل"],
        .styleParchment: ["Пергамент", "Parchment", "رَقّ"],
        .styleAmber: ["Янтарь", "Amber", "عنبر"],
        .styleInk: ["Тушь", "Ink", "حبر"],
        .styleDawn: ["Заря", "Dawn", "فجر"],
        .styleOpal: ["Опал", "Opal", "أوبال"],
        .styleCoal: ["Уголь", "Coal", "فحم"],
        .sizeSmall: ["Малый", "Small", "صغير"],
        .sizeMedium: ["Средний", "Medium", "متوسط"],
        .sizeLarge: ["Большой", "Large", "كبير"],
        .lengthShort: ["Короткая", "Short", "قصيرة"],
        .lengthFull: ["Полная", "Full", "كاملة"],
        .alignLeading: ["По левому краю", "Left", "إلى البداية"],
        .alignCenter: ["По центру", "Centred", "توسيط"],
        .formatStory: ["Сторис", "Story", "ستوري"],
        .formatSquare: ["Квадрат", "Square", "مربع"],
        .formatWallpaper: ["Обои", "Wallpaper", "خلفية"],
        .backToDaily: ["к аяту дня", "back to today’s ayah", "إلى آية اليوم"],
        .share: ["Поделиться", "Share", "مشاركة"],
        .contextPill: ["Где и когда ниспослан", "Where and when it was revealed", "أين ومتى نزلت"],
        .placesTitle: ["Места", "Places", "الأماكن"],
        .placesProgress: ["Сейчас %d из %d — чем больше, тем чаще аят попадается на глаза", "%d of %d — the more places, the more often an ayah catches your eye", "%d من %d — كلما زادت الأماكن زاد ظهور الآية أمام عينيك"],
        .groupScreens: ["На экранах", "On screens", "على الشاشات"],
        .groupMoment: ["В моменте", "In the moment", "في اللحظة"],
        .lookTitle: ["Вид", "Look", "المظهر"],
        .preview: ["Предпросмотр", "Preview", "معاينة"],
        .size: ["Размер", "Size", "الحجم"],
        .font: ["Шрифт", "Font", "الخط"],
        .languageAndEdition: ["Язык и перевод", "Language and translation", "اللغة والترجمة"],
        .systemFont: ["Системный", "System", "النظام"],
        .verseLength: ["Длина аята", "Ayah length", "طول الآية"],
        .alignment: ["Выравнивание", "Alignment", "المحاذاة"],
        .lockColorNote: ["Цвет здесь задаёт iOS — виджет подстраивается под обои", "iOS sets the color here — the widget adapts to your wallpaper", "لون الودجت هنا يحدده iOS، فهو يتكيّف مع خلفيتك"],
        .appIcon: ["Иконка приложения", "App icon", "أيقونة التطبيق"],
        .shareTitle: ["Поделиться", "Share", "مشاركة"],
        .sendAction: ["Отправить", "Send", "إرسال"],
        .wordmark: ["Подпись Misbah", "Misbah mark", "توقيع Misbah"],
        .context: ["Контекст", "Context", "السياق"],
        .understood: ["Понятно", "Got it", "حسنًا"],
        .close: ["Закрыть", "Close", "إغلاق"],
        .openSettings: ["Открыть настройки", "Open Settings", "فتح الإعدادات"],
        .markDone: ["Отметить, что готово", "Mark as done", "تحديد كمنجز"],
        .paywallTitle: ["Аят везде, где ты смотришь", "The ayah everywhere you look", "الآية في كل مكان تنظر إليه"],
        .subscribe: ["Оформить", "Subscribe", "اشترك"],
        .restore: ["Восстановить покупки", "Restore purchases", "استعادة المشتريات"],
        .paywallLegal: ["Подписка продлевается автоматически. Отменить можно в настройках Apple ID.", "The subscription renews automatically. Cancel any time in your Apple ID settings.", "يتجدد الاشتراك تلقائيًا. يمكنك الإلغاء في أي وقت من إعدادات Apple ID."],
        .perkSurfaces: ["StandBy и обои с аятом", "StandBy and ayah wallpapers", "StandBy وخلفيات بالآيات"],
        .perkStyles: ["Все наборы стилей для приложения, виджетов и локскрина", "Every style set for the app, widgets and lock screen", "كل مجموعات الأنماط للتطبيق والودجت وشاشة القفل"],
        .perkIcons: ["Иконки приложения на выбор", "A choice of app icons", "أيقونات تطبيق للاختيار"],
        .demoVerse: ["Истинно, и при тяготе бывает льгота.", "Lo! with hardship goeth ease.", "إِنَّ مَعَ ٱلْعُسْرِ يُسْرًا"],
        .demoReference: ["Аш-Шарх 94:6", "Ash-Sharh 94:6", "الشرح 94:6"],
        .pauseVerse: ["Которые воздержаны от празднословия.", "And who shun vain conversation.", "وَٱلَّذِينَ هُمْ عَنِ ٱللَّغْوِ مُعْرِضُونَ"],
        .pauseReference: ["Аль-Муминун 23:3", "Al-Mu'minun 23:3", "المؤمنون 23:3"],
        .obNotifyEyebrow: ["АЯТ ДНЯ", "AYAH OF THE DAY", "آية اليوم"],
        .notifyNow: ["сейчас", "now", "الآن"],
        .obTrackEyebrow: ["ОДИН ВОПРОС", "ONE QUESTION", "سؤال واحد"],
        .obTrackTitle: ["Сейчас iPhone спросит про отслеживание", "Your iPhone is about to ask about tracking", "سيسألك iPhone الآن عن التتبّع"],
        .obTrackSub: ["Misbah находит людей через рекламу. Если разрешишь, мы узнаем, какая реклама привела тебя, — и перестанем платить за ту, что не работает. Аяты и твои ответы туда не уходят. Ответ можно поменять в Настройках iPhone", "Misbah finds people through ads. If you allow it, we learn which ad brought you here — and stop paying for the ones that don’t work. Your ayat and answers are never shared. You can change this in iPhone Settings", "يصل Misbah إلى الناس عبر الإعلانات. إن سمحت عرفنا أي إعلان جاء بك، فنكفّ عن الدفع لما لا ينفع. الآيات وإجاباتك لا تُشارَك أبدًا. يمكنك تغيير ذلك من إعدادات iPhone"],
        .obTrackCta: ["Продолжить", "Continue", "متابعة"],
        .dailyVerseTitle: ["Аят дня в уведомлении", "Ayah of the day as a notification", "آية اليوم في إشعار"],
        .dailyVerseOn: ["Каждый день в %@", "Every day at %@", "كل يوم عند %@"],
        .dailyVerseOff: ["Выключено", "Off", "متوقف"],
        .dailyVerseSub: ["Тот же аят, что на «Сегодня», — в выбранное время", "The same ayah as on Today, at the time you choose", "هي نفس آية «اليوم» في الوقت الذي تختاره"],
        .dailyVerseTime: ["Время", "Time", "الوقت"],
        .notifyDenied: ["Уведомления для Misbah выключены в настройках iPhone", "Notifications for Misbah are turned off in iPhone Settings", "الإشعارات لـ Misbah متوقفة في إعدادات iPhone"],
        .comeback3Title: ["Аят на сегодня уже ждёт", "Today’s ayah is waiting", "آية اليوم بانتظارك"],
        .comeback3Body: ["Минута тишины — и одна строка, которая останется с тобой на весь день.", "One quiet minute — and a line to carry with you all day.", "دقيقة هدوء، وسطر يرافقك يومك كله."],
        .comeback7Title: ["Неделя без аята", "A week without an ayah", "أسبوع بلا آية"],
        .comeback7Body: ["Поставь его на экран блокировки — и он будет встречать тебя сам, без приложения.", "Put it on your lock screen and it will greet you on its own — no app needed.", "ضعها على شاشة القفل لتستقبلك وحدها دون فتح التطبيق."],
        .widgetGoneTitle: ["Аят пропал с экрана?", "Has your ayah left the screen?", "هل اختفت الآية من شاشتك؟"],
        .widgetGoneBody: ["Виджета Misbah давно не видно. Вернуть его — двадцать секунд.", "The Misbah widget hasn’t shown up for a while. Putting it back takes twenty seconds.", "لم يظهر ودجت Misbah منذ مدة. إعادته تستغرق عشرين ثانية."],
        .secondHomeTitle: ["Аят уже на экране блокировки", "Your ayah is on the lock screen", "آيتك على شاشة القفل"],
        .secondHomeBody: ["Поставь его и на рабочий стол — будет перед глазами весь день. Двадцать секунд.", "Add it to your Home Screen too — it stays in sight all day. Twenty seconds.", "ضعها أيضًا على الشاشة الرئيسية لتبقى أمام عينيك طوال اليوم. عشرون ثانية."],
        .secondLockTitle: ["Аят уже на рабочем столе", "Your ayah is on the Home Screen", "آيتك على الشاشة الرئيسية"],
        .secondLockBody: ["Поставь его и на экран блокировки — увидишь, даже не разблокируя телефон.", "Add it to your lock screen too — you’ll see it without even unlocking.", "ضعها أيضًا على شاشة القفل لتراها دون أن تفتح الهاتف."],
        .cancelTitle: ["Пробная неделя отменена", "Your free week is cancelled", "أُلغي أسبوعك المجاني"],
        .cancelSub: ["Доступ остаётся до конца недели. Подскажи, что не так, — можно отметить несколько.", "You keep access until the week ends. What didn’t work? You can pick more than one.", "يبقى الوصول حتى نهاية الأسبوع. ما الذي لم يعجبك؟ يمكنك اختيار أكثر من سبب."],
        .cancelSkip: ["Пропустить", "Skip", "تخطٍّ"],
        .cancelThanks: ["Спасибо — это правда помогает", "Thank you — this really helps", "شكرًا، هذا يساعدنا حقًا"],
        .cancelSend: ["Отправить", "Send", "إرسال"],
        .reasonPrice: ["Дорого", "Too expensive", "غالٍ جدًا"],
        .reasonUnused: ["Редко открываю", "I rarely use it", "نادرًا ما أستخدمه"],
        .reasonFreeEnough: ["Хватает бесплатного", "The free version is enough", "النسخة المجانية تكفيني"],
        .reasonNotWhat: ["Не то, что нужно", "Not what I was looking for", "ليس ما كنت أبحث عنه"],
        .reasonJustLooking: ["Хотелось просто посмотреть", "I just wanted to look around", "أردت أن أتصفح فقط"],
        .reasonOther: ["Другое", "Something else", "سبب آخر"],
        .welcomeEyebrow: ["ПОДАРОК К НАЧАЛУ", "A WELCOME GIFT", "هدية ترحيب"],
        .welcomeTitle: ["Первый год Pro — за %@", "Your first year of Pro for %@", "سنتك الأولى من Pro بـ %@"],
        .welcomeSub: ["Вместо %@. Все фоны, наборы и шрифты, StandBy и обои", "Instead of %@. Every background, colour set and font, StandBy and wallpapers", "بدلًا من %@. كل الخلفيات ومجموعات الألوان والخطوط، وStandBy والخلفيات"],
        .welcomeTerms: ["Оплата сразу за первый год, дальше %@ в год. Продлевается автоматически — отменить можно в настройках Apple ID", "Paid once for the first year, then %@ a year. Renews automatically — cancel any time in your Apple ID settings", "دفعة واحدة عن السنة الأولى، ثم %@ في السنة. يتجدد تلقائيًا، ويمكنك الإلغاء في أي وقت من إعدادات Apple ID"],
        .welcomeCta: ["Забрать за %@", "Get it for %@", "احصل عليه بـ %@"],
        .welcomeNo: ["Нет, спасибо", "No, thanks", "لا، شكرًا"],
        .pwPickedEyebrow: ["ТВОЙ ВЫБОР", "YOUR PICK", "اختيارك"],
        .analyticsTitle: ["Помогать улучшать Misbah", "Help improve Misbah", "المساعدة في تحسين Misbah"],
        .analyticsNote: ["Анонимная статистика: какие экраны открывают и где застревают. Без текста аятов и без твоих ответов.", "Anonymous stats: which screens people open and where they get stuck. No ayah text and none of your answers.", "إحصاءات مجهولة: أي الشاشات تُفتح وأين يتعثر الناس. بلا نص الآيات وبلا إجاباتك."],
        .wnIconsEyebrow: ["НОВОЕ В MISBAH", "NEW IN MISBAH", "جديد في Misbah"],
        .wnIconsTitle: ["Пять новых иконок", "Five new icons", "خمس أيقونات جديدة"],
        .wnIconsSub: ["«Ночь» — бесплатно, для всех: тапни, и она уже на рабочем столе. Остальные четыре — с Pro", "Night is free for everyone: tap it and it’s on your home screen. The other four come with Pro", "«ليل» مجانية للجميع: المسها فتصبح على شاشتك الرئيسية. الأربع الأخرى مع Pro"],
        .wnFree: ["бесплатно", "free", "مجانًا"],
        .wnSkip: ["Пропустить", "Skip", "تخطٍّ"],
        .wnPicturesEyebrow: ["НОВЫЕ КАРТИНКИ", "NEW PICTURES", "صور جديدة"],
        .wnPicturesTitle: ["Четыре новые картинки", "Four new pictures", "أربع صور جديدة"],
        .wnPicturesSub: ["Фон для аята в приложении, виджетах и на обоях. Тапни — посмотришь со своим аятом", "A background for your ayah in the app, widgets and wallpaper. Tap to see it with your ayah", "خلفية للآية في التطبيق والودجت وعلى الشاشة. المسها لترى آيتك عليها"],
        .wnSetPicture: ["Поставить фоном", "Use as background", "استخدمها خلفية"],
        .wnUnlockPicture: ["Включить с Pro", "Unlock with Pro", "افتحها مع Pro"],
        .wnDailyTitle: ["Пусть аят приходит сам", "Let the ayah come to you", "دع الآية تأتيك"],
        .wnDailySub: ["Одно уведомление в день, в %@ — тот же аят, что у тебя на экране. Без рекламы. Время меняется в «Местах»", "One notification a day at %@ — the same ayah as on your screen. No ads. Change the time in Places", "إشعار واحد كل يوم عند %@، وهو نفس الآية على شاشتك. بلا إعلانات. يمكن تغيير الوقت في «الأماكن»"],
        .wnDailyCta: ["Присылать аят каждый день", "Send me an ayah every day", "أرسل لي آية كل يوم"],
        .wnDone: ["Готово", "Done", "تم"],
        .promoTitle: ["Новости и обновления", "News and updates", "الأخبار والتحديثات"],
        .promoSub: ["Иногда — о новых иконках, картинках и предложениях. Выключить можно в «Местах»", "Now and then — new icons, pictures and offers. Turn it off any time in Places", "بين حين وآخر: أيقونات وصور وعروض جديدة. يمكنك إيقافه في «الأماكن»"],
        .promoPlacesSub: ["Новинки и предложения", "New features and offers", "المزايا والعروض الجديدة"],
        .rateApp: ["Оценить Misbah", "Rate Misbah", "قيّم Misbah"],
        .pushTokenCopied: ["Токен уведомлений скопирован", "Push token copied", "تم نسخ رمز الإشعارات"],
        .corpusFailedTitle: ["Не удалось прочитать аяты", "Could not read the ayat", "تعذّرت قراءة الآيات"],
        .corpusFailedHint: ["Переустановите приложение", "Reinstall the app", "أعد تثبيت التطبيق"],
        .sceneDesert: ["Пустыня", "Desert", "صحراء"],
        .sceneStars: ["Звёзды", "Stars", "نجوم"],
        .sceneDome: ["Купол", "Dome", "قبة"],
        .sceneLantern: ["Фонарь", "Lantern", "فانوس"],
        .sceneGarden: ["Сад", "Garden", "حديقة"],
        .sceneMosaic: ["Мозаика", "Mosaic", "فسيفساء"],
        .sceneLattice: ["Орнамент", "Lattice", "زخرفة"],
        .iconMosaic: ["Мозаика", "Mosaic", "فسيفساء"],
        .iconStar: ["Звезда", "Star", "نجمة"],
        .iconDawn: ["Рассвет", "Dawn", "فجر"],
        .iconDome: ["Купол", "Dome", "قبة"],
        .iconRosette: ["Розетка", "Rosette", "وردة"],
        .iconLight: ["Свет", "Light", "نور"],
        .styleEmerald: ["Изумруд", "Emerald", "زمردي"],
        .showArabic: ["Показывать арабский текст", "Show the Arabic text", "إظهار النص العربي"],
    ]
}

extension L10n {
    /// Название состояния для чипов в онбординге.
    ///
    /// Состояния лежат в корпусе одинаковыми во всех языках — по ним
    /// фильтруется пул, и общий идентификатор здесь правильный. Но показывать
    /// его нельзя: идентификаторы русские. Отдельная таблица, а не ключи в общем
    /// перечислении, потому что список задаёт корпус, а не код; тест сверяет
    /// одно с другим.
    public func theme(_ id: String) -> String {
        guard let row = L10n.themes[id] else { return id }
        return row[index]
    }

    /// Порядок значений тот же: ru, en, ar.
    static let themes: [String: [String]] = [
        "бессонница": ["Бессонница", "Sleeplessness", "الأرق"],
        "благодарность": ["Благодарность", "Gratitude", "الشكر"],
        "вина": ["Раскаяние", "Repentance", "التوبة"],
        "доверие": ["Упование", "Trust", "التوكل"],
        "любовь": ["Милость", "Mercy", "الرحمة"],
        "надежда": ["Надежда", "Hope", "الأمل"],
        "начало дела": ["Начало дела", "A new start", "بداية جديدة"],
        "немощь": ["Слабость", "Weakness", "الضعف"],
        "одиночество": ["Одиночество", "Loneliness", "الوحدة"],
        "прощение": ["Прощение", "Forgiveness", "المغفرة"],
        "решение": ["Решение", "A decision", "القرار"],
        "сомнение": ["Сомнение", "Doubt", "الشك"],
        "страх": ["Страх", "Fear", "الخوف"],
        "тревога": ["Тревога", "Anxiety", "القلق"],
        "усталость": ["Усталость", "Tiredness", "التعب"],
        "утрата": ["Утрата", "Loss", "الفقد"],
    ]

    /// Номер языка в строке таблицы.
    var index: Int {
        switch locale {
        case .ru: 0
        case .en: 1
        case .ar: 2
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
    /// должно быть на языке интерфейса.
    public var mockDate: String {
        let calendar = Calendar(identifier: .gregorian)
        guard let date = calendar.date(from: DateComponents(year: 2025, month: 9, day: 3))
        else { return "" }
        return date.formatted(
            .dateTime.weekday(.wide).day().month(.wide)
                .locale(locale.formattingLocale)
        )
    }
}
