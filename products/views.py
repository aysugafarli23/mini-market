import requests
from django.shortcuts import render
from django.http import HttpResponse

def product_list(request):
    try:
        response = requests.get('http://127.0.0.1:8000/products-api/list/')
        response.raise_for_status()  # Raise an exception for HTTP errors
        products = response.json()
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
    
    return render(request, 'base.html', {'products': products})