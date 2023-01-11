from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('products/', views.products, name='Products'),
    path('customer/', views.customer, name='Customer'),
]