from django.http import HttpResponse
from django.shortcuts import render, redirect
from trackApp.models import AuthUser
from trackApp.models import *

# Create your views here.

# def home(request):
#     return render(request, 'login.html') 

# def home(request):
#     if request.session._session:
#         user_id = request.session['user_id']
#         user = AuthUser.objects.filter(id=user_id)
#         return render(request, 'home.html', {'user':user})
#         print(user_id)
#     return render(request, 'login.html')

#     if not user.is_valid():
#         return render(request, 'login.html')

def index(request):
    if request.session._session:
        user_id = request.session['user_id']
        user = AuthUser.objects.filter(id=user_id)
        return render(request, 'home.html', {'user':user})
    return redirect('/login')

# def home(request):
#     if request.session._session:
#         user_id = request.session['id']
#         user = AuthUser.objects.filter(id=user_id)
#         return render(request, 'home.html', {'user':user})
#     return redirect('/login')