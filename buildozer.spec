[app]

# (str) Title of your application
title = FaceMatcherApp

# (str) Package name
package.name = facematcher

# (str) Package domain (needed for android packaging)
package.domain = org.facematcher

# (str) Source files where the include_exts resides (relative to spec file)
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,xml

# (list) Application requirements
requirements = python3,kivy,pillow,opencv,numpy,plyer,android

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support.
android.minAPI = 21

# (list) Supported architectures
android.architectures = arm64-v8a

# (str) Accept Android SDK license automatically
android.accept_sdk_license = True

# (str) Android NDK version
android.ndk = 25b

# (str) Android APK versioning
version = 0.1

# (str) Application versioning (used by android)
android.versionCode = 1

# (list) Application meta-data
android.meta_data =

# (str) The Android app's icon
# icon.filename = %(source.dir)s/data/icon.png

# (list) Pattern to whitelist files
source.exclude_dirs = tests, bin, .git, .github

# (str) Presplash
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Log level
log_level = 2

# (str) Android logcat filters
android.logcat_filters = *:S python:D

[buildozer]

# (int) Log level
log_level = 2

# (str) Path to build artifact storage
# build_dir = ./.buildozer

# (str) Path to build output (APK)
bin_dir = ./bin
