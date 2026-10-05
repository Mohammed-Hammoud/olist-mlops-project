# استخدام صورة بايثون رسمية وخفيفة
FROM python:3.12-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# تحديث pip وتثبيت متطلبات الإنتاج الخفيفة مباشرة
RUN pip install --no-cache-dir --upgrade pip

# نسخ ملف متطلبات الإنتاج
COPY requirements-prod.txt ./

# تثبيت الحزم عبر pip التقليدي المضمون
RUN pip install --no-cache-dir -r requirements-prod.txt

# نسخ باقي ملفات المشروع الأساسية
COPY . .

# فتح المنفذ للتطبيق
EXPOSE 8000

# أمر التشغيل
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]