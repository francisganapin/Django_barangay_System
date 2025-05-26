from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# Create your views here.


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print('User authenticated succesffuly')
            login(request,user)
            return redirect('resident_list')
        else:  
            # if user was failed
            print('Authentication Failed!')    

    return render(request,'login.html')