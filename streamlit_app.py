import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.title("🛍️ AI Customer Segmentation App")

st.write("Enter customer RFM values to predict segment.")

# Input fields
recency = st.number_input("Recency (days since last purchase)", min_value=0)
frequency = st.number_input("Frequency (number of purchases)", min_value=0)
monetary = st.number_input("Monetary (total spend)", min_value=0.0)

if st.button("Predict Segment"):

    features = np.array([[recency, frequency, monetary]])
    scaled = scaler.transform(features)
    cluster = model.predict(scaled)

    segment = int(cluster[0])

    st.success(f"Customer belongs to Cluster {segment}")

    # Optional interpretation
    if segment == 0:
        st.write("🛒 Regular Buyer ⭐")
    elif segment == 1:
        st.write("💰 Price Sensitive 💰")
    elif segment == 2:
        st.write("⚠ At Risk Customer ⚠")
    else:
        st.write("💎 High Value Loyalist 💎")