
import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open('model_xgb.pkl', 'rb'))

st.title("📉 Telco Customer Churn Prediction")

st.markdown("""
Masukkan informasi pelanggan untuk memprediksi apakah pelanggan akan berhenti berlangganan (churn) atau tidak.
""")

# Input fields
gender = st.selectbox("Jenis Kelamin", ['Male', 'Female'])
senior = st.selectbox("Apakah Senior Citizen?", [0, 1])
partner = st.selectbox("Memiliki Partner?", [0, 1])
dependents = st.selectbox("Memiliki Tanggungan?", [0, 1])
tenure = st.slider("Tenure (dalam bulan)", 0, 72, 12)
monthly_charges = st.slider("Biaya Bulanan", 0, 150, 70)
total_charges = st.slider("Total Biaya", 0, 10000, 2000)

# Data input
input_data = pd.DataFrame({
    'gender': [1 if gender == 'Male' else 0],
    'SeniorCitizen': [senior],
    'Partner': [partner],
    'Dependents': [dependents],
    'tenure': [tenure],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges]
})

# Predict button
if st.button("🔍 Prediksi Churn"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Pelanggan kemungkinan besar AKAN CHURN.")
    else:
        st.success("✅ Pelanggan kemungkinan TIDAK churn.")
