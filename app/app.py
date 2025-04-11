import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('C:\\Users\\billt\\OneDrive\\Pictures\\Project\\Unsupervised_Clustering_Solution\\models\\locksmith.pkl')

# Title of the app
st.title("Locksmith Customer Clustering")

# User inputs
llaves_duplicadas = st.number_input("Enter the number of duplicate keys:", min_value=0)
cambios_cerradura = st.number_input("Enter the number of lock changes:", min_value=0)
visitas = st.number_input("Enter the number of visits to the business:", min_value=0)
promedio_gastado = st.number_input("Enter the average amount spent per purchase ($):", min_value=0.0)

# Ensure the columns are named correctly (in Spanish)
input_data = pd.DataFrame([[llaves_duplicadas, cambios_cerradura, visitas, promedio_gastado]],
                          columns=['Llaves_duplicadas', 'Cambios_cerradura', 'Visitas', 'Promedio_gastado'])

# Predict the cluster to which the customer belongs
predicted_cluster = model.predict(input_data)

# Display the result
st.write(f"The new customer belongs to cluster: {predicted_cluster[0]}")
