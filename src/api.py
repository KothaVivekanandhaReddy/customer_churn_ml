from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from src.predict import ChurnPredictor
from src.preprocess import (
    load_data,
    clean_data,
    handle_missing_values
)

app = FastAPI()

predictor = ChurnPredictor(
    "models/rf_top10_features.pkl"
)

class Customer(BaseModel):

    customer_satisfaction: float
    num_service_calls: int
    num_complaints: float
    monthlycharges: float
    totalcharges: float
    days_since_signup: int
    annual_income: float
    credit_score: float
    days_since_last_interaction: int

    contract: str

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API Running"
    }

@app.post("/predict")
def predict(customer: Customer):

    customer_df = pd.DataFrame(
        [customer.dict()]
    )

    result = predictor.predict(
        customer_df
    )

    return result

