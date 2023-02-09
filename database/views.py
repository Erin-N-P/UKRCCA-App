from django.shortcuts import render

# Create your views here.

# get
def user_list(request):
    return render(request, "user_register/user_list.html")

# put and post request // insert and update
def user_form(request):
    return render(request, "user_register/user_form.html")

# delete request
def user_delete(request):
    return