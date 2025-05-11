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

# creating raster file paths
raster_precipitation_path_2020 = "data/rastar/nepal_climate_data/nepal_precipitation_2020.tif"
raster_precipitation_path_2050 = "data/rastar/nepal_climate_data/nepal_precipitation_2050.tif"
raster_temperature_path_2020 = "data/rastar/nepal_climate_data/nepal_temperature_2020.tif"
raster_temperature_path_2050 = "data/rastar/nepal_climate_data/nepal_temperature_2050.tif"

def nepal_GIS(gdf):
	st.write("Districts and Province of Nepal")
	fig, ax = plt.subplots(figsize=(6, 6))
	gdf.plot(ax=ax, cmap="viridis", edgecolor="black")
	ax.set_title("Districts of Nepal")
	st.pyplot(fig)

	# Plot by State Code
	fig, ax = plt.subplots(figsize=(10, 6))
	gdf.plot(column="STATE_CODE", cmap="Set2", legend=False, ax=ax)
	ax.set_title("Provinces of Nepal")
	st.pyplot(fig)

# Function to load raster image
def read_raster(path):
	with rasterio.open(path) as src:
		raster_src = src.read(1)
		profile = src.profile

	return raster_src, profile

def visualize_raster_data():
    temp_2020, temp_profile_2020 = read_raster(raster_temperature_path_2020)
    temp_2050, temp_profile_2050 = read_raster(raster_temperature_path_2050)
    precip_2020, precip_profile_2020 = read_raster(raster_precipitation_path_2020)
    precip_2050, precip_profile_2050 = read_raster(raster_precipitation_path_2050)

    # --- Temperature 2020 ---
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    im1 = ax1.imshow(temp_2020, cmap="coolwarm", interpolation="nearest")
    plt.colorbar(im1, ax=ax1, label="Temperature (°C)")
    ax1.set_title("Temperature Data 2020 - Nepal")
    st.pyplot(fig1)

    # --- Temperature 2050 ---
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    im2 = ax2.imshow(temp_2050, cmap="coolwarm", interpolation="nearest")
    plt.colorbar(im2, ax=ax2, label="Temperature (°C)")
    ax2.set_title("Temperature Data 2050 - Nepal")
    st.pyplot(fig2)

    # --- Precipitation 2020 ---
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    im3 = ax3.imshow(precip_2020, cmap="Blues", interpolation="nearest")
    plt.colorbar(im3, ax=ax3, label="Precipitation (mm)")
    ax3.set_title("Precipitation Data 2020 - Nepal")
    st.pyplot(fig3)

    # --- Precipitation 2050 (Optional if needed) ---
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    im4 = ax4.imshow(precip_2050, cmap="Blues", interpolation="nearest")
    plt.colorbar(im4, ax=ax4, label="Precipitation (mm)")
    ax4.set_title("Precipitation Data 2050 - Nepal")
    st.pyplot(fig4)
