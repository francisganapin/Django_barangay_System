from django.urls import path
from .views import ServicesView,ServicesDeleteView

urlpatterns = [
    path('service/list/<int:pk>/delete/', ServicesDeleteView.as_view(), name='service_class_delete'),
    path('service/list/', ServicesView.as_view(), name='service_list'),

    
]
