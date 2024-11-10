
import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load("penguin_model.pkl")

st.title("Penguin Species Prediction")

# Collect user input
bill_length = st.number_input("Bill Length (mm)", min_value=32.1, max_value=59.6)
bill_depth = st.number_input("Bill Depth (mm)", min_value=13.1, max_value=21.5)
flipper_length = st.number_input("Flipper Length (mm)", min_value=172, max_value=231)
body_mass = st.number_input("Body Mass (g)", min_value=2700, max_value=6300)
sex = st.selectbox("Sex", ("Male", "Female"))
island = st.selectbox("Island", ("Biscoe", "Dream", "Torgersen"))

# Convert inputs to a DataFrame
input_data = pd.DataFrame({
    'bill_length_mm': [bill_length],
    'bill_depth_mm': [bill_depth],
    'flipper_length_mm': [flipper_length],
    'body_mass_g': [body_mass],
    'sex_Male': [1 if sex == "Male" else 0],
    'island_Dream': [1 if island == "Dream" else 0],
    'island_Torgersen': [1 if island == "Torgersen" else 0]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"The predicted species is: {prediction[0]}")
