from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import pickle


def prepare_features(df):
    """
    Prepares X and y for model training
    """
    target = 'avg_mean_temp'
    features = df.drop(columns=[target])
    X = features.select_dtypes(include=[np.number])
    y = df[target]
    return X, y
