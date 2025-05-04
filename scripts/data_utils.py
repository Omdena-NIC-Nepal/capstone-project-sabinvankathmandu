import pandas as pd

def load_climate_data(file_path = "data/yearly_climate_nepal.csv"):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"File not found at {file_path}. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to check null values
def check_null_values(df):
    null_counts = df.isnull().sum()
    print("Null values in each column:\n", null_counts)
    return null_counts

# Function to handle null values using a given strategy
def handle_null_values(df, strategy='mean'):
    df_cleaned = df.copy()
    for column in df_cleaned.select_dtypes(include=['float64', 'int64']).columns:
        if df_cleaned[column].isnull().sum() > 0:
            if strategy == 'mean':
                df_cleaned[column].fillna(df_cleaned[column].mean(), inplace=True)
            elif strategy == 'median':
                df_cleaned[column].fillna(df_cleaned[column].median(), inplace=True)
            elif strategy == 'ffill':
                df_cleaned[column].fillna(method='ffill', inplace=True)
            else:
                raise ValueError("Unsupported strategy. Use 'mean', 'median', or 'ffill'.")
    print(f"Null values handled using '{strategy}' strategy.")
    return df_cleaned

# Function to generate general summary statistics
def general_summary_statistics(df):
    summary = df.describe()
    print("General Summary Statistics:\n", summary)
    return summary


# df = load_climate_data()
# check_null_values(df)
# df_cleaned = handle_null_values(df, strategy='mean')
# general_summary_statistics(df_cleaned)
