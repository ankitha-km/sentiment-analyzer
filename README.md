# SentimentIQ 🎯
Real-time Sentiment Analysis API powered by NLP and explainable AI.

## Tech Stack
- **ML**: TF-IDF + Logistic Regression + SMOTE
- **Explainability**: SHAP
- **API**: FastAPI
- **Container**: Docker
- **Orchestration**: Kubernetes
- **Cloud**: AWS EC2

## Project Structure
sentiment-analyzer/
├── data/               ← dataset (not tracked)
├── notebook/           ← EDA + model training
├── model/              ← saved model (not tracked)
├── app/                ← FastAPI app
├── explainability/     ← SHAP analysis
├── k8s/                ← Kubernetes configs
├── Dockerfile
└── requirements.txt

## Progress
- [x] Phase 1 — EDA & Data Cleaning
- [x] Phase 2 — Model Training + SHAP
- [ ] Phase 3 — FastAPI
- [ ] Phase 4 — Docker
- [ ] Phase 5 — Kubernetes
- [ ] Phase 6 — AWS EC2