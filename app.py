import streamlit as st
import pickle
import numpy as np
import os

st.title("Kraljic Category Prediction App")
st.write("Enter Product Details:")

# ✅ Safe model loading (for Streamlit Cloud)
model_path = os.path.join(os.path.dirname(__file__), "Like.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

# Input fields
lead_time = st.number_input("Lead Time (Days)", min_value=0)
order_volume = st.number_input("Order Volume (Units)", min_value=0)
cost = st.number_input("Cost per Unit")
supply_risk = st.slider("Supply Risk Score", 1, 5)
profit_impact = st.slider("Profit Impact Score", 1, 5)
environmental_impact = st.slider("Environmental Impact", 1, 5)
single_source = st.selectbox("Single Source Risk", ["No", "Yes"])

# Encoding
single_source = 1 if single_source == "Yes" else 0

if st.button("Predict Category"):
    input_data = np.array([[lead_time, order_volume, cost,
                            supply_risk, profit_impact,
                            environmental_impact, single_source]])

    prediction = model.predict(input_data)
    st.success(f"Predicted Kraljic Category: {prediction[0]}")
