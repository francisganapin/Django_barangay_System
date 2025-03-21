from django.urls import path
from .views import *

urlpatterns = [
    path('complaints/', Complaint_list_view.as_view(), name='complaints'),
    path('complaints/<int:pk>',archive_status_complaint,name='complaint_status_update')
]
