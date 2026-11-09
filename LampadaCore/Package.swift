// swift-tools-version: 6.2
import PackageDescription

let package = Package(
    name: "LampadaCore",
    platforms: [.iOS(.v17), .macOS(.v14), .watchOS(.v10)],
    products: [
        .library(name: "LampadaCore", targets: ["LampadaCore"]),
        .library(name: "LampadaPurchases", targets: ["LampadaPurchases"]),
        .library(name: "LampadaUI", targets: ["LampadaUI"]),
        .library(name: "LampadaWidgets", targets: ["LampadaWidgets"]),
    ],
    dependencies: [
        // Отдельный SPM-зеркальный репозиторий: основной покупается ещё и через
        // CocoaPods, и в нём лишние цели, которые SPM пытается собрать.
        .package(url: "https://github.com/RevenueCat/purchases-ios-spm.git", from: "5.14.0"),
    ],
    targets: [
        // Движок и данные. Изоляции не навязывает: его линкуют и приложение,
        // и расширения виджета, каждый со своими правилами.
        .target(name: "LampadaCore", resources: [.process("Resources")]),

        // Интерфейс. Главный актор по умолчанию — это UI-модуль, и почти весь
        // его код и так обязан жить на главном потоке.
        .target(
            name: "LampadaUI",
            dependencies: ["LampadaCore"],
            resources: [.process("Resources")],
            swiftSettings: [.defaultIsolation(MainActor.self)]
        ),

        // Виджеты. Содержимое целиком под `#if os(iOS)`: WidgetKit на маке
        // есть не весь, а тесты гоняются именно там.
        // Зависимость от LampadaUI нужна ради общих фонов: картинки лежат в её
        // ресурсах, и обращаться к ним из чужого бандла нельзя.
        .target(
            name: "LampadaWidgets",
            dependencies: ["LampadaCore", "LampadaUI"],
            swiftSettings: [.defaultIsolation(MainActor.self)]
        ),

        // Покупки живут отдельно от интерфейса намеренно. `LampadaUI` линкует
        // расширение виджета, и RevenueCat уехал бы в него следом — расширению
        // он не нужен ни на грамм, а лимит памяти у виджета жёсткий.
        .target(
            name: "LampadaPurchases",
            dependencies: [
                "LampadaCore",
                .product(name: "RevenueCat", package: "purchases-ios-spm"),
                .product(name: "RevenueCatUI", package: "purchases-ios-spm"),
            ],
            swiftSettings: [.defaultIsolation(MainActor.self)]
        ),

        .testTarget(name: "LampadaCoreTests", dependencies: ["LampadaCore"]),
        .testTarget(
            name: "LampadaUITests",
            dependencies: ["LampadaUI", "LampadaCore"],
            swiftSettings: [.defaultIsolation(MainActor.self)]
        ),
    ]
)
