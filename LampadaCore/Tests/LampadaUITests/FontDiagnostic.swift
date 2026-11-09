import CoreText
import Foundation
import LampadaCore
import Testing
@testable import LampadaUI

@Suite("Шрифты")
struct FontTests {

    /// Все шрифты набора, кроме системного: у него нет ни своего файла, ни
    /// вариативных осей, и проверять там нечего.
    /// `nonisolated` обязательно: аргументы `@Test` вычисляются вне актора, а
    /// пакет собирается с изоляцией на `MainActor` по умолчанию.
    nonisolated static let bundled = VerseFont.allCases.filter { $0 != .system }

    /// Шрифты вариативные, и их дефолтные инстансы называются не так, как
    /// семейство. Если обращаться по PostScript-имени, оси уже не подвинуть,
    /// а если ошибиться с именем — CoreText молча подставит системный шрифт,
    /// и это видно только глазами.
    @Test(arguments: bundled)
    func `шрифт создаётся из своего семейства`(face: VerseFont) {
        #expect(Fonts.registered)
        let font = Fonts.ctFont(face.family, size: 20, axes: [Fonts.wghtTag: 400])
        #expect(CTFontCopyFamilyName(font) as String == face.family)
    }

    /// Ось `wght` должна действительно двигать начертание.
    ///
    /// Это не теория: у невариативного шрифта значение оси принимается молча и
    /// не делает ничего — полужирные подписи остались бы обычными, и заметить
    /// это можно было бы только глазами. Из-за этого из набора убраны PT Serif
    /// и Spectral, у которых вариативных версий не существует.
    @Test(arguments: bundled)
    func `ось веса двигает начертание`(face: VerseFont) {
        func weight(_ axis: CGFloat) -> Double {
            let font = Fonts.ctFont(face.family, size: 20, axes: [Fonts.wghtTag: axis])
            let traits = CTFontCopyTraits(font) as? [CFString: Any] ?? [:]
            return traits[kCTFontWeightTrait] as? Double ?? 0
        }
        let regular = weight(400)
        let semibold = weight(600)
        #expect(abs(regular) < 0.1, "\(face.family): 400 дал вес \(regular)")
        #expect(semibold > regular + 0.15,
                "\(face.family): 600 дал \(semibold) против \(regular) — ось не работает")
    }

    /// Смысл поправки в том, чтобы разные начертания выглядели одного размера.
    /// Если она посчитана верно, видимая высота букв у всех совпадает с
    /// Literata; допуск — 2%, точнее не имеет смысла.
    @Test(arguments: VerseFont.allCases)
    func `поправка выравнивает видимый размер`(face: VerseFont) {
        func opticalHeight(_ face: VerseFont) -> CGFloat {
            let size = 100 * Fonts.opticalScale(face)
            let font = face == .system
                ? CTFontCreateUIFontForLanguage(.system, size, nil)!
                : Fonts.ctFont(face.family, size: size, axes: [Fonts.wghtTag: 400])
            return CTFontGetXHeight(font) * 0.65 + CTFontGetCapHeight(font) * 0.35
        }
        let base = opticalHeight(.literata)
        let actual = opticalHeight(face)
        #expect(abs(actual - base) / base < 0.02,
                "\(face.family): видимая высота \(actual) против \(base) у Literata")
    }

    /// Ради этого всё и затевалось: при смене шрифта абзац не должен менять
    /// высоту, иначе интерфейс скачет. Проверяем, что заданная высота строки
    /// получается одинаковой у всех начертаний.
    @Test(arguments: VerseFont.allCases)
    func `высота строки одна для всех начертаний`(face: VerseFont) {
        let size: CGFloat = 19
        // Берём самое тесное значение из макетов: если сходится оно, сходятся
        // и все остальные.
        let target = Fonts.tightestLineHeight
        let spacing = Fonts.lineSpacing(face, size: size, lineHeight: target)
        let corrected = size * Fonts.opticalScale(face)
        let font = face == .system
            ? CTFontCreateUIFontForLanguage(.system, corrected, nil)!
            : Fonts.ctFont(face.family, size: corrected, axes: [Fonts.wghtTag: 400])
        let natural = CTFontGetAscent(font) + CTFontGetDescent(font) + CTFontGetLeading(font)

        // Добавка не должна упираться в ноль: это значило бы, что собственная
        // высота строки уже больше заданной и выровнять её нечем.
        #expect(spacing > 0, "\(face.family): своя высота строки \(natural) выше заданной")
        #expect(abs(natural + spacing - size * target) < 0.01)
    }
}
