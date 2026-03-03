# 🛍️ AI-Powered Customer Segmentation

## 📌 Project Overview

This project builds an end-to-end AI-based customer segmentation system using RFM analysis and K-Means clustering.  
It segments retail customers into meaningful business groups to enable targeted marketing and improved revenue optimization.

---

## 🎯 Business Objective

Retail businesses often treat all customers the same, leading to inefficient marketing strategies and low ROI.

This project helps:
- Identify high-value loyal customers
- Detect at-risk customers
- Segment price-sensitive buyers
- Improve campaign targeting

---

## 🧠 Methodology

### 1️⃣ Data Cleaning
- Removed missing Customer IDs
- Removed negative quantities (returns)
- Removed invalid prices

### 2️⃣ Feature Engineering (RFM Model)
- **Recency** → Days since last purchase
- **Frequency** → Number of purchases
- **Monetary** → Total customer spend

### 3️⃣ Feature Scaling
Used StandardScaler to normalize feature ranges.

### 4️⃣ Clustering
Applied K-Means clustering to segment customers.

### 5️⃣ Model Evaluation
- Used Elbow Method to determine optimal clusters
- Silhouette Score: **0.61** (Good clustering)

### 6️⃣ Dimensionality Reduction
Used PCA for visualization and faster computation.

---

## 📊 Results

Identified 4 customer segments:

- 💎 High Value Loyalists
- 🛒 Regular Buyers
- 💰 Price Sensitive Customers
- ⚠ At Risk Customers

---

## 📊 Power BI Dashboard

The Power BI dashboard file is included in the `dashboards/` folder.

It visualizes:
- Revenue contribution by segment
- Customer distribution
- VIP revenue percentage
- Behavioral cluster insights

---

## 🌐 Streamlit Deployment

A real-time prediction app was built using Streamlit.

Users can input:
- Recency
- Frequency
- Monetary

And get instant customer segment prediction.

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- PCA
- Power BI
- Streamlit
- GitHub

---

## 📂 Project Structure
