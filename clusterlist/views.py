from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'clusters/dashboard.html')


def cluster_data(request):
    return render(request, 'clusters/clusters.html')

