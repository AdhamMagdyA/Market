
from email.errors import FirstHeaderLineIsContinuationDefect
from django.conf import settings
from django.shortcuts import render
from carts.models import Cart
from core.models import Authorization
from .models import User
from sellers.models import Seller
from products.models import Category,Product
from market.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

# Create your views here.

# couldn't make it work :"(
class AdminCharts(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        print('here 1')
        
        usersCount=User.objects.filter(userAuth =Authorization.objects.get(auth_name="user")).count()
        adminsCount=User.objects.filter(userAuth =Authorization.objects.get(auth_name="admin")).count()
        sellerCount=Seller.objects.filter(userAuth=Authorization.objects.get(auth_name="seller")).count()

        

        # Second Chart , Favorate Category for Customers
        soldFood=0
        soldToys=0
        soldKidswear=0
        soldMenswear=0
        soldWomenswear=0
        soldElectronics=0
        soldLaptops=0
        soldPhones=0
        soldFurniture=0
        soldKitchen=0

        products =serializers.serialize( "python", Category.objects.all() )
        # for cat in categories:
        #     print(cat)

        # for pro in products:
        #     print(pro['fields'].get('sold')) 

        for pro in products:
            if pro['fields'].get('category')==11:
                soldFood=soldFood+pro['fields'].get('sold')
            elif pro['fields'].get('category')==10: 
                soldToys=soldToys+pro['fields'].get('sold')
            elif pro['fields'].get('category')==9:
                soldKidswear=soldKidswear+pro['fields'].get('sold')
            elif pro['fields'].get('category')==8:
                soldMenswear=soldMenswear+pro['fields'].get('sold')
            elif pro['fields'].get('category')==7:
                soldWomenswear=soldWomenswear+pro['fields'].get('sold')
            elif pro['fields'].get('category')==6:
                soldElectronics=soldElectronics+pro['fields'].get('sold')
            elif pro['fields'].get('category')==5:
                soldLaptops=soldLaptops+pro['fields'].get('sold')
            elif pro['fields'].get('category')==4:
                soldPhones=soldPhones+pro['fields'].get('sold')
            elif pro['fields'].get('category')==3:
                soldFurniture=soldFurniture+pro['fields'].get('sold')
            elif pro['fields'].get('category')==2:
                soldKitchen=soldKitchen+pro['fields'].get('sold')
                


        categoryLables=["Food","Toys","Kidswear","Menswear","Womenswear","Electronics","Laptops","Phones","Furniture","Kitchen"]

        numCatSoldItems=[soldFood,soldToys,soldKidswear,soldMenswear,soldWomenswear,soldElectronics,soldLaptops,soldPhones,soldFurniture,soldKitchen]

        
        adminChartsData={
            'usersCount':usersCount,
            'adminsCount':adminsCount,
            'sellersCount':sellerCount,
            'categoryLables':categoryLables,
            'numCatSoldItems':numCatSoldItems

        }
        print ("form adminsCharts",adminChartsData)
        return Response(adminChartsData)



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
    #first chart , our different users number
    usersNum=User.objects.filter(userAuth =Authorization.objects.get(auth_name="user")).count()
    adminsNum=User.objects.filter(userAuth =Authorization.objects.get(auth_name="admin")).count()
    sellerNum=Seller.objects.filter(userAuth=Authorization.objects.get(auth_name="seller")).count()


    # Second Chart , Favorate Category for Customers
    soldFood=0
    soldToys=0
    soldKidswear=0
    soldMenswear=0
    soldWomenswear=0
    soldElectronics=0
    soldLaptops=0
    soldPhones=0
    soldFurniture=0
    soldKitchen=0
    
    products = serializers.serialize( "python", Product.objects.all() )

    categories =serializers.serialize( "python", Category.objects.all() )
    # for cat in categories:
    #     print(cat)

    # for pro in products:
    #     print(pro['fields'].get('sold')) 

    for pro in products:
        if pro['fields'].get('category')==11:
            soldFood=soldFood+pro['fields'].get('sold')
        elif pro['fields'].get('category')==10: 
            soldToys=soldToys+pro['fields'].get('sold')
        elif pro['fields'].get('category')==9:
            soldKidswear=soldKidswear+pro['fields'].get('sold')
        elif pro['fields'].get('category')==8:
            soldMenswear=soldMenswear+pro['fields'].get('sold')
        elif pro['fields'].get('category')==7:
            soldWomenswear=soldWomenswear+pro['fields'].get('sold')
        elif pro['fields'].get('category')==6:
            soldElectronics=soldElectronics+pro['fields'].get('sold')
        elif pro['fields'].get('category')==5:
            soldLaptops=soldLaptops+pro['fields'].get('sold')
        elif pro['fields'].get('category')==4:
            soldPhones=soldPhones+pro['fields'].get('sold')
        elif pro['fields'].get('category')==3:
            soldFurniture=soldFurniture+pro['fields'].get('sold')
        elif pro['fields'].get('category')==2:
            soldKitchen=soldKitchen+pro['fields'].get('sold')
        


    # categoryLables=["Food","Toys","Kidswear","Menswear","Womenswear","Electronics","Laptops","Phones","Furniture","Kitchen"]

    # numCatSoldItems=[soldFood,soldToys,soldKidswear,soldMenswear,soldWomenswear,soldElectronics,soldLaptops,soldPhones,soldFurniture,soldKitchen]

    adminHomeContext={
        'usersNum':usersNum,
        'adminsNum':adminsNum,
        'sellersNum':sellerNum,

        'soldFood':soldFood,
        'soldToys':soldToys,
        'soldKidswear':soldKidswear,
        'soldMenswear':soldMenswear,
        'soldWomenswear':soldWomenswear,
        'soldElectronics':soldElectronics,
        'soldLaptops':soldLaptops,
        'soldPhones':soldPhones,
        'soldFurniture':soldFurniture,
        'soldKitchen':soldKitchen

        # 'categoryLables':categoryLables,
        # 'numCatSoldItems':numCatSoldItems
    }
    print ("from admin_home : ",adminHomeContext)
    return render(request, 'admins/admin_home.html',adminHomeContext)


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
