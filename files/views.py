from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, "test.html")

def logIn(request):
    return render(request, "logIn.html")

def base(request):
    return render(request, "base.html")

def home(request):
    return render(request, "home.html")

def score(request):
    return render(request, "score.html")    

def lboard(request):
    return render(request, "leaderboard.html")

def submit(request):
    return render(request, "submit.html")