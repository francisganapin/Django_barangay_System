from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from function.a2_resident_function.models import Residents_model
from function.a3_services_function.models import Service_model
from function.a4_complaints_function.models import Complaints_model
from function.a5_annoucement_function.models import Announcement_model

@login_required
def model_analytic(request):
    resident = Residents_model.objects.count()
    services = Service_model.objects.count()
    complaints = Complaints_model.objects.count()
    announcement_count = Announcement_model.objects.count()
    announcements_list = Announcement_model.objects.filter(is_active=True).order_by('-published_date')[:4]
    
    context ={
        'resident': resident,
        'services': services,
        'complaints': complaints,
        'announcement_count': announcement_count,
        'announcements': announcements_list
    }
    return render(request,'homepage.html',context)
    