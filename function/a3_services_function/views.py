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

    

    def get_service_list(self,request):

        service_list = Service_model.objects.all()

        if request.method == 'POST':
            service_name = request.POST.get('service_name')
            description = request.POST.get('description')
            fee = request.POST.get('fee')
            service_id = request.POST.get('service_id')
            status = request.POST.get('status')

            if service_name:
                service_list = service_list.filter(service_name__icontains=service_name)
            if description:
                service_list = service_list.filter(description__icontains=description)
            if fee:
                service_list = service_list.filter(fee__icontains=fee)
            if service_id: 
                service_list = service_list.filter(id=service_id)
            if status:
                service_list = service_list.filter(status__icontains=status)


        data = service_list.values('id','service_name','description','fee','status')


        return data


    def get(self,request):
        form = self.form_service()
        service_list = self.get_service_list(request)

        paginator = Paginator(service_list,11)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request,self.template_name,{'service_list':page_obj,'form':form})

    def post(self,request):
        form = self.form_service(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
        
        service_list = self.get_service_list(request)
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


