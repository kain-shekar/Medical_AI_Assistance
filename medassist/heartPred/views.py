import pickle
import pandas as pd
import numpy as np
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os

# Load the model and scaler
MODEL_PATH = os.path.join(settings.BASE_DIR, 'heartPred/model/heart_prediction_model')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'heartPred/model/scaledfun')

model = pickle.load(open(MODEL_PATH, 'rb'))
scaler = pickle.load(open(SCALER_PATH, 'rb'))

# Show form page
def heart_form(request):
    return render(request, 'form.html')

# Predict function
@csrf_exempt
def heart_predict(request):
    prediction_text = None
    if request.method == 'POST':
        try:
            data = [float(x) for x in request.POST.values()]
            print(data)
            scaled_data = scaler.transform(np.array(data).reshape(1, -1))
            output = model.predict(scaled_data)[0]

            if output == 0:
                prediction_text = "🟢 The patient does not have heart disease."
            else:
                prediction_text = "🔴 The patient is at risk of heart disease."

        except Exception as e:
            prediction_text = f"❗ Error: {e}"

    return render(request, 'form.html', {'prediction_text': prediction_text})