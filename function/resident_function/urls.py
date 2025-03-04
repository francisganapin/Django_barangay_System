from django.urls import path
from .views import  ResidentCreateView,ResidentExportView

urlpatterns = [
    path('residents/', ResidentCreateView.as_view(), name='resident_list'),
    path('residents/export/', ResidentExportView.as_view(), name='resident_list_export')
    
]
