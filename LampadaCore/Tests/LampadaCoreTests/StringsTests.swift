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

    /// Порядок значений в таблице один: ru, en, ar. Короткая строка уронила бы
    /// приложение на арабском — индекс 2 за пределами массива, — поэтому все
    /// три языка читаются по каждому ключу.
    @Test
    func `каждая строка читается на всех трёх языках`() {
        for key in L10n.Key.allCases {
            for locale in AppLocale.allCases {
                #expect(!L10n(locale)[key].isEmpty, "\(key.rawValue) — \(locale.rawValue)")
            }
        }
    }

    /// Арабская строка — арабская, а не английская, подставленная запасным
    /// вариантом. Исключения — имена, которые не переводятся: StandBy, Pro.
    @Test
    func `арабский интерфейс переведён, а не подменён английским`() {
        let untranslated: Set<L10n.Key> = [.unlockStandBy]
        for key in L10n.Key.allCases where !untranslated.contains(key) {
            let ar = L10n(.ar)[key]
            #expect(ar.isArabicScript || ar == L10n(.en)[key], "\(key.rawValue): \(ar)")
            if ar == L10n(.en)[key] {
                // Совпадает с английским — значит, в строке нет слов вовсе (число,
                // имя, знак). Слова латиницей быть не должны.
                #expect(!ar.contains { $0.isLetter }, "\(key.rawValue): \(ar)")
            }
        }
    }

    /// Подстановки в переводе те же, что в английском: потерянный %@ роняет
    /// строку в «%@» на экране, лишний — читает мусор из памяти.
    @Test(arguments: [AppLocale.ru, .ar])
    func `подстановки совпадают с английскими`(locale: AppLocale) {
        let pattern = /%(\d\$)?[@d]/
        for key in L10n.Key.allCases {
            let english = L10n(.en)[key].matches(of: pattern).map { String($0.output.0) }
            let local = L10n(locale)[key].matches(of: pattern).map { String($0.output.0) }
            #expect(english.sorted() == local.sorted(), "\(locale.rawValue): \(key.rawValue)")
        }
    }

    /// Следов прежнего приложения в интерфейсе быть не должно.
    @Test(arguments: AppLocale.allCases)
    func `в строках нет следов прежнего приложения`(locale: AppLocale) {
        let l10n = L10n(locale)
        let forbidden = ["Lampada", "LAMPADA", "Библи", "Bible", "Христ", "Christ", "Иисус", "Jesus",
                         "Псалом", "Psalm", "Евангел", "Gospel", "церк", "church", "молитв", "prayer",
                         "الكتاب المقدس", "المسيح", "كنيسة"]
        for key in L10n.Key.allCases {
            let text = l10n[key]
            for word in forbidden {
                #expect(!text.localizedCaseInsensitiveContains(word),
                        "\(locale.rawValue) \(key.rawValue): «\(word)» в «\(text)»")
            }
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
        // И наоборот: переведённое состояние, которого нет в корпусе, — мусор.
        for theme in L10n.themes.keys {
            #expect(inCorpus.contains(theme), "лишний перевод: \(theme)")
        }
    }

    @Test
    func `названия состояний на каждом языке отличаются от идентификатора`() {
        for id in L10n.themes.keys {
            for locale in [AppLocale.en, .ar] {
                #expect(L10n(locale).theme(id) != id, "\(locale.rawValue): \(id)")
            }
        }
        #expect(L10n(.ru).theme("страх") == "Страх")
        #expect(L10n(.en).theme("страх") == "Fear")
        #expect(L10n(.ar).theme("страх") == "الخوف")
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
        #expect(Legal.privacy.path.hasSuffix("/privacy"))
        #expect(!Legal.privacy.absoluteString.contains("lampada"))
    }

    /// «≈ 22 дня», а не «22 дней»: у русского три формы, у английского две, у
    /// арабского четыре.
    @Test
    func `число со словом в нужной форме`() {
        let ru = L10n(.ru)
        #expect(ru.count(1, .daysUnit) == "1 день")
        #expect(ru.count(22, .daysUnit) == "22 дня")
        #expect(ru.count(45, .daysUnit) == "45 дней")
        #expect(ru.count(11, .daysUnit) == "11 дней")
        #expect(ru.count(214, .versesUnit) == "214 аятов")
        #expect(ru.count(21, .versesUnit) == "21 аят")
        #expect(ru.count(3, .versesUnit) == "3 аята")

        let en = L10n(.en)
        #expect(en.count(1, .daysUnit) == "1 day")
        #expect(en.count(45, .daysUnit) == "45 days")
        #expect(en.count(1, .versesUnit) == "1 ayah")
        #expect(en.count(7, .versesUnit) == "7 ayat")
        #expect(en.count(0, .versesUnit) == "0 ayat")

        let ar = L10n(.ar)
        #expect(ar.count(1, .versesUnit) == "1 آية")
        #expect(ar.count(2, .versesUnit) == "2 آيتان")
        #expect(ar.count(5, .versesUnit) == "5 آيات")
        #expect(ar.count(10, .versesUnit) == "10 آيات")
        #expect(ar.count(11, .versesUnit) == "11 آية")
        #expect(ar.count(45, .daysUnit) == "45 يومًا")
        #expect(ar.count(8, .daysUnit) == "8 أيام")
    }

    /// Дата в макете экрана блокировки должна быть на языке интерфейса.
    @Test
    func `дата в макете переводится`() {
        #expect(L10n(.ru).mockDate.contains("сентябр"))
        #expect(L10n(.en).mockDate.contains("September"))
        let ar = L10n(.ar).mockDate
        #expect(ar.contains("سبتمبر"))
        // Цифры западные: остальные числа интерфейса подставляются так же.
        #expect(ar.contains("3"))
        #expect(!ar.contains("٣"))
    }
}
