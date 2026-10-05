from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
from src.predict import DeliveryPredictor
from src.logger import setup_logger

logger = setup_logger("api")
app = FastAPI(title="Olist Delivery Delay Prediction API", version="1.0.0")

# تهيئة المُتنبئ مرة واحدة عند بدء تشغيل الخدمة
predictor = DeliveryPredictor()

class OrderInput(BaseModel):
    order_purchase_timestamp: str
    customer_state: str
    total_items: float
    total_price: float
    total_freight: float
    total_payment_value: float
    payment_installments_count: float

class PredictionResponse(BaseModel):
    is_late: int
    probability: float
    model_version: str
    latency_ms: float

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "olist-mlops-api"}

@app.post("/predict", response_model=PredictionResponse)
def predict_order(order: OrderInput):
    start_time = time.time()
    try:
        data = order.model_dump()
        result = predictor.predict(data)
        latency = (time.time() - start_time) * 1000
        
        logger.info(f"نجاح الطلب | زمن الاستجابة: {latency:.2f}ms | النتيجة: {result}")
        
        return {
            **result,
            "latency_ms": latency
        }
    except Exception as e:
        logger.error(f"فشل معالجة الطلب: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))