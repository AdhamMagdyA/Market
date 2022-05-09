from urllib import request
from django.shortcuts import render

# Create your views here.

def signup (request):
    return render(request, 'sign_log_forms/user_signup_form.html',{})

def signupBusiness (request):
    return render(request, 'sign_log_forms/business_signup.html',{})

def login (request):
    return render(request, 'sign_log_forms/login.html',{})
