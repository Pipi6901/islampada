import Foundation

/// Языки релиза. Одновременно и код языка, и имя файла корпуса.
///
/// Арабский — это сам Коран без перевода: у него в корпусе основной текст и есть
/// оригинал, а интерфейс идёт справа налево. Остальные языки — перевод (Pickthall
/// для английского, Саблуков для русского) с арабским оригиналом над ним.
///
/// Языки добавляются вместе с переводом, который можно свободно распространять:
/// пока для французского и турецкого такого нет (см. `docs/TRANSLATIONS.md`).
public enum AppLocale: String, Sendable, Hashable, CaseIterable, Codable, Identifiable {
    public var id: String { rawValue }

    case en, ru, ar

    /// Язык по настройкам устройства.
    ///
    /// Берётся `preferredLanguages`, а не `Locale.current`: человек может
    /// держать регион США и первым языком русский, и показывать ему при этом
    /// английский было бы неверно. Список перебирается по порядку, поэтому
    /// выигрывает первый язык, который мы поддерживаем.
    public static func detect(
        preferred: [String] = Locale.preferredLanguages
    ) -> AppLocale {
        for tag in preferred {
            let code = Locale(identifier: tag).language.languageCode?.identifier
            if let code, let match = AppLocale(rawValue: code) {
                return match
            }
        }
        return .en
    }

    /// Пишется справа налево. Интерфейс на таком языке зеркалится целиком.
    public var isRightToLeft: Bool { self == .ar }

    /// Локаль для форматов дат и чисел.
    ///
    /// У арабского — западные цифры: вся остальная надпись набрана строками
    /// интерфейса, где числа подставляются как есть, и восточные цифры в одной
    /// дате среди западных выглядели бы чужеродно.
    public var formattingLocale: Locale {
        switch self {
        case .ar: Locale(identifier: "ar-u-nu-latn")
        case .en, .ru: Locale(identifier: rawValue)
        }
    }
}
