from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="House Price Prediction API")

# Load trained model
model = joblib.load("model/house_price_model.pkl")

# Input schema (California housing features)
class HouseInput(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def home():
    return {"message": "House Price Prediction API is running successfully!"}

@app.post("/predict")
def predict_price(data: HouseInput):

    input_data = np.array([[ 
        data.MedInc,
        data.HouseAge,
        data.AveRooms,
        data.AveBedrms,
        data.Population,
        data.AveOccup,
        data.Latitude,
        data.Longitude
    ]])

    prediction = model.predict(input_data)

    return {"predicted_house_price": float(prediction[0])}
