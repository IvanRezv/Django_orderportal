from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product),
    path('', views.home),
    path('customer/<str:pk_test>/', views.customer),
]

