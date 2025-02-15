from django.urls import path
from .views import resident_class_view

urlpatterns = [
    path('residents/', resident_class_view, name='resident_list'),
]
