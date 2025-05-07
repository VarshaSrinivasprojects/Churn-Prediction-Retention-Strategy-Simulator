import streamlit as st
import pandas as pd
import numpy as np

st.title("📉 Churn Risk Predictor (Simulated Vertex AI)")

st.markdown("Enter customer details to estimate churn risk. This simulates calling a deployed Vertex AI model.")

# Simulated form input
monthly_charges = st.slider("Monthly Charges ($)", 20.0, 120.0, 70.0)
tenure = st.slider("Tenure (months)", 1, 72, 12)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "None"])
payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

if st.button("Predict Churn Risk"):
    # Simulate payload to Vertex AI endpoint
    payload = {
        "monthly_charges": monthly_charges,
        "tenure": tenure,
        "contract": contract,
        "internet": internet,
        "payment": payment
    }

    # Simulate response based on some simple logic
    risk_score = 0.3  # base
    if contract == "Month-to-month":
        risk_score += 0.3
    if internet == "Fiber optic":
        risk_score += 0.2
    if payment == "Electronic check":
        risk_score += 0.1
    if tenure < 12:
        risk_score += 0.2
    if monthly_charges > 80:
        risk_score += 0.1

    risk_score = min(risk_score, 0.95)

    st.subheader("🔎 Churn Risk Prediction")
    st.metric(label="Estimated Churn Probability", value=f"{risk_score:.0%}")
    st.progress(risk_score)
