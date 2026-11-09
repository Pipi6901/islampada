#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генерирует Lampada.xcodeproj без сторонних инструментов.

Формат pbxproj — старый plist от NeXT. Пишется он руками редко, но здесь это
дешевле, чем ставить генератор проектов на машину: нужен один таргет
приложения, который линкует локальный пакет.

objectVersion 77 — формат Xcode 16+, в нём есть синхронизированные группы
(PBXFileSystemSynchronizedRootGroup): папка подключается целиком, и файлы не
надо перечислять поимённо.
"""
import os, hashlib

ROOT = os.path.expanduser("~/Desktop/lampada/App")
PROJ = os.path.join(ROOT, "Lampada.xcodeproj")


def uid(name):
    """Стабильный 24-символьный идентификатор из имени."""
    return hashlib.sha1(name.encode()).hexdigest()[:24].upper()


ids = {k: uid(k) for k in [
    "project", "target", "productRef", "productsGroup", "mainGroup",
    "buildConfigListProject", "buildConfigListTarget",
    "debugProject", "releaseProject", "debugTarget", "releaseTarget",
    "sourcesPhase", "frameworksPhase", "resourcesPhase",
    "syncGroup", "packageRef", "packageProductUI", "packageProductWidgets",
    "packageProductPurchases", "buildFilePurchases",
    # Firebase — только приложению, расширение виджета его не линкует
    "firebaseRef", "firebaseAnalytics", "firebaseCore", "firebaseMessaging",
    "buildFileFirebaseAnalytics", "buildFileFirebaseCore", "buildFileFirebaseMessaging",
    # Meta (реклама) и Amplitude — тоже только приложению
    "facebookRef", "facebookCore", "buildFileFacebookCore",
    "amplitudeRef", "amplitudeSwift", "buildFileAmplitude",
    "buildFileUI", "buildFileWidgets",
    # расширение виджета
    "wTarget", "wProductRef", "wSyncGroup", "wSourcesPhase", "wFrameworksPhase",
    "wResourcesPhase", "wBuildConfigList", "wDebug", "wRelease",
    "wPackageProduct", "wBuildFile", "wDependency", "wProxy",
    "embedPhase", "embedFile",
]}

SHARED_W = """
				CODE_SIGNING_ALLOWED = YES;
				CODE_SIGNING_REQUIRED = YES;
				CODE_SIGN_ENTITLEMENTS = LampadaWidget.entitlements;
				"CODE_SIGN_IDENTITY[sdk=iphoneos*]" = "Apple Distribution";
				"CODE_SIGN_IDENTITY[sdk=iphonesimulator*]" = "-";
				CODE_SIGN_STYLE = Manual;
				DEVELOPMENT_TEAM = VG9U7V4AAL;
				CURRENT_PROJECT_VERSION = 1;
				VERSIONING_SYSTEM = "apple-generic";
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = WidgetInfo.plist;
				INFOPLIST_KEY_CFBundleDisplayName = Lampada;
				IPHONEOS_DEPLOYMENT_TARGET = 17.0;
				MARKETING_VERSION = 1.0.2;
				PRODUCT_BUNDLE_IDENTIFIER = com.astonio.misbah.widgets;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = iphoneos;
				SKIP_INSTALL = YES;
				SUPPORTED_PLATFORMS = "iphonesimulator iphoneos";
				SWIFT_VERSION = 6.0;
				TARGETED_DEVICE_FAMILY = "1";
