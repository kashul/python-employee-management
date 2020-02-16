from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000')

    else:
        return render(request, 'home/home.html')


def logoutapp(request):
    logout(request)

    return redirect('http://127.0.0.1:8000')
