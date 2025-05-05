import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a global style
sns.set_theme(style="whitegrid")

# 1. Temperature Trends
def plot_temperature_trends(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['year'], df['avg_mean_temp'], label='Avg Mean Temp', marker='o')
    plt.plot(df['year'], df['avg_min_temp'], label='Avg Min Temp', marker='x')
    plt.plot(df['year'], df['avg_max_temp'], label='Avg Max Temp', marker='s')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.title('Yearly Temperature Trends in Nepal')
    plt.legend()
    plt.tight_layout()
    plt.show()

# 2. Relative Humidity
def plot_relative_humidity(df):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='year', y='relative_humidity', marker='o', color='teal')
    plt.title('Yearly Relative Humidity in Nepal')
    plt.ylabel('Relative Humidity (%)')
    plt.xlabel('Year')
    plt.tight_layout()
    plt.show()

# 3. Precipitation and Rainfall
def plot_precipitation_rainfall(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['year'], df['precipitation_max'], label='Max Precipitation', marker='D')
    plt.plot(df['year'], df['annual_rainfall'], label='Annual Rainfall', marker='^')
    plt.xlabel('Year')
    plt.ylabel('Precipitation (mm)')
    plt.title('Yearly Precipitation and Rainfall in Nepal')
    plt.legend()
    plt.tight_layout()
    plt.show()

# 4. Agricultural Land Area
def plot_agriculture_land(df):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='year', y='agri_land_area', marker='s', color='green')
    plt.title('Agricultural Land Area Over Years in Nepal')
    plt.ylabel('Agri Land Area')
    plt.xlabel('Year')
    plt.tight_layout()
    plt.show()

# 5. Fertilizer Use
def plot_fertilizer_usage(df):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='year', y='fertilizer_kg_per_ha', marker='^', color='orange')
    plt.title('Fertilizer Usage Over Years in Nepal')
    plt.ylabel('Fertilizer (kg/ha)')
    plt.xlabel('Year')
    plt.tight_layout()
    plt.show()

# 6. Population Density
def plot_population_density(df):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='year', y='population_density', marker='o', color='purple')
    plt.title('Population Density Growth in Nepal')
    plt.ylabel('People per sq.km')
    plt.xlabel('Year')
    plt.tight_layout()
    plt.show()

# 7. Correlation Heatmap
def plot_correlation_heatmap(df):
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Heatmap of Climate Indicators')
    plt.tight_layout()
    plt.show()
