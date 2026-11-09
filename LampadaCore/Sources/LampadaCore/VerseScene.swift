import Foundation

/// Фон-изображение вместо цветной заливки.
///
/// Выбирается там же, где наборы цвета, и тем же жестом: это второй ряд плиток
/// на экране «Вид». Одно исключает другое — выбрал картинку, цветной набор
/// перестаёт действовать, и наоборот.
///
/// Все сюжеты без людей и животных: пустыня, звёзды, купол мечети, фонарь, сад и
/// два орнамента.
///
/// У каждого фона своя палитра. Она не декоративная: из неё выводятся плашки,
/// линии, приглушённый текст и заливка кнопок — всё то же, что у цветных
/// наборов. Значения посчитаны по самим изображениям (`tools/art/build_assets.py`),
/// а не подобраны на глаз.
///
/// ФАЙЛ СГЕНЕРИРОВАН `tools/art/build_assets.py` — не править руками.
public enum VerseScene: String, Sendable, Hashable, Codable, CaseIterable, Identifiable {
    case desert
    case stars
    case dome
    case lantern
    case garden
    case mosaic
    case lattice

    public var id: String { rawValue }

    /// Имя набора в каталоге. Формат подставляется по месту: `-tall` для экрана
    /// и обоев, `-wide` для среднего виджета и StandBy, `-square` для остальных.
    public var asset: String { "bg-\(rawValue)" }

    /// Светлый ли текст поверх картинки.
    ///
    /// Определяется самим изображением: тёмная картинка — светлый текст.
    public var prefersLightText: Bool {
        switch self {
        case .stars, .dome, .lantern, .garden, .lattice: true
        case .desert, .mosaic: false
        }
    }

    /// Плотность подложки под текстом.
    ///
    /// Ноль означает, что картинка держит текст сама. Значения посчитаны от
    /// яркости в той полосе, где реально лежит аят: подложка доводит контраст до
    /// 4,5:1 — порога, ниже которого текст на светлом участке перестаёт
    /// читаться. Подложка не сплошная, а сгущается только в этой полосе, иначе
    /// картинка гаснет целиком и смысл её теряется.
    public var scrim: Double {
        switch self {
        case .desert: 0.19
        case .stars: 0.0
        case .dome: 0.41
        case .lantern: 0.02
        case .garden: 0.32
        case .mosaic: 0.0
        case .lattice: 0.0
        }
    }

    /// Полоса, в которой подложка держится на полную силу, в долях высоты
    /// экрана. Совпадает с местом ссылки, аята и плашки контекста.
    public static let textBand: ClosedRange<Double> = 0.27...0.67

    public var titleKey: L10n.Key {
        switch self {
        case .desert: .sceneDesert
        case .stars: .sceneStars
        case .dome: .sceneDome
        case .lantern: .sceneLantern
        case .garden: .sceneGarden
        case .mosaic: .sceneMosaic
        case .lattice: .sceneLattice
        }
    }

    /// Бесплатна только «Пустыня» — самая спокойная. Остальные за подпиской:
    /// это и есть тот платный набор, ради которого фоны затевались.
    public var isPremium: Bool { self != .desert }

    /// Те же четыре цвета, что у цветного набора. `background` здесь не рисуется
    /// (сверху лежит картинка), но задаёт светлоту для плашек и кнопок.
    public var palette: (background: UInt32, second: UInt32, text: UInt32, accent: UInt32) {
        switch self {
        case .desert: (0xCDAB87, 0xC4A689, 0x201C1A, 0x8F6E54)
        case .stars: (0x203D4E, 0x1A2C3B, 0xEEECE6, 0xE8C27A)
        case .dome: (0x65766B, 0x3C4E51, 0xEEECE6, 0xE2B866)
        case .lantern: (0x2A3937, 0x192D32, 0xEEECE6, 0xE8C27A)
        case .garden: (0x574C3B, 0x49463B, 0xEEECE6, 0xC9A24A)
        case .mosaic: (0xE3EEEA, 0xE0ECE8, 0x201C1A, 0x0F6F6A)
        case .lattice: (0x163D3B, 0x143333, 0xEEECE6, 0xD4AF37)
        }
    }
}
