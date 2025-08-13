from flask import Flask, request, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.model.predict import load_model, make_prediction
from src.monitoring.logger import setup_logger

app = Flask(__name__)
logger = setup_logger()

model_path = 'models/house_price_model.pkl'
model = load_model(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    logger.info("Received data for prediction: %s", data)
    
    try:
        prediction = make_prediction(model, data)
        logger.info("Prediction made: %s", prediction)
        return jsonify({'prediction': prediction}), 200
    except Exception as e:
        logger.error("Error during prediction: %s", str(e))
        return jsonify({'error': 'Prediction failed'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)