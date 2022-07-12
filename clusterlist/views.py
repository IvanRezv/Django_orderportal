from django.shortcuts import render
from django.http import HttpResponse

from .models import *


# Create your views here.


def home(request):
    clusters = Cluster.objects.all()
    total_clusters = clusters.count()
    total_tickets = Cluster.objects.values('rds_link').distinct().count()
    context = {'total_clusters': total_clusters, 'total_tickets': total_tickets}
    return render(request, 'clusters/dashboard.html', context)


def cluster_data(request):
    clusters = Cluster.objects.all()
    return render(request, 'clusters/clusters.html', {'clusters': clusters})
