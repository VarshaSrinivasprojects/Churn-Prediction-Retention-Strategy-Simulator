# Churn Predictor Web App (Simulated Vertex AI)

A Streamlit app that simulates churn prediction by calling a Vertex AI endpoint behind the scenes.

## Features
- Accepts customer details via UI
- Simulates churn risk based on rules
- Ready for replacement with actual Vertex AI endpoint in `predict.py`

## To Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## To Deploy to Cloud Run
1. Build the image:
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/churn-app
```

2. Deploy to Cloud Run:
```bash
gcloud run deploy churn-app --image gcr.io/YOUR_PROJECT_ID/churn-app --platform managed --allow-unauthenticated --region us-central1
```
