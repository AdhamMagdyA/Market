from django.shortcuts import render

# Create your views here.
def userHome(request):
    return render(request, 'core/user_home.html')