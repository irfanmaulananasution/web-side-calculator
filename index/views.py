from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'index.html')

#this is technically just a proxy
def calculate_api(request):
    if request.method == 'GET':
        input = dict(request.GET)
        response = requests.get('https://rest-side-calculator.herokuapp.com/calculate', data=input)
        return JsonResponse(response.json())