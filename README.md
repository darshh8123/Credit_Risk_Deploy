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

Step 1: Clone the Repository

Clone this repository to your local machine.

Step 2: Install Dependencies

Navigate to the project directory and install the required libraries.

pip install pandas scikit-learn streamlit joblib


Step 3: Train the Model

The app requires a pre-trained model to make predictions. Run the credit_risk_trainer.py script to download the dataset, train the model, and save it as credit_risk_pipeline.pkl.

python credit_risk_trainer.py


Step 4: Run the Web App

Once the model is saved, you can launch the Streamlit application.

streamlit run app.py


The app will open in your web browser. You can now use the interface to make predictions.

Note: The dataset used in this project is the public German Credit Data
