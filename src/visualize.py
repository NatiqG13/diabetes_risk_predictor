import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import shap

from src.evaluate import evaluate_model
from src.evaluate import compute_cost_curve
from src.interpret import get_model_coefficients
from src.interpret import run_shap

def plot_cost_curve(threshold, total_cost, FN, FP):
    df = pd.DataFrame({"Threshold" : threshold, "Total cost": total_cost})
    df.plot(x="Threshold",y="Total cost")
    plt.title("Total Hospital Cost vs. Diabetes Alert Threshold")
    plt.xlabel("Threshold")
    plt.ylabel("Total Cost")

    plt.show()
    plt.close()


    best_index = np.argmin(total_cost)


    best_threshold = threshold[best_index]
    best_FN = FN[best_index]
    best_FP = FP[best_index]
    best_total_cost = total_cost[best_index]

    print(f"Lowest cost {best_total_cost} occurs at threshold {best_threshold} with {best_FP} FPs and {best_FN}  FNs")

    return best_threshold

def plot_shap(logreg, X_test):
    explainer, shap_values, X_test = run_shap(logreg, X_test)

    shap.summary_plot(shap_values, X_test)  

    shap.plots.waterfall(shap.Explanation(values=shap_values[0], base_values=explainer.expected_value, data=X_test.iloc[0], feature_names=X_test.columns))  

    plt.close()

def print_business_summary(thresholds, total_cost, FP, FN):
    best_index = np.argmin(total_cost)
    best_threshold = thresholds[best_index]
    best_fp = FP[best_index]
    best_fn = FN[best_index]
    best_cost = total_cost[best_index]

    print("\nBusiness Recommendation Summary:")
    print(f" Recommended threshold: {best_threshold}")
    print(f" Expected cost at the chosen threshold: ${best_cost}")
    print(f" False Positives: {best_fp} → may lead to unnecessary alerts")
    print(f" False Negatives: {best_fn} → missed diabetes cases or delayed intervention")



    