# Base image — Python 3.11 slim (smaller size)
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (Docker cache optimization)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy model files
COPY model/ ./model/

# Copy app files
COPY app/ ./app/

# Download NLTK data inside container
RUN python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet')"

# Expose port 8000
EXPOSE 8000

# Run the app from app/ folder
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "app"]
