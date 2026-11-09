import AVFoundation
import SwiftUI

/// Зацикленная заставка первого экрана.
///
/// Раньше здесь стояла картинка — стоп-кадр той же сцены. Живой огонь на первом
/// экране объясняет название лучше любого текста, ради этого ролик и снимали.
///
/// Зациклено через `AVPlayerLooper`, а не перезапуском по уведомлению о конце:
/// на стыке иначе видно рывок в чёрный кадр, а петля должна быть незаметной.
///
/// Звуковая дорожка из файла вырезана совсем, а не заглушена флагом. Заглушённый
/// плеер всё равно поднимает аудиосессию и приглушает чужую музыку — заставка не
/// имеет на это права. `isMuted` ниже оставлен на случай, если файл однажды
/// заменят на другой, со звуком.
struct HeroVideo: View {
    var body: some View {
        #if os(iOS)
        Player()
        #else
        // На маке гоняются только тесты, и проигрыватель там не нужен.
        Image("hero", bundle: .module).resizable().scaledToFill()
        #endif
    }
}

#if os(iOS)
import UIKit

private struct Player: UIViewRepresentable {
    func makeUIView(context: Context) -> PlayerView {
        PlayerView()
    }

    func updateUIView(_ view: PlayerView, context: Context) {}
}

/// Слой проигрывателя во всю вьюху.
///
/// Отдельный `UIView` с `AVPlayerLayer` в качестве layerClass — иначе слой
/// пришлось бы вручную растягивать при каждом изменении размеров, и на повороте
/// или смене размера шрифта он бы отставал.
private final class PlayerView: UIView {
    override static var layerClass: AnyClass { AVPlayerLayer.self }

    private var looper: AVPlayerLooper?

    override init(frame: CGRect) {
        super.init(frame: frame)
        guard let url = Bundle.module.url(forResource: "hero-loop", withExtension: "mp4") else {
            return
        }
        let queue = AVQueuePlayer()
        queue.isMuted = true
        // Заставка не должна прерывать чужую музыку: без этого AVPlayer
        // забирает аудиосессию себе, даже когда сам молчит.
        queue.preventsDisplaySleepDuringVideoPlayback = false
        looper = AVPlayerLooper(player: queue, templateItem: AVPlayerItem(url: url))

        let layer = self.layer as! AVPlayerLayer
        layer.player = queue
        layer.videoGravity = .resizeAspectFill
        queue.play()
    }

    required init?(coder: NSCoder) { fatalError("init(coder:) не используется") }
}
#endif
