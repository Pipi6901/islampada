import Foundation

/// Карточка — единица показа. Текст уже склеен и знак в конце нормализован на
/// сборке корпуса, поэтому здесь ничего доделывать не нужно: `text` и
/// `reference` кладутся на экран как есть.
public struct Card: Sendable, Hashable, Identifiable, Codable {
    public let id: String
    /// Отрывок, к которому карточка принадлежит. Ключ для строки контекста.
    public let passage: String
    /// Тема состояния: «страх», «усталость» и так далее.
    public let theme: String
    /// Подпись в нумерации своего издания: «Псалом 22:1», «Psaume 23:1».
    public let reference: String
    public let text: String
    /// Арабский оригинал аята. В арабском бандле его нет: там `text` и есть
    /// оригинал, и показывать его дважды незачем.
    public var arabic: String? = nil

    // Ключи в бандле короткие: файл на тысячу карточек, и длинные имена
    // добавили бы к каждому языку заметный вес ни за что.
    private enum CodingKeys: String, CodingKey {
        case id
        case passage = "p"
        case theme = "th"
        case reference = "r"
        case text = "t"
        case arabic = "a"
    }
}

/// Из чего состоит показ карточки на конкретном языке.
///
/// Арабский интерфейс показывает один оригинал, остальные — оригинал над
/// переводом (если человек не выключил оригинал в «Виде»). Решается здесь, а не
/// на каждом экране: экранов семь, и расходиться в этом им нельзя.
public struct VerseParts: Sendable, Hashable {
    /// Арабский текст аята.
    public let original: String?
    /// Перевод. У арабского интерфейса его нет: перевод там — сам оригинал.
    public let translation: String?

    public init(original: String?, translation: String?) {
        self.original = original
        self.translation = translation
    }

    /// Самое длинное из показываемого: по нему экраны подбирают кегль.
    public var longest: Int {
        max(original?.count ?? 0, translation?.count ?? 0)
    }
}

extension Card {
    /// Что показывать на экране. В арабском бандле `text` и есть оригинал, в
    /// остальных оригинал лежит в `arabic`, а `text` — перевод.
    public func parts(locale: AppLocale, showsArabic: Bool) -> VerseParts {
        if locale == .ar { return VerseParts(original: text, translation: nil) }
        guard showsArabic, let arabic else { return VerseParts(original: nil, translation: text) }
        return VerseParts(original: arabic, translation: text)
    }

    /// Текст для уведомления: арабский оригинал строкой выше перевода.
    public var notificationBody: String {
        guard let arabic else { return text }
        return arabic + "\n" + text
    }

    /// Укороченный текст для экрана блокировки.
    ///
    /// Места там на три строки мелким кеглем. Длинный стих система обрезает
    /// многоточием посреди слова, и выходит бессмыслица — тем более что
    /// карточка-продолжение может начинаться с середины фразы.
    ///
    /// Режем сами и по смыслу: сначала ищем конец предложения — по нему обрыв
    /// не виден вовсе, — и только если его нет, обрываем по последнему пробелу.
    public var shortText: String { Card.shorten(text) }

    /// Отдельно от `shortText`, потому что расширению виджета карточка не
    /// достаётся — у него на руках только готовая строка из ленты.
    public static func shorten(_ text: String) -> String {
        // Для арабского хватает того же предела: `count` считает графемы, и
        // огласовки вместе с буквой — один символ, как и на глаз.
        let limit = 78
        guard text.count > limit else { return text }
        let head = text.prefix(limit)
        if let stop = head.lastIndex(where: { ".!?;".contains($0) }),
           head.distance(from: head.startIndex, to: stop) > limit / 3 {
            return String(head[...stop])
        }
        guard let space = head.lastIndex(of: " ") else { return String(head) + "…" }
        return String(head[..<space]) + "…"
    }
}

/// Издание, из которого взяты тексты.
public struct Edition: Sendable, Hashable, Codable {
    public let id: String
    public let name: String
    public let license: String
    public let source: String
}

/// Корпус одного языка: всё, что нужно приложению, и ничего лишнего.
public struct Corpus: Sendable, Hashable, Codable {
    public let schema: Int
    public let lang: String
    public let edition: Edition
    public let cards: [Card]
    /// Строка контекста по идентификатору отрывка.
    public let contexts: [String: String]
    /// Строка авторства арабского текста (Tanzil, CC BY 3.0): лицензия требует
    /// называть источник и давать ссылку на tanzil.net.
    public let arabicCredit: String?
    /// Полное уведомление Tanzil об авторских правах. Лицензия требует
    /// воспроизводить его вместе с текстом; экран «Язык и перевод» показывает
    /// его целиком.
    public let arabicNotice: String?

    /// Контекст для карточки. Отсутствие контекста — не ошибка данных, а повод
    /// не показывать блок: интерфейс должен это переживать.
    public func context(for card: Card) -> String? {
        contexts[card.passage]
    }

    /// Карточки выбранных тем. Пустой набор означает весь корпус, а не пустой
    /// пул: человек, не выбравший ничего, должен видеть всё.
    ///
    /// Порядок сохраняется, поэтому индексы отфильтрованного пула остаются
    /// стабильными между запусками.
    public func cards(themes: Set<String>) -> [Card] {
        themes.isEmpty ? cards : cards.filter { themes.contains($0.theme) }
    }

    /// Все темы, встречающиеся в корпусе.
    public var themes: Set<String> {
        Set(cards.map(\.theme))
    }
}

extension Corpus {
    /// Загружает корпус языка из ресурсов пакета.
    ///
    /// Разбор синхронный и намеренно не `async`: файл лежит в бандле, читается
    /// за миллисекунды, и расширению виджета негде дожидаться задачи.
    public static func load(_ locale: AppLocale) throws -> Corpus {
        // `Bundle.module` сгенерирован как internal, поэтому в значении
        // аргумента по умолчанию его использовать нельзя — только в теле.
        try load(locale, from: .module)
    }

    /// То же, но из указанного бандла: приложение кладёт корпус в свой ресурс,
    /// а не тянет пакетный.
    public static func load(_ locale: AppLocale, from bundle: Bundle) throws -> Corpus {
        guard let url = bundle.url(forResource: "corpus-\(locale.rawValue)",
                                   withExtension: "json") else {
            throw CorpusError.missingResource(locale)
        }
        let data = try Data(contentsOf: url)
        return try JSONDecoder().decode(Corpus.self, from: data)
    }
}

public enum CorpusError: Error, Sendable, Hashable {
    case missingResource(AppLocale)
}

extension String {
    /// Есть ли в строке арабское письмо.
    ///
    /// По этому признаку экраны, виджеты и предпросмотры выбирают шрифт Корана:
    /// латинские и кириллические начертания арабских букв не содержат. Лежит в
    /// ядре, а не в интерфейсе, потому что нужна и расширению виджета.
    public var isArabicScript: Bool {
        unicodeScalars.contains { (0x0600...0x06FF).contains($0.value) }
    }
}
