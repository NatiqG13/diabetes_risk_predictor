import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.data_loader import clean_data
from src.feature_engineering import engineer_features
from src.train import train_model
from src.interpret import run_shap, build_alert_table

st.set_page_config(page_title="Diabetes Risk Predictor", layout="centered")


st.title("Diabetes Risk Predictor")
st.markdown("This app flags patients at risk of diabetes based on early clinical data.")


st.sidebar.header("Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])


threshold = st.sidebar.slider("Alert Threshold", 0.1, 0.9, 0.1, 0.1)


if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    st.sidebar.markdown("Or use default sample data.")
    data = pd.read_csv("data/raw.csv")



df = clean_data(data)
df = engineer_features(df)
logreg, X_test, y_test = train_model(df)
explainer, shap_values, _ = run_shap(logreg, X_test)
alerts_df = build_alert_table(logreg, X_test, threshold, shap_values)


st.subheader(" Patient Risk Alerts")
st.dataframe(alerts_df.head(10))


st.subheader(" Global Feature Importance")
st.image("outputs/Shap1.png", use_container_width=True)

st.subheader(" Single Prediction Breakdown")
st.image("outputs/Shap2.png", use_container_width=True)

st.subheader(" Hospital Cost Curve")
st.image("outputs/THCvDAT.png", use_container_width=True)


st.subheader(" Download Full Alert Report")
csv = alerts_df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, "alert_report.csv", "text/csv")
