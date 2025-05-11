import numpy as np
import pandas as pd

def make_prediction(model, year, avg_min_temp, avg_max_temp, relative_humidity,
                    precipitation_max, annual_rainfall, agri_land_area, cropland_pct,
                    fertilizer_kg_per_ha, population_density):
    """
    Predict the average mean temperature using the trained model and input features.
    """
    features = np.array([[year, avg_min_temp, avg_max_temp, relative_humidity,
                          precipitation_max, annual_rainfall, agri_land_area,
                          cropland_pct, fertilizer_kg_per_ha, population_density]])
    return model.predict(features)[0]


def get_historical_values(df, column_name):
    """
    Return historical year-wise values for a specified column.
    """
    return df[['year', column_name]].dropna().sort_values(by='year')


def get_historical_average(df, column_name):
    """
    Return the mean of a specific feature across all years.
    """
    return df[column_name].mean()

