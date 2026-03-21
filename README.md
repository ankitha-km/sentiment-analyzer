# SentimentIQ 🎯

Real-time 4-class Sentiment Analysis API powered by NLP and Explainable AI.

## 🌐 Live Demo
**App:** https://sentimentiq-nwr2.onrender.com  
**API Docs:** https://sentimentiq-nwr2.onrender.com/docs

## 🏗️ Tech Stack
| Layer | Technology |
|-------|-----------|
| ML Model | TF-IDF + Logistic Regression |
| Explainability | SHAP |
| Class Balancing | SMOTE |
| API | FastAPI |
| Container | Docker |
| Orchestration | Kubernetes |
| Cloud | AWS EC2 |
| Hosting | Render |

## 📊 Model Performance
- Dataset: 74,682 tweets (Kaggle)
- Classes: Positive, Negative, Neutral, Irrelevant
- Accuracy: ~86% on validation set

## 🗂️ Project Structure
sentiment-analyzer/
├── app/
│   ├── main.py          ← FastAPI app
│   ├── predict.py       ← ML prediction logic
│   └── static/
│       └── index.html   ← UI
├── model/
│   ├── model.pkl
│   ├── vectorizer.pkl
│   └── label_encoder.pkl
├── notebook/
│   └── 01_eda_and_model.ipynb
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile
└── requirements.txt

## 🚀 Run Locally
git clone https://github.com/ankitha-km/sentiment-analyzer.git
cd sentiment-analyzer
pip install -r requirements.txt
cd app
uvicorn main:app --reload

## 🐳 Run with Docker
docker pull ysgsvsv65/sentimentiq:v1
docker run -d -p 8000:8000 ysgsvsv65/sentimentiq:v1

## 📡 API Usage
POST /predict
Content-Type: application/json

{
  "text": "I absolutely love this product!"
}

Response:
{
  "sentiment": "Positive",
  "confidence": 0.87,
  "probabilities": {
    "Positive": 0.87,
    "Negative": 0.05,
    "Neutral": 0.06,
    "Irrelevant": 0.02
  }
}