# Credit Risk Prediction App

## Project Overview

This project is an end-to-end machine learning application designed to predict the credit risk of loan applicants. It's built to demonstrate the full lifecycle of a machine learning model, from data acquisition and training to deployment in an interactive web application.

The core goal is to provide a user-friendly tool for financial institutions to make data-driven decisions and mitigate the risk of loan defaults.

## Key Features

Credit Risk Prediction: The application predicts whether a loan applicant is a "good" or "bad" credit risk based on their financial and demographic information.

End-to-End ML Pipeline: The project includes a complete machine learning pipeline for data preprocessing, model training, and prediction.

Interactive Web App: A clean and responsive user interface built with Streamlit allows users to input applicant details and get real-time risk predictions.

Technology Stack

Python: The primary programming language for all components.

### Data & ML Libraries:

pandas: For data manipulation and analysis.

scikit-learn: For building the machine learning model and pipeline.

joblib: For saving and loading the trained model.

### Model:

Random Forest Classifier: A powerful, non-linear model chosen to handle the complex, imbalanced nature of the credit risk dataset.

### Web Framework:

Streamlit: Used to create and host the interactive web application.

### How to Run the App
Clone the Repository: Get the project files onto your local machine.

Install Dependencies: Run pip install pandas scikit-learn streamlit joblib in your terminal.

Train the Model: Run python credit_risk_trainer.py. This creates the credit_risk_pipeline.pkl file.

Run the App: Once the model is ready, run streamlit run app.py to launch the web application.

The app will open in your web browser. You can now use the interface to make predictions.

### The interface(Streamlit) 
<img width="931" height="760" alt="Screenshot 2025-09-08 120931" src="https://github.com/user-attachments/assets/af2f99d7-1ad8-4506-ab76-1d87b854d76c" />

### The prediction made by the model
<img width="896" height="381" alt="Screenshot 2025-09-08 122647" src="https://github.com/user-attachments/assets/32be1c74-a8a9-4ca8-9a22-7c6f47525a22" />


<img width="910" height="418" alt="Screenshot 2025-09-08 121311" src="https://github.com/user-attachments/assets/070201ff-21cc-4636-87db-e4622caffcc1" />