"""

# LD_RUNPATH_SEARCH_PATHS обязателен с 1.0.2. До неё все зависимости были
# статическими, и путь к Frameworks внутри бандла не требовался. Facebook SDK
# (FBSDKCoreKit, FBAEMKit, FBSDKCoreKit_Basics) и AmplitudeCore — динамические:
# Xcode кладёт их в Lampada.app/Frameworks, но без этого пути dyld их не ищет,
# и приложение падало на запуске с «Library not loaded: @rpath/FBSDKCoreKit»
# (TestFlight, сборка 22, 05.11.2026).
SHARED = """
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				ASSETCATALOG_COMPILER_ALTERNATE_APPICON_NAMES = "night flame christ paul david fresco vitrage cross christmas easter dove";
				ASSETCATALOG_COMPILER_INCLUDE_ALL_APPICON_ASSETS = YES;
				ENABLE_DEBUG_DYLIB = NO;
				CODE_SIGNING_ALLOWED = YES;
				CODE_SIGNING_REQUIRED = YES;
				CODE_SIGN_ENTITLEMENTS = Lampada.entitlements;
				"CODE_SIGN_IDENTITY[sdk=iphoneos*]" = "Apple Distribution";
				"CODE_SIGN_IDENTITY[sdk=iphonesimulator*]" = "-";
				CODE_SIGN_STYLE = Manual;
				DEVELOPMENT_TEAM = VG9U7V4AAL;
				CURRENT_PROJECT_VERSION = 1;
				VERSIONING_SYSTEM = "apple-generic";
				ENABLE_PREVIEWS = YES;
				GENERATE_INFOPLIST_FILE = YES;
				INFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO;
				INFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;
				INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;
				INFOPLIST_KEY_UILaunchScreen_Generation = YES;
				INFOPLIST_KEY_UISupportedInterfaceOrientations = UIInterfaceOrientationPortrait;
				INFOPLIST_KEY_CFBundleDisplayName = Lampada;
				INFOPLIST_FILE = LampadaInfo.plist;
				IPHONEOS_DEPLOYMENT_TARGET = 17.0;
				MARKETING_VERSION = 1.0.2;
				OTHER_LDFLAGS = "-ObjC";
				LD_RUNPATH_SEARCH_PATHS = ("$(inherited)", "@executable_path/Frameworks", );
				PRODUCT_BUNDLE_IDENTIFIER = com.astonio.misbah;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = iphoneos;
				SUPPORTED_PLATFORMS = "iphonesimulator iphoneos";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 6.0;
				TARGETED_DEVICE_FAMILY = "1";
