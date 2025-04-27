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
        # fazendo as validações
        if not first_name:
            messages.add_message(request, constants.WARNING, 'O nome não pode ser vazio!')
            return redirect('/accounts/register')
        if not surname:
            messages.add_message(request, constants.WARNING, 'O sobrenome não pode ser vazio!')
            return redirect('/accounts/register')
        if not email:
            messages.add_message(request, constants.WARNING, 'O email não pode ser vazio!')
            return redirect('/accounts/register')
        if password != confirm_password:
            messages.add_message(request, constants.WARNING, 'As senhas informadas não são iguais!')
            return redirect('/accounts/register')
        # verificando se existe algum usuário cadastrado com o e-mail
        user = CustomUser.objects.filter(email = email)
        if user:
            messages.add_message(request, constants.WARNING, 'Já existe um usuário cadastrado com esse e-mail!')
            return redirect('/accounts/register')
        # criando um novo usuário
        new_user = CustomUser.objects.create_user(
            first_name = first_name,
            surname = surname,
            email = email,
            password = password,
        )
        # salvando o usuário no banco de dados
        new_user.save()
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
        # fazendo as validações
        if not first_name:
            messages.add_message(request, constants.WARNING, 'O nome não pode ser vazio!')
            return redirect('/accounts/register')
        if not surname:
            messages.add_message(request, constants.WARNING, 'O sobrenome não pode ser vazio!')
            return redirect('/accounts/register')
        if not email:
            messages.add_message(request, constants.WARNING, 'O email não pode ser vazio!')
            return redirect('/accounts/register')
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