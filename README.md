**Diabetes Risk Predictor**

- Helps identify patients who could potentially be at risk of having diabetes using logistic regression, cost optimization, and interpretable model explanations.

- This project predicts a patient's risk of diabetes by analyzing early health indicators such as glucose, insulin, BMI, and age. It uses logistic regression to classify risk levels and identify which features contribute most to each prediction.
- The system tunes decision thresholds to minimize hospital costs, prioritizes reducing false negatives, and generates accessible tables for doctors to review.
- It also includes visual tools like cost graphs and SHAP plots to explain how predictions are made.
- The final output supports hospital decision-making by flagging high-risk patients and clearly showing which clinical factors had the most impact.

**Features:**

- Uses logistic regression on clinical features like glucose, insulin, BMI, and age.
- Includes cost aware threshold tuning to help reduce false negatives.
- Explains predictions using both model coefficients and SHAP values.
- Visualizes cost vs threshold tradeoffs using line graphs.
- Outputs a report showing which patients were flagged and why.

  **Streamlit:**
- You can view this project through a live streamlit web app:
- https://natiqg13-diabetes-risk-predictor-app-qj0zgo.streamlit.app/
- You can also upload your own CSV of patient data.
- The web app allows you to adjust alert thresholds, view risk scores, top contributing features, SHAP predictions, and cost tradeoffs.
- It also allows you to download the CSV file that's currently in use.
  

**How to run the project:**

- Clone the repository.
- Go to the project folder.
- Create and activate a virtual environment (python -m venv venv) (.\venv\Scripts\activate)
- Install dependencies (pip install -r requirements.txt)
- Run the project in main. (python main.py)
- After running, you'll see visual plots (SHAP, cost curves), summary of threshold predictions, model coefficients, and a CSV report showing patient alerts.

  **Project Outputs:**
  - Cost Curve Plot: Line graphs showing hospital costs at different thresholds.
  - SHAP Summary Plot: Helps highlight which clinical features will have the greatest impact on model predictions overall.
  - Shap Waterfall Plot: Helps break down why one specific patient was flagged.
  - Model Coefficient Features: Shows the influence of each feature within the logistic regression model.
  - CSV: Flags high risk patients and explains why they were flagged.


![Figure_1](https://github.com/user-attachments/assets/836b7cea-da7f-4eee-a86a-3544c5bb0c30)
![Figure_2](https://github.com/user-attachments/assets/dca81b47-026b-4b0f-be78-8da9adb74058)
![Figure_3](https://github.com/user-attachments/assets/b8519d3c-eac0-410a-b8da-4533da29c28b)
![Figure_4](https://github.com/user-attachments/assets/2e0f492d-fa32-46a7-b332-a3550b7be351)
![Figure_5](https://github.com/user-attachments/assets/40886235-fec2-4ed2-925e-12d0fc3ef3a0)
![Figure_6](https://github.com/user-attachments/assets/9deda789-4162-47fe-b8d9-f371b1881acb)
![Figure_7](https://github.com/user-attachments/assets/e2a6ec83-e653-42f5-a6e9-a7168903df73)
![THCvDAT](https://github.com/user-attachments/assets/46eda958-017c-49e3-a04d-a5f02f8f4ff6)
![Shap1](https://github.com/user-attachments/assets/fa533706-e07b-4068-8749-6bf80101f5f0)
![Shap2](https://github.com/user-attachments/assets/225b4a22-471c-40be-bc20-b5ef712e48bd)


