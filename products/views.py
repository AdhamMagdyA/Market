
from operator import index
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products = Product.objects.all()
    pages = Paginator(products, 3)
    pageNumber = request.GET.get('page')
    page = pages.get_page(pageNumber)
    return render(request, 'products/index.html', {'pages': pages, 'current_page': page})

def add(request):
    return render(request, 'products/add_product.html')

def get(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_details.html', {'product': product})
