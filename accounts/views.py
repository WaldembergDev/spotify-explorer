from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import auth
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(request, email = email, password = password)
        if user:
            auth.login(request, user)
            redirect('/plataform/home')
        else:
            messages.add_message(request, constants.WARNING, message='E-mail ou senha inválidos!')
            return render(request, 'login.html')
            
