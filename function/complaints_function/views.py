from django.shortcuts import render
from .models import  Complaints_model

from django.http import JsonResponse
from .models import Complaints_model
from django.views.generic import View

from .models import Complaints_model


class Complaint_list_view(View):
    complaint_list = Complaints_model.objects.select_related('resident').values(
        'complaint_id', 
        'resident__resident_id',  # ForeignKey ID
        'resident__first_name',  # Include first name
        'resident__last_name',  # Include last name
        'complaint_date', 
        'description', 
        'status'
    )

    Pending = ''
    Resolved = ''
 
   
    
    template_name = 'list_complaint.html'
    print(complaint_list)


    def get(self,request):

        list_data = self.complaint_list
        context = {'Pending':self.Pending,
               'Resolved':self.Resolved,
               'complaint_list':list_data
               }

     
        return render(request,self.template_name,context)
        
    