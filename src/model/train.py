import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os
 
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Assuming the target variable is 'price' and features are all other columns
    X = data.drop('price', axis=1)
    y = data['price']
    return X, y

def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

def save_model(model, model_path):
    joblib.dump(model, model_path)

def main():
    base_path = 'C:\\Users\\sweta\\Documents\\Python_Scripts\\house-price-api\\house-price-api'
    data_file_path = os.path.join(base_path, 'data', 'house_prices.csv')  # Adjust path as necessary
    model_save_path = os.path.join(base_path, 'models', 'house_price_model.pkl')  # Adjust path as necessary

    data = load_data(data_file_path)
    X, y = preprocess_data(data)
    model = train_model(X, y)
    save_model(model, model_save_path)

if __name__ == "__main__":
    main()