from django.urls import path
from .views import * 

urlpatterns = [
    path('residents/', ResidentCreateView.as_view(), name='resident_list'),
    
]
