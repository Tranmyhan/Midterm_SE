from django.urls import path
from . import views
urlpatterns = [
    path('', views.home), #hàm home trong views.py
    path('products/', views.products),
    path('customer/', views.customer),
]