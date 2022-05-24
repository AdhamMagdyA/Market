import imp
from django.shortcuts import render, redirect
from core.models import Authorization
from sellers.models import Seller
from users.views import generateRondamPassword
from django.core.mail import EmailMultiAlternatives
from market.settings import EMAIL_HOST_USER

# Create your views here.
def signupBusiness (request): 
    if request.method == 'POST' :
        recaptcha = request.POST.get('g-recaptcha-response')
        if recaptcha:
            if request.FILES['fileName']:
                companyName = request.POST.get('company_name')
                email= request.POST.get('email')
                taxNumber = request.POST.get('Com-Num')
                companyDescription = request.POST.get('company_description')
                password= generateRondamPassword()
                type=Authorization.objects.get(auth_name="seller")
                data=Seller(companyName=companyName, email=email, taxNumber=taxNumber, companyDiscription=companyDescription, password=password, sellerPhoto=request.FILES['fileName'],userAuth=type)
                data.save()
                 #send email to company
                subject = 'Welcome '+companyName+' in Souq Market'
                message = 'Hope you are enjoying your account with us. Your password is: ' + password + " you can login to your account and reset your password in your profile page thank you. Souq Market admins team."
                htmlMessage="<h1>Welcome "+companyName+" in Souq Market.</h1><br><h2><p>Hope you are enjoying your account with us.</p> Your password is:</h2><h1> " + password + "</h1> <h2><p>you can login to your account and reset your password in your profile page thank you.</p></h2> <h4>Souq Market admins team.</h4>"
                to = str(email)
                mail=EmailMultiAlternatives(subject,message,EMAIL_HOST_USER, [to])
                mail.attach_alternative(htmlMessage, "text/html")
                mail.send()
                return render(request,'core/login.html',{'message': 'You have successfully registered. Please check your email to get your password.'})

        else:
            return render(request, 'sellers/business_signup.html', {'error': 'Please check the recaptcha'})
    return render(request, 'sellers/business_signup.html',{})



def seller_home (request):
    return render(request, 'sellers/seller_home.html',{})
