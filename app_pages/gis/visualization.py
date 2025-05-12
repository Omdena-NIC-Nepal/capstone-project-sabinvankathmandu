import sys
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
import numpy as np
from rasterio.mask import mask
import seaborn as sns

sys.path.append(
    "C:/My Computer/D DRIVE/Omdena/assignment/capstoneproject/capstone-project-sabinvankathmandu"
)

def plot_precip_trend(monthly_mean_precip_2020, monthly_mean_precip_2050):
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(7, 5))

    # Plot 2020 precipitation data
    ax.plot(
        range(1, 13),
        monthly_mean_precip_2020,
        marker="o",
        linestyle="-",
        color="b",
        label="2020 Precipitation"
    )

    # Plot 2050 precipitation data
    ax.plot(
        range(1, 13),
        monthly_mean_precip_2050,
        marker="s",
        linestyle="--",
        color="r",
        label="2050 Precipitation"
    )

    # Formatting
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean Precipitation (mm)")
    ax.set_title("Monthly Precipitation Trends: 2020 vs. 2050")
    ax.legend()
    ax.grid(True)

    # Show in Streamlit
    st.pyplot(fig)


# Function to return monthly values of raster files (band values)
def monthly_values(path):
	with rasterio.open(path) as src:
		monthly_values = [src.read(i) for i in range(1, 13)]  # Load all 12 bands

	return monthly_values

# function to calculate the monthly mean values
def monthly_mean(monthly_values):
	monthly_means = [np.mean(month) for month in monthly_values]
	return monthly_means

# Function to plot the monthly trends of temp or precipitations
def plot_montly_trend(monthly_means, label, units, year):
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(7, 5))

    # Plotting the data
    ax.plot(range(1, 13), monthly_means, marker="o", linestyle="-", color="b")
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax.set_xlabel("Month")
    ax.set_ylabel(f"Mean {label} ({units})")
    ax.set_title(f"Monthly {label} Trend ({year})")
    ax.grid(True)

    # Display in Streamlit
    st.pyplot(fig)

# creating raster file paths
raster_precipitation_path_2020 = "data/rastar/nepal_climate_data/nepal_precipitation_2020.tif"
raster_precipitation_path_2050 = "data/rastar/nepal_climate_data/nepal_precipitation_2050.tif"
raster_temperature_path_2020 = "data/rastar/nepal_climate_data/nepal_temperature_2020.tif"
raster_temperature_path_2050 = "data/rastar/nepal_climate_data/nepal_temperature_2050.tif"

def plot_monthly_trend():
	monthly_temp_2020 = monthly_values(raster_temperature_path_2020)
	monthly_temp_2050 = monthly_values(raster_temperature_path_2050)
	monthly_precip_2020 = monthly_values(raster_precipitation_path_2020)
	monthly_precip_2050 = monthly_values(raster_precipitation_path_2050)

	# Computing the montlhy mean temp and precipitation for 2020 / 50
	monthly_mean_temp_2020 = monthly_mean(monthly_temp_2020)
	monthly_mean_temp_2050 = monthly_mean(monthly_temp_2050)
	monthly_mean_precip_2020 = monthly_mean(monthly_precip_2020)
	monthly_mean_precip_2050 = monthly_mean(monthly_precip_2050)

	#plotting the montly trend of precipation and temperatures
	plot_montly_trend(monthly_mean_precip_2020, "Precipitations", "mm", 2020)
	plot_montly_trend(monthly_mean_precip_2050, "Precipitations", "mm", 2050)
	plot_montly_trend(monthly_mean_temp_2020, "Temperatures", "°C", 2020)
	plot_montly_trend(monthly_mean_temp_2050, "Temperatures", "°C", 2050)

	plot_precip_trend(monthly_mean_precip_2020, monthly_mean_precip_2050)



