from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', views.product),
    path('', views.home),
    path('customer/', views.customer),
]

