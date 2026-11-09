import Foundation
import Testing
@testable import LampadaCore

@Suite("Строки интерфейса")
struct StringsTests {

    /// Пропущенная строка не падает, а молча отдаёт пустоту: подписи в таблице
    /// нет — subscript вернёт «». На экране это дыра, которую видно только
    /// глазами и только на том языке, где её забыли. Проверка дешёвая, а
    /// пропустить ключ при правке легко.
    @Test(arguments: AppLocale.allCases)
    func `ни один ключ не остался без строки`(locale: AppLocale) {
        let l10n = L10n(locale)
        for key in L10n.Key.allCases {
            #expect(!l10n[key].isEmpty, "\(key.rawValue) — \(locale.rawValue)")
        }
    }

    /// Порядок значений в таблице один и тот же: ru, en, de, fr, es. Строка
    /// короче пяти значений означала бы сдвиг — испанский показал бы
    /// французское. Так как индекс берётся по языку, короткая строка ещё и
    /// уронила бы приложение.
    @Test
    func `у каждой строки ровно пять переводов`() {
        for key in L10n.Key.allCases {
            let ru = L10n(.ru)[key]
            #expect(!ru.isEmpty, "\(key.rawValue)")
            // Испанский — последний в строке: если он читается, длины хватает.
            #expect(!L10n(.es)[key].isEmpty, "\(key.rawValue)")
        }
    }

    /// У языков, добавленных отдельными словарями, запасной вариант —
    /// английский, и пропуск прошёл бы незамеченным: английская строка посреди
    /// португальского экрана. Поэтому словари сверяются с перечнем ключей.
    @Test
    func `у новых языков переведён каждый ключ`() {
        for key in L10n.Key.allCases {
            #expect(L10n.portuguese[key]?.isEmpty == false, "pt: \(key.rawValue)")
            #expect(L10n.italian[key]?.isEmpty == false, "it: \(key.rawValue)")
            #expect(L10n.korean[key]?.isEmpty == false, "ko: \(key.rawValue)")
        }
        for theme in L10n.themes.keys {
            #expect(L10n.portugueseThemes[theme] != nil, "pt: \(theme)")
            #expect(L10n.italianThemes[theme] != nil, "it: \(theme)")
            #expect(L10n.koreanThemes[theme] != nil, "ko: \(theme)")
        }
    }

    /// Подстановки в переводе те же, что в английском: потерянный %@ роняет
    /// строку в «%@» на экране, лишний — читает мусор из памяти.
    @Test(arguments: [AppLocale.pt, .it, .ko])
    func `подстановки совпадают с английскими`(locale: AppLocale) {
        let pattern = /%(\d\$)?[@d]/
        for key in L10n.Key.allCases {
            let english = L10n(.en)[key].matches(of: pattern).map { String($0.output.0) }
            let local = L10n(locale)[key].matches(of: pattern).map { String($0.output.0) }
            #expect(english.sorted() == local.sorted(), "\(locale.rawValue): \(key.rawValue)")
        }
    }

    /// Список состояний задаёт корпус, а переводы — код. Разъехаться им легко:
    /// достаточно добавить в корпус новую тему, и в онбординге появится русский
    /// чип посреди английских — молча, потому что запасной вариант возвращает
    /// сам идентификатор.
    @Test(arguments: AppLocale.allCases)
    func `у каждого состояния из корпуса есть перевод`(locale: AppLocale) throws {
        let corpus = try Corpus.load(locale)
        let inCorpus = Set(corpus.cards.map(\.theme))
        for theme in inCorpus.sorted() {
            #expect(L10n.themes[theme] != nil, "нет перевода: \(theme)")
        }
    }

    /// Ссылки с пейволла — не украшение: по правилу 3.1.2 они обязаны быть на
    /// экране оплаты, и первую подачу ревью отклонило именно за отсутствие
    /// условий. Проверка ловит подмену на заглушку и на http, который iOS
    /// откроет, но ревьюер засчитает за нерабочую ссылку.
    @Test
    func `ссылки на условия и политику ведут наружу`() {
        #expect(Legal.terms.scheme == "https")
        #expect(Legal.privacy.scheme == "https")
        #expect(Legal.terms.host == "www.apple.com")
        #expect(Legal.privacy.absoluteString.hasSuffix("lampada-privacy.html"))
    }

    /// «≈ 22 дня», а не «22 дней»: у русского три формы, у французского ноль
    /// идёт в единственное число.
    @Test
    func `число со словом в нужной форме`() {
        let ru = L10n(.ru)
        #expect(ru.count(1, .daysUnit) == "1 день")
        #expect(ru.count(22, .daysUnit) == "22 дня")
        #expect(ru.count(45, .daysUnit) == "45 дней")
        #expect(ru.count(11, .daysUnit) == "11 дней")
        #expect(ru.count(214, .versesUnit) == "214 стихов")
        #expect(ru.count(21, .versesUnit) == "21 стих")
        #expect(L10n(.en).count(1, .daysUnit) == "1 day")
        #expect(L10n(.pt).count(0, .daysUnit).hasPrefix("0 "))
        #expect(L10n(.it).count(45, .daysUnit) == "45 giorni")
        #expect(L10n(.ko).count(45, .daysUnit) == "45일")
        #expect(L10n(.ko).count(8, .fontsUnit) == "글꼴 8개")
        #expect(L10n(.en).count(45, .daysUnit) == "45 days")
        #expect(L10n(.fr).count(0, .versesUnit) == "0 verset")
        #expect(L10n(.de).count(10, .iconsUnit) == "10 Symbole")
    }

    /// Дата в макете экрана блокировки должна быть на языке интерфейса.
    @Test
    func `дата в макете переводится`() {
        #expect(L10n(.ru).mockDate.contains("сентябр"))
        #expect(L10n(.en).mockDate.contains("September"))
        #expect(L10n(.de).mockDate.contains("September"))
    }
}
