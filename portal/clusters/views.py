from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('test home page')


def product(request):
    return HttpResponse('test product page')


def customer(request):
    return HttpResponse('test customer page')