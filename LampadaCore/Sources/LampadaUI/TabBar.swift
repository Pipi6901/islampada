import LampadaCore
import SwiftUI

/// Вкладки приложения. Их ровно три, и добавлять четвёртую не планируется:
/// «Сегодня» — то, ради чего открывают, «Места» — то, ради чего ставят,
/// «Вид» — то, что настраивают один раз.
public enum Tab: String, Sendable, Hashable, CaseIterable, Identifiable {
    case today
    case places
    case look

    public var id: String { rawValue }

    /// Вкладка по имени шага тура. Тур живёт в `LampadaCore` и про перечисление
    /// вкладок не знает — знать ему и незачем.
    init(coachTab: String) {
        self = Tab(rawValue: coachTab) ?? .today
    }

    var titleKey: L10n.Key {
        switch self {
        case .today: .tabToday
        case .places: .placesTitle
        case .look: .lookTitle
        }
    }

    /// Объёмные иконки нарисованы под этот интерфейс отдельно; системных
    /// символов того же настроения нет.
    var asset: String {
        switch self {
        case .today: "fire"
        case .places: "phone"
        case .look: "palette"
        }
    }
}
