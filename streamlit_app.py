import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

st.title("Water Quality Prediction App")

# Display project image from URL
image_url = "https://www.citinewsroom.com/wp-content/uploads/2026/02/ODASO-2.jpeg"
st.image(image_url, caption="Water treatment at Odaso, GH", use_column_width=True)  # [1]

@st.cache_resource
def load_model():
    return joblib.load("random_forest_pipeline.joblib")

model = load_model()

st.subheader("Model performance")

@st.cache_data
def compute_metrics():
    # Load the same data used for training/evaluation
    df = pd.read_csv("water_quality.csv")

    feature_cols = ["year", "month", "ph", "turbidity", "conductivity", "temperature"]
    target_col = "coagulant_dosage"

    X = df[feature_cols]
    y = df[target_col]

    # Use the pipeline to get predictions on this dataset
    y_pred = model.predict(X)

    r2 = r2_score(y, y_pred)
    rmse = np.sqrt(mean_squared_error(y, y_pred))

    return r2, rmse

r2, rmse = compute_metrics()

# Show metrics in the main area (or in the sidebar if you prefer)
col1, col2 = st.columns(2)
with col1:
    st.metric("R² score", f"{r2:.3f}")
with col2:
    st.metric("RMSE (kg/day)", f"{rmse:.3f}")

st.subheader("Enter water quality values")

year = st.number_input("Year", min_value=1900, max_value=2100, value=2026, step=1)
month = st.number_input("Month", min_value=1, max_value=12, value=7, step=1)
ph = st.number_input("pH", value=7.0, format="%.2f")
turbidity = st.number_input("Turbidity (NTU)", value=0.0, format="%.2f")
conductivity = st.number_input("Conductivity (µS/cm)", value=0.0, format="%.2f")
temperature = st.number_input("Temperature (°C)", value=25.0, format="%.2f")

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