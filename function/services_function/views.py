from django.shortcuts import render,redirect
from django import  forms
from .models import Service_model
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import View
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator

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
        form = self.form_service()
        service_list = self.service_class_view()

        paginator = Paginator(service_list,11)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request,self.template_name,{'service_list':page_obj,'form':form})

    def post(self,request):
        form = self.form_service(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
        
        service_list = self.service_class_view()
        paginator = Paginator(service_list,11)
        page_number = request.POST.get('page',1)
        page_obj = paginator.get_page(page_number)



        return render(request,self.template_name,{'service_list':page_obj,'form':form})
       

@method_decorator(login_required, name='dispatch')     
class ServicesDeleteView(View):
    
    def post(self,request,pk,*args,**kwargs):
        service_list_instance =  get_object_or_404(Service_model,pk=pk)
        service_list_instance.delete()
        return redirect('service_list')


