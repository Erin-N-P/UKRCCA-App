from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.shortcuts import render
from .serializers import ScoreSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status, viewsets

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
        'Endpoint': '/score-post/',
        'method': 'PUT',
        'total_score': {'points': ""},
        'time_taken': {'time': ""},
        },
    ]
    return Response(routes)

@api_view(['POST'])
def add_items(request):
    score = ScoreSerializer(data=request.data)
 
    # validating for already existing data
    if Score.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if score.is_valid():
        score.save()
        return Response(score.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def insert_items(request):
    pass

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
        
def score_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ScoreForm()
        else:
            score = Score.objects.get(pk=id)
            form = ScoreForm(instance=score)
        return render(request, "score_register/score_form.html", {'form': form})
    else:
        if id == 0:
            form = ScoreForm(request.POST)
        else:
            score = Score.objects.get(pk=id)
            form = ScoreForm(request.POST, instance=score)
        if form.is_valid():
            form.save()
            return redirect('/user/score/')
        else:
            return render(request, "score_register/score_form.html", {'form': form})


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
