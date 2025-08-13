# House Price Prediction API

This project is a simple REST API for predicting house prices using a regression model. It is designed for beginners to understand the basics of model deployment and MLOps.

## Project Structure

```
house-price-api
├── src
│   ├── api
│   │   └── main.py          # Entry point for the REST API
│   ├── model
│   │   ├── train.py         # Logic for training the regression model
│   │   └── predict.py       # Functions for making predictions
│   ├── monitoring
│   │   └── logger.py        # Logging setup for monitoring
│   └── utils
│       └── data_loader.py   # Utility functions for data loading and preprocessing
├── requirements.txt          # Project dependencies
├── Dockerfile                 # Docker configuration for the application
├── cloud_deploy
│   └── deploy.yaml           # Cloud deployment configuration
├── README.md                 # Project documentation
└── .gitignore                # Files to ignore in Git
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd house-price-api
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Train the model:**
   Run the training script to train the regression model and save it.
   ```
   python src/model/train.py
   ```

4. **Run the API:**
   Start the Flask application.
   ```
   python src/api/main.py
   ```

5. **Access the API:**
   The API will be available at `http://localhost:5000/predict`. You can send POST requests with the required input data to get predictions.

## Usage Example

To get predictions, send a POST request to the `/predict` endpoint with the following JSON body:

```json
{
  "feature1": value1,
  "feature2": value2,
  ...
}
```
In PowerShell: (example POST request)
```
Invoke-WebRequest -Uri http://localhost:5000/predict -Method POST -Headers @{"Content-Type" = "application/json"} -Body '{"size": 1400, "bedrooms": 3}'
```
## Monitoring and Logging

The application includes basic logging functionality to monitor API usage and model performance. Logs can be found in the specified log file.

## Deployment

The project can be deployed to a cloud platform using the provided `deploy.yaml` configuration file. Follow the instructions in that file to set up the necessary resources.

## Steps to Deploy

1. Push Your Code to GitHub
Create a new GitHub repository.
Push your project code to it.

2. Deploy on Render
Go to https://render.com and sign up/log in.
Click "New +" → "Web Service".
Connect your GitHub repo.
For Environment, choose Docker.
Set the Port to 5000.
Click Create Web Service.
Render will build your Docker image and deploy your app.
You’ll get a public URL like https://your-app.onrender.com.

3. Test Your API
Once deployed, send a POST request to https://your-app.onrender.com/predict as you did locally.

4. Monitoring and Logs
Render provides logs in the dashboard for free.
For advanced monitoring, you can integrate third-party services, but for most beginners, Render’s built-in logs are enough.

Example post request in PowerShell:

```
Invoke-WebRequest -Uri https://house-price-api-rfod.onrender.com/predict -Method POST -Headers @{"Content-Type" = "application/json"} -Body '{"size": 1400, "bedrooms": 3}'
```

## License

This project is open-source and available under the MIT License.