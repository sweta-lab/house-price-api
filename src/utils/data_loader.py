def load_data(file_path):
    import pandas as pd
    
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Example preprocessing steps
    data = data.dropna()  # Remove missing values
    data = pd.get_dummies(data)  # Convert categorical variables to dummy variables
    return data

def load_and_preprocess_data(file_path):
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    return processed_data