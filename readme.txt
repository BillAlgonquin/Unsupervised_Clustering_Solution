# Locksmith Clustering App

## Description

This project is an app built with **Streamlit** that predicts customer clusters for a locksmith business based on various input features. The app uses **KMeans Clustering** to categorize clients into different groups based on their behaviors, such as the number of keys duplicated, changes in locks, number of visits, and average spending per service.

## Features

- Predict which cluster a new customer falls into based on their data.
- Provide a clear and easy-to-use interface to input customer details.

## Requirements

To run this app, you need to have the following libraries installed:

- `streamlit`
- `joblib`
- `pandas`
- `scikit-learn`
- `matplotlib`

## Installation

1. Clone this repository:

   ```bash
   git clone <repository_url>
2. Navigate to the project folder:

  ```bash
cd locksmith-clustering-app
3. Install the required dependencies:

  ```bash
pip install -r requirements.txt

4. Run the app using Streamlit:

  ```bash
streamlit run app.py

Usage
Once the app is running, you can input the customer data (number of keys duplicated, changes in locks, visits, and average spending) and it will predict the cluster to which the customer belongs.

License
This project is licensed under the MIT License - see the LICENSE file for details.