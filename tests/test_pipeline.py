import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_prediction_endpoint():
    payload = {
        "order_purchase_timestamp": "2018-01-01 10:00:00",
        "customer_state": "SP",
        "total_items": 1.0,
        "total_price": 75.0,
        "total_freight": 15.0,
        "total_payment_value": 90.0,
        "payment_installments_count": 1.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "is_late" in data
    assert "probability" in data
    assert data["model_version"] == "v1.0.0"