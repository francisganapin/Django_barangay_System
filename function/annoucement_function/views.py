from django.shortcuts import render,redirect
from .models import Announcement_model
from django.http import JsonResponse
from .models import Announcement_model
import requests
from django import  forms

def show_announcement_view(request):
    # Get all data of announcement
    data = list(Announcement_model.objects.values('id','title',
                                                   'content',
                                                   'published_date',
                                                   'expiry_date',
                                                   'is_active'))
    return JsonResponse(data, safe=False)
    


class AnnoucementForm(forms.ModelForm):
    class Meta:
        model = Announcement_model
        fields = "title","content","expiry_date","is_active"
        widgets ={
            'expiry_date':forms.DateInput(attrs={'type':'date'}),
        }



def list_announcement_view(request):
    #api url 
    api_url_list = 'http://127.0.0.1:8000/annoucement/'


    if request.method =='POST':
        form = AnnoucementForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('list_announcement_view')
    else:
        form = AnnoucementForm()

    try:
        response = requests.get(api_url_list,timeout=5)
        response.raise_for_status()
        
        posts = response.json() if isinstance(response.json(),list) else []
        print(posts)
    except:
        print('data was not exist')
    return render(request,'list_announcement.html',{'list':posts,'form':form})