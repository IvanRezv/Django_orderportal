from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(requests):
    return HttpResponse('Home page')


def cluster_data(requests):
    return HttpResponse('CLuster data')