import pandas as pd
import matplotlib.pyplot as plt

from src.data_loader import load_data, clean_data
from src.eda import plot_feature_kde
from src.feature_engineering import engineer_features
from src.train import train_model
from src.evaluate import evaluate_model, compute_cost_curve
from src.visualize import plot_cost_curve, plot_shap, print_business_summary
from src.interpret import get_model_coefficients, build_alert_table, run_shap

path = 'data/raw.csv'

df = load_data(path)
df = clean_data(df)
df = engineer_features(df)
logreg, X_test, y_test = train_model(df)
plot_feature_kde(df)
thresholds, precisions, recalls, FN, FP = evaluate_model(logreg, X_test, y_test)
total_cost = compute_cost_curve(y_test, logreg.predict_proba(X_test)[:,1], thresholds, 1000, 100, FN, FP)
best_threshold = plot_cost_curve(thresholds, total_cost, FN, FP)
coef_df = get_model_coefficients(logreg, X_test)
print(coef_df)
plot_shap(logreg, X_test)
print_business_summary(thresholds, total_cost, FP, FN)


explainer, shap_values, _ = run_shap(logreg, X_test)
alert_df = build_alert_table(logreg, X_test, best_threshold, shap_values)
print(alert_df.head()) 
alert_df.to_csv("outputs/doctor_alert_report.csv", index=False)









