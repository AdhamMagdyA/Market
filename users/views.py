from cgitb import strong
import imp
from multiprocessing import context
from unicodedata import name
from urllib import request
from django.conf import settings
from django.shortcuts import redirect, render
from carts.models import Cart
from core.models import Authorization
from .models import User
from products.models import Category
from market.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
from django.core.files.storage import FileSystemStorage

# Create your views here.

def generateRondamPassword():
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


def signup (request):
    #check if recaptcha was validated
    if request.method == 'POST':
        recaptcha = request.POST.get('g-recaptcha-response')
        if recaptcha: 
            if request.FILES['upload']:
                firstName= request.POST.get('first_name')
                lastName= request.POST.get('last_name')
                email= request.POST.get('email')
                password= generateRondamPassword()
                # create new cart and assign it to the user
                userCart=Cart()
                userCart.save()
                type=Authorization.objects.get(auth_name="user")
                data=User(first_name=firstName, last_name=lastName, email=email, password=password, userCart=userCart, userPhoto=request.FILES['upload'], userAuth=type)
                data.save()
                #send email to the user
                subject = 'Welcome '+firstName+' in Souq Market'
                message = 'Hope you are enjoying your account with us. Your password is: ' + password + " you can login to your account and reset your password in your profile page thank you. Souq Market admins team."
                htmlMessage="<h1>Welcome "+firstName+" in Souq Market.</h1><br><h2><p>Hope you are enjoying your account with us.</p> Your password is:</h2><h1> " + password + "</h1> <h2><p>you can login to your account and reset your password in your profile page thank you.</p></h2> <h4>Souq Market admins team.</h4>"
                to = str(email)
                mail=EmailMultiAlternatives(subject,message,EMAIL_HOST_USER, [to])
                mail.attach_alternative(htmlMessage, "text/html")
                mail.send()
                return render(request,'core/login.html',{'message': 'You have successfully registered. Please check your email to get your password.'})

        else:
            return render(request, 'users/user_signup_form.html', {'error': 'Please check the recaptcha'})
    return render(request, 'users/user_signup_form.html')


def user_home (request):
    return render(request, 'users/user_home.html',{})




def admin_home (request):
    return render(request, 'admins/admin_home.html',{})

def admin_profile (request):
    return render(request, 'admins/admin_profile.html',{})

def admin_profile_edit (request):
    return render(request, 'admins/admin_profile_edit.html',{})
















        
        # ch= request.POST.getList('choices')
        # print(ch)
        #if ch.lenght >0 :
        #preferedUserCategories=Category.objects.get(name=ch[0])

        # ch= request.POST.get('cb1')
        # ch1=Category.objects.contains(ch)
        # ch= request.POST.get('cb2')
        # ch= request.POST.get('cb3')

        # User.preferedUserCategories.get_object(id=ch1.id)


        # User.preferedUserCategories.append(ch1)
        # User.preferedUserCategories.append(ch2)
        # User.preferedUserCategories.append(ch3)
