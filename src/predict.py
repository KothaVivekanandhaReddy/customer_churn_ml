import joblib


class ChurnPredictor:

    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, customer_df):

        probability = self.model.predict_proba(
            customer_df
        )[0][1]

        prediction = self.model.predict(
            customer_df
        )[0]

        return {
            "prediction": int(prediction),
            "churn_probability": round(
                float(probability),
                4
            )
        }
    
