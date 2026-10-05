import pandas as pd
import joblib
import yaml
from src.preprocessing import DataPreprocessor
from src.logger import setup_logger

logger = setup_logger("predictor")

class DeliveryPredictor:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
            
        self.preprocessor = DataPreprocessor(config_path)
        
        model_path = self.config["paths"]["model_path"]
        self.model = joblib.load(model_path)
        logger.info(f"تم تحميل النموذج بنجاح من المسار: {model_path}")

    def predict(self, data_dict: dict) -> dict:
        try:
            # تحويل المدخلات إلى DataFrame صف واحد
            df = pd.DataFrame([data_dict])
            
            # المعالجة عبر الـ Preprocessor
            X = self.preprocessor.transform(df)
            
            # التنبؤ
            pred = self.model.predict(X)[0]
            proba = self.model.predict_proba(X)[0][1]
            
            result = {
                "is_late": int(pred),
                "probability": float(proba),
                "model_version": "v1.0.0"
            }
            
            # تسجيل الطلب والنتيجة في الـ Logs (كما يطلب التاسك)
            logger.info(f"طلب تنبؤ ناجح | المدخلات: {data_dict} | النتيجة: {result}")
            
            return result
        except Exception as e:
            logger.error(f"حدث خطأ أثناء عملية التنبؤ للمدخلات {data_dict}: {str(e)}")
            raise e