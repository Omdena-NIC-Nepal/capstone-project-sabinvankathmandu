from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import pickle

# Prepare features for model training
def prepare_features(df):
    """
    Prepares X and y for model training
    """
    target = 'avg_mean_temp'
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
        raise ValueError("Choose: 'Gradient Boosting', 'Ridge', 'Lasso', or 'Random Forest'")

    model.fit(X_train, y_train)
    return model
