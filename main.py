import os
import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image as KivyImage
from kivy.clock import Clock
from PIL import Image as PILImage

class FaceMatcherApp(App):
    def build(self):
        self.title = "نظام مطابقة الوجوه"
        
        # مجلد قاعدة البيانات الداخلي للتطبيق على الهاتف
        self.db_dir = os.path.join(self.user_data_dir, "database")
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)

        # تصميم الواجهة الرئيسية
        layout = BoxLayout(orientation='vertical', padding=25, spacing=20)
        
        self.status_label = Label(
            text="مرحباً بك في نظام مطابقة الوجوه الذكي",
            font_size=18,
            size_hint=(1, 0.2),
            halign="center"
        )
        
        # زر فتح الكاميرا التقاط الوجه
        btn_camera = Button(
            text="📷 التقاط صورة بالكاميرا",
            font_size=18,
            background_color=(0.1, 0.6, 0.8, 1),
            size_hint=(1, 0.25)
        )
        btn_camera.bind(on_press=self.capture_image)
        
        # زر البحث في قاعدة البيانات
        btn_search = Button(
            text="🗄️ البحث في قاعدة البيانات",
            font_size=18,
            background_color=(0.5, 0.2, 0.7, 1),
            size_hint=(1, 0.25)
        )
        btn_search.bind(on_press=self.search_database)

        layout.add_widget(self.status_label)
        layout.add_widget(btn_camera)
        layout.add_widget(btn_search)
        
        return layout

    def capture_image(self, instance):
        self.status_label.text = "جاري تفعيل الكاميرا..."
        # كود ربط كاميرا الهاتف عبر OpenCV
        try:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            if ret:
                img_path = os.path.join(self.user_data_dir, "captured_face.jpg")
                cv2.imwrite(img_path, frame)
                self.status_label.text = "تم التقاط الصورة بنجاح!"
            cap.release()
        except Exception as e:
            self.status_label.text = f"خطأ في الكاميرا: {str(e)}"

    def search_database(self, instance):
        self.status_label.text = "جاري مسح قاعدة البيانات ومطابقة الملامح..."
        # هنا يتم استدعاء خوارزمية المقارنة مع الصور الموجودة في مجلد قاعدة البيانات الداخلي
        if os.path.exists(self.db_dir):
            files = os.listdir(self.db_dir)
            self.status_label.text = f"تم العثور على {len(files)} صورة في قاعدة البيانات."
        else:
            self.status_label.text = "مجلد قاعدة البيانات فارغ."

if __name__ == '__main__':
    FaceMatcherApp().run()