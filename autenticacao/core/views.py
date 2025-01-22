from django.shortcuts import render, redirect
from .forms import UsuarioCriarForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')


def registro(request):
    form = UsuarioCriarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    context = {
        'form': form
    }
    return render(request, 'registro.html', context)

def autenticar(request):
    if request.POST:
        usuario = request.POST ["usuario"]
        senha = request.POST ["senha"]
        user = authenticate(request, username = usuario, password = senha)
        if user is not None:
            login(request,user)
            return redirect ("perfil")
        else:
            return render (request, 'login.html')
    else:  
        return render (request, 'login.html')
    