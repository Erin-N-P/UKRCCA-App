from django.urls import path, include
from . import views

# two routes for the user_form and user_list
urlpatterns = [
    # calling the functions from views
    path('', views.user_form, name = 'user_insert'), # get and post req. for insert operations
    path('<int:id>/', views.user_form, name = 'user_update'), # get and post req. for update operations
    path('list/', views.user_list), # get and retrieve req. to display data
    path('delete/<int:id>/', views.user_delete, name = 'user_delete'),
    path('comp/', views.comp_form, name = 'comp_insert'),
    path('comp/list/', views.comp_list)
]