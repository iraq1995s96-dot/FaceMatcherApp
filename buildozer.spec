[app]

# (str) Title of your application
# [Faceprint] ضع اسم تطبيقك هنا
title = FaceMatcherApp

# (str) Package name
# [تعديل] اسم الحزمة (بدون مسافات، حروف صغيرة)
package.name = facematcherapp

# (str) Package domain (needed for android/ios packaging)
# [android] اسم النطاق الخاص بك (مثال: com.yourname أو org.yourcompany)
package.domain = org.facematcher

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,txt,csv

# (list) List of inclusions using pattern matching
# source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
# source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
# source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# [تعديل هام جداً] أضف هنا كل المكتبات التي يستخدمها تطبيقك
# إذا كنت تستخدم KivyMD أضف ,kivymd,pillow
# إذا كنت تستخدم requests أضف ,requests
requirements = python3,kivy,kivymd,pillow

# (str) Application icon
# icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Allow the application to be run on the desktop
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the application
# android.whitelist =

# (str) Path to a custom whitelist file
# android.whitelist_src =

# (str) Path to a custom blacklist file
# android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# android.add_src =

# (list) Android AAR archives to add (currently works only with sdl2 bootstrap)
# android.add_aars =

# (list) Gradle dependencies to add (currently works only with sdl2 bootstrap)
# android.gradle_dependencies =

# (bool) Add the kotlin support
# android.enable_kotlin = False

# (str) python-for-android branch to use, defaults to master
# p4a.branch = master

# (str) python-for-android specific commit to use, defaults to HEAD
# p4a.commit = HEAD

# (str) python-for-android git clone directory (if empty, it will be automatically cloned)
# p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes
# p4a.local_recipes =

# (str) Filename to the hook for p4a
# p4a.hook =

# (str) Bootstrap to use for android builds (sdl2, webview, service_only, ...)
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
# p4a.port =

# (str) Custom commands to run before p4a
# p4a.custom_cmd =


# Android specific

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# [تعديل] تم تحديد المعماريات الأكثر شيوعاً للهواتف الحديثة لتسريع البناء
android.archs = arm64-v8a, armeabi-v7a

# (int) Android API to use
# [تعديل] إصدار API الحديث والمستقر
android.api = 33

# (int) Minimum API required
# [تعديل] الحد الأدنى للإصدارات القديمة
android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 33

# (str) Android NDK version to use
# [تعديل] تم تثبيته ليتوافق مع الـ Workflow
android.ndk = 25b

# (int) Android NDK API to use (optional)
# android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
# android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
# android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
# android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
# [تعديل] هام جداً لمنع توقف البناء
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the application
# android.whitelist =

# (str) Path to a custom whitelist file
# android.whitelist_src =

# (str) Path to a custom blacklist file
# android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# android.add_src =

# (list) Android AAR archives to add (currently works only with sdl2 bootstrap)
# android.add_aars =

# (list) Gradle dependencies to add (currently works only with sdl2 bootstrap)
# android.gradle_dependencies =

# (bool) Add the kotlin support
# android.enable_kotlin = False

# (str) python-for-android branch to use, defaults to master
# p4a.branch = master

# (str) python-for-android specific commit to use, defaults to HEAD
# p4a.commit = HEAD

# (str) python-for-android git clone directory (if empty, it will be automatically cloned)
# p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes
# p4a.local_recipes =

# (str) Filename to the hook for p4a
# p4a.hook =

# (str) Bootstrap to use for android builds (sdl2, webview, service_only, ...)
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
# p4a.port =

# (str) Custom commands to run before p4a
# p4a.custom_cmd =


# iOS specific

# (str) Path to a custom kivy-ios folder
# ios.kivy_ios_dir = ../kivy-ios

# (str) Name of the certificate to use for signing the debug version
# ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
# ios.codesign.release = %(ios.codesign.debug)s


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#        [app]
#        source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
#
#    This can be translated into:
#
#        [app:source.exclude_patterns]
#        license
#        data/audio/*.wav
#        data/images/original/*
#
#    -----------------------------------------------------------------------------

#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, if you want to deploy a demo version of your application without
#    HD content, you can use a profile named "demo" to exclude the HD content.
#
#        [app@demo]
#        source.exclude_patterns = data/images/original/*
#
#    Then, run buildozer with the profile:
#
#        buildozer -p demo android debug
#
#    -----------------------------------------------------------------------------
