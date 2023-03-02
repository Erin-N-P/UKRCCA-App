from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import createUser


# Create your views here.

def test(request):
    return render(request, 'test.html')


def base(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def lboard(request):
    return render(request, 'leaderboard.html')


def score(request):
    return render(request, 'score.html')


def submit(request):
    form = createUser()
    return render(request, 'submit.html', {"form": form})


def base(request):
    return render(request, 'base.html')
