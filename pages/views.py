import pickle
import pandas as pd
from django.shortcuts import render


def aboutPageView(request):
    return render(request, 'about.html')


def tryOut(request):
    return render(request, 'tryout.html')


def makePrediction(request):
    if request.method == "POST":
        form_data = {
            'est_diameter_min': request.POST['est_diameter_min'],
            'est_diameter_max': request.POST['est_diameter_max'],
            'relative_velocity': request.POST['relative_velocity'],
            'miss_distance': request.POST['miss_distance'],
            'absolute_magnitude': request.POST['absolute_magnitude'],
        }

        with open('./rf_model.pkl', 'rb') as f:
            loadedModel = pickle.load(f)

        prediction = loadedModel.predict(pd.DataFrame([form_data]))
        if prediction:
            prediction = "Hazardous!"
        else:
            prediction = "Not Hazardous"
        return render(request, 'tryout.html', {'prediction': prediction})
    else:
        # Redirect to the form page if not a POST request
        return render(request, 'tryout.html')
