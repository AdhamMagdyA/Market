from django.shortcuts import redirect, render
from users.models import User
from products.models import Product
from django.contrib.auth.decorators import login_required

def index(request):
    id1=request.user.user_id
    cart = User.objects.get(user_id=id1).userCart
    data=cart.cartProducts.all()
    return render(request, 'carts/cart.html', {'data': data})

#@login_required (login_url='login')
def addToCart(request,id):
    try:
        userFound=User.objects.get(first_name=request.user)
    except:
        userFound=None
    print("user= "+str(request.user))
    if (userFound!=None):
        id1=request.user.user_id
        cart = User.objects.get(user_id=id1).userCart
        product = Product.objects.get(id=id)
        cart.cartProducts.add(product)
        cart.save()
        return redirect('cart')
    else:
        return redirect('login')
    
    
def removeFromCart(request,id):
    try:
        userFound=User.objects.get(first_name=request.user)
    except:
        userFound=None
    print("user= "+str(request.user))
    if (userFound!=None):
        id1=request.user.user_id
        cart = User.objects.get(user_id=id1).userCart
        product = Product.objects.get(id=id)
        cart.cartProducts.remove(product)
        cart.save()
        return redirect('cart')
    else:
        return redirect('login')

    