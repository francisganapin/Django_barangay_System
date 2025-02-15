from django.urls import path
from .views import complaints_list_views

urlpatterns = [
    path('complaints/', complaints_list_views, name='complaints_list_views'),
]
