from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import os
from django.conf import settings
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import ExtraTreesRegressor
import numpy as np
import pandas as pd
import random
from collections import Counter

def home(request):
    return render(request, 'index.html')






def withAdd(request):
    data_path = os.path.join(settings.BASE_DIR, 'civil', 'with_add.csv')

    try:
        data = pd.read_excel(data_path)  
        data = data.fillna(0)  
    except FileNotFoundError:
        print("الملف غير موجود. تأكد من أن المسار صحيح.")
        data = pd.DataFrame()

    if data.empty:
        return render(request, 'withAdd.html', {'error': 'لم يتم العثور على بيانات التدريب.'})

    print("Columns in training data:", data.columns.tolist())

    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    print("Feature columns used for training:", X.columns.tolist())

    model = RandomForestRegressor(random_state=42)
    model.fit(X, y)

    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)  
    accuracy_percentage = r2 * 100

    predicted_output = None
    input_values = None
    error = None

    if request.method == 'POST':
        try:
            
            inputs = []
            for col in X.columns:
                value_str = request.POST.get(col.lower().replace(" ", "").replace("/","").replace("-",""), None)
                if value_str is None:
                    raise ValueError(f"Missing input for {col}")
                value = float(value_str)
                inputs.append(value)

            input_values = inputs
            print("Inputs received:", input_values)

            
            new_input_df = pd.DataFrame([inputs], columns=X.columns)

            predicted_output = model.predict(new_input_df)[0]
            print("Predicted output:", predicted_output)

        except Exception as e:
            error = str(e)
            print("Error during prediction:", error)

    context = {
        'predicted_output': predicted_output,
        'input_values': input_values,
        'error': error,
        'accuracy_percentage': f"{accuracy_percentage:.2f}%",  
        
    }
    return render(request, 'withAdd.html', context)










def without(request):
    
    data_path = os.path.join(settings.BASE_DIR, 'civil', 'without.csv')

   
    try:
        data = pd.read_excel(data_path) 
        data = data.fillna(0)  
    except FileNotFoundError:
        print("الملف غير موجود. تأكد من أن المسار صحيح.")
        data = pd.DataFrame()

    if data.empty:
        return render(request, 'without.html', {'error': 'لم يتم العثور على بيانات التدريب.'})

    print("Columns in training data:", data.columns.tolist())

    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    print("Feature columns used for training:", X.columns.tolist())

    model = RandomForestRegressor(random_state=42)
    model.fit(X, y)

    predicted_output = None
    input_values = None
    error = None

    if request.method == 'POST':
        try:
            
            inputs = []
            for col in X.columns:
                value_str = request.POST.get(col.lower().replace(" ", "").replace("/","").replace("-",""), None)
                if value_str is None:
                    raise ValueError(f"Missing input for {col}")
                value = float(value_str)
                inputs.append(value)

            input_values = inputs
            print("Inputs received:", input_values)

            
            new_input_df = pd.DataFrame([inputs], columns=X.columns)

            predicted_output = model.predict(new_input_df)[0]
            print("Predicted output:", predicted_output)

        except Exception as e:
            error = str(e)
            print("Error during prediction:", error)

    context = {
        'predicted_output': predicted_output,
        'input_values': input_values,
        'error': error,
    }
    return render(request, 'without.html', context)


