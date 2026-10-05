import pandas as pd
import numpy as np
import joblib
import json
import yaml

class DataPreprocessor:
    def __init__(self, config_path="config/config.yaml"):
        # قراءة ملف الإعدادات
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
            
        paths = self.config["paths"]
        
        # تحميل جميع الـ Fitted Objects المحفوظة مسبقاً من النوت بوك
        self.scaler = joblib.load(paths["scaler_path"])
        self.imputer = joblib.load(paths["imputer_path"])
        
        encoder_data = joblib.load(paths["encoder_path"])
        self.state_risk_map = encoder_data["state_risk_map"]
        self.default_risk = encoder_data["default_risk"]
        
        with open(paths["features_path"], "r", encoding="utf-8") as f:
            self.feature_list = json.load(f)
            
        self.numerical_cols = [
            'total_items', 'total_price', 'total_freight', 
            'total_payment_value', 'payment_installments_count',
            'purchase_hour', 'purchase_day_of_week', 'purchase_month'
        ]

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """تطبيق نفس خطوات المعالجة والتحويل دون أي إعادة تدريب (No re-fitting)"""
        df = df.copy()
        
        # 1. استخراج الميزات الزمنية
        df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
        df['purchase_hour'] = df['order_purchase_timestamp'].dt.hour
        df['purchase_day_of_week'] = df['order_purchase_timestamp'].dt.dayofweek
        df['purchase_month'] = df['order_purchase_timestamp'].dt.month
        
        # 2. تطبيق الـ Imputer المحفوظ
        df[self.numerical_cols] = self.imputer.transform(df[self.numerical_cols])
        
        # 3. تطبيق الـ Scaler المحفوظ
        df[self.numerical_cols] = self.scaler.transform(df[self.numerical_cols])
        
        # 4. ترميز الولايات باستخدام القاموس المحفوظ
        df['state_risk_encoded'] = df['customer_state'].map(self.state_risk_map).fillna(self.default_risk)
        
        # إرجاع الميزات النهائية بالترتيب المطلوب للنموذج
        return df[self.feature_list]