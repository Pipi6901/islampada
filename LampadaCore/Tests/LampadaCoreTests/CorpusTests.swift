import Foundation
import Testing
@testable import LampadaCore

@Suite("Корпус")
struct CorpusTests {

    @Test(arguments: AppLocale.allCases)
    func `бандл каждого языка читается`(locale: AppLocale) throws {
        let corpus = try Corpus.load(locale)
        #expect(corpus.lang == locale.rawValue)
        #expect(corpus.cards.count == 288)
        // Переводы — общественное достояние (Пикталл, Саблуков). Арабский текст
        // Tanzil под CC BY 3.0: его лицензия требует назвать источник, и строка
        // с именем проекта обязана ехать в каждом бандле.
        switch locale {
        case .en, .ru: #expect(corpus.edition.license == "Public Domain")
        case .ar: #expect(corpus.edition.license.hasPrefix("CC BY 3.0"))
        }
        let credit = try #require(corpus.arabicCredit)
        #expect(credit.contains("Tanzil"))
        #expect(credit.contains("tanzil.net"))
    }

    /// Ни одна карточка не должна приехать пустой или обрубленной. Порог низкий
    /// намеренно: в корпусе есть короткие аяты.
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

    /// Темы одни на все языки: фильтр человека сохраняется при смене языка.
    @Test
    func `темы карточек одинаковы во всех языках`() throws {
        let reference = try Corpus.load(.en).cards.map(\.theme)
        for locale in AppLocale.allCases where locale != .en {
            #expect(try Corpus.load(locale).cards.map(\.theme) == reference,
                    "расхождение тем в \(locale.rawValue)")
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

    // MARK: - Арабский оригинал

    /// В арабском бандле оригинал — это `text`, отдельного поля нет; в остальных
    /// оригинал лежит в `arabic`, а `text` — перевод на латинице или кириллице.
    @Test
    func `оригинал лежит там, где ему положено`() throws {
        for card in try Corpus.load(.ar).cards {
            #expect(card.arabic == nil, "\(card.id): в арабском бандле оригинал дважды")
            #expect(card.text.isArabicScript, "\(card.id): \(card.text)")
        }
        for locale in [AppLocale.en, .ru] {
            for card in try Corpus.load(locale).cards {
                let original = try #require(card.arabic, "\(card.id) без оригинала в \(locale.rawValue)")
                #expect(original.isArabicScript)
                #expect(!card.text.isArabicScript, "\(card.id): перевод набран арабским")
            }
        }
    }

    /// Лицензия Tanzil разрешает копировать текст только без изменений. Один и
    /// тот же аят обязан быть побуквенно одинаковым во всех трёх бандлах.
    @Test
    func `арабский оригинал одинаков во всех бандлах`() throws {
        let ar = try Corpus.load(.ar).cards
        for locale in [AppLocale.en, .ru] {
            let cards = try Corpus.load(locale).cards
            #expect(cards.count == ar.count)
            for (translated, original) in zip(cards, ar) {
                #expect(translated.id == original.id)
                #expect(translated.arabic == original.text,
                        "\(locale.rawValue) \(translated.id): оригинал отличается")
            }
        }
    }

    /// Текст Tanzil — арабский блок Юникода и пробел. Всё остальное (латиница,
    /// цифры, знаки препинания) — следы порчи при сборке.
    @Test
    func `в арабском тексте только арабские знаки и пробел`() throws {
        for card in try Corpus.load(.ar).cards {
            for scalar in card.text.unicodeScalars {
                let allowed = scalar == " " || (0x0600...0x06FF).contains(scalar.value)
                #expect(allowed, "\(card.id): U+\(String(scalar.value, radix: 16, uppercase: true))")
            }
            #expect(!card.text.hasPrefix(" ") && !card.text.hasSuffix(" "), "\(card.id): пробел по краю")
            #expect(!card.text.contains("  "), "\(card.id): двойной пробел")
        }
    }

    @Test
    func `нумерация подписей по языкам`() throws {
        func reference(_ locale: AppLocale, _ id: String) throws -> String {
            try #require(Corpus.load(locale).cards.first { $0.id == id }).reference
        }
        // Номер суры и аята общий, названия суры — на языке интерфейса.
        #expect(try reference(.en, "9-51") == "At-Tawbah 9:51")
        #expect(try reference(.ru, "9-51") == "Ат-Тауба 9:51")
        #expect(try reference(.ar, "9-51") == "التوبة 9:51")
    }

    // MARK: - Что показывать

    @Test
    func `арабский интерфейс показывает один оригинал`() throws {
        let card = try #require(Corpus.load(.ar).cards.first)
        for shows in [true, false] {
            let parts = card.parts(locale: .ar, showsArabic: shows)
            #expect(parts.original == card.text)
            #expect(parts.translation == nil)
        }
    }

    @Test
    func `перевод показывается с оригиналом или без него`() throws {
        let card = try #require(Corpus.load(.ru).cards.first)

        let both = card.parts(locale: .ru, showsArabic: true)
        #expect(both.original == card.arabic)
        #expect(both.translation == card.text)

        let translationOnly = card.parts(locale: .ru, showsArabic: false)
        #expect(translationOnly.original == nil)
        #expect(translationOnly.translation == card.text)
    }

    @Test
    func `без оригинала в карточке показывается только перевод`() {
        let card = Card(id: "x", passage: "p", theme: "t", reference: "A 1:1", text: "Text")
        let parts = card.parts(locale: .en, showsArabic: true)
        #expect(parts.original == nil)
        #expect(parts.translation == "Text")
    }

    @Test
    func `текст для уведомления начинается с оригинала`() throws {
        let card = try #require(Corpus.load(.en).cards.first)
        let original = try #require(card.arabic)
        #expect(card.notificationBody == original + "\n" + card.text)
        let arabicCard = try #require(Corpus.load(.ar).cards.first)
        #expect(arabicCard.notificationBody == arabicCard.text)
    }

    // MARK: - Состав и фильтр

    @Test(arguments: AppLocale.allCases)
    func `карточка не обрывается на запятой`(locale: AppLocale) throws {
        let corpus = try Corpus.load(locale)
        let unfinished: Set<Character> = [",", ";", ":", "—", "–", "-", "،", "؛"]
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

    /// Каждая тема набирает достаточно аятов, чтобы пул не повторялся неделями.
    @Test
    func `в каждой теме не меньше десяти аятов`() throws {
        let corpus = try Corpus.load(.en)
        for theme in corpus.themes {
            #expect(corpus.cards(themes: [theme]).count >= 10, "тема «\(theme)»")
        }
    }

    // MARK: - Язык

    @Test
    func `язык устройства определяется по списку предпочтений`() {
        #expect(AppLocale.detect(preferred: ["ar-SA", "en-US"]) == .ar)
        #expect(AppLocale.detect(preferred: ["ru-BY", "en-US"]) == .ru)
        #expect(AppLocale.detect(preferred: ["en-GB"]) == .en)
        // Первый поддерживаемый, а не первый в списке.
        #expect(AppLocale.detect(preferred: ["de-DE", "ru-RU"]) == .ru)
        #expect(AppLocale.detect(preferred: ["tr-TR", "fr-FR", "ar-EG"]) == .ar)
        #expect(AppLocale.detect(preferred: ["ja-JP"]) == .en)
        #expect(AppLocale.detect(preferred: []) == .en)
    }

    @Test
    func `справа налево пишется только арабский`() {
        #expect(AppLocale.ar.isRightToLeft)
        #expect(!AppLocale.en.isRightToLeft)
        #expect(!AppLocale.ru.isRightToLeft)
    }
}
