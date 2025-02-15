from django.shortcuts import render
from .models import Residents_model
# Create your views here.


def resident_class_view(request):
    
    resident_list = Residents_model.objects.all()

    return render(request,'resident_list.html',{'resident_list':resident_list})