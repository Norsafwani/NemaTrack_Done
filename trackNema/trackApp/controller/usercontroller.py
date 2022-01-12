# Create your views here. where all the functions lies
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from trackApp.models import Nema, AuthUser
from django.shortcuts import redirect
from datetime import date, datetime
from trackApp.models import AuthUser, AuthPermission
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import logout, authenticate, login

def home(request):
    endclientlist = Nema.objects.all()
    # print('print this', product)
    content = {
        'endclientlist':endclientlist,
    }
    return render(request, 'home.html', content)

#Function for Login
def submit_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(password)
        log = AuthUser(username=username, password=password) 
        log = AuthenticationForm(data = request.POST)

        if log.is_valid():
            objUser = AuthUser.objects.get(username=username)
            # request.session['user_id'] = objUser.id
            # print(objUser.id)
            # return render(request, 'home.html') 
            return redirect ('home')
        else:
            return HttpResponse ('Wrong username or password')

#Function for Logout
def logout_nema(request):
    logout(request)
    return redirect('/')
    # return render(request, 'login.html') 