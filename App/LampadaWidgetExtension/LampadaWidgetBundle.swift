import LampadaWidgets
import SwiftUI
import WidgetKit

/// Точка входа расширения. Само содержимое виджета живёт в пакете
/// `LampadaWidgets`: его линкует и приложение, поэтому дублировать нечего.
@main
struct LampadaWidgetBundle: WidgetBundle {
    var body: some Widget {
        LampadaWidget()
        // Кнопка в Пункте управления появилась только в iOS 18. Приложение
        // поддерживает и 17-ю, там бандл соберётся из одного виджета.
        if #available(iOS 18.0, *) {
            VerseControl()
        }
    }
}
