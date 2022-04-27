
from operator import index
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def add(request):
    return render(request, 'products/add_product.html')

def get(request):
    return render(request, 'products/product_details.html')
