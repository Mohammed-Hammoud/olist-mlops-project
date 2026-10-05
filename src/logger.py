import logging
import os

def setup_logger(name: str, log_file: str = "logs/app.log", level=logging.INFO):
    # إنشاء مجلد السجلات بأمان دون تعقيد
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # منع تكرار الـ Handlers إذا تم استدعاء الـ logger أكثر من مرة
    if not logger.handlers:
        # File Handler
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setLevel(level)

        # Stream Handler (Console)
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger