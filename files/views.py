from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, "test.html")

def logIn(request):
    return render(request, "logIn.html")

def base(request):
    return render(request, "base.html")

def lboard(request):
    return render(request, "leaderboard.html")

def submit(request):
    return render(request, "submit.html")