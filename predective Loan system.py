
import numpy as np
import pickle 
import streamlit as st
import os
loaded_model = pickle.load(open(r"C:\Users\user\Downloads\trained_model.sav", "rb"))
def Loan_prediction(input_data):
      input_data_as_numpy_array=np.asarray(input_data)
      input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
      prediction=loaded_model.predict(input_data_reshaped)
      print(prediction)
      if (prediction[0]==0):
        return  'approved'
      else:
       return  'Not approved'
def main():
    #giving a title
    st.title("Loan Prediction Web App")     
st.title("Loan Approval Prediction")
# Input fields
applicant_income = st.number_input("Applicant Income")
coapplicant_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_amount_term = st.number_input("Loan Amount Term")
credit_history = st.selectbox("Credit History", [0, 1])
gender = st.selectbox("Gender", ["Female", "Male"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])  
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Convert categorical input to binary encoding
gender_female = 1 if gender == "Female" else 0
gender_male = 1 if gender == "Male" else 0
married_no = 1 if married == "No" else 0
married_yes = 1 if married == "Yes" else 0
dependents_0 = 1 if dependents == "0" else 0
dependents_1 = 1 if dependents == "1" else 0
dependents_3_plus = 1 if dependents == "3+" else 0
education_graduate = 1 if education == "Graduate" else 0
education_not_graduate = 1 if education == "Not Graduate" else 0
self_employed_no = 1 if self_employed == "No" else 0
self_employed_yes = 1 if self_employed == "Yes" else 0
property_area_rural = 1 if property_area == "Rural" else 0
property_area_semiurban = 1 if property_area == "Semiurban" else 0
property_area_urban = 1 if property_area == "Urban" else 0

# Create a feature vector for prediction
features = [
    applicant_income,
    coapplicant_income,
    loan_amount,
    loan_amount_term,
    credit_history,
    gender_female,
    gender_male,
    married_no,
    married_yes,
    dependents_0,
    dependents_1,
    dependents_2,
    dependents_3_plus,  
    education_graduate,
    education_not_graduate,
    self_employed_no,
    self_employed_yes,
    property_area_rural,
    property_area_semiurban,
    property_area_urban,
]
# Create a button for prediction
if st.button("Predict Loan Approval"):
    prediction = Loan_prediction(features)
    st.success(f"Prediction: {prediction}")

if __name__ == '__main__':
    main()
