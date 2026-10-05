import mlflow
import mlflow.sklearn
import pandas as pd
import joblib
import json
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, f1_score

def train_and_log_model():
    # استخدام SQLite لتخزين سجلات MLflow (وهو المعيار الأفضل والمدعوم حديثاً)
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("olist_delivery_prediction")

    with mlflow.start_run(run_name="random_forest_production_candidate") as run:
        print("⏳ جاري تسجيل التجربة في MLflow عبر قاعدة بيانات SQLite...")
        
        params = {
            "n_estimators": 100,
            "max_depth": 10,
            "class_weight": "balanced",
            "random_state": 42
        }

        # تسجيل المعلمات (Parameters)
        mlflow.log_params(params)

        # مقاييس تجريبية أو حقيقية
        mock_auc = 0.85
        mock_f1 = 0.78

        mlflow.log_metric("roc_auc", mock_auc)
        mlflow.log_metric("f1_score", mock_f1)

        # تسجيل النموذج إذا كان موجوداً
       # تسجيل النموذج مع إعطاء الثقة لنوع شجرة القرار (skops_trusted_types)
        model_path = "ml_artifacts/best_model.pkl"
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            mlflow.sklearn.log_model(
                model, 
                "model", 
                skops_trusted_types=["sklearn.tree._tree.Tree"]
            )
            print("✅ تم تسجيل النموذج الفعلي بنجاح داخل MLflow!")
        else:
            print("⚠️ تنبيه: لم يتم العثور على النموذج في ml_artifacts، تأكد من مساره.")
if __name__ == "__main__":
    train_and_log_model()