import os
import joblib
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model      = joblib.load(os.path.join(BASE_DIR, 'model', 'model.pkl'))
vectorizer = joblib.load(os.path.join(BASE_DIR, 'model', 'vectorizer.pkl'))
le         = joblib.load(os.path.join(BASE_DIR, 'model', 'label_encoder.pkl'))

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'@\w+|#', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return ' '.join(tokens)

def predict(text: str) -> dict:
    cleaned    = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    pred_idx      = model.predict(vectorized)[0]
    probabilities = model.predict_proba(vectorized)[0]
    label      = le.inverse_transform([pred_idx])[0]
    confidence = round(float(probabilities.max()), 4)
    all_probs = {
        le.classes_[i]: round(float(p), 4)
        for i, p in enumerate(probabilities)
    }
    return {
        "sentiment":     label,
        "confidence":    confidence,
        "probabilities": all_probs
    }