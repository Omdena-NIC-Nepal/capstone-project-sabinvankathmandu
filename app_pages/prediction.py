from scripts.climate.prediction import *
from scripts.climate.models import load_model

import sys
import streamlit as st
import matplotlib.pyplot as plt

sys.path.append(
    "C:/My Computer/D DRIVE/Omdena/assignment/capstoneproject/capstone-project-sabinvankathmandu"
)

def show(df):
    st.title("📈 Predict Average Mean Temperature")

    # Load trained model
    model = load_model()
    if model is None:
        st.error("Trained model not found! Please train the model first.")
        st.stop()

    # Input climate feature values
    st.subheader("Enter Climate Features")

    year = st.number_input("Year", min_value=1900, max_value=2100, value=2025)
    avg_min_temp = st.number_input("Avg Min Temp (°C)", value=5.0)
    avg_max_temp = st.number_input("Avg Max Temp (°C)", value=15.0)
    relative_humidity = st.number_input("Relative Humidity (%)", value=70.0)
    precipitation_max = st.number_input("Max Precipitation (mm)", value=60.0)
    annual_rainfall = st.number_input("Annual Rainfall (mm)", value=1200.0)
    agri_land_area = st.number_input("Agricultural Land Area (hectares)", value=2000.0)
    cropland_pct = st.number_input("Cropland Percentage (%)", value=40.0)
    fertilizer_kg_per_ha = st.number_input("Fertilizer Use (kg/ha)", value=100.0)
    population_density = st.number_input("Population Density (people/km²)", value=200.0)

    # Predict button
    if st.button("🔮 Predict Temperature"):
        prediction = make_prediction(
            model,
            year, avg_min_temp, avg_max_temp, relative_humidity,
            precipitation_max, annual_rainfall, agri_land_area,
            cropland_pct, fertilizer_kg_per_ha, population_density
        )
        st.success(f"🌡️ Predicted Average Mean Temperature: **{prediction:.2f} °C**")

        # Optional: show historical average
        st.subheader("📊 Historical Context")
        historical_avg = get_historical_average(df, "avg_mean_temp")
        st.write(f"Historical Average Temperature: **{historical_avg:.2f} °C**")

        st.line_chart(get_historical_values(df, "avg_mean_temp").set_index("year"))
