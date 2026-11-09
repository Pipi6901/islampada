#if os(iOS)
import LampadaCore
import LampadaUI
import SwiftUI
import WidgetKit

/// Вид виджета для всех семейств.
///
/// Одна вьюха на все размеры, а не шесть отдельных: содержимое одно и то же,
/// разное только сколько его помещается. Разводить это по файлам значило бы
/// шесть раз чинить одну и ту же опечатку.
public struct VerseWidgetView: View {
    let entry: VerseEntry

    @Environment(\.widgetFamily) private var family
    /// `false` — система убрала подложку. Так бывает в StandBy: там виджет
    /// рисуется на чёрном.
    @Environment(\.showsWidgetContainerBackground) private var showsBackground

    public init(entry: VerseEntry) {
        self.entry = entry
    }

    public var body: some View {
        switch family {
        case .accessoryInline:
            // Одна строка без переносов: система обрежет сама, поэтому ссылка
            // важнее текста — по ней можно найти стих целиком.
            Text(entry.reference)

        case .accessoryCircular:
            ZStack {
                AccessoryWidgetBackground()
                Image(systemName: "flame")
                    .font(.system(size: 20))
            }

        case .accessoryRectangular:
            lockScreen

        default:
            if isStandBy && !entry.isPro {
                lockedStandBy
            } else {
                home
            }
        }
    }

    /// StandBy показывает только маленькие виджеты и только без подложки.
    ///
    /// Других признаков у системы нет. Если iOS уберёт подложку маленькому
    /// виджету где-то ещё — например, на экране блокировки iPad, — без подписки
    /// там тоже встанет замок. Проверять на устройстве.
    private var isStandBy: Bool {
        family == .systemSmall && !showsBackground
    }

    /// StandBy без подписки: стих виден, но не читается, поверх замок.
    ///
    /// Не пустая плитка с замком: размытый стих показывает, что именно здесь
    /// будет, и дразнит, а не просто запрещает. Тап ведёт на пейволл.
    private var lockedStandBy: some View {
        ZStack {
            homeContent
                .blur(radius: 7)
                .accessibilityHidden(true)

            VStack(spacing: 6) {
                Image(systemName: "lock.fill")
                    .font(.system(size: 18, weight: .semibold))
                Text(lockedNote)
                    .font(.system(size: 12, weight: .semibold))
                    .multilineTextAlignment(.center)
                    .minimumScaleFactor(0.8)
            }
            .foregroundStyle(.white)
            .padding(.horizontal, 6)
        }
        .containerBackground(for: .widget) {
            background
        }
        .widgetURL(URL(string: "lampada://pro"))
    }

    /// Своего выбора языка у расширения нет — берётся настройка приложения, а
    /// без неё язык устройства, как и у подписи в галерее виджетов.
    private var lockedNote: String {
        L10n(AppSettings().language ?? .detect())[.standByLocked]
    }

    /// Прямоугольный виджет на экране блокировки.
    ///
    /// Здесь три строки мелким кеглем и больше ничего. Раньше сюда клали полный
    /// стих: система обрезала его многоточием посреди слова, и на карточке-
    /// продолжении выходило «ты, которого Я взял от концов земли и приз…» —
    /// набор слов.
    ///
    /// Теперь текст режется по смыслу (см. `Card.shortText`), а ссылка стоит
    /// первой: она короткая, всегда влезает целиком и позволяет найти стих, даже
    /// если сам он не поместился.
    private var lockScreen: some View {
        VStack(alignment: alignment, spacing: 1) {
            Text(entry.reference)
                .font(.system(size: 11, weight: .semibold))
                .lineLimit(1)
                .widgetAccentable()

            Text(entry.lockLength == .short ? entry.shortText : entry.text)
                .font(verse(12))
                .lineLimit(2)
                // Ужать мелкий текст лучше, чем оборвать: на два кегля мельче
                // строка ещё читается, а многоточие уносит half фразы.
                .minimumScaleFactor(0.8)
        }
        .multilineTextAlignment(entry.lockAlignment == .center ? .center : .leading)
        .frame(maxWidth: .infinity,
               alignment: entry.lockAlignment == .center ? .center : .leading)
    }

    /// Шрифт стиха — тот же, что в приложении.
    ///
    /// Начертания лежат в ресурсах `LampadaUI`, а расширение её линкует, так что
    /// регистрация в процессе происходит сама при первом обращении.
    private func verse(_ size: CGFloat) -> Font {
        Fonts.font(entry.lockFont, size: size, weight: 400)
    }

    private var homeAlignment: HorizontalAlignment {
        entry.widgetAlignment == .center ? .center : .leading
    }

