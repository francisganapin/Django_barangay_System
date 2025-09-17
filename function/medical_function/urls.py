from django.urls import path
from .views import  show_medecine_view,MedecineCreateView,show_appointment_view

urlpatterns = [
    path('medecine_list_json/',show_medecine_view, name='medecine_list_json'),
    path('appointment_list_json',show_appointment_view,name='show_appointment_json'),
    
    path('medicine_list/',MedecineCreateView.as_view(), name='list_medecine_view')
]

