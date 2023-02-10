from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.

# get
def user_list(request):
    return render(request, "user_register/user_list.html")

# put and post request // insert and update
def user_form(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, "user_register/user_form.html", {'form':form})
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/list')
# delete request
def user_delete(request):
    return