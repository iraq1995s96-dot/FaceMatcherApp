[app]

# (str) Title of your application
title = FaceMatcherApp

# (str) Package name
package.name = facematcher

# (str) Package domain (needed for android packaging)
package.domain = org.facematcher

# (str) Source files where the include_exts resides (relative to spec file)
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,pillow

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minAPI = 21

# (list) Supported architectures
android.architectures = arm64-v8a, armeabi-v7a

# (str) Accept Android SDK license automatically
android.accept_sdk_license = True

# (str) Android NDK version
android.ndk = 25b

# (str) Android APK versioning
version = 0.1
