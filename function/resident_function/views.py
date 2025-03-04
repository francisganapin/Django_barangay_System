from django.shortcuts import render,redirect
from django import  forms
from .models import Residents_model
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import View
from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import date 
#resident 

import csv # 2/13/2025
from django.http import HttpResponse # import this to have csv


class ResidentForm(forms.ModelForm):

    class Meta:
        model = Residents_model
        GEN_CHOICES =  [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
        fields = '__all__'
        widgets = {
            'birth_date':forms.DateInput(attrs={'type':'date'}),
            'gender':forms.Select(choices=GEN_CHOICES),
        }

class ResidentCreateView(View):
    form_class = ResidentForm
    template_name = 'resident_list.html'
    success_url = reverse_lazy('resident_list')

    

    def get(self, request):
        form = self.form_class()
        resident_list = Residents_model.objects.all()
        paginator = Paginator(resident_list,12)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {
            'form': form,
            'resident_list': page_obj
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        resident_list = Residents_model.objects.all()
        return render(request, self.template_name, {
            'form': form,
            'resident_list': resident_list
        })
    
class ResidentExportView(View):
 
    def post(self,request):
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": f'attachment; filename="resident_list_{date.today()}.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow([ 'resident_id','first_name','last_name','birth_date','address','contact_number','house_id','gender'])
        resident_list = Residents_model.objects.all()
        for resident in resident_list:
            writer.writerow([
                resident.resident_id,
                resident.first_name,
                resident.last_name,
                resident.birth_date,
                resident.address,
                resident.contact_number,
                resident.house_id, 
                resident.gender 
            ])   
        return response     