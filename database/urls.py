from django.urls import path, include
from . import views

# two routes for the user_form and user_list
urlpatterns = [

    # calling the functions from views
    path('', views.user_list), # localhost:{portnumber}/user/form
    path('list/', views.user_list) # localhost:{portnumber}/user/list
]