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

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ResidentForm(forms.ModelForm):

    class Meta:
        model = Residents_model
        GEN_CHOICES =  [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
        fields = '__all__'
        exclude = 'is_archive',
        widgets = {
            'birth_date':forms.DateInput(attrs={'type':'date'}),
            'gender':forms.Select(choices=GEN_CHOICES),
        }

    def clean_resident_id(self):
        resident_id = self.cleaned_data.get('resident_id')

        # add this to check if resident id was not 7 characterd 
        if len(resident_id) != 8:
            raise forms.ValidationError('Make input 9 character') 

        if Residents_model.objects.filter(resident_id=resident_id).exists():
            raise forms.ValidationError('This id is already exist')
        return resident_id



@method_decorator(login_required, name='dispatch')
class ResidentCreateView(View):
    form_class = ResidentForm
    template_name = 'resident_list.html'
    success_url = reverse_lazy('resident_list')


    def get_resident_list(self,request):
        resident_list = Residents_model.objects.all()

        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            resident_id = request.POST.get('resident_id')
            gender = request.POST.get('gender')
            house_id = request.POST.get('house_id')

            if first_name:
                resident_list = resident_list.filter(first_name__icontains=first_name)
            if last_name:
                resident_list = resident_list.filter(last_name__icontains=last_name)
            if resident_id:
                resident_list = resident_list.filter(resident_id__icontains=resident_id)
            if gender:
                resident_list = resident_list.filter(gender__iexact=gender)
            if house_id:
                resident_list = resident_list.filter(house_id__icontains=house_id)

        data = resident_list.values('resident_id','first_name','last_name','birth_date',
                                    'address','contact_number','house_id','gender')
        return data
    
    def get(self, request):
        form = self.form_class()
        resident_list = self.get_resident_list(request)
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
        resident_list = self.get_resident_list(request)
        return render(request, self.template_name, {
            'form': form,
            'resident_list': resident_list
        })
    

@method_decorator(login_required, name='dispatch')
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