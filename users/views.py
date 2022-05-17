import imp
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render

from carts.models import Cart
from .models import User
from products.models import Category


from django.core.files.storage import FileSystemStorage

# Create your views here.



def signup (request):
    if request.method == 'POST' and request.FILES['upload']:
        firstName= request.POST.get('first_name')
        lastName= request.POST.get('last_name')
        email= request.POST.get('email')
        password= request.POST.get('password')
        # create new cart and assign it to the user
        userCart=Cart()
        userCart.save()
        # ch= request.POST.getList('choices')
        # print(ch)
        #if ch.lenght >0 :
         #preferedUserCategories=Category.objects.get(name=ch[0])
        fss=FileSystemStorage()
        # file = fss.save(upload.name, upload)
        data=User(first_name=firstName, last_name=lastName, email=email, password=password, userCart=userCart, userPhoto=request.FILES['upload'])
        data.save()
        return redirect('home')
    return render(request, 'users/user_signup_form.html',{})


def user_home (request):
    return render(request, 'users/user_home.html',{})




def admin_home (request):
    return render(request, 'users/admin_home.html',{})


















        # ch= request.POST.get('cb1')
        # ch1=Category.objects.contains(ch)
        # ch= request.POST.get('cb2')
        # ch= request.POST.get('cb3')

        # User.preferedUserCategories.get_object(id=ch1.id)


        # User.preferedUserCategories.append(ch1)
        # User.preferedUserCategories.append(ch2)
        # User.preferedUserCategories.append(ch3)
