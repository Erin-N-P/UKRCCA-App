from django.shortcuts import render, redirect
from .forms import UserForm
from .models import NewUser

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
            user = NewUser.objects.get(pk=id) # i thought pk was just a variable name but no, it has to be pk
            form = UserForm(instance=user)
        return render(request, "user_register/user_form.html", {'form':form})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = NewUser.objects.get(pk=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/user/list')
# delete request
def user_delete(request, id):
    user = NewUser.objects.get(pk=id)
    user.delete()
    return redirect('/user/list/')