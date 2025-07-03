import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def engineer_features(df):
    """
    Add or modify features in the dataset.
    Returns a new DataFrame with engineered features.
    """
    df['BMI_Age_Interaction'] = df['BMI'] * df['Age']
    features = df.drop(columns=["Outcome"])
    target = df["Outcome"]

    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    df_scaled = pd.DataFrame(features_scaled, columns=features.columns)
    df_scaled["Outcome"] = target.values



    return df_scaled
