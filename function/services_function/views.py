from django.shortcuts import render
from django import  forms
from .models import *
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import CreateView




def service_class_view(request):

    service_list = Service_model.objects.all()

    return render(request,'service_list.html',{'service_list':service_list})







def resident_class_view(request):
    
    resident_list = Residents_model.objects.all()

    return render(request,'resident_list.html',{'resident_list':resident_list})


#resident 
class ResidentForm(forms.ModelForm):
    class Meta:
        model = Residents_model
        fields = '__all__'

class ResidentCreateView(CreateView):
    form_class = ResidentForm
    template_name ='resident_form.html'
    success_url = reverse_lazy('resident_class_view')