import imp
from django.http import HttpRequest
from django.shortcuts import redirect




# def unauthenticated_user(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.user.authenticated:
#             return redirect('home')
#         else:
#             return view_func(request, *args, **kwargs)
#     return wrapper_func