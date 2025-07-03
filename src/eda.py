import pandas as pd
import matplotlib.pyplot as plt


def plot_feature_kde(df):
    '''
    Plots kde curves for specific clinical features, separated by diabetes outcome (Diabetic = 1, Non diabetic = 0).
    '''
  
    
    Glucose_Outcome1 = df['Glucose'][df['Outcome'] == 1]
    Glucose_Outcome0 = df['Glucose'][df['Outcome'] == 0]

    BloodPressure_Outcome1 = df['BloodPressure'][df['Outcome'] == 1]
    BloodPressure_Outcome0 = df['BloodPressure'][df['Outcome'] == 0]

    SkinThickness_Outcome1 = df['SkinThickness'][df['Outcome'] == 1]
    SkinThickness_Outcome0 = df['SkinThickness'][df['Outcome'] == 0]

    Insulin_Outcome1 = df['Insulin'][df['Outcome'] == 1]
    Insulin_Outcome0 = df['Insulin'][df['Outcome'] == 0]

    BMI_Outcome1 = df['BMI'][df['Outcome'] == 1]
    BMI_Outcome0 = df['BMI'][df['Outcome'] == 0]

    DiabetesPedigreeFunction_Outcome1 = df['DiabetesPedigreeFunction'][df['Outcome'] == 1]
    DiabetesPedigreeFunction_Outcome0 = df['DiabetesPedigreeFunction'][df['Outcome'] == 0]

    Age_Outcome1 = df['Age'][df['Outcome'] == 1]
    Age_Outcome0 = df['Age'][df['Outcome'] == 0]


    Glucose_Outcome = pd.DataFrame({'Glucose Outcome 0': Glucose_Outcome0, 'Glucose Outcome 1': Glucose_Outcome1})
    BloodPressure_Outcome = pd.DataFrame({'Blood Pressure Outcome 0': BloodPressure_Outcome0, 'Blood Pressure Outcome 1': BloodPressure_Outcome1})
    SkinThickness_Outcome = pd.DataFrame({'Skin Thickness Outcome 0': SkinThickness_Outcome0, 'Skin Thickness Outcome 1': SkinThickness_Outcome1})
    Insulin_Outcome = pd.DataFrame({'Insulin Outcome 0': Insulin_Outcome0, 'Insulin Outcome 1': Insulin_Outcome1})
    BMI_Outcome = pd.DataFrame({'BMI Outcome 0': BMI_Outcome0, 'BMI Outcome 1': BMI_Outcome1})
    DiabetesPedigreeFunction_Outcome = pd.DataFrame({'Diabetes Pedigree Function Outcome 0': DiabetesPedigreeFunction_Outcome0, 'Diabetes Pedigree Function Outcome 1': DiabetesPedigreeFunction_Outcome1})
    Age_Outcome = pd.DataFrame({'Age Outcome 0': Age_Outcome0, 'Age Outcome 1': Age_Outcome1})

    GlucosePlot = Glucose_Outcome.plot.kde()
    GlucosePlot.set_title("Glucose KDE")
    GlucosePlot.set_xlabel("Glucose")
    GlucosePlot.set_ylabel("Density")

    BloodPressurePlot = BloodPressure_Outcome.plot.kde()
    BloodPressurePlot.set_title("Blood Pressure KDE")
    BloodPressurePlot.set_xlabel("Blood Pressure")
    BloodPressurePlot.set_ylabel("Density")

    SkinThicknessPlot = SkinThickness_Outcome.plot.kde()
    SkinThicknessPlot.set_title("Skin Thickness KDE")
    SkinThicknessPlot.set_xlabel("Skin Thickness")
    SkinThicknessPlot.set_ylabel("Density")

    InsulinPlot = Insulin_Outcome.plot.kde()
    InsulinPlot.set_title("Insulin KDE")
    InsulinPlot.set_xlabel("Insulin")
    InsulinPlot.set_ylabel("Density")

    BMIPlot = BMI_Outcome.plot.kde()
    BMIPlot.set_title("BMI KDE")
    BMIPlot.set_xlabel("BMI")
    BMIPlot.set_ylabel("Density")

    DiabetesPedigreeFunctionPlot = DiabetesPedigreeFunction_Outcome.plot.kde()
    DiabetesPedigreeFunctionPlot.set_title("Diabetes Pedigree Function KDE")
    DiabetesPedigreeFunctionPlot.set_xlabel("Diabetes Pedigree Function")
    DiabetesPedigreeFunctionPlot.set_ylabel("Density")

    AgePlot = Age_Outcome.plot.kde()
    AgePlot.set_title("Age KDE")
    AgePlot.set_xlabel("Age")
    AgePlot.set_ylabel("Density")

    plt.show()