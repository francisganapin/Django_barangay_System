from django.shortcuts import render,redirect,get_object_or_404
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
        'status',
        'archive'
    )


    template_name = 'list_complaint.html'
    print(get_complaint_list)


    def get(self,request):
        form = self.form_complaint()
        list_data = self.get_complaint_list()
        list_data_exclude = [item for item in list_data if item['archive'] != True ]
        context = {'Pending':self.Pending,
               'Resolved':self.Resolved,
               'complaint_list':list_data_exclude,
               'form':form
               }
        return render(request,self.template_name,context)
        

    def post(self,request):
        form = self.form_complaint(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect('complaints')
        
        list_data = self.get_complaint_list()
        list_data_exclude = [item for item in list_data if item['archive'] != True ]
        context = {'Pending':self.Pending,
               'Resolved':self.Resolved,
               'complaint_list':list_data_exclude,
               'form':form
               
               }
        return render(request,self.template_name,context)

    #def post_update(self,request):

        


def archive_status_complaint(request,pk):


    complaint_list_instance =  get_object_or_404(Complaints_model,pk=pk)
    complaint_list_instance.archive = True
    complaint_list_instance.save()
    return redirect('complaints')


#i will update this later so it would work later thanks
#def update_status_complaint(request,pk):

    #if 'update_complaint_status' in request.POST:
        #complaint_id_2 = request.POST.get('complaint_id')
        #complaint_status = request.POST.get('status')

        #try:
            #complaint_status = Complaints_model.objects.get(complaint_id=complaint_id_2)
            #complaint.status = complaint_status
            #complaint.save()
            #return redirect('complaints')
        #except Complaints_model.DoesNotExist:
            #print('error')