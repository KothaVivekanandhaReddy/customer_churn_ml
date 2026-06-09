import pandas as pd


def load_data(file_path):
    return pd.read_csv(file_path)


def clean_data(df):

    df = df.copy()

    if "customer_id" in df.columns:
        df.drop(columns=["customer_id"], inplace=True)

    df["signup_date"] = pd.to_datetime(df["signup_date"])

    df["days_since_signup"] = (
        pd.Timestamp.now() - df["signup_date"]
    ).dt.days

    df.drop(columns=["signup_date"], inplace=True)

    return df


def handle_missing_values(df):

    df = df.copy()

    df["annual_income"] = df["annual_income"].fillna(
        df["annual_income"].median()
    )

    df["credit_score"] = df["credit_score"].fillna(
        df["credit_score"].median()
    )

    df["customer_satisfaction"] = df["customer_satisfaction"].fillna(
        df["customer_satisfaction"].median()
    )

    df["avg_monthly_gb"] = df["avg_monthly_gb"].fillna(
        df["avg_monthly_gb"].median()
    )

    df["num_complaints"] = df["num_complaints"].fillna(
        df["num_complaints"].median()
    )

    return df