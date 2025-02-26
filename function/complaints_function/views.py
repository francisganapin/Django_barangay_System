from django.shortcuts import render,redirect
from .models import  Complaints_model

from django.http import JsonResponse
from .models import Complaints_model
from django.views.generic import View

from .models import Complaints_model
from django import  forms


class ComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaints_model
        fields = '__all__'
        widgets = {
                    'complaint_date':forms.DateInput(attrs={'type':'date'}),

                }
class Complaint_list_view(View):

    form_complaint = ComplaintsForm
    Pending = ''
    Resolved = ''
    def get_complaint_list(self):
        return  Complaints_model.objects.select_related('resident').values(
        'complaint_id', 
        'resident__resident_id',  # ForeignKey ID
        'resident__first_name',  # Include first name
        'resident__last_name',  # Include last name
        'complaint_date', 
        'description', 
        'status'
    )


    template_name = 'list_complaint.html'
    print(get_complaint_list)


    def get(self,request):
        form = self.form_complaint()
        list_data = self.get_complaint_list()
        context = {'Pending':self.Pending,
               'Resolved':self.Resolved,
               'complaint_list':list_data,
               'form':form
               }
        return render(request,self.template_name,context)
        

    def post(self,request):
        form = self.form_complaint(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('complaints')
        list_data = self.get_complaint_list()
        context = {'Pending':self.Pending,
               'Resolved':self.Resolved,
               'complaint_list':list_data,
               'form':form
               }
        return render(request,self.template_name,context)

