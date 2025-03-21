from django.urls import path
from .views import ClearanceMaker

urlpatterns = [
    path('clearance_form/', ClearanceMaker.as_view(), name='clearance_form'),
    path('generate_clearance/', ClearanceMaker.as_view(), name='generate_clearance'),
]