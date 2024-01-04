# from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor

df=pd.read_csv("Final_Data.csv")
# print(df)

X = df.drop(columns=['Unnamed: 0', 'Date', 'Siltation_Amount'])
y = df['Siltation_Amount']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.head())
model = AdaBoostRegressor()
model.fit(X_train, y_train)

with open("adabost_siltation_pred.pkl",'wb') as model_file: 
    pickle.dump(model,model_file)
# print(df.head())
# print(df.columns)
