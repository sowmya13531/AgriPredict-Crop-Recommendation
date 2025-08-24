# app.py
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Prediction function
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_data = pd.DataFrame([{
        'N': N,
        'P': P,
        'K': K,
        'temperature': temperature,
        'humidity': humidity,
        'ph': ph,
        'rainfall': rainfall
    }])

    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.markdown("<h1 style='color: green;'>SmartAgri - Crop Recommendation System</h1>", unsafe_allow_html=True)
#st.markdown("Enter the soil and environmental parameters below:")
st.markdown(f"<h3 style='color: green;'>🌱 Recommended crop: {predict_crop}</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", 0, 140)
    P = st.number_input("Phosphorus (P)", 0, 140)
    K = st.number_input("Potassium (K)", 0, 200)
    temperature = st.number_input("Temperature (°C)", 0.0, 50.0)

with col2:
    humidity = st.number_input("Humidity (%)", 0.0, 100.0)
    ph = st.number_input("Soil pH", 0.0, 14.0)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0)


if st.button('Recommend Crop'):
    crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
    st.markdown(
        f"""
        <div style='
            background-color: #28a745;  /* bootstrap success green */
            color: white;
            padding: 15px;
            border-radius: 5px;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
        '>
            🌱 Recommended crop: {crop}
        </div>
        """, 
        unsafe_allow_html=True
    )
