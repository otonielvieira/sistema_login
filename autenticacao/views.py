from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('plataforma/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        usuario = auth.authenticate(username=username, password=senha)


        if not usuario:
            return redirect('erro5')
        else:
            auth.login(request, usuario)
            return redirect('plataforma/')

        #return HttpResponse(f'<h1 style="text-align:center;color:grey;">Bem-vindo à àrea restrita {email}<h1>')



def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('plataforma/') #obs retirar esse if se for cadastrar so logado e colocar a permissao so pra logado
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

        if not senha == confirmar_senha:
            return redirect('erro')
        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            return redirect('erro2')

        user = User.objects.filter(username=username)

        if user.exists():
            return redirect('erro3')

        try:
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.save()
            return redirect('login')
        except:
            return redirect('erro4')

        #return HttpResponse(f'<h1 style="text-align:center;color:grey;">Bem-vindo à àrea restrita {username}<h1>')


def erro(request):
    return render(request, 'erro.html')

def erro2(request):
    return render(request, 'erro2.html')

def erro3(request):
    return render(request, 'erro3.html')

def erro4(request):
    return render(request, 'erro4.html')

def erro5(request):
    return render(request, 'erro5.html')

def sair(request):
    auth.logout(request)
    return redirect('login')
