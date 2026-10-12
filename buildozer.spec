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
# تأكدنا من تضمين بايثون، ومكتبة kivy، والمكتبات الثقيلة المطلوبة للتعرف على الوجوه
requirements = python3,kivy,pillow
# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
# إذن الكاميرا وقراءة التخزين ضروريان لتطبيق التعرف على الوجوه
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minAPI = 21

# (str) Android APK versioning
version = 0.1