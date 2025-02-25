from django.urls import path
from .views import *

urlpatterns = [
    path('complaints/', Complaint_list_view.as_view(), name='complaints')
]
