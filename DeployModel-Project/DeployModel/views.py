from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(requset):
    return render(requset,"home.html")

def result(requset):

    cls = joblib.load('best_model_xgb.sav')

    # Convert request parameters to numeric values
    lis = [
        int(requset.GET['passenger_count']),
        int(requset.GET['hour']),
        int(requset.GET['day']),
        int(requset.GET['month']),
        int(requset.GET['weekday']),
        int(requset.GET['year']),
        float(requset.GET['jfk_dist']),
        float(requset.GET['ewr_dist']),
        float(requset.GET['lga_dist']),
        float(requset.GET['sol_dist']),
        float(requset.GET['nyc_dist']),
        float(requset.GET['distance']),
        float(requset.GET['bearing']),
    ]

    # Predict and format the result
    ans = cls.predict([lis])[0]  # Get the first value from the prediction array
    formatted_ans = f"${ans:.2f}"  # Format the answer as a string with 2 decimal places and a dollar sign

    return render(requset, 'result.html', {'ans': formatted_ans})