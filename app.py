import streamlit as st
import sys
from app_pages import data_exploratoins, dataanalysis, train_model, prediction
from scripts.climate.data_utils import load_climate_data
from app_pages.gis import overview, spatial_eda

st.set_page_config(page_title="Sabin Nepal Climate Analysis", page_icon=" ", layout="wide")
st.title("Nepal Climate Trend Analysis and Predictions")
st.markdown("We analyse nepal climatic data, preditcs the future trends")

df = load_climate_data()
gdf = spatial_eda.load_vector()

# Sidebar navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["🌍 Climate","🌎 GIS", "🌦️ Weather"])
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
        data_exploratoins.show(df)
    with tab3:
        train_model.show(df)
    with tab4:
        prediction.show(df)

# if st.button("Predict Temperature"):
#     st.write("We will predict temperature in a moment")


elif menu == "🌎 GIS":
    st.title("GIS Data Analysis for Nepal")
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Overview",
        "🌍 Spatial EDA",
        "🌐 Raster/Vector Data",
        "🗺️ Interactive Maps"
    ])

    with tab1:
        overview.show()
    with tab2:
        spatial_eda.check_basic_info(spatial_eda.load_vector())
    with tab3:
        st.header(tab3)
    with tab4:
        st.header(tab4)

