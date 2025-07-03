import pandas as pd
from sklearn.metrics import confusion_matrix
import numpy as np



def evaluate_model(model, X_test,y_test):
    '''
    Evaluates precision and recall at thresholds from 0.1 to 0.9 and returns error counts.
    '''

    probs = model.predict_proba(X_test)[:,1]

    threshold = np.arange(0.1, 1.0, 0.1)
    precision_scores = []
    recall_scores = []
    TN = []
    FP = []
    FN = []
    TP = []


    for t in threshold:
        y_pred = probs >= t
        cm= confusion_matrix(y_test,y_pred)
        TN.append(cm[0,0])
        FP.append(cm[0,1])
        FN.append(cm[1,0])
        TP.append(cm[1,1])
        precision_scores.append(TP[-1] / (TP[-1] + FP[-1]))
        recall_scores.append(TP[-1] / (TP[-1] + FN[-1]))


    return threshold, precision_scores, recall_scores, FN, FP

def compute_cost_curve(y_true, y_probs, threshold, cost_fn, cost_fp,FN,FP):
    '''
    Computes total cost at each threshold based on FN and FP counts and their respective costs.
    '''

    
    total_costs = []

    for i in range(len(threshold)):
        total_costs.append((FN[i]*cost_fn) + (FP[i]*cost_fp))

    return total_costs




   