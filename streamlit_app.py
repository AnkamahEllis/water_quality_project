import streamlit as st
import pandas as pd
import joblib

st.title("Water Quality Prediction App")

@st.cache_resource
def load_model():
    return joblib.load("random_forest_pipeline.joblib")

model = load_model()

st.subheader("Enter water quality values")

year = st.number_input("Year", min_value=1900, max_value=2100, value=2026, step=1)
month = st.number_input("Month", min_value=1, max_value=12, value=7, step=1)
ph = st.number_input("pH", value=7.0, format="%.2f")
turbidity = st.number_input("Turbidity", value=0.0, format="%.2f")
conductivity = st.number_input("Conductivity", value=0.0, format="%.2f")
temperature = st.number_input("Temperature", value=25.0, format="%.2f")

input_df = pd.DataFrame([{
    "year": year,
    "month": month,
    "ph": ph,
    "turbidity": turbidity,
    "conductivity": conductivity,
    "temperature": temperature
}])

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted coagulant dosage (kg/day): {prediction:.3f}")