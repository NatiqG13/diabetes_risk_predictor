import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from src.model import get_logistic_model
from src.data_loader import load_data, clean_data
from src.feature_engineering import engineer_features

def train_model(df):
    '''
    Creates train/test/splits and drops outcome from x value and initializes outcome into the y values.
    '''
    logreg = get_logistic_model()

    X = df.drop(columns=["Outcome"])
    y = df["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)

    logreg.fit(X_train,y_train)

    return logreg, X_test, y_test

