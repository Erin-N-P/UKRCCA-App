from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render
from files.models import NewUser
from files.forms import MyForm

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
    return render(request, 'submit.html')

def base(request):
    return render(request, 'base.html')

def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'submit.html', {'form': form})