import Foundation

/// Тариф на платном экране.
///
/// Цена здесь — уже готовая строка, а не число: её форматирует магазин, в
/// каждой стране своя валюта и свои правила записи. Складывать «$» с числом
/// самим значило бы показать доллары там, где Apple возьмёт рубли.
public struct PaywallPlan: Sendable, Hashable, Identifiable {
    public enum Period: String, Sendable, Hashable {
        case week, month, year
    }

    public let period: Period
    public let price: String
    /// Есть ли вводный бесплатный период. По решению v0.5 он только у годового:
    /// триал на всех тарифах сразу уводит людей на недельный, и годовой
    /// перестаёт продаваться вовсе.
    public let hasTrial: Bool

    public init(period: Period, price: String, hasTrial: Bool = false) {
        self.period = period
        self.price = price
        self.hasTrial = hasTrial
    }

    public var id: String { period.rawValue }

    public var nameKey: L10n.Key {
        switch period {
        case .week: .planWeek
        case .month: .planMonth
        case .year: .planYear
        }
    }

    public var noteKey: L10n.Key {
        switch period {
        case .week: .planWeekNote
        case .month: .planMonthNote
        case .year: .planYearNote
        }
    }

    /// Заглушка на случай, когда магазин ещё не ответил или в сборке его нет
    /// вовсе. Цены совпадают с App Store Connect для США — это те же значения,
    /// что стоят в макете, и по ним экран можно смотреть без сети.
    public static let placeholder: [PaywallPlan] = [
        PaywallPlan(period: .week, price: "$2.99"),
        PaywallPlan(period: .month, price: "$5.99"),
        PaywallPlan(period: .year, price: "$24.99", hasTrial: true),
    ]

    /// Что предложить по умолчанию. Годовой: он и выгоднее человеку, и
    /// единственный с бесплатной неделей.
    public static let preferred: Period = .year
}
