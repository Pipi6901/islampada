import LampadaCore
import SwiftUI

/// Названия языков и изданий.
///
/// Живут отдельным файлом, а не в онбординге, где были раньше: их читают и
/// «Вид», и лист выбора языка, и подпись под стихом. Привязка к экрану, который
/// человек видит один раз в жизни, была случайной.
///
/// Названия НЕ переводятся: язык в списке подписан на себе самом, иначе
/// человек, открывший приложение на чужом языке, не найдёт свой. Издания — имена
/// собственные, у них перевода нет вовсе.
extension AppLocale {
    var nativeName: String {
        switch self {
        case .en: "English"
        case .ru: "Русский"
        case .de: "Deutsch"
        case .fr: "Français"
        case .es: "Español"
        case .pt: "Português"
        case .it: "Italiano"
        case .ko: "한국어"
        }
    }

    /// Короткое имя издания для подписи под стихом: в макете там
    /// «СИНОДАЛЬНЫЙ», а не «Синодальный перевод» — длинное не влезает.
    var editionShort: String {
        switch self {
        case .en: "WEB"
        case .ru: "Синодальный"
        case .de: "Luther 1912"
        case .fr: "Segond 1910"
        case .es: "Reina-Valera"
        case .pt: "Bíblia Livre"
        case .it: "Riveduta"
        case .ko: "개역한글"
        }
    }

    var editionName: String {
        switch self {
        case .en: "World English Bible"
        case .ru: "Синодальный перевод"
        case .de: "Luther 1912"
        case .fr: "Louis Segond 1910"
        case .es: "Reina-Valera 1909"
        case .pt: "Bíblia Livre"
        case .it: "Riveduta 1927"
        case .ko: "개역한글"
        }
    }

    /// Строка авторства под изданием в листе выбора языка.
    ///
    /// Есть только у Bíblia Livre: остальные издания — общественное достояние,
    /// а она под CC BY 4.0, и лицензия требует назвать авторов, дать ссылку на
    /// лицензию и сказать, что текст правился, — сборка заменяет запятую или
    /// двоеточие в конце стиха точкой (см. `build-bundle.py`).
    var editionCredit: String? {
        switch self {
        case .pt: "© Diego Santos, Mario Sérgio, Marco Teles · CC BY 4.0 · pontuação final ajustada"
        case .en, .ru, .de, .fr, .es, .it, .ko: nil
        }
    }
}
