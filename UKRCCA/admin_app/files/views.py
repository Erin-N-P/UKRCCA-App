from django.shortcuts import render
from django.shortcuts import redirect

def files(request):
    return render(request, 'base.html')

def files(request):
    return render(request, 'compcre.html')

def files(request):
    return render(request, 'comps.html')

def files(request):
    return render(request, 'home.html')

def files(request):
    return render(request, 'leadb.html')

def files(request):
    return render(request, 'login.html')

def redirect_view(request):
    response = redirect('/home')
    return response