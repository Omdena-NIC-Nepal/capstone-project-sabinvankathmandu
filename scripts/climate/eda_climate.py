import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Function to check null values
# def check_null_values(df):
#     null_counts = df.isnull().sum()
#     print("Null values in each column:\n", null_counts)
#     return null_counts


# Function to handle null values using a given strategy
# def handle_null_values(df, strategy="mean"):
#     df_cleaned = df.copy()
#     for column in df_cleaned.select_dtypes(include=["float64", "int64"]).columns:
#         if df_cleaned[column].isnull().sum() > 0:
#             if strategy == "mean":
#                 df_cleaned[column].fillna(df_cleaned[column].mean(), inplace=True)
#             elif strategy == "median":
#                 df_cleaned[column].fillna(df_cleaned[column].median(), inplace=True)
#             elif strategy == "ffill":
#                 df_cleaned[column].fillna(method="ffill", inplace=True)
#             else:
#                 raise ValueError(
#                     "Unsupported strategy. Use 'mean', 'median', or 'ffill'."
#                 )
#     print(f"Null values handled using '{strategy}' strategy.")
#     return df_cleaned


# Function to generate general summary statistics
def general_summary_statistics(df):
    summary = df.describe()
    print("General Summary Statistics:\n", summary)
    return summary


def plot_eda(df):
    """
    Perform EDA with different visualizations on Nepal climate dataset.
    """

    # 1. Line plot of average mean temperature over years
    plt.figure()
    sns.lineplot(x="year", y="avg_mean_temp", data=df, marker="o", color="tomato")
    plt.title("Average Mean Temperature Over Years")
    plt.xlabel("Year")
    plt.ylabel("Avg Mean Temp (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 2. Bar plot of annual rainfall over years
    plt.figure()
    sns.barplot(x="year", y="annual_rainfall", data=df, palette="Blues_d")
    plt.title("Annual Rainfall Over Years")
    plt.xticks(rotation=45)
    plt.xlabel("Year")
    plt.ylabel("Annual Rainfall (mm)")
    plt.tight_layout()
    plt.show()

    # 3. Scatter plot: population density vs avg_mean_temp
    plt.figure()
    sns.scatterplot(
        x="population_density",
        y="avg_mean_temp",
        data=df,
        hue="year",
        palette="coolwarm",
        legend=False,
    )
    plt.title("Population Density vs Avg Mean Temp")
    plt.xlabel("Population Density")
    plt.ylabel("Avg Mean Temp (°C)")
    plt.tight_layout()
    plt.show()

    # 4. Correlation heatmap
    plt.figure()
    corr = df.select_dtypes(include="number").corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="YlGnBu")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

    # 5. Line plot comparing min and max temperature over time
    plt.figure()
    sns.lineplot(x="year", y="avg_min_temp", data=df, label="Min Temp", marker="o")
    sns.lineplot(x="year", y="avg_max_temp", data=df, label="Max Temp", marker="o")
    plt.title("Min and Max Temperatures Over Years")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 6. Line plot: Relative humidity over years
    plt.figure()
    sns.lineplot(x="year", y="relative_humidity", data=df, marker="o", color="teal")
    plt.title("Relative Humidity Over Years")
    plt.xlabel("Year")
    plt.ylabel("Relative Humidity (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 7. Scatter: Fertilizer usage vs Cropland percentage
    plt.figure()
    sns.scatterplot(
        x="fertilizer_kg_per_ha",
        y="cropland_pct",
        data=df,
        hue="year",
        palette="viridis",
        s=80,
    )
    plt.title("Fertilizer Use vs Cropland Percentage")
    plt.xlabel("Fertilizer (kg/ha)")
    plt.ylabel("Cropland Area (%)")
    plt.tight_layout()
    plt.show()

    # 8. Line plot: Agricultural land area over years
    plt.figure()
    sns.lineplot(x="year", y="agri_land_area", data=df, marker="o", color="brown")
    plt.title("Agricultural Land Area Over Years")
    plt.xlabel("Year")
    plt.ylabel("Agri Land Area (sq km)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 9. Population growth trend
    plt.figure()
    sns.lineplot(x="year", y="population_density", data=df, marker="o", color="purple")
    plt.title("Population Density Growth Over Years")
    plt.xlabel("Year")
    plt.ylabel("People per sq km")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 10. Pairplot of climate and agriculture features
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
    plt.suptitle("Pairwise Relationships Between Climate & Agri Features", y=1.02)
    plt.tight_layout()
    plt.show()
