from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.shortcuts import render, redirect
from .forms import *
from .models import *
import django
from django.shortcuts import render
from .serializers import ScoreSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status, viewsets
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
django.utils.encoding.force_text = force_str


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


def error_404(request, exception):
    return render(request, 'competition_register/not-found.html')


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


@api_view(['GET', 'PUT', 'DELETE'])
def edit_items(request, id):
    try:
        score = Score.objects.get(pk=id)
    except Score.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ScoreSerializer(score)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ScoreSerializer(score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
    elif request.method == 'DELETE':
        score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.

# get


def user_list(request):
    context = {
        'user_list': NewUser.objects.all()
    }

    return render(request, "user_register/user_list.html", context)


@login_required
def dashboard(request):
    return render(request,
                  'login.html',)


def account_register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/register/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return render(request, 'account/register/register_email_confirm.html', {'form': registerForm})
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/register/account_register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = NewUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)
        return redirect('/')
    else:
        return render(request, 'account/register/activation_invalid.html')


def user_delete(request, id):
    user = NewUser.objects.get(pk=id)
    user.delete()
    return redirect('/user/list/')


def comp_list(request):
    context = {
        'comp_list': Competition.objects.all()
    }
    return render(request, "competition_register/comp_list.html", context)


@login_required
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
            comp = form.save()
            return redirect(f'/comp/success/{comp.id}')
        else:
            return render(request, "competition_register/comp_form.html", {'form': form}, {'comp_id': comp.id})


def score_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UserScore()
        else:
            score = Score.objects.get(pk=id)
            form = UserScore(instance=score)
        return render(request, "score_register/score_form.html", {'form': form})
    else:
        if id == 0:
            form = UserScore(request.POST)
        else:
            score = Score.objects.get(pk=id)
            form = UserScore(request.POST, instance=score)
        if form.is_valid():
            form.save()
            return redirect('/user/score/')
        else:
            return render(request, "score_register/score_form.html", {'form': form})


@login_required
def comp_delete(request, id):
    comp = Competition.objects.get(pk=id)
    comp.delete()
    return redirect('/account/comp/list/')


@login_required
def comp_test(request, ref):
    context = {
        'comp': Competition.objects.get(ref_code=f'{ref}')
    }
    try:
        return render(request, "competition_register/comp_test.html", context)
    except Competition.DoesNotExist:
        return render(request, "competition_register/not-found.html")


@login_required
def comp_success(request, id):
    context = {
        'comp': Competition.objects.get(pk=id)
    }
    try:
        return render(request, "competition_register/success.html", context)
    except Competition.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@login_required
def rule_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = RuleForm()
        else:
            rule = Rule.objects.get(pk=id)
            form = RuleForm(instance=rule)
        return render(request, "ruleset_register/rule_form.html", {'form': form})
    else:
        if id == 0:
            form = RuleForm(request.POST)
        else:
            rule = Rule.objects.get(pk=id)
            form = RuleForm(request.POST, instance=rule)
        if form.is_valid():
            form.save()
            return redirect('/ruleset/rule')
        return render(request, "ruleset_register/rule_form.html", {'form': form})


@login_required
def rule_list(request):

    return render(request, "home.html")


@login_required
def test(request):
    return render(request, 'test.html')


@login_required
def base(request):
    return render(request, 'base.html')


@login_required
def login(request):
    return render(request, 'login.html')


def home(request):
    context = {
        'light': Rule.objects.filter(ruleset_id=3),
        'full': Rule.objects.filter(ruleset_id=4),
    }
    return render(request, 'home.html', context)


@login_required
def lboard(request):
    context = {
        'score_list': Competition.objects.all()
    }
    return render(request, 'leaderboard.html', context)


@login_required
def score(request):
    return render(request, 'score.html')


@login_required
def submit(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UserScore()
        else:
            score = Score.objects.get(pk=id)
            form = UserScore(instance=score)
        return render(request, 'submit.html', {'form': form})
    else:
        if id == 0:
            form = UserScore(request.POST)
        else:
            score = Score.objects.get(pk=id)
            form = UserScore(request.POST, instance=score)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'submit.html', {"form": form})


def base1(request):
    return render(request, 'base1.html')


@login_required
def ruleset_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = RulesetForm()
        else:
            rs = Ruleset.objects.all(pk=id)
            form = Ruleset(instance=rs)
        return render(request, "ruleset_register/ruleset_form.html", {'form': form})
    else:
        if id == 0:
            form = RulesetForm(request.POST)
        else:
            rs = Ruleset.objects.get(pk=id)
            form = RulesetForm(instance=rs)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "ruleset_register/ruleset_form.html", {'form': form})
    