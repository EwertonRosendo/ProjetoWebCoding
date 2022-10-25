from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        email = request.POST.get('email_cadastro')
        senha1 = request.POST.get('password_cadastro1')
        senha2 = request.POST.get('password_cadastro2')

        user = User.objects.filter(username=email).first()
        if (user) or (senha1!=senha2):
            return HttpResponse("Usuario já existe ou as senhas não são iguais")

        user = User.objects.create_user(username=email, password=senha1)
        user.save()
        return redirect('login')
    else:
        return HttpResponse("DEU MERDA NA VIEW DE CADASTRO")

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        email = request.POST.get("email_login")
        senha = request.POST.get("senha_login")

        user = authenticate(username=email, password=senha)

        if user:
            django_login(request, user)
            return redirect('kaka')
        else:
            return HttpResponse("EMAIL OU SENHA INVALIDOS")
    else:
        return HttpResponse("DEU MERDA NA VIEW DE LOGIN ")

def infos(request):
    return render(request, 'infos.html')

def  home(request):
    return render(request, 'home.html')