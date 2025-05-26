from django.shortcuts import render,redirect
from django import  forms
from .models import Service_model
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import View
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Service_model
        fields = 'service_name','description','fee'


@method_decorator(login_required, name='dispatch')
class ServicesView(View):
    template_name ='service_list.html'
    form_service = ServicesForm

    
    def service_class_view(self):
        service_list = Service_model.objects.all()
        return service_list

    def get(self,request):
        service_list = self.service_class_view()
        print(service_list)
        form = self.form_service()
        return render(request,self.template_name,{'service_list':service_list,'form':form})

    def post(self,request):
        form = self.form_service(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
        service_list = self.service_class_view()
        return render(request,self.template_name,{'service_list':service_list,'form':form})
       

@method_decorator(login_required, name='dispatch')     
class ServicesDeleteView(View):
    
    def post(self,request,pk,*args,**kwargs):
        service_list_instance =  get_object_or_404(Service_model,pk=pk)
        service_list_instance.delete()
        return redirect('service_list')


