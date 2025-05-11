import sys
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
import numpy as np
from rasterio.mask import mask
import fiona
import seaborn as sns

sys.path.append(
    "C:/My Computer/D DRIVE/Omdena/assignment/capstoneproject/capstone-project-sabinvankathmandu"
)


def load_vector(path="data/vector/Shape_Data/local_unit.shp"):
    try:

        gdf = gpd.read_file(path)
        return gdf
    except Exception as e:
        st.error(f"❌ Failed to load vector data: {e}")
        return None


def check_basic_info(gdf):
    if gdf is None:
        st.error("GeoDataFrame could not be loaded.")
        return

    st.subheader("🧾 Basic GeoDataFrame Info")
    st.write("🔹 Head of GeoDataFrame:")
    gdf_display = gdf.copy()
    gdf_display['geometry'] = gdf_display['geometry'].astype(str)
    st.write(gdf_display.head())

    st.write("🔹 Coordinate Reference System (CRS):")
    st.code(gdf.crs)

    st.write("🔹 Geometry column:")
    st.write(gdf.geometry.astype(str))
    st.write("🔹 Null values in each column:")
    st.write(gdf.isnull().sum())
