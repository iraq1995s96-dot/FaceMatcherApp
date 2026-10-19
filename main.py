import os
import cv2
import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image as KivyImage
from kivy.clock import Clock, mainthread
from kivy.graphics.texture import Texture
from kivy.utils import platform
from plyer import camera as plyer_camera


class FaceMatcherApp(App):
    def build(self):
        self.title = "نظام مطابقة الوجوه"
        self.captured_path = None

        # مجلد قاعدة البيانات الداخلي للتطبيق على الهاتف
        self.db_dir = os.path.join(self.user_data_dir, "database")
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)

        # تحميل كاشف الوجوه (Haar Cascade) المضمّن مع OpenCV
        try:
            cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            self.face_cascade = cv2.CascadeClassifier(cascade_path)
            if self.face_cascade.empty():
                self.face_cascade = None
        except Exception:
            self.face_cascade = None

        # تصميم الواجهة الرئيسية
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.status_label = Label(
            text="مرحباً بك في نظام مطابقة الوجوه الذكي",
            font_size=16,
            size_hint=(1, 0.15),
            halign="center",
            text_size=(None, None)
        )

        # صورة معاينة
        self.preview = KivyImage(size_hint=(1, 0.4))

        # زر التقاط صورة
        btn_camera = Button(
            text="📷 التقاط صورة بالكاميرا",
            font_size=16,
            background_color=(0.1, 0.6, 0.8, 1),
            size_hint=(1, 0.15)
        )
        btn_camera.bind(on_press=self.capture_image)

        # زر حفظ الوجه في قاعدة البيانات
        btn_save = Button(
            text="💾 حفظ الوجه في قاعدة البيانات",
            font_size=16,
            background_color=(0.2, 0.7, 0.3, 1),
            size_hint=(1, 0.15)
        )
        btn_save.bind(on_press=self.save_face)

        # زر البحث في قاعدة البيانات
        btn_search = Button(
            text="🔍 البحث في قاعدة البيانات",
            font_size=16,
            background_color=(0.5, 0.2, 0.7, 1),
            size_hint=(1, 0.15)
        )
        btn_search.bind(on_press=self.search_database)

        layout.add_widget(self.status_label)
        layout.add_widget(self.preview)
        layout.add_widget(btn_camera)
        layout.add_widget(btn_save)
        layout.add_widget(btn_search)

        return layout

    # ============ التقاط صورة ============
    def capture_image(self, instance):
        self.status_label.text = "جاري تفعيل الكاميرا..."
        try:
            img_path = os.path.join(self.user_data_dir, "captured_face.jpg")
            # حذف الصورة القديمة إن وُجدت
            if os.path.exists(img_path):
                os.remove(img_path)

            if platform == "android":
                plyer_camera.take_picture(
                    filename=img_path,
                    on_complete=self._on_camera_done
                )
            else:
                # على الحاسوب: استخدام OpenCV مباشرة
                cap = cv2.VideoCapture(0)
                ret, frame = cap.read()
                cap.release()
                if ret:
                    cv2.imwrite(img_path, frame)
                    self._on_camera_done(img_path)
                else:
                    self.status_label.text = "تعذّر فتح الكاميرا على الحاسوب."
        except Exception as e:
            self.status_label.text = f"خطأ في الكاميرا: {str(e)}"

    @mainthread
    def _on_camera_done(self, filename):
        if filename and os.path.exists(filename):
            self.captured_path = filename
            self.status_label.text = "✅ تم التقاط الصورة بنجاح!"
            self._show_preview(filename)
        else:
            self.status_label.text = "❌ لم يتم التقاط صورة."

    def _show_preview(self, path):
        try:
            img = cv2.imread(path)
            if img is None:
                return
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.flip(img, 0)
            buf = img.tobytes()
            texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='rgb')
            texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
            self.preview.texture = texture
        except Exception as e:
            self.status_label.text = f"خطأ في المعاينة: {str(e)}"

    # ============ حفظ الوجه ============
    def save_face(self, instance):
        if not self.captured_path or not os.path.exists(self.captured_path):
            self.status_label.text = "⚠️ التقط صورة أولاً قبل الحفظ."
            return

        try:
            img = cv2.imread(self.captured_path)
            if img is None:
                self.status_label.text = "❌ تعذّر قراءة الصورة."
                return

            # كشف الوجه
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = []
            if self.face_cascade is not None:
                faces = self.face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(80, 80))

            if len(faces) == 0:
                self.status_label.text = "❌ لم يتم كشف وجه واضح. جرّب صورة أوضح."
                return

            # حفظ الوجه الأول المكتشف
            x, y, w, h = faces[0]
            face_img = img[y:y + h, x:x + w]

            # اسم فريد لكل وجه
            count = len([f for f in os.listdir(self.db_dir) if f.endswith(".jpg")])
            save_path = os.path.join(self.db_dir, f"face_{count + 1}.jpg")
            cv2.imwrite(save_path, face_img)

            self.status_label.text = f"✅ تم حفظ الوجه ({count + 1}) في قاعدة البيانات."
        except Exception as e:
            self.status_label.text = f"خطأ في الحفظ: {str(e)}"

    # ============ البحث والمطابقة ============
    def search_database(self, instance):
        if not self.captured_path or not os.path.exists(self.captured_path):
            self.status_label.text = "⚠️ التقط صورة أولاً للبحث."
            return

        try:
            files = [f for f in os.listdir(self.db_dir) if f.endswith(".jpg")]
            if not files:
                self.status_label.text = "🗄️ قاعدة البيانات فارغة. احفظ وجوهاً أولاً."
                return

            # استخراج الوجه من الصورة الملتقطة
            query_img = cv2.imread(self.captured_path)
            if query_img is None:
                self.status_label.text = "❌ تعذّر قراءة الصورة الملتقطة."
                return

            gray_q = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
            faces_q = []
            if self.face_cascade is not None:
                faces_q = self.face_cascade.detectMultiScale(gray_q, 1.1, 5, minSize=(80, 80))

            if len(faces_q) == 0:
                self.status_label.text = "❌ لم يتم كشف وجه في الصورة الملتقطة."
                return

            x, y, w, h = faces_q[0]
            query_face = cv2.resize(gray_q[y:y + h, x:x + w], (100, 100))

            # مقارنة بـ histogram لكل وجه في القاعدة
            best_match = None
            best_score = float("inf")

            for fname in files:
                fpath = os.path.join(self.db_dir, fname)
                db_img = cv2.imread(fpath, cv2.IMREAD_GRAYSCALE)
                if db_img is None:
                    continue
                db_face = cv2.resize(db_img, (100, 100))

                # مقارنة histogram
                hist_q = cv2.calcHist([query_face], [0], None, [256], [0, 256])
                hist_d = cv2.calcHist([db_face], [0], None, [256], [0, 256])
                cv2.normalize(hist_q, hist_q, 0, 1, cv2.NORM_MINMAX)
                cv2.normalize(hist_d, hist_d, 0, 1, cv2.NORM_MINMAX)

                score = cv2.compareHist(hist_q, hist_d, cv2.HISTCMP_BHATTACHARYYA)

                if score < best_score:
                    best_score = score
                    best_match = fname

            # عتبة القبول (كلما قلّت القيمة زاد التشابه)
            if best_match and best_score < 0.5:
                similarity = round((1 - best_score) * 100, 1)
                self.status_label.text = (
                    f"✅ تم العثور على تطابق!\n"
                    f"الملف: {best_match}\n"
                    f"نسبة التشابه: {similarity}%"
                )
            else:
                self.status_label.text = (
                    f"❌ لا يوجد تطابق واضح.\n"
                    f"أفضل نتيجة: {round((1 - best_score) * 100, 1) if best_match else 0}%"
                )
        except Exception as e:
            self.status_label.text = f"خطأ في البحث: {str(e)}"


if __name__ == '__main__':
    FaceMatcherApp().run()
