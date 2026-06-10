import os
import joblib
import boto3


class ChurnPredictor:

    def __init__(self, model_path):

        if not os.path.exists(model_path):

            os.makedirs("models", exist_ok=True)

            s3 = boto3.client(
                "s3",
                aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                region_name=os.getenv("AWS_REGION")
            )

            s3.download_file(
                "customer-churn-ml-26",
                "rf_top10_features.pkl",
                model_path
            )

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