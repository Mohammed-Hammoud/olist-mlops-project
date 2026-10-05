import logging
import os
import sys

def setup_logger(name="olist_mlops"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # منع تكرار الـ handlers إذا تم استدعاء الlogger أكثر من مرة
    if not logger.handlers:
        # 1. إنشاء مجلد للسجلات إذا لم يكن موجوداً
        os.makedirs("logs", exist_ok.is_dir() if hasattr(os.makedirs, 'is_dir') else os.makedirs("logs", exist_ok=True))
        
        # تنسيق السجلات (Timestamp - Level - Name - Message)
        formatter = logging.Formatter(
            '%(asctime)s - [%(levelname)s] - %(name)s - %(message)s'
        )
        
        # أ. إرسال السجلات إلى الـ Console (الشاشة)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # ب. إرسال السجلات إلى ملف (File Handler)
        file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    return logger