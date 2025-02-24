from django.urls import path
from .views import * 

urlpatterns = [
    path('service/list/', service_class_view, name='service_class_view'),
    
]
