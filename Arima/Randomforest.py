# from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split


# Import the RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor

# Load your data
df = pd.read_csv("Final_Data.csv")

# Separate features and target variable
X = df.drop(columns=['Unnamed: 0', 'Date', 'Siltation_Amount'])
y = df['Siltation_Amount']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a RandomForestRegressor model
model = RandomForestRegressor()

# Fit the model
model.fit(X_train, y_train)

# Save the model to a file
with open("randomforest.pkl", 'wb') as model_file:
    pickle.dump(model, model_file)
