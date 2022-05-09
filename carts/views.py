from django.shortcuts import render

# Create your views here.
def get(request):
    return render(request, 'carts/cart.html')