"""

# Текст системного окна отслеживания (ATT). В 1.0.2 его в сборке НЕТ: Meta
# отложена до 1.0.3, а App Store Connect не пускает на ревью приложение с этим
# текстом, пока анкета App Privacy говорит «без отслеживания». Заявить
# отслеживание без самого окна — частый отказ по правилу 5.1.2.
#
# Вернуть вместе с ключами Meta: TRACKING = True и перенести переводы окна из
# App/tracking-1.0.3/InfoPlist.xcstrings обратно в App/Lampada/ — папка
# подключается к таргету целиком, и всё, что в ней лежит, попадает в сборку.
TRACKING = False
if TRACKING:
    SHARED += ('\t\t\t\tINFOPLIST_KEY_NSUserTrackingUsageDescription = "Так мы узнаем, какая '
               'реклама Lampada в Instagram и Facebook привела тебя. Стихи и ответы не передаются.";\n')

pbxproj = f"""// !$*UTF8*$!
{{
	archiveVersion = 1;
	classes = {{}};
	objectVersion = 77;
	objects = {{

/* Begin PBXBuildFile section */
		{ids['buildFileUI']} /* LampadaUI in Frameworks */ = {{isa = PBXBuildFile; productRef = {ids['packageProductUI']} /* LampadaUI */; }};
		{ids['buildFileWidgets']} /* LampadaWidgets in Frameworks */ = {{isa = PBXBuildFile; productRef = {ids['packageProductWidgets']} /* LampadaWidgets */; }};
		{ids['buildFilePurchases']} /* LampadaPurchases in Frameworks */ = {{isa = PBXBuildFile; productRef = {ids['packageProductPurchases']} /* LampadaPurchases */; }};
		{ids['buildFileFirebaseAnalytics']} /* FirebaseAnalyticsCore in Frameworks */ = {{isa = PBXBuildFile; productRef = {ids['firebaseAnalytics']} /* FirebaseAnalyticsCore */; }};
		{ids['buildFileFirebaseCore']} /* FirebaseCore in Frameworks */ = {{isa = PBXBuildFile; productRef = {ids['firebaseCore']} /* FirebaseCore */; }};
		{ids['buildFileFirebaseMessaging']} /* FirebaseMessaging in Frameworks */ = {{isa = PBXBuildFile; productRef = {ids['firebaseMessaging']} /* FirebaseMessaging */; }};
		{ids['buildFileFacebookCore']} /* FacebookCore in Frameworks */ = {{isa = PBXBuildFile; productRef = {ids['facebookCore']} /* FacebookCore */; }};
		{ids['buildFileAmplitude']} /* AmplitudeSwift in Frameworks */ = {{isa = PBXBuildFile; productRef = {ids['amplitudeSwift']} /* AmplitudeSwift */; }};
		{ids['wBuildFile']} /* LampadaWidgets in Frameworks */ = {{isa = PBXBuildFile; productRef = {ids['wPackageProduct']} /* LampadaWidgets */; }};
		{ids['embedFile']} /* LampadaWidgetExtension.appex in Embed Foundation Extensions */ = {{isa = PBXBuildFile; fileRef = {ids['wProductRef']} /* LampadaWidgetExtension.appex */; settings = {{ATTRIBUTES = (RemoveHeadersOnCopy, ); }}; }};
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		{ids['productRef']} /* Lampada.app */ = {{isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = Lampada.app; sourceTree = BUILT_PRODUCTS_DIR; }};
		{ids['wProductRef']} /* LampadaWidgetExtension.appex */ = {{isa = PBXFileReference; explicitFileType = "wrapper.app-extension"; includeInIndex = 0; path = LampadaWidgetExtension.appex; sourceTree = BUILT_PRODUCTS_DIR; }};
/* End PBXFileReference section */

/* Begin PBXFileSystemSynchronizedRootGroup section */
		{ids['syncGroup']} /* Lampada */ = {{isa = PBXFileSystemSynchronizedRootGroup; path = Lampada; sourceTree = "<group>"; }};
		{ids['wSyncGroup']} /* LampadaWidgetExtension */ = {{isa = PBXFileSystemSynchronizedRootGroup; path = LampadaWidgetExtension; sourceTree = "<group>"; }};
/* End PBXFileSystemSynchronizedRootGroup section */

/* Begin PBXFrameworksBuildPhase section */
		{ids['frameworksPhase']} = {{
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
				{ids['buildFileUI']} /* LampadaUI in Frameworks */,
				{ids['buildFilePurchases']} /* LampadaPurchases in Frameworks */,
				{ids['buildFileFirebaseAnalytics']} /* FirebaseAnalyticsCore in Frameworks */,
				{ids['buildFileFirebaseCore']} /* FirebaseCore in Frameworks */,
				{ids['buildFileFirebaseMessaging']} /* FirebaseMessaging in Frameworks */,
				{ids['buildFileFacebookCore']} /* FacebookCore in Frameworks */,
				{ids['buildFileAmplitude']} /* AmplitudeSwift in Frameworks */,
				{ids['buildFileWidgets']} /* LampadaWidgets in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
		{ids['wFrameworksPhase']} = {{
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
				{ids['wBuildFile']} /* LampadaWidgets in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXCopyFilesBuildPhase section */
		{ids['embedPhase']} /* Embed Foundation Extensions */ = {{
			isa = PBXCopyFilesBuildPhase;
			buildActionMask = 2147483647;
			dstPath = "";
			dstSubfolderSpec = 13;
			files = (
				{ids['embedFile']} /* LampadaWidgetExtension.appex in Embed Foundation Extensions */,
			);
			name = "Embed Foundation Extensions";
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXCopyFilesBuildPhase section */

/* Begin PBXGroup section */
		{ids['mainGroup']} = {{
			isa = PBXGroup;
			children = (
				{ids['syncGroup']} /* Lampada */,
				{ids['wSyncGroup']} /* LampadaWidgetExtension */,
				{ids['productsGroup']} /* Products */,
			);
			sourceTree = "<group>";
		}};
		{ids['productsGroup']} /* Products */ = {{
			isa = PBXGroup;
			children = (
				{ids['productRef']} /* Lampada.app */,
				{ids['wProductRef']} /* LampadaWidgetExtension.appex */,
			);
			name = Products;
			sourceTree = "<group>";
		}};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		{ids['target']} /* Lampada */ = {{
			isa = PBXNativeTarget;
			buildConfigurationList = {ids['buildConfigListTarget']};
			buildPhases = (
				{ids['sourcesPhase']},
				{ids['frameworksPhase']},
				{ids['resourcesPhase']},
				{ids['embedPhase']} /* Embed Foundation Extensions */,
			);
			buildRules = ();
			dependencies = (
				{ids['wDependency']} /* PBXTargetDependency */,
			);
			fileSystemSynchronizedGroups = (
				{ids['syncGroup']} /* Lampada */,
			);
			name = Lampada;
			packageProductDependencies = (
				{ids['packageProductUI']} /* LampadaUI */,
				{ids['packageProductWidgets']} /* LampadaWidgets */,
				{ids['packageProductPurchases']} /* LampadaPurchases */,
				{ids['firebaseAnalytics']} /* FirebaseAnalyticsCore */,
				{ids['firebaseCore']} /* FirebaseCore */,
				{ids['firebaseMessaging']} /* FirebaseMessaging */,
				{ids['facebookCore']} /* FacebookCore */,
				{ids['amplitudeSwift']} /* AmplitudeSwift */,
			);
			productName = Lampada;
			productReference = {ids['productRef']} /* Lampada.app */;
			productType = "com.apple.product-type.application";
		}};
		{ids['wTarget']} /* LampadaWidgetExtension */ = {{
			isa = PBXNativeTarget;
			buildConfigurationList = {ids['wBuildConfigList']};
			buildPhases = (
				{ids['wSourcesPhase']},
				{ids['wFrameworksPhase']},
				{ids['wResourcesPhase']},
			);
			buildRules = ();
			dependencies = ();
			fileSystemSynchronizedGroups = (
				{ids['wSyncGroup']} /* LampadaWidgetExtension */,
			);
			name = LampadaWidgetExtension;
			packageProductDependencies = (
				{ids['wPackageProduct']} /* LampadaWidgets */,
			);
			productName = LampadaWidgetExtension;
			productReference = {ids['wProductRef']} /* LampadaWidgetExtension.appex */;
			productType = "com.apple.product-type.app-extension";
		}};
/* End PBXNativeTarget section */

/* Begin PBXTargetDependency section */
		{ids['wDependency']} /* PBXTargetDependency */ = {{
			isa = PBXTargetDependency;
			target = {ids['wTarget']} /* LampadaWidgetExtension */;
			targetProxy = {ids['wProxy']} /* PBXContainerItemProxy */;
		}};
/* End PBXTargetDependency section */

/* Begin PBXContainerItemProxy section */
		{ids['wProxy']} /* PBXContainerItemProxy */ = {{
			isa = PBXContainerItemProxy;
			containerPortal = {ids['project']} /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = {ids['wTarget']};
			remoteInfo = LampadaWidgetExtension;
		}};
/* End PBXContainerItemProxy section */

/* Begin PBXProject section */
		{ids['project']} /* Project object */ = {{
			isa = PBXProject;
			attributes = {{
				BuildIndependentTargetsInParallel = 1;
				LastSwiftUpdateCheck = 2630;
				LastUpgradeCheck = 2630;
				TargetAttributes = {{
					{ids['target']} = {{
						CreatedOnToolsVersion = 26.3;
					}};
					{ids['wTarget']} = {{
						CreatedOnToolsVersion = 26.3;
					}};
				}};
			}};
			buildConfigurationList = {ids['buildConfigListProject']};
			developmentRegion = ru;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				ru,
				de,
				fr,
				es,
				"pt-BR",
				it,
				ko,
				Base,
			);
			mainGroup = {ids['mainGroup']};
			minimizedProjectReferenceProxies = 1;
			packageReferences = (
				{ids['packageRef']} /* XCLocalSwiftPackageReference "../LampadaCore" */,
				{ids['firebaseRef']} /* XCRemoteSwiftPackageReference "firebase-ios-sdk" */,
				{ids['facebookRef']} /* XCRemoteSwiftPackageReference "facebook-ios-sdk" */,
				{ids['amplitudeRef']} /* XCRemoteSwiftPackageReference "Amplitude-Swift" */,
			);
			preferredProjectObjectVersion = 77;
			productRefGroup = {ids['productsGroup']} /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				{ids['target']} /* Lampada */,
				{ids['wTarget']} /* LampadaWidgetExtension */,
			);
		}};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		{ids['resourcesPhase']} = {{
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = ();
			runOnlyForDeploymentPostprocessing = 0;
		}};
		{ids['wResourcesPhase']} = {{
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = ();
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		{ids['sourcesPhase']} = {{
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = ();
			runOnlyForDeploymentPostprocessing = 0;
		}};
		{ids['wSourcesPhase']} = {{
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = ();
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		{ids['debugProject']} /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				ONLY_ACTIVE_ARCH = YES;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = "DEBUG $(inherited)";
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
			}};
			name = Debug;
		}};
		{ids['releaseProject']} /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				MTL_ENABLE_DEBUG_INFO = NO;
				SWIFT_COMPILATION_MODE = wholemodule;
				VALIDATE_PRODUCT = YES;
			}};
			name = Release;
		}};
		{ids['debugTarget']} /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{{SHARED}			}};
			name = Debug;
		}};
		{ids['releaseTarget']} /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{{SHARED}			}};
			name = Release;
		}};
		{ids['wDebug']} /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{{SHARED_W}			}};
			name = Debug;
		}};
		{ids['wRelease']} /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{{SHARED_W}			}};
			name = Release;
		}};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		{ids['buildConfigListProject']} = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				{ids['debugProject']} /* Debug */,
				{ids['releaseProject']} /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
		{ids['buildConfigListTarget']} = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				{ids['debugTarget']} /* Debug */,
				{ids['releaseTarget']} /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
		{ids['wBuildConfigList']} = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				{ids['wDebug']} /* Debug */,
				{ids['wRelease']} /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
