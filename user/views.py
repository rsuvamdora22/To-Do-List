from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login  , logout

# Create your views here.
def dora(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')

            user = User.objects.create(username = username, email = email)

            user.set_password(password)
            user.save()
            return redirect('login')
        
    else:
        form = Register()
    return render(request,'register.html',{'form':form})  


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Credentials')
        else:
            auth_login(request, user)
            return redirect('list/main')

    return render(request, 'login.html')
      


def log_out(request):
    logout(request)
    return redirect('login')
