import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import rasterio
import rasterio.mask
import geopandas as gpd
import seaborn as sns

# ---------------------- Helper Functions ----------------------
def mask_raster(raster_path, vector_path):
    with rasterio.open(raster_path) as src:
        vector_data = gpd.read_file(vector_path)
        vector_data = vector_data.to_crs(src.crs)
        geoms = vector_data.geometry.values
        masked_image, _ = rasterio.mask.mask(src, geoms, crop=True)
        masked_image = np.where(masked_image == src.nodata, np.nan, masked_image)
    return masked_image[0]

def raster_stats(raster_data):
    return {
        "mean": np.nanmean(raster_data),
        "median": np.nanmedian(raster_data),
        "std": np.nanstd(raster_data),
        "min": np.nanmin(raster_data),
        "max": np.nanmax(raster_data)
    }

def monthly_values(raster_path):
    with rasterio.open(raster_path) as src:
        values = src.read()
        values = np.where(values == src.nodata, np.nan, values)
    return values

def monthly_mean(values):
    return [np.nanmean(month) for month in values]

def plot_monthly_trend(monthly_means, label, units, year):
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(range(1, 13), monthly_means, marker="o", linestyle="-", color="b")
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax.set_xlabel("Month")
    ax.set_ylabel(f"Mean {label} ({units})")
    ax.set_title(f"Monthly {label} Trend ({year})")
    ax.grid()
    st.pyplot(fig)

def load_raster_data(raster_path):
    with rasterio.open(raster_path) as src:
        data = src.read(1)
        data = np.where(data == src.nodata, np.nan, data)
    return data

def plot_distribution(data1, data2, title, xlabel, color1, color2):
    fig, ax = plt.subplots()
    sns.histplot(data1.flatten(), bins=30, color=color1, label="2020", kde=True, ax=ax)
    sns.histplot(data2.flatten(), bins=30, color=color2, label="2050", kde=True, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Frequency")
    ax.legend()
    st.pyplot(fig)

def plot_comparison(data1, data2, title, ylabel, color1, color2):
    stats1 = raster_stats(data1)
    stats2 = raster_stats(data2)
    labels = list(stats1.keys())
    values1 = list(stats1.values())
    values2 = list(stats2.values())

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar(x - width/2, values1, width, label='2020', color=color1)
    ax.bar(x + width/2, values2, width, label='2050', color=color2)

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    st.pyplot(fig)

# ---------------------- Streamlit App ----------------------
def app():
    st.title("\U0001F4CD GIS Raster Climate EDA for Nepal")
    st.markdown("Explore masked raster, monthly trends, and distribution comparisons for temperature and precipitation in Nepal (2020 vs 2050).")

    # File paths
    raster_temperature_path_2020 = "data/temp_2020.tif"
    raster_temperature_path_2050 = "data/temp_2050.tif"
    raster_precipitation_path_2020 = "data/precip_2020.tif"
    raster_precipitation_path_2050 = "data/precip_2050.tif"
    vector_boundary_path = "data/nepal_boundary.shp"

    st.header("\U0001F5FA\uFE0F Masked Raster Visualizations")
    if st.checkbox("Show Masked Precipitation Maps"):
        mask_2020 = mask_raster(raster_precipitation_path_2020, vector_boundary_path)
        mask_2050 = mask_raster(raster_precipitation_path_2050, vector_boundary_path)

        fig1, ax1 = plt.subplots()
        ax1.imshow(mask_2020, cmap="Blues")
        ax1.set_title("Precipitation - Nepal 2020")
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots()
        ax2.imshow(mask_2050, cmap="Blues")
        ax2.set_title("Precipitation - Nepal 2050")
        st.pyplot(fig2)

    st.header("\U0001F4CA Monthly Trends")
    if st.checkbox("Show Monthly Trends (Temp & Precip)"):
        monthly_temp_2020 = monthly_values(raster_temperature_path_2020)
        monthly_temp_2050 = monthly_values(raster_temperature_path_2050)
        monthly_precip_2020 = monthly_values(raster_precipitation_path_2020)
        monthly_precip_2050 = monthly_values(raster_precipitation_path_2050)

        plot_monthly_trend(monthly_mean(monthly_precip_2020), "Precipitation", "mm", 2020)
        plot_monthly_trend(monthly_mean(monthly_precip_2050), "Precipitation", "mm", 2050)
        plot_monthly_trend(monthly_mean(monthly_temp_2020), "Temperature", "°C", 2020)
        plot_monthly_trend(monthly_mean(monthly_temp_2050), "Temperature", "°C", 2050)

    st.header("\U0001F4C8 Histogram Comparisons")
    if st.checkbox("Show Distributions (Temp & Precip)"):
        temp_2020 = load_raster_data(raster_temperature_path_2020)
        temp_2050 = load_raster_data(raster_temperature_path_2050)
        precip_2020 = load_raster_data(raster_precipitation_path_2020)
        precip_2050 = load_raster_data(raster_precipitation_path_2050)

        plot_distribution(temp_2020, temp_2050, "Temperature Distribution (2020 vs 2050)", "Temperature (°C)", "orange", "purple")
        plot_distribution(precip_2020, precip_2050, "Precipitation Distribution (2020 vs 2050)", "Precipitation (mm)", "green", "blue")

    st.header("\U0001F4CB Summary Statistics")
    if st.checkbox("Show Statistical Comparison (Bar Charts)"):
        temp_2020 = load_raster_data(raster_temperature_path_2020)
        temp_2050 = load_raster_data(raster_temperature_path_2050)
        precip_2020 = load_raster_data(raster_precipitation_path_2020)
        precip_2050 = load_raster_data(raster_precipitation_path_2050)

        plot_comparison(temp_2020, temp_2050, "Temperature Summary Comparison", "Temperature (°C)", "orange", "purple")
        plot_comparison(precip_2020, precip_2050, "Precipitation Summary Comparison", "Precipitation (mm)", "green", "blue")

if __name__ == "__main__":
    app()
