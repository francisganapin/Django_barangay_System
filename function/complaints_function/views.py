from django.shortcuts import render
from .models import  Complaints_model

from django.http import JsonResponse
from .models import Complaints_model


from .models import Complaints_model

def complaints_list_views(request):
    complaint_list = Complaints_model.objects.select_related('resident').values(
        'complaint_id', 
        'resident__id',  # ForeignKey ID
        'resident__first_name',  # Include first name
        'resident__last_name',  # Include last name
        'complaint_date', 
        'description', 
        'status'
    )

    return render(request,'template/list_complaint.html',{'complaint_list':complaint_list})
