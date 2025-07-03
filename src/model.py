from sklearn.linear_model import LogisticRegression

def get_logistic_model():
    """
    Returns a logistic regression model instance
    """
    logreg = LogisticRegression(random_state=16)
    return logreg
