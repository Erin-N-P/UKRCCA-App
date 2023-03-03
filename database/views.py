from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

# get


def user_list(request):
    context = {
        'user_list': NewUser.objects.all()
    }

    return render(request, "user_register/user_list.html", context)

# put and post request // insert and update


def user_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else:
            # i thought pk was just a variable name but no, it has to be pk
            user = NewUser.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(request, "user_register/user_form.html", {'form': form})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = NewUser.objects.get(pk=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/user/list')
        else:
            return render(request, "user_register/user_form.html", {'form':form})
# delete request


def user_delete(request, id):
    user = NewUser.objects.get(pk=id)
    user.delete()
    return redirect('/user/list/')


def comp_list(request):
    context = {
        'comp_list': Competition.objects.all()
    }
    return render(request, "competition_register/comp_list.html", context)


def comp_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CompetitionForm()
        else:
            comp = Competition.objects.get(pk=id)
            form = CompetitionForm(instance=comp)
        return render(request, "competition_register/comp_form.html", {'form': form})
    else:
        if id == 0:
            form = CompetitionForm(request.POST)
        else:
            comp = Competition.objects.get(pk=id)
            form = CompetitionForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
            return redirect('/user/comp/list/')
        else:
            return render(request, "competition_register/comp_form.html", {'form': form})


def comp_delete(id):
    comp = Competition.objects.all(pk=id)
    comp.delete()
    return redirect('/user/comp/list/')


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


def base1(request):
    return render(request, 'base1.html')
