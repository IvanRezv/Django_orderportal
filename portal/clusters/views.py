from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'clusters/dashboard.html')


def product(request):
    return render(request, 'clusters/products.html')


def customer(request):
    return render(request, 'clusters/customer.html')