/* End XCConfigurationList section */

/* Begin XCLocalSwiftPackageReference section */
		{ids['packageRef']} /* XCLocalSwiftPackageReference "../LampadaCore" */ = {{
			isa = XCLocalSwiftPackageReference;
			relativePath = ../LampadaCore;
		}};
/* End XCLocalSwiftPackageReference section */

/* Begin XCRemoteSwiftPackageReference section */
		{ids['firebaseRef']} /* XCRemoteSwiftPackageReference "firebase-ios-sdk" */ = {{
			isa = XCRemoteSwiftPackageReference;
			repositoryURL = "https://github.com/firebase/firebase-ios-sdk";
			requirement = {{
				kind = upToNextMinorVersion;
				minimumVersion = 13.0.1;
			}};
		}};
		{ids['facebookRef']} /* XCRemoteSwiftPackageReference "facebook-ios-sdk" */ = {{
			isa = XCRemoteSwiftPackageReference;
			repositoryURL = "https://github.com/facebook/facebook-ios-sdk";
			requirement = {{
				kind = upToNextMinorVersion;
				minimumVersion = 18.1.1;
			}};
		}};
		{ids['amplitudeRef']} /* XCRemoteSwiftPackageReference "Amplitude-Swift" */ = {{
			isa = XCRemoteSwiftPackageReference;
			repositoryURL = "https://github.com/amplitude/Amplitude-Swift";
			requirement = {{
				kind = exactVersion;
				version = 1.19.3;
			}};
		}};
