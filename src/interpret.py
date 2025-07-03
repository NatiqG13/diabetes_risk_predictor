import pandas as pd
import numpy as np
import shap

from src.model import get_logistic_model

def get_model_coefficients(logreg, X_test):

    coefficients = logreg.coef_
    coefficients = coefficients.flatten()

    names = zip(X_test.columns, coefficients)
    intercept = logreg.intercept_

    features = []
    coefficient = []
    abs_coefficients = []

    for name, coef in names:
        features.append(name)
        coefficient.append(coef)
        abs_coefficients.append(abs(coef))

    coef_df = pd.DataFrame({'Feature': features, 'Coefficient': coefficient, 'Absolute': abs_coefficients })
    coef_df.sort_values(by='Absolute', ascending=False, inplace=True)

    return coef_df

def run_shap(logreg, X_test):
    explainer = shap.LinearExplainer(logreg, X_test)
    shap_values = explainer.shap_values(X_test)
    return explainer, shap_values, X_test

def build_alert_table(model, X_test, threshold, shap_values, top_n=3):
    probs = model.predict_proba(X_test)[:, 1]
    alerts = probs >= threshold

    top_features = []
    for i in range(len(X_test)):
        shap_row = shap_values[i]
        top_indices = np.argsort(np.abs(shap_row))[-top_n:][::-1]
        top_feats = X_test.columns[top_indices].tolist()
        top_features.append(", ".join(top_feats))

    alert_df = pd.DataFrame({
        "PatientID": X_test.index,
        "Risk Score": probs.round(3),
        "Alert Triggered": alerts,
        "Top Features": top_features
    })

    return alert_df


       
















