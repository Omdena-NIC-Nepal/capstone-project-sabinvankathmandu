from scripts.climate.eda_climate import *
import sys
import streamlit as st

sys.path.append("C:/My Computer/D DRIVE/Omdena/assignment/capstoneproject/capstone-project-sabinvankathmandu")

def check_null_values(df):
    null_counts = df.isnull().sum()
    st.write("Null values in each column:")
    st.write(null_counts)
    return null_counts


# Function to handle null values using a given strategy
def handle_null_values(df, strategy="mean"):
    df_cleaned = df.copy()
    for column in df_cleaned.select_dtypes(include=["float64", "int64"]).columns:
        if df_cleaned[column].isnull().sum() > 0:
            if strategy == "mean":
                df_cleaned[column].fillna(df_cleaned[column].mean(), inplace=True)
            elif strategy == "median":
                df_cleaned[column].fillna(df_cleaned[column].median(), inplace=True)
            elif strategy == "ffill":
                df_cleaned[column].fillna(method="ffill", inplace=True)
            else:
                raise ValueError(
                    "Unsupported strategy. Use 'mean', 'median', or 'ffill'."
                )
    st.write(f"Null values handled using '{strategy}' strategy.")
    return df_cleaned


# Function to generate general summary statistics
def general_summary_statistics(df):
    summary = df.describe()
    st.write("General Summary Statistics:")
    st.write(summary)
    return summary


def plot_eda(df):
    """
    Perform EDA with different visualizations on Nepal climate dataset.
    """

    # 1. Line plot of average mean temperature over years
    st.subheader("Average Mean Temperature Over Years")
    plt.figure()
    sns.lineplot(x="year", y="avg_mean_temp", data=df, marker="o", color="tomato")
    plt.xlabel("Year")
    plt.ylabel("Avg Mean Temp (°C)")
    plt.grid(True)
    st.pyplot(plt)

    # 2. Bar plot of annual rainfall over years
    st.subheader("Annual Rainfall Over Years")
    plt.figure()
    sns.barplot(x="year", y="annual_rainfall", data=df, palette="Blues_d")
    plt.xticks(rotation=45)
    plt.xlabel("Year")
    plt.ylabel("Annual Rainfall (mm)")
    st.pyplot(plt)

    # 3. Scatter plot: population density vs avg_mean_temp
    st.subheader("Population Density vs Avg Mean Temp")
    plt.figure()
    sns.scatterplot(
        x="population_density",
        y="avg_mean_temp",
        data=df,
        hue="year",
        palette="coolwarm",
        legend=False,
    )
    plt.xlabel("Population Density")
    plt.ylabel("Avg Mean Temp (°C)")
    st.pyplot(plt)

    # 4. Correlation heatmap
    st.subheader("Correlation Heatmap")
    plt.figure()
    corr = df.select_dtypes(include="number").corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="YlGnBu")
    st.pyplot(plt)

    # 5. Line plot comparing min and max temperature over time
    st.subheader("Min and Max Temperatures Over Years")
    plt.figure()
    sns.lineplot(x="year", y="avg_min_temp", data=df, label="Min Temp", marker="o")
    sns.lineplot(x="year", y="avg_max_temp", data=df, label="Max Temp", marker="o")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

    # 6. Line plot: Relative humidity over years
    st.subheader("Relative Humidity Over Years")
    plt.figure()
    sns.lineplot(x="year", y="relative_humidity", data=df, marker="o", color="teal")
    plt.xlabel("Year")
    plt.ylabel("Relative Humidity (%)")
    plt.grid(True)
    st.pyplot(plt)

    # 7. Scatter: Fertilizer usage vs Cropland percentage
    st.subheader("Fertilizer Use vs Cropland Percentage")
    plt.figure()
    sns.scatterplot(
        x="fertilizer_kg_per_ha",
        y="cropland_pct",
        data=df,
        hue="year",
        palette="viridis",
        s=80,
    )
    plt.xlabel("Fertilizer (kg/ha)")
    plt.ylabel("Cropland Area (%)")
    st.pyplot(plt)

    # 8. Line plot: Agricultural land area over years
    st.subheader("Agricultural Land Area Over Years")
    plt.figure()
    sns.lineplot(x="year", y="agri_land_area", data=df, marker="o", color="brown")
    plt.xlabel("Year")
    plt.ylabel("Agri Land Area (sq km)")
    plt.grid(True)
    st.pyplot(plt)

    # 9. Population growth trend
    st.subheader("Population Density Growth Over Years")
    plt.figure()
    sns.lineplot(x="year", y="population_density", data=df, marker="o", color="purple")
    plt.xlabel("Year")
    plt.ylabel("People per sq km")
    plt.grid(True)
    st.pyplot(plt)

    # 10. Pairplot of climate and agriculture features
    st.subheader("Pairwise Relationships Between Climate & Agri Features")
    climate_cols = [
        "avg_mean_temp",
        "avg_min_temp",
        "avg_max_temp",
        "annual_rainfall",
        "precipitation_max",
        "agri_land_area",
        "cropland_pct",
        "fertilizer_kg_per_ha",
    ]
    sns.pairplot(df[climate_cols], diag_kind="kde", corner=True)
    st.pyplot(plt)


def show(df):
    st.header("Climate Data Analysis - Nepal")
    # Example usage of functions
    check_null_values(df)
    df_cleaned = handle_null_values(df, strategy="mean")
    general_summary_statistics(df_cleaned)
    plot_eda(df_cleaned)
