from operator import index
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from sellers.models import Seller
from .models import Category, Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    category = request.GET.get('category')
    if(category):
        products = Product.objects.filter(category_id=category)
    else:
        products = Product.objects.all()

    pages = Paginator(products, 3)
    pageNumber = request.GET.get('page')
    page = pages.get_page(pageNumber)
    return render(request, 'products/index.html', {'pages': pages, 'current_page': page})

def add(request):
    if request.method == 'POST':
        product = Product()
        product.productName = request.POST.get('prodtitle')
        product.productPrice = request.POST.get('prodPrice')
        product.productOldPrice = request.POST.get('prodOldPrice')
        product.productDiscription = request.POST.get('des')
        # get the correct category
        category_id = request.POST.get('prodCategory')
        category = Category.objects.get(id=category_id)
        print(category)
        product.category = category

        product.available = request.POST.get('prodAmount')
        # add product image
        product.productImage =request.FILES['upload']
        # add product seller
        seller = Seller.objects.filter(user_id=request.user.user_id)[0]
        product.productSeller = seller
        # initialize sold with 0
        product.sold = 0
        # initialize activition with false
        product.active = False
        product.save()
        return HttpResponse('<h1>Product added</h1>')
    categories = Category.objects.all()
    return render(request, 'products/add_product.html', {'categories': categories})

def get(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_details.html', {'product': product})