/* End XCRemoteSwiftPackageReference section */

/* Begin XCSwiftPackageProductDependency section */
		{ids['firebaseAnalytics']} /* FirebaseAnalyticsCore */ = {{
			isa = XCSwiftPackageProductDependency;
			package = {ids['firebaseRef']} /* XCRemoteSwiftPackageReference "firebase-ios-sdk" */;
			productName = FirebaseAnalyticsCore;
		}};
		{ids['firebaseCore']} /* FirebaseCore */ = {{
			isa = XCSwiftPackageProductDependency;
			package = {ids['firebaseRef']} /* XCRemoteSwiftPackageReference "firebase-ios-sdk" */;
			productName = FirebaseCore;
		}};
		{ids['firebaseMessaging']} /* FirebaseMessaging */ = {{
			isa = XCSwiftPackageProductDependency;
			package = {ids['firebaseRef']} /* XCRemoteSwiftPackageReference "firebase-ios-sdk" */;
			productName = FirebaseMessaging;
		}};
		{ids['facebookCore']} /* FacebookCore */ = {{
			isa = XCSwiftPackageProductDependency;
			package = {ids['facebookRef']} /* XCRemoteSwiftPackageReference "facebook-ios-sdk" */;
			productName = FacebookCore;
		}};
		{ids['amplitudeSwift']} /* AmplitudeSwift */ = {{
			isa = XCSwiftPackageProductDependency;
			package = {ids['amplitudeRef']} /* XCRemoteSwiftPackageReference "Amplitude-Swift" */;
			productName = AmplitudeSwift;
		}};
		{ids['packageProductPurchases']} /* LampadaPurchases */ = {{
			isa = XCSwiftPackageProductDependency;
			productName = LampadaPurchases;
		}};
		{ids['packageProductUI']} /* LampadaUI */ = {{
			isa = XCSwiftPackageProductDependency;
			productName = LampadaUI;
		}};
		{ids['packageProductWidgets']} /* LampadaWidgets */ = {{
			isa = XCSwiftPackageProductDependency;
			productName = LampadaWidgets;
		}};
		{ids['wPackageProduct']} /* LampadaWidgets */ = {{
			isa = XCSwiftPackageProductDependency;
			productName = LampadaWidgets;
		}};
