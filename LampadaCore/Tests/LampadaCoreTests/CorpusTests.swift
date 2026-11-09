import Foundation
import Testing
@testable import LampadaCore

@Suite("Корпус")
struct CorpusTests {

    @Test(arguments: AppLocale.allCases)
    func `бандл каждого языка читается`(locale: AppLocale) throws {
        let corpus = try Corpus.load(locale)
        #expect(corpus.lang == locale.rawValue)
        #expect(corpus.cards.count == 1003)
        // Все издания — общественное достояние, кроме Bíblia Livre: она под
        // CC BY 4.0, и строка лицензии с авторами едет в бандле.
        if locale == .pt {
            #expect(corpus.edition.license.hasPrefix("CC BY 4.0"))
        } else {
            #expect(corpus.edition.license == "Public Domain")
        }
    }

    /// Ни одна карточка не должна приехать пустой или обрубленной. Порог в
    /// восемь символов низкий намеренно: «Jesus wept» из Ин 11:35 есть в корпусе.
    @Test(arguments: AppLocale.allCases)
    func `у карточек есть текст и подпись`(locale: AppLocale) throws {
        let corpus = try Corpus.load(locale)
        for card in corpus.cards {
            #expect(card.text.count >= 8, "\(card.id) в \(locale.rawValue): \(card.text)")
            #expect(!card.reference.isEmpty, "\(card.id) без подписи")
            #expect(card.reference.contains(":"), "\(card.id): \(card.reference)")
        }
    }

    /// Приложение переключает язык, не трогая смещение и не пересчитывая пул,
    /// поэтому состав и порядок карточек обязаны совпадать во всех языках.
    @Test
    func `состав карточек одинаков во всех языках`() throws {
        let reference = try Corpus.load(.en).cards.map(\.id)
        for locale in AppLocale.allCases where locale != .en {
            #expect(try Corpus.load(locale).cards.map(\.id) == reference,
                    "расхождение в \(locale.rawValue)")
        }
    }

    @Test(arguments: AppLocale.allCases)
    func `у каждой карточки есть контекст`(locale: AppLocale) throws {
        let corpus = try Corpus.load(locale)
        for card in corpus.cards {
            let context = try #require(corpus.context(for: card), "нет контекста у \(card.id)")
            #expect(!context.isEmpty)
        }
    }

    @Test
    func `нумерация подписей отличается там, где отличаются издания`() throws {
        let en = try Corpus.load(.en)
        let ru = try Corpus.load(.ru)
        let fr = try Corpus.load(.fr)
        func reference(_ corpus: Corpus, _ id: String) throws -> String {
            try #require(corpus.cards.first { $0.id == id }).reference
        }
        // Пс 23 в еврейской нумерации — Пс 22 в Синодальном.
        #expect(try reference(en, "psa-23-1#0") == "Psalm 23:1")
        #expect(try reference(ru, "psa-23-1#0") == "Псалом 22:1")
        // Пс 13: Синодальный и Segond нумеруют надписание отдельным стихом.
        #expect(try reference(en, "psa-13-1#0") == "Psalm 13:1")
        #expect(try reference(ru, "psa-13-1#0") == "Псалом 12:2")
        #expect(try reference(fr, "psa-13-1#0") == "Psaume 13:2")
    }

    /// Надписание псалма — не текст псалма. Немецкое и французское издания
    /// печатают его внутри первого стиха, и оно снимается на сборке.
    @Test
    func `надписания псалмов не попали в карточки`() throws {
        let openings = ["Ein Psalm", "Ein Lied", "Eine Unterweisung", "Ein Gebet",
                        "Cantique de", "Cantique des", "Psaume de", "Salmo de",
                        "Cántico", "Al Músico", "Начальнику хора"]
        for locale in AppLocale.allCases {
            let corpus = try Corpus.load(locale)
            for card in corpus.cards {
                #expect(!openings.contains { card.text.hasPrefix($0) },
                        "\(locale.rawValue) \(card.id): \(card.text.prefix(40))")
            }
        }
    }

    @Test(arguments: AppLocale.allCases)
    func `карточка не обрывается на запятой`(locale: AppLocale) throws {
        let corpus = try Corpus.load(locale)
        let unfinished: Set<Character> = [",", ";", ":", "—", "–", "-"]
        for card in corpus.cards {
            let last = try #require(card.text.last)
            #expect(!unfinished.contains(last), "\(card.id): …\(card.text.suffix(24))")
        }
    }

    @Test
    func `фильтр по темам сужает пул, не ломая его`() throws {
        let corpus = try Corpus.load(.ru)
        let theme = try #require(corpus.themes.sorted().first)
        let filtered = corpus.cards(themes: [theme])
        #expect(!filtered.isEmpty)
        #expect(filtered.count < corpus.cards.count)
        #expect(filtered.allSatisfy { $0.theme == theme })
        // На суженном пуле движок обязан работать так же.
        let engine = VerseEngine(poolCount: filtered.count)
        let seen = Set((0..<filtered.count).map { engine.index(offset: $0, on: 739_500) })
        #expect(seen.count == filtered.count)
    }

    /// Пустой набор тем означает «показывать всё», а не пустой пул: человек,
    /// не выбравший ничего в онбординге, должен видеть корпус целиком.
    @Test
    func `пустой набор тем не сужает пул`() throws {
        let corpus = try Corpus.load(.ru)
        #expect(corpus.cards(themes: []).count == corpus.cards.count)
    }

    /// Несколько тем складываются, а не пересекаются.
    @Test
    func `несколько тем складываются`() throws {
        let corpus = try Corpus.load(.ru)
        let two = Set(corpus.themes.sorted().prefix(2))
        let filtered = corpus.cards(themes: two)
        #expect(filtered.count == two.reduce(0) { $0 + corpus.cards(themes: [$1]).count })
        #expect(filtered.allSatisfy { two.contains($0.theme) })
    }

    @Test
    func `язык устройства определяется по списку предпочтений`() {
        #expect(AppLocale.detect(preferred: ["es-MX", "en-US"]) == .es)
        #expect(AppLocale.detect(preferred: ["ja-JP", "fr-CA"]) == .fr)
        #expect(AppLocale.detect(preferred: ["ko-KR"]) == .ko)
        #expect(AppLocale.detect(preferred: ["pt-PT", "en-US"]) == .pt)
        #expect(AppLocale.detect(preferred: ["it-CH"]) == .it)
        #expect(AppLocale.detect(preferred: ["ja-JP"]) == .en)
        #expect(AppLocale.detect(preferred: []) == .en)
    }
}
