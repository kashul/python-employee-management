from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate

# Create your views here.


def loging(request):
    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        try:
            userName = User.objects.get(email=email)
            user = authenticate(request, username=userName, password=password)

            if user is not None:
                login(request, user)

                return redirect('http://127.0.0.1:8000/log/home')
            else:

                messages.info(request, 'wrong password')
                return redirect('http://127.0.0.1:8000')

        except User.DoesNotExist:
            return redirect('http://127.0.0.1:8000')

    return render(request, 'log/log.html')