/* End XCSwiftPackageProductDependency section */
	}};
	rootObject = {ids['project']} /* Project object */;
}}
"""

# В схеме запуска — `-FIRDebugEnabled`: при запуске из Xcode и в симуляторе
# события Firebase сразу видны в DebugView. На архив для App Store флаг не
# влияет: он относится только к запуску, а не к сборке.
scheme = f"""<?xml version="1.0" encoding="UTF-8"?>
<Scheme LastUpgradeVersion = "2630" version = "1.7">
   <BuildAction parallelizeBuildables = "YES" buildImplicitDependencies = "YES">
      <BuildActionEntries>
         <BuildActionEntry buildForTesting = "YES" buildForRunning = "YES" buildForProfiling = "YES" buildForArchiving = "YES" buildForAnalyzing = "YES">
            <BuildableReference
               BuildableIdentifier = "primary"
               BlueprintIdentifier = "{ids['target']}"
               BuildableName = "Lampada.app"
               BlueprintName = "Lampada"
               ReferencedContainer = "container:Lampada.xcodeproj">
            </BuildableReference>
         </BuildActionEntry>
      </BuildActionEntries>
   </BuildAction>
   <TestAction buildConfiguration = "Debug" selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB" selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB" shouldUseLaunchSchemeArgsEnv = "YES">
      <Testables></Testables>
   </TestAction>
   <LaunchAction buildConfiguration = "Debug" selectedDebuggerIdentifier = "Xcode.DebuggerFoundation.Debugger.LLDB" selectedLauncherIdentifier = "Xcode.DebuggerFoundation.Launcher.LLDB" launchStyle = "0" useCustomWorkingDirectory = "NO" ignoresPersistentStateOnLaunch = "NO" debugDocumentVersioning = "YES" debugServiceExtension = "internal" allowLocationSimulation = "YES">
      <BuildableProductRunnable runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "{ids['target']}"
            BuildableName = "Lampada.app"
            BlueprintName = "Lampada"
            ReferencedContainer = "container:Lampada.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
      <CommandLineArguments>
         <CommandLineArgument argument = "-FIRDebugEnabled" isEnabled = "YES">
         </CommandLineArgument>
      </CommandLineArguments>
   </LaunchAction>
   <ProfileAction buildConfiguration = "Release" shouldUseLaunchSchemeArgsEnv = "YES" savedToolIdentifier = "" useCustomWorkingDirectory = "NO" debugDocumentVersioning = "YES">
      <BuildableProductRunnable runnableDebuggingMode = "0">
         <BuildableReference
            BuildableIdentifier = "primary"
            BlueprintIdentifier = "{ids['target']}"
            BuildableName = "Lampada.app"
            BlueprintName = "Lampada"
            ReferencedContainer = "container:Lampada.xcodeproj">
         </BuildableReference>
      </BuildableProductRunnable>
   </ProfileAction>
   <AnalyzeAction buildConfiguration = "Debug"></AnalyzeAction>
   <ArchiveAction buildConfiguration = "Release" revealArchiveInOrganizer = "YES"></ArchiveAction>
</Scheme>
"""

os.makedirs(os.path.join(PROJ, "xcshareddata", "xcschemes"), exist_ok=True)
open(os.path.join(PROJ, "project.pbxproj"), "w").write(pbxproj)
open(os.path.join(PROJ, "xcshareddata", "xcschemes", "Lampada.xcscheme"), "w").write(scheme)
print("создан", PROJ)
