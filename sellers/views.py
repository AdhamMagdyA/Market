from django.shortcuts import render

# Create your views here.

def signupBusiness (request):
    return render(request, 'sellers/business_signup.html',{})



def seller_home (request):
    return render(request, 'sellers/seller_home.html',{})
