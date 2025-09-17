from django.urls import path
from .views import login_view
from django.contrib.auth import views as auth_views #input this auth_view to have have option to logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view, name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout') # input this one if you want to logout the user

]