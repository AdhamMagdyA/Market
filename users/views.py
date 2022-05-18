import imp
from multiprocessing import context
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from carts.models import Cart
from core.models import Authorization
from .models import User
from products.models import Category


from django.core.files.storage import FileSystemStorage

# Create your views here.



def signup (request):
    #check if recaptcha was validated
    if request.method == 'POST':
        recaptcha = request.POST.get('g-recaptcha-response')
        if recaptcha: 
            if request.FILES['upload']:
                firstName= request.POST.get('first_name')
                lastName= request.POST.get('last_name')
                email= request.POST.get('email')
                password= request.POST.get('password')
                # create new cart and assign it to the user
                userCart=Cart()
                userCart.save()
                type=Authorization.objects.get(auth_name="user")
                data=User(first_name=firstName, last_name=lastName, email=email, password=password, userCart=userCart, userPhoto=request.FILES['upload'], userAuth=type)
                data.save()
                return redirect('login')
        else:
            print("recaptcha not validated")
            return render(request, 'users/user_signup_form.html', {'error': 'Please check the recaptcha'})
    return render(request, 'users/user_signup_form.html')


def user_home (request):
    return render(request, 'users/user_home.html',{})




def admin_home (request):
    return render(request, 'admins/admin_home.html',{})

















        
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
