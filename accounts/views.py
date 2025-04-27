from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import auth
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def login(request):
    # verificando se existe algum usuário logado
    if request.user.is_authenticated:
        return redirect('/plataform/home')
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email:
            messages.add_message(request, constants.WARNING, 'O e-mail deve ser preenchido!')
            return redirect('/accounts/login')
        if not password:
            messages.add_message(request, constants.WARNING, 'A senha deve ser preenchida!')
            return redirect('/accounts/login')
        user = auth.authenticate(request, email = email, password = password)
        print(user)
        if user:
            auth.login(request, user)
            return redirect('/plataform/home')
        else:
            messages.add_message(request, constants.WARNING, message='E-mail ou senha inválidos!')
            return render(request, 'login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            pass
        user = CustomUser.objects.create_user(
            first_name = first_name,
            surname = surname,
            email = email,
            password = password,
        )
        user.save()
        messages.add_message(request, constants.SUCCESS, 'Conta criada com sucesso!')
        return redirect('/accounts/register')


def logout(request):
    auth.logout(request)
    return redirect('/accounts/login')


def profile(request):
    if request.method == 'GET':
        return render(request, 'profile.html')
    else:
        first_name = request.POST.get('first_name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password')
        if password != confirm_password:
            messages.add_message(request, constants.WARNING, 'As senhas informadas não são iguais!')
            return redirect('/account/profile')
        # obtendo o usuário logado
        user = request.user
        # alterando os dados do usuário logado
        user.first_name = first_name
        user.surname = surname
        user.email = email
        user.set_password(password)
        user.save()
        # mantendo o usuário logado
        auth.update_session_auth_hash(request, user)
        # redirecionando o usuário para o template profile
        return redirect('/accounts/profile')