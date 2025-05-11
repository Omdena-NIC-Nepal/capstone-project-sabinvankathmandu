import pandas as pd
import streamlit as st


@st.cache_data
def load_climate_data(file_path="data/yearly_climate_nepal.csv"):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"File not found at {file_path}. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def prepare_features(df, target='avg_mean_temp'):
    # Define features to use (excluding target and obviously correlated columns)
    features = [
        'year',
        'avg_min_temp', 'avg_max_temp', 'relative_humidity',
        'precipitation_max', 'annual_rainfall',
        'agri_land_area', 'cropland_pct', 'fertilizer_kg_per_ha',
        'population_density'
    ]

    # Drop target from feature list if present
    if target in features:
        features.remove(target)

    X = df[features]
    y = df[target]

    return X, y

# df = load_climate_data()
# check_null_values(df)
# df_cleaned = handle_null_values(df, strategy='mean')
# general_summary_statistics(df_cleaned)


