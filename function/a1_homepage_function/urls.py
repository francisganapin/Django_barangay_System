from django.urls import path
from .views import  model_analytic

urlpatterns = [
    path('homepage/',model_analytic, name='homepage'),
    
]
