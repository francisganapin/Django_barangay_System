from django.contrib import admin
from django.urls import path
from .views import show_announcement_view,list_announcement_view


urlpatterns =[
    path('annoucement/',show_announcement_view,name='show_anouncement_view'),
    path('annoucement_list/',list_announcement_view,name='list_announcement_view'),

    
]