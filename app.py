import streamlit as st
import sys
from app_pages import data_exploratoins, dataanalysis, train_model, prediction
from scripts.climate.data_utils import load_climate_data

st.set_page_config(page_title="Sabin Nepal Climate Analysis", page_icon=" ", layout="wide")
st.title("Nepal Climate Trend Analysis and Predictions")
st.markdown("We analyse nepal climatic data, preditcs the future trends")

df = load_climate_data()


# Sidebar navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["🌍 Climate", "🌦️ Weather"])
df = load_climate_data()

if menu == "🌍 Climate":
    st.title("🌍 Climate Data Analysis and Prediction")
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📊 Data Exploration", "📈 EDA", "🤖 Model Creation", "🔮 Prediction & Vizualization"]
    )
# --- TAB 1: Data Exploration ---
with tab1:
    dataanalysis.show(df)
with tab2:
    st.write("Tab2")
with tab3:
    st.write("Tab3")
with tab4:
    st.write("Tab4")

if st.button("Predict Temperature"):
    st.write("We will predict temperature in a moment")
