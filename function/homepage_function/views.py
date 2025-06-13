from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from function.resident_function.models import Residents_model
from function.services_function.models import Service_model
from function.complaints_function.models import Complaints_model
from function.annoucement_function.models import Announcement_model

@login_required
def model_analytic(request):
    resident = Residents_model.objects.count()
    services = Service_model.objects.count()
    complaints = Complaints_model.objects.count()
    anouncement = Announcement_model.objects.count()
    context ={
        'resident':resident,
        'services':services,
        'complaints':complaints,
        'anouncement':anouncement
    }
    return render(request,'homepage.html',context)
    