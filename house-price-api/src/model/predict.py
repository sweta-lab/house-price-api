def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def make_prediction(model, input_data):
    import numpy as np
    # If input_data is a dict, use its values
    if isinstance(input_data, dict):
        input_array = np.array(list(input_data.values())).reshape(1, -1)
    else:
        input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0]

def get_prediction(model_path, input_data):
    model = load_model(model_path)
    price = make_prediction(model, input_data)
    return price