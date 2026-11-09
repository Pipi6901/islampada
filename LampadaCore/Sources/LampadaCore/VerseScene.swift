import Foundation

/// Фон-изображение вместо цветной заливки.
///
/// Выбирается там же, где наборы цвета, и тем же жестом: это второй ряд плиток
/// на экране «Вид». Одно исключает другое — выбрал картинку, цветной набор
/// перестаёт действовать, и наоборот.
///
/// У каждого фона своя палитра. Она не декоративная: из неё выводятся плашки,
/// линии, приглушённый текст и заливка кнопок — всё то же, что у цветных
/// наборов. Значения подобраны по самим изображениям, а не на глаз.
public enum VerseScene: String, Sendable, Hashable, Codable, CaseIterable, Identifiable {
    case shepherd
    case clouds
    case pastel
    case oldbook
    case fresco
    case christ
    case paul
    case david
    // С 1.0.2: генерация в стиле прежних фонов, 9:16 с апскейлом до высокого
    // варианта — см. `build-art.py`.
    case galilee
    case star
    case gethsemane
    case cross

    public var id: String { rawValue }

    /// Имя набора в каталоге. Формат подставляется по месту: `-tall` для экрана
    /// и обоев, `-wide` для среднего виджета и StandBy, `-square` для остальных.
    public var asset: String { "bg-\(rawValue)" }

    /// Светлый ли текст поверх картинки.
    ///
    /// Определяется самим изображением, а не тем, где подложка дешевле: на
    /// тёмной иконе белая пелена ради экономии выглядела бы дико.
    public var prefersLightText: Bool {
        switch self {
        case .fresco, .christ, .paul, .david, .star, .gethsemane, .cross: true
        case .shepherd, .clouds, .pastel, .oldbook, .galilee: false
        }
    }

    /// Плотность подложки под текстом.
    ///
    /// Ноль означает, что картинка держит текст сама. Значения посчитаны от
    /// яркости в той полосе, где реально лежит стих: подложка доводит контраст
    /// до 4,5:1 — порога, ниже которого текст перестаёт читаться на светлом
    /// участке. Подложка не сплошная, а сгущается только в этой полосе, иначе
    /// картинка гаснет целиком и смысл её теряется.
    public var scrim: Double {
        switch self {
        case .shepherd, .clouds, .pastel, .fresco, .galilee, .gethsemane: 0
        case .oldbook: 0.07
        // Звезда и сияние креста стоят прямо в полосе стиха: в среднем фон
        // там тёмный, но под самыми яркими строками контраст проседает.
        case .cross: 0.22
        case .star: 0.3
        case .david: 0.24
        case .paul: 0.31
        case .christ: 0.37
        }
    }

    /// Полоса, в которой подложка держится на полную силу, в долях высоты
    /// экрана. Совпадает с местом ссылки, стиха и плашки контекста.
    public static let textBand: ClosedRange<Double> = 0.27...0.67

    public var titleKey: L10n.Key {
        switch self {
        case .shepherd: .sceneShepherd
        case .clouds: .sceneClouds
        case .pastel: .scenePastel
        case .oldbook: .sceneOldBook
        case .fresco: .sceneFresco
        case .christ: .sceneChrist
        case .paul: .scenePaul
        case .david: .sceneDavid
        case .galilee: .sceneGalilee
        case .star: .sceneStar
        case .gethsemane: .sceneGethsemane
        case .cross: .sceneCross
        }
    }

    /// Бесплатен только «Пастырь» — самый спокойный. Остальные за подпиской:
    /// это и есть тот платный набор, ради которого фоны затевались.
    public var isPremium: Bool { self != .shepherd }

    /// Те же четыре цвета, что у цветного набора. `background` здесь не рисуется
    /// (сверху лежит картинка), но задаёт светлоту для плашек и кнопок.
    public var palette: (background: UInt32, second: UInt32, text: UInt32, accent: UInt32) {
        switch self {
        case .shepherd: (0xEFE6DA, 0xF5EFE7, 0x201C1A, 0x8F6E54)
        case .clouds: (0xFDF8F3, 0xFEFBF7, 0x201C1A, 0xB29D87)
        case .pastel: (0xDDE0EF, 0xE9EBF4, 0x201C1A, 0x837459)
        case .oldbook: (0xBDCECB, 0xD4DFDD, 0x201C1A, 0x064851)
        case .fresco: (0x11100B, 0x0C0C08, 0xEEECE6, 0xC9A227)
        case .christ: (0x1B2436, 0x141B29, 0xEEECE6, 0xC8A24A)
        case .paul: (0x1D2738, 0x161D2A, 0xEEECE6, 0xC49A4E)
        case .david: (0x1C2537, 0x151C29, 0xEEECE6, 0xC9A94F)
        case .galilee: (0xE5DAC9, 0xE7DDCC, 0x201C1A, 0x7E6A52)
        case .star: (0x2E6C72, 0x154E58, 0xEEECE6, 0xE8C27A)
        case .gethsemane: (0x3C3A2C, 0x363527, 0xEEECE6, 0xC9A24A)
        case .cross: (0x365262, 0x1D3344, 0xEEECE6, 0xC9A227)
        }
    }
}
