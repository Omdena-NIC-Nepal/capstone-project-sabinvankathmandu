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




df = load_climate_data()
# check_null_values(df)
# df_cleaned = handle_null_values(df, strategy='mean')
# general_summary_statistics(df_cleaned)


