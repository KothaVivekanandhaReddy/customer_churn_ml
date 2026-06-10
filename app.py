import streamlit as st
import requests

API_URL = "https://customer-churn-ml-qae4.onrender.com/predict"

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊"
)

st.title("📊 Customer Churn Prediction Dashboard")

st.write(
    "Enter customer details and predict churn probability."
)

customer_satisfaction = st.slider(
    "Customer Satisfaction",
    1,
    10,
    5
)

num_service_calls = st.number_input(
    "Number of Service Calls",
    min_value=0,
    value=1
)

num_complaints = st.number_input(
    "Number of Complaints",
    min_value=0,
    value=0
)

monthlycharges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=50.0
)

totalcharges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

days_since_signup = st.number_input(
    "Days Since Signup",
    min_value=0,
    value=365
)

annual_income = st.number_input(
    "Annual Income",
    min_value=0.0,
    value=50000.0
)

credit_score = st.number_input(
    "Credit Score",
    min_value=300.0,
    max_value=850.0,
    value=650.0
)

days_since_last_interaction = st.number_input(
    "Days Since Last Interaction",
    min_value=0,
    value=30
)

contract = st.selectbox(
    "Contract Type",
    [
        "month_to_month",
        "one_year",
        "two_year"
    ]
)

if st.button("Predict Churn"):

    payload = {
        "customer_satisfaction": customer_satisfaction,
        "num_service_calls": num_service_calls,
        "num_complaints": num_complaints,
        "monthlycharges": monthlycharges,
        "totalcharges": totalcharges,
        "days_since_signup": days_since_signup,
        "annual_income": annual_income,
        "credit_score": credit_score,
        "days_since_last_interaction": days_since_last_interaction,
        "contract": contract
    }

    response = requests.post(
        API_URL,
        json=payload
    )

    result = response.json()

    st.success("Prediction Complete")

    st.metric(
        "Churn Probability",
        result["churn_probability"]
    )

    st.metric(
        "Prediction",
        result["prediction"]
    )