    private func homeVerse(_ size: CGFloat) -> Font {
        Fonts.font(entry.widgetFont, size: size, weight: 400)
    }

    private var alignment: HorizontalAlignment {
        entry.lockAlignment == .center ? .center : .leading
    }

    /// Виджеты на рабочем столе и в StandBy: текст, под ним ссылка.
    ///
    /// Текст стоит по центру по вертикали, а не жмётся к верхнему краю: стих
    /// короче доступного места — обычное дело, и прижатый вверх он оставлял под
    /// собой пустую половину плитки.
    private var home: some View {
        homeContent
            .containerBackground(for: .widget) {
                background
            }
    }

    /// Текст и ссылка без подложки. Отдельно от `home`, потому что ими же
    /// рисуется размытый стих под замком в StandBy, а подложку виджет
    /// объявляет один раз, у корня.
    private var homeContent: some View {
        VStack(alignment: homeAlignment, spacing: 8) {
            Spacer(minLength: 0)
            Text(entry.text)
                .font(homeVerse(size))
                .foregroundStyle(verseColor)
                .lineSpacing(size * 0.3)
                .minimumScaleFactor(0.6)
                .lineLimit(lineLimit)

            Text(entry.reference)
                .font(.system(size: 10, weight: .medium))
                .foregroundStyle(referenceColor)
                .tracking(0.4)
            Spacer(minLength: 0)
        }
        .multilineTextAlignment(entry.widgetAlignment == .center ? .center : .leading)
        .frame(maxWidth: .infinity, maxHeight: .infinity,
               alignment: entry.widgetAlignment == .center ? .center : .leading)
    }

    /// Цвета набора годятся, только пока под текстом лежит его подложка.
    ///
    /// Без неё — в StandBy — виджет стоит на чёрном, и у светлых наборов
    /// («Пергамент», «Заря», «Опал») тёмный текст пропадал целиком.
    private var verseColor: Color {
        showsBackground ? Color(hex: palette.text) : .white
    }

    private var referenceColor: Color {
        showsBackground ? Color(hex: palette.accent) : .white.opacity(0.6)
    }

    /// Палитра берётся у картинки, когда она выбрана: цвет текста и акцента
    /// должен считаться от того, что реально лежит под ними.
    private var palette: (background: UInt32, second: UInt32, text: UInt32, accent: UInt32) {
        entry.scene?.palette ?? entry.style.palette
    }

    /// Широкий виджет и StandBy берут горизонтальную версию картинки, остальные
    /// квадратную: одна и та же композиция в этих пропорциях не живёт.
    @ViewBuilder private var background: some View {
        if let scene = entry.scene {
            SceneBackground(scene: scene, variant: family == .systemMedium ? .wide : .square)
        } else {
            Color(hex: palette.background)
        }
    }

    /// Маленький виджет — это примерно две строки текста, большой — десять.
    /// Кегль и лимит подобраны так, чтобы длинный стих ужимался, а короткий
    /// не тонул в пустоте.
    private var size: CGFloat {
        switch family {
        case .systemSmall: entry.text.count > 90 ? 11 : 14
        case .systemLarge: entry.text.count > 300 ? 15 : 19
        default: entry.text.count > 160 ? 12 : 15
        }
    }

    private var lineLimit: Int {
        switch family {
        case .systemSmall: 6
        case .systemLarge: 16
        default: 5
        }
    }
}

extension Color {
    init(hex: UInt32) {
        self.init(
            .sRGB,
            red: Double((hex >> 16) & 0xFF) / 255,
            green: Double((hex >> 8) & 0xFF) / 255,
            blue: Double(hex & 0xFF) / 255,
            opacity: 1
        )
    }
}

/// Объявление виджета. `@main` живёт в расширении: там же права на группу и
/// свой Info.plist, поэтому здесь только тело.
public struct LampadaWidget: Widget {
    public init() {}

    private var gallery: L10n { L10n(AppSettings().language ?? .detect()) }

    public var body: some WidgetConfiguration {
        StaticConfiguration(kind: "LampadaVerse", provider: VerseProvider()) { entry in
            VerseWidgetView(entry: entry)
        }
        // Подпись в галерее виджетов берётся из настройки приложения, а если
        // человек до неё не дошёл — из языка устройства. Своего выбора языка у
        // расширения нет, и статические строки остались бы русскими для всех.
        .configurationDisplayName(gallery[.widgetDisplayName])
        .description(gallery[.widgetDescription])
        .supportedFamilies([
            .systemSmall, .systemMedium, .systemLarge,
            .accessoryRectangular, .accessoryCircular, .accessoryInline,
        ])
    }
}
#endif
