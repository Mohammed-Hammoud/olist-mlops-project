
```markdown
# 📦 Olist Delivery Delay Prediction - MLOps Pipeline

An end-to-end, production-grade **MLOps** pipeline designed to predict e-commerce shipping delivery delays using the Brazilian **Olist** dataset. This project covers the full machine learning lifecycle—from exploratory data analysis and model tracking to automated quality assurance, high-performance API serving, containerization, and continuous integration.

---

## 🚀 MLOps Lifecycle Architecture

1. **Environment & Dependency Management:** Powered by **`uv`** for lightning-fast package installation and strict version alignment (`scikit-learn==1.5.1`).
2. **Model Tracking & Registry:** Managed via **`MLflow`** to log parameters, metrics, and artifact storage (`best_model.pkl`).
3. **Model Serving:** Built with **`FastAPI`** and **`Uvicorn`** to expose low-latency inference endpoints.
4. **Quality Assurance & Testing:** Automated test suites using **`pytest`** and **`httpx`** to validate pipeline health and endpoint responses.
5. **Containerization:** Isolated via **`Docker`** for seamless, reproducible deployments across any cloud or local environment.
6. **Continuous Integration (CI/CD):** Automated code validation and testing pipelines via **`GitHub Actions`**.

---

## 📁 Project Structure

```text
olist_mlops_project/
│
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD pipeline
│
├── app/
│   └── main.py                # FastAPI application and routing
│
├── src/
│   ├── predict.py             # Inference pipeline & preprocessing logic
│   └── logger.py              # Centralized logging configuration
│
├── tests/
│   └── test_pipeline.py       # Automated integration & unit tests
│
├── ml_artifacts/
│   └── best_model.pkl         # Trained and serialized production model
│
├── .dockerignore              # Exclusions for Docker build context
├── Dockerfile                 # Container build configuration
├── requirements.txt           # Full development requirements
└── README.md                  # Project documentation

```

---

## 🛠️ Getting Started (Local Setup)

### 1. Prerequisites

* Python 3.12+
* `uv` (Fast Python package installer)

### 2. Environment Setup

Run the following commands in your terminal:

```bash
# Create a virtual environment
uv venv .venv --python 3.12

# Activate the environment (Windows PowerShell)
.venv\Scripts\activate

# Install production dependencies
uv pip install -r requirements-prod.txt

```

### 3. Run Automated Quality Assurance (QA)

Validate system health and endpoint behavior using `pytest`:

```bash
python -m pytest

```

### 4. Run the API Locally

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload --port 8000

```

The interactive API documentation will be available at: `http://127.0.0.1:8000/docs`

---

## 🔌 API Usage Example

You can test the prediction endpoint (`/post /predict`) using the following JSON payload:

```json
{
    "order_purchase_timestamp": "2018-01-01 10:00:00",
    "customer_state": "SP",
    "total_items": 1.0,
    "total_price": 75.0,
    "total_freight": 15.0,
    "total_payment_value": 90.0,
    "payment_installments_count": 1.0
}

```

---

## 🐳 Containerization (Docker)

To build and run the model service inside an isolated Docker container:

```bash
# Build the Docker image
docker build -t olist-mlops-service .

# Run the container and bind port 8000
docker run -p 8000:8000 olist-mlops-service

```

---

## 👨‍💻 Tech Stack

* **Language:** Python 3.12
* **Package Management:** `uv`
* **Machine Learning:** Scikit-Learn
* **Tracking & Registry:** MLflow
* **API Framework:** FastAPI & Uvicorn
* **Testing:** Pytest & HTTPX
* **CI/CD:** GitHub Actions
* **Containerization:** Docker
