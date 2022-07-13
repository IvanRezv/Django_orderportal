from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product, name="products"),
    path('', views.home, name="home"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
]

