import Foundation

/// Языки релиза. Одновременно и код языка, и имя файла корпуса.
///
/// Португальский, итальянский и корейский — с 1.0.2, ради рынков Бразилии,
/// Италии и Кореи (`docs/new-languages.md`). Их строки интерфейса лежат не в
/// общей таблице, а в своих файлах — `Strings+pt.swift` и рядом.
public enum AppLocale: String, Sendable, Hashable, CaseIterable, Codable, Identifiable {
    public var id: String { rawValue }

    case en, ru, de, fr, es, pt, it, ko

    /// Язык по настройкам устройства.
    ///
    /// Берётся `preferredLanguages`, а не `Locale.current`: человек может
    /// держать регион США и первым языком испанский, и показывать ему при этом
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
}
