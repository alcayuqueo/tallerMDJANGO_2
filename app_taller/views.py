from django.shortcuts import render

# Create your views here.


def index(request):
    context={}
    return render(request, 'app_taller/index.html', context)

def register(request):
    context={}
    return render(request, 'app_taller/register.html', context)

def login(request):
    context={}
    return render(request, 'app_taller/login.html', context)

def productos(request):
    context={}
    return render(request, 'app_taller/productos.html', context)

def contacto(request):
    context={}
    return render(request, 'app_taller/contacto.html', context)

def quienessomos(request):
    context={}
    return render(request, 'app_taller/quienessomos.html', context)