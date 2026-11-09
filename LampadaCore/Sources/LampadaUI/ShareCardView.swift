import LampadaCore
import SwiftUI

/// Формат картинки для шеринга — макет 12.
enum ShareFormat: String, Hashable, Identifiable, CaseIterable {
    case story
    case square
    case wallpaper

    var id: String { rawValue }

    var titleKey: L10n.Key {
        switch self {
        case .story: .formatStory
        case .square: .formatSquare
        case .wallpaper: .formatWallpaper
        }
    }

    /// Размер выгружаемой картинки в пикселях.
    var pixels: CGSize {
        switch self {
        case .story: CGSize(width: 1080, height: 1920)
        case .square: CGSize(width: 1080, height: 1080)
        case .wallpaper: CGSize(width: 1179, height: 2556)
        }
    }

    var aspectRatio: CGFloat { pixels.width / pixels.height }
}

/// Карточка для шеринга.
///
/// Все размеры выражены долями ширины, а не точками: одна и та же вьюха
/// показывается на экране шириной в пару сотен точек и рендерится в 1080
/// пикселей. То, что человек видит перед отправкой, и то, что уйдёт в сторис,
/// — один код, и разъехаться им негде.
struct ShareCardView: View {
    /// Оформление приходит из окружения, поэтому в `ImageRenderer` его надо
    /// проставить руками: у отрисовки вне иерархии экранов своего окружения нет,
    /// и картинка ушла бы со шрифтом по умолчанию вместо выбранного.
    @Environment(\.theme) private var theme
    let card: Card
    let style: VerseStyle
    var format: ShareFormat = .story
    /// Подпись «LAMPADA» внизу. Убирается бесплатно — так решено в спеке.
    var showsWordmark: Bool = true
    /// Ширина, от которой считается всё остальное.
    let width: CGFloat

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            ReferenceLabel(reference: card.reference, tint: accentColor,
                           size: unit * 2.6, dash: unit * 3.6)

            Spacer(minLength: 0)

            Text(card.text)
                .font(theme.display(verseSize))
                .foregroundStyle(verseColor)
                .lineSpacing(theme.spacing(verseSize, lineHeight: 1.885))
                .multilineTextAlignment(.leading)
                .fixedSize(horizontal: false, vertical: true)

            Spacer(minLength: 0)

            if showsWordmark {
                Text("LAMPADA")
                    .font(theme.ui(unit * 2.4, weight: 600))
                    .tracking(unit * 0.9)
                    .foregroundStyle(verseColor.opacity(0.38))
            }
        }
        .padding(unit * 8)
        .frame(width: width, height: width / format.aspectRatio, alignment: .leading)
        .background(background)
    }

    /// Фон карточки — тот же, что человек выбрал для приложения: отправленная
    /// картинка должна выглядеть как его экран, а не как чужая заготовка.
    @ViewBuilder private var background: some View {
        if let scene = theme.scene {
            SceneBackground(scene: scene, variant: format == .square ? .square : .tall)
        } else {
            style.fill
        }
    }

    /// На картинке цвет текста задаёт она сама, а не набор, который она закрыла.
    private var verseColor: Color { theme.scene == nil ? style.textColor : theme.text }
    private var accentColor: Color { theme.scene == nil ? style.accentColor : theme.accent }

    /// Базовая единица — сотая доля ширины. От неё считаются отступы и кегли,
    /// поэтому карточка выглядит одинаково в любом размере.
    private var unit: CGFloat { width / 100 }

    /// Кегль от длины стиха: пул неоднородный, один размер на всё не годится.
    private var verseSize: CGFloat {
        let factor: CGFloat = switch card.text.count {
        case ..<60: 7.6
        case ..<140: 6.2
        case ..<260: 5.0
        case ..<420: 4.1
        default: 3.4
        }
        return unit * factor
    }
}

/// Экран «Поделиться» — макет 12.
///
/// Карточка занимает всё свободное место, сохраняя пропорции формата; под ней
/// выбор формата, тумблер подписи и кнопка отправки.
struct ShareScreen: View {
    let card: Card
    @Bindable var settings: AppSettings
    let entitlements: any EntitlementStore

    @Environment(\.dismiss) private var dismiss
    @Environment(\.l10n) private var l10n
    @Environment(\.theme) private var theme

    @State private var format: ShareFormat = .story
    @State private var showsWordmark = true

    var body: some View {
        ZStack {
            ScreenBackground(glow: .bottomLeft)

            VStack(spacing: 16) {
                header
                preview
                Segmented(selection: $format, items: ShareFormat.allCases) { l10n[$0.titleKey] }
                wordmarkToggle

                ShareLink(item: rendered, preview: SharePreview(card.reference, image: rendered)) {
                    Text(l10n[.sendAction])
                }
                .buttonStyle(PrimaryButton())
            }
            .padding(.horizontal, 26)
            .padding(.top, 12)
            .padding(.bottom, 34)
            // По высоте экран и так подстраивается — карточка берёт ту высоту,
            // что осталась. По ширине ему нужна колонка: иначе на широком
            // экране iPhone Duo кнопка и переключатели растянулись бы на всю
            // ширину.
            .readableColumn()
        }
    }

    private var header: some View {
        HStack {
            Text(l10n[.shareTitle])
                .font(theme.display(26))
                .foregroundStyle(theme.text)
            Spacer()
            Button { dismiss() } label: {
                Image(systemName: "xmark")
                    .font(.system(size: 15, weight: .medium))
                    .foregroundStyle(theme.textFaint)
                    .frame(width: 44, height: 44)
                    .contentShape(Rectangle())
            }
            .buttonStyle(.plain)
            .accessibilityLabel(l10n[.close])
        }
    }

    /// Ширину карточки диктует доступная высота: у сторис пропорции 9:16, и
    /// если считать от ширины экрана, карточка не поместится по вертикали.
    private var preview: some View {
        GeometryReader { geometry in
            let fitted = min(geometry.size.width, geometry.size.height * format.aspectRatio)
            ShareCardView(card: card, style: style, format: format,
                          showsWordmark: showsWordmark, width: fitted)
                .clipShape(RoundedRectangle(cornerRadius: 20, style: .continuous))
                .shadow(color: .black.opacity(theme.isLight ? 0.14 : 0.3), radius: 24, y: 8)
                .frame(maxWidth: .infinity, maxHeight: .infinity)
        }
    }

    private var wordmarkToggle: some View {
        Toggle(isOn: $showsWordmark) {
            Text(l10n[.wordmark])
                .font(theme.ui(13))
                .foregroundStyle(theme.textMuted)
        }
        .tint(theme.accent)
    }

    private var style: VerseStyle { settings.style(for: .app) }

    /// Отрисовка в полном размере: карточка на экране и картинка на выходе —
    /// одна вьюха, отличается только ширина.
    @MainActor private var rendered: Image {
        let renderer = ImageRenderer(
            content: ShareCardView(card: card, style: style, format: format,
                                   showsWordmark: showsWordmark,
                                   width: format.pixels.width)
                .themed(theme)
        )
        renderer.scale = 1
        #if canImport(UIKit)
        if let image = renderer.uiImage {
            return Image(uiImage: image)
        }
        #endif
        return Image(systemName: "photo")
    }
}
