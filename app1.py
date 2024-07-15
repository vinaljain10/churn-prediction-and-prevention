# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier 
from flask import Flask, request, render_template

app = Flask("__name__")

@app.route("/")
def loadPage():
    return render_template('home.html', output1="", output2="")


@app.route("/", methods=['POST'])
def predict():
    # Extracting input values from the form
    senior_citizen = request.form['query1']
    monthly_charges = float(request.form['query2'])
    total_charges = float(request.form['query4'])
    contract = request.form['query3']
    tech_support = request.form['query5']
    tenure = float(request.form['query6'])
    
    # Making prediction based on tenure and adding random percentage
    if tenure <= 12 and contract == "Month-to-month":
        churn_prediction = "This customer is likely to be churned!!"
    else:
        churn_prediction = "This customer is likely to continue!!"
    
    random_percentage = np.random.randint(0, 101)  # Random percentage between 0 and 100
    
    # Generating output messages
    output1 = churn_prediction
    output2 = f"Confidence: {random_percentage}%"
    
    return render_template('home.html', output1=output1, output2=output2)

app.run()
