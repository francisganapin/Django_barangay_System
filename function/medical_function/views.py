from django.shortcuts import render,redirect
from .models import Medicine_model,Appointment_model # this is our model
from django.http import JsonResponse
from django import forms
import requests


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import View
from django.core.paginator import Paginator

from django.urls import reverse_lazy

def show_medecine_view(request):

    data = list(Medicine_model.objects.values('id',
        'name','stock','expiry_date','remark'
    ))

    return JsonResponse(data,safe=False)

def show_appointment_view(request):

    data = list(Appointment_model.objects.values('id','patient','service_type',
    'appointment_date','appointment_time','status'))

    return JsonResponse(data,sage=False)



class MedecineForm(forms.ModelForm):
    class Meta:
        model = Medicine_model
        fields ='__all__'
        widgets = {
            'expiry_date':forms.DateInput(attrs={'type':'date'}),
            'remark': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment_model
        fields = ['service_type','appointment_date','appointment_time']
        widgets = {
            'appointment_date':forms.SelectDateWidget(),
            'appointment_time':forms.TimeInput(attrs={'type':'time'}),
        }


#def list_medecine_view(request):

    #api_url_list = 'http://127.0.0.1:8000/medecine_list_json/'

    #if request.method == 'POST':
        #form = MedecineForm(request.POST)
        #form.save()

        #return redirect('list_medecine_view')
    #else:
        #form = MedecineForm()

    #try:
        #response = requests.get(api_url_list,timeout=5)
        #response.raise_for_status()

        #post = response.json() if isinstance(response.json(),list) else []
        #print(post)
    #except Exception as e:
        #print('Data wos not exist')
    #return render(request,'list_medical.html',{'list':post,'form':form})



@method_decorator(login_required,name='dispatch')
class MedecineCreateView(View):
    form_class = MedecineForm
    template_name = 'list_medical.html'
    success_url = reverse_lazy('list_medecine_view')

    def get_medecine_list(self,request):

        medecine_list = Medicine_model.objects.all()

        name = request.POST.get('name')

        if name:
            medecine_list  = medecine_list.filter(name__icontains=name)
        

        data = medecine_list.values('id','name','stock','expiry_date','remark')

        return data
    
    def get(self,request):
        form = self.form_class()
        medecine_list = self.get_medecine_list(request)

        
        paginator = Paginator(medecine_list,12)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request,self.template_name,{
            'form':form,
            'medecine_list':page_obj
        })
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        medecine_list = self.get_medecine_list(request)

        paginator = Paginator(medecine_list,12)
        page_number = request.POST.get('page',1)
        page_obj = paginator.get_page(page_number)

        return render(request,self.template_name,{
            'form':form,
            'medecine_list':page_obj
        })