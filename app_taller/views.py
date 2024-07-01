from django.shortcuts import render

# Create your views here.


def index(request):
    context={}
    return render(request, 'app_taller/index.html', context)

def contacto(request):
    context={}
    return render(request, 'app_taller/contacto.html', context)