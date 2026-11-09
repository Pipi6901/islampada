import Foundation

/// Ссылки, которые обязаны быть рядом с подпиской.
///
/// Правило 3.1.2 требует их в двух местах сразу: на странице App Store и в
/// самом приложении, на экране, где человек платит. В описании они лежат
/// текстом — из-за их отсутствия ревью и отклонило первую подачу. Здесь та же
/// пара для пейволла.
///
/// Условия — стандартный EULA Apple, тот самый, на который человек и так
/// соглашается при покупке. Своё соглашение писать не нужно: пока его нет в
/// App Store Connect, действует это, и подсовывать вместо него самодельный
/// текст было бы неправдой.
public enum Legal {
    public static let terms = URL(
        string: "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/")!

    /// Уведомление Tanzil об авторских правах. Лицензия (CC BY 3.0) разрешает
    /// копировать текст только без изменений и требует указывать источник и
    /// ссылку на сайт, — поэтому те же слова едут в каждом бандле корпуса
    /// (`arabicNotice`) и стоят на экране выбора языка.
    public static let tanzilNotice =
        "Quran text: Tanzil Project (https://tanzil.net), Creative Commons Attribution 3.0. "
        + "Permission is granted to copy and distribute verbatim copies of this text, but "
        + "changing it is not allowed. This copy of the Quran text is carefully produced, "
        + "highly verified and continuously monitored by a group of specialists at Tanzil Project."

    public static let tanzil = URL(string: "https://tanzil.net")!

    /// Политика конфиденциальности и условия лежат на Firebase Hosting проекта Misbah
    /// (`docs/legal/misbah/`). Адрес поменять, когда проект заведён: имя сайта у
    /// каждого проекта своё.
    public static let privacy = URL(
        string: "https://misbah-app.web.app/privacy.html")!
}
