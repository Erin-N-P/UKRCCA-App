from django.shortcuts import render
from .forms import UserForm

# Create your views here.

# get
def user_list(request):
    return render(request, "user_register/user_list.html")

# put and post request // insert and update
def user_form(request):
    form = UserForm()
    return render(request, "user_register/user_form.html", {'form':form})

# delete request
def user_delete(request):
    return