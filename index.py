import streamlit as st
import pandas as pd
import joblib

# --- Step 1: Set up the Streamlit Page ---
# This must be the very first Streamlit command in the script.
st.set_page_config(page_title="Credit Risk Prediction App", layout="wide")

# --- Step 2: Load the Trained Model Pipeline ---
# The model file is created by the 'credit_risk_trainer.py' script.
try:
    pipeline = joblib.load('credit_risk_pipeline.pkl')
except FileNotFoundError:
    st.error("Error: The model file 'credit_risk_pipeline.pkl' was not found.")
    st.info("Please run the 'credit_risk_trainer.py' script first to train and save the model.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred while loading the model: {e}")
    st.stop()

# --- Custom CSS for Styling ---
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main-header {
        color: #1a1a1a;
        font-size: 2.5em;
        font-weight: 600;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .sub-header {
        color: #4a4a4a;
        font-size: 1.2em;
        font-weight: 400;
        text-align: center;
        margin-bottom: 2em;
    }
    .stForm {
        background-color: #ffffff;
        padding: 2em;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        background-color: #4a90e2;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #357bd9;
    }
    .result-container {
        margin-top: 2em;
        padding: 1.5em;
        border-radius: 10px;
    }
    .success-box {
        background-color: #e6ffed;
        border: 2px solid #5cb85c;
    }
    .error-box {
        background-color: #fff0f0;
        border: 2px solid #d9534f;
    }
    .st-bd {
        padding-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">💸 Credit Risk Prediction App</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Please enter the applicant\'s details and click **Predict**.</p>', unsafe_allow_html=True)

# --- Step 3: Create the Input Form ---
# The input fields must match the features used for training the model.
with st.form(key='credit_risk_form'):
    st.subheader("Applicant Details")
    col1, col2, col3 = st.columns(3)
    with col1:
        # Categorical Features
        checking_account = st.selectbox("Checking Account Status", ['A11', 'A12', 'A13', 'A14'], help="A11:<0 DM, A12:>=0DM & <200DM, A13:>=200DM, A14:no checking account")
        credit_history = st.selectbox("Credit History", ['A30', 'A31', 'A32', 'A33', 'A34'], help="A30:no credits, A31:all credits paid, A32:all paid back, A33:some loans paid back, A34:past credit delays")
        purpose = st.selectbox("Purpose of Loan", ['A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 'A49', 'A410'], help="A40:car, A41:furniture, A42:radio/TV, A43:domestic appliances, A44:repairs, A45:education, A46:vacation, A47:retraining, A48:business, A49:other, A410:used car")
        savings_account = st.selectbox("Savings Account Status", ['A61', 'A62', 'A63', 'A64', 'A65'], help="A61:<100DM, A62:100-500DM, A63:500-1000DM, A64:>=1000DM, A65:no savings account")
        employment_since = st.selectbox("Employment Since", ['A71', 'A72', 'A73', 'A74', 'A75'], help="A71:<1 year, A72:1-4 years, A73:4-7 years, A74:>=7 years, A75:unemployed")
        
    with col2:
        personal_status = st.selectbox("Personal Status", ['A91', 'A92', 'A93', 'A94'], help="A91:male divorcee/separated, A92:female divorcee/separated/married, A93:male single, A94:male married/widowed")
        other_debtors = st.selectbox("Other Debtors", ['A101', 'A102', 'A103'], help="A101:none, A102:co-applicant, A103:guarantor")
        property_type = st.selectbox("Property Type", ['A121', 'A122', 'A123', 'A124'], help="A121:real estate, A122:building society, A123:car, A124:unknown/no property")
        other_installment_plans = st.selectbox("Other Installment Plans", ['A141', 'A142', 'A143'], help="A141:bank, A142:stores, A143:none")
        housing = st.selectbox("Housing Status", ['A151', 'A152', 'A153'], help="A151:rent, A152:own, A153:free")
        
    with col3:
        job = st.selectbox("Job Type", ['A171', 'A172', 'A173', 'A174'], help="A171:unemployed/unskilled, A172:unskilled, A173:skilled, A174:highly skilled")
        telephone = st.selectbox("Telephone", ['A191', 'A192'], help="A191:none, A192:yes")
        foreign_worker = st.selectbox("Foreign Worker", ['A201', 'A202'], help="A201:yes, A202:no")
        
    st.markdown("---")
    st.subheader("Loan and Personal Financial Details")
    col4, col5 = st.columns(2)
    with col4:
        # Numerical Features
        duration = st.slider("Duration of Loan (months)", min_value=0, max_value=72, value=12)
        credit_amount = st.number_input("Credit Amount (DM)", min_value=0, value=2000)
        installment_rate = st.slider("Installment Rate (% of income)", min_value=1, max_value=4, value=2)
        residence_since = st.slider("Residence Since (years)", min_value=1, max_value=4, value=2)
    with col5:
        age = st.slider("Age (years)", min_value=18, max_value=75, value=30)
        existing_credits = st.slider("Existing Credits at this Bank", min_value=0, max_value=4, value=1)
        dependents = st.slider("Number of Dependents", min_value=1, max_value=3, value=1)
        
    st.markdown("---")
    predict_button = st.form_submit_button(label="Predict Credit Risk")

# --- Step 4: Handle Prediction and Display Results ---
if predict_button:
    # Create a DataFrame from user inputs. Column names and order must EXACTLY match the training data.
    # The order of columns is critical and must match the order in the trainer script's pipelines.
    input_data = pd.DataFrame([[
        duration, credit_amount, installment_rate, residence_since, age, existing_credits, dependents,
        checking_account, credit_history, purpose, savings_account, employment_since, personal_status,
        other_debtors, property_type, other_installment_plans, housing, job, telephone, foreign_worker
    ]], columns=['duration', 'credit_amount', 'installment_rate', 'residence_since', 'age', 'existing_credits', 'dependents',
                'checking_account', 'credit_history', 'purpose', 'savings_account', 'employment_since', 'personal_status',
                'other_debtors', 'property', 'other_installment_plans', 'housing', 'job', 'telephone', 'foreign_worker'])

    # Make the prediction
    try:
        # The model's pipeline expects the original feature names.
        prediction = pipeline.predict(input_data)[0]
        prediction_proba = pipeline.predict_proba(input_data)[0]

        st.subheader("🔎 Prediction Result")
        
        # Display the results
        if prediction == 1: # 1 for bad risk (default)
            st.error("🚨 This applicant is classified as a **High Credit Risk**.")
            st.markdown(f"**Default Probability:** {prediction_proba[1]:.2%}")
        else: # 0 for good risk
            st.success("✅ This applicant is classified as a **Low Credit Risk**.")
            st.markdown(f"**Default Probability:** {prediction_proba[1]:.2%}")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.info("⚠️ This might be due to a mismatch between the input data and the model's expected features. Please check your `credit_risk_trainer.py` and ensure the column names and data types are correct.")

# --- Step 5: How to Run the App ---
# 1. Save this file as 'app.py' in the same directory as your trained model.
# 2. Run the 'credit_risk_trainer.py' script first.
# 3. Then, in your terminal, run the Streamlit app:
#    streamlit run app.py
