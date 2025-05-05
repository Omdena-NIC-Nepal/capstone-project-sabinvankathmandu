from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import pickle
import numpy as np


# Prepare features for model training
def prepare_features(df):
    """
    Prepares X and y for model training
    """
    target = "avg_mean_temp"
    features = df.drop(columns=[target])
    X = features.select_dtypes(include=[np.number])
    y = df[target]
    return X, y


# Split Data
def split_data(X, y, test_size=0.2):
    """
    Split datas into train/test sets
    """
    return train_test_split(X, y, test_size=test_size, random_state=42)


# Train Model
def train_model(X_train, y_train, model_type="Ridge"):
    """
    Train a regression model
    """
    if model_type == "Gradient Boosting":
        model = GradientBoostingRegressor(random_state=42)
    elif model_type == "Ridge":
        model = Ridge(alpha=1.0)
    elif model_type == "Lasso":
        model = Lasso(alpha=0.1)
    elif model_type == "Random Forest":
        model = RandomForestRegressor(random_state=42)
    else:
        raise ValueError(
            "Choose: 'Gradient Boosting', 'Ridge', 'Lasso', or 'Random Forest'"
        )

    model.fit(X_train, y_train)
    return model


# Evaluate Model
def evaluate_model(model, X_train, y_train, X_test, y_test):
    """
    Evaluate performance
    """
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    metrics = {
        "train_rmse": np.sqrt(mean_squared_error(y_train, y_pred_train)),
        "test_rmse": np.sqrt(mean_squared_error(y_test, y_pred_test)),
        "train_r2": r2_score(y_train, y_pred_train),
        "test_r2": r2_score(y_test, y_pred_test),
        "train_mae": mean_absolute_error(y_train, y_pred_train),
        "test_mae": mean_absolute_error(y_test, y_pred_test),
        "y_test": y_test,
        "y_pred_test": y_pred_test,
    }
    return metrics


# Save Model
def save_model(model, file_name='../model/climate_model.pkl'):
    with open(file_name, 'wb') as file:
        pickle.dump(model, file)

# Load Model
def load_model(file_name='../model/climate_model.pkl'):
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None
