from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login as auth_login, logout
# from .decorators import unauthenticated_user

# Create your views here.

def userHome(request):
    return render(request, 'core/user_home.html')


# @unauthenticated_user
def login (request):
    if request.method == 'POST':
        req_email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate(request=None, username=req_email,password=password)
        if user is not None:
            auth_login(request,user)
            if user.userAuth.auth_name == "user" :
                return redirect('userhome')
            elif user.userAuth.auth_name == 'seller':
                return redirect('sellerhome')
            elif user.userAuth.auth_name == 'admin':
                return redirect('adminhome')

        else:
            messages.info(request, "Username Or Password Is Incorrect")

    return render(request, 'core/login.html',{})
    
        

def logout(request):
    logout(request)
    return redirect('home')

def userProfile(request):
    return render(request, 'core/profile_user.html',{})

def userEditProfile(request):
    return render(request, 'core/user_profile_edit.html',{})
