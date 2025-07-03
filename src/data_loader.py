import pandas as pd


def load_data(path):
    '''
    Loads a CSV from the given path and returns a DataFrame.
    '''
    df = pd.read_csv(path)
    return df

def clean_data(df):
    '''
    Used to clean the values by replacing the 0s with the median.
    '''
    median_glucose = df['Glucose'][df['Glucose'] != 0].median()
    median_bloodPressure = df['BloodPressure'][df['BloodPressure'] != 0].median()
    median_skinThickness = df['SkinThickness'][df['SkinThickness'] != 0].median()
    median_insulin = df['Insulin'][df['Insulin'] != 0].median()
    median_bmi = df['BMI'][df['BMI'] != 0].median()
    median_diabetesPedigreeFunction = df['DiabetesPedigreeFunction'][df['DiabetesPedigreeFunction'] != 0].median()
    median_age = df['Age'][df['Age'] != 0].median()

    df['Glucose'] = df['Glucose'].replace(0,median_glucose)
    df['BloodPressure'] = df['BloodPressure'].replace(0,median_bloodPressure)
    df['SkinThickness'] = df['SkinThickness'].replace(0,median_skinThickness)
    df['Insulin'] = df['Insulin'].replace(0,median_insulin)
    df['BMI'] = df['BMI'].replace(0,median_bmi)
    df['DiabetesPedigreeFunction'] = df['DiabetesPedigreeFunction'].replace(0,median_diabetesPedigreeFunction)
    df['Age'] = df['Age'].replace(0,median_age)

    return df