from django.shortcuts import render,redirect
from .models import Announcement_model
from django.http import JsonResponse
from .models import Announcement_model
import requests
from django import  forms

from django.core.paginator import Paginator

def show_announcement_view(request):
    # Get all data of announcement
    announcments = Announcement_model.objects.values('id','title',
                                                   'content',
                                                   'published_date',
                                                   'expiry_date',
                                                   'is_active')
    # paginator secotr
    page = request.GET.get('page',1)
    per_page = request.GET.get('per_page',12)

    paginator = Paginator(announcments,per_page)
    page_obj = paginator.get_page(page)

    data = list(page_obj.object_list)
    
    response = {
        'total_items':paginator.count,
        'total_page':paginator.num_pages,
        'current_page':page_obj.number,
        'has_next':page_obj.has_next(),
        'has_previous':page_obj.has_previous(),
        'announcement':data,
    }

    return JsonResponse(response, safe=False)
        



class AnnoucementForm(forms.ModelForm):
    class Meta:
        model = Announcement_model
        fields = "title", "content", "expiry_date", "is_active"
        widgets ={
            'expiry_date':forms.DateInput(attrs={'type':'date'}),
        }



def list_announcement_view(request):

    if request.method == 'POST':
        form = AnnoucementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_announcement_view')
    else:
        form = AnnoucementForm()



    title_search = request.GET.get('search','').strip()
    filters = {"is_active":True}


    if title_search:
         filters['title__icontains'] = title_search

        # Get all data of announcement
   
    # ✅ Apply filters
    announcements = Announcement_model.objects.filter(**filters).values(
        'id',
        'title',
        'content',
        'published_date',
        'expiry_date',
        'is_active'
    )

    print("GET DATA:", request.GET)
    # paginator secotr
    page = request.GET.get('page',1)
    per_page = request.GET.get('per_page',12)

    paginator = Paginator(announcements,per_page)
    page_obj = paginator.get_page(page)

    data = list(page_obj.object_list)
    
    

    return render(request,'list_announcement.html',{'form':form,
        'total_items':paginator.count,
        'page_obj': page_obj,  # ✅ Pass full pagination object
        'total_page':paginator.num_pages,
        'current_page':page_obj.number,
        'has_next':page_obj.has_next(),
        'has_previous':page_obj.has_previous(),
        'announcement':data,})