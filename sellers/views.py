from django.shortcuts import render, redirect

from sellers.models import Seller

# Create your views here.
   
def signupBusiness (request): 
    if request.method == 'POST' and request.FILES['fileName']:
        companyName = request.POST.get('company_name')
        email= request.POST.get('email')
        taxNumber = request.POST.get('Com-Num')
        companyDescription = request.POST.get('company_description')
        password= request.POST.get('password')
        data=Seller(companyName=companyName, email=email, taxNumber=taxNumber, companyDiscription=companyDescription, password=password, sellerPhoto=request.FILES['fileName'])
        data.save()
        return redirect('home')
    return render(request, 'sellers/business_signup.html',{})



def seller_home (request):
    return render(request, 'sellers/seller_home.html',{})
