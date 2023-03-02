from django.urls import path, include
from . import views

# two routes for the user_form and user_list
urlpatterns = [
    # calling the functions from views
    # get and post req. for insert operations
    path('', views.user_form, name='user_insert'),
    # get and post req. for update operations
    path('<int:id>/', views.user_form, name='user_update'),
    path('list/', views.user_list),  # get and retrieve req. to display data
    path('delete/<int:id>/', views.user_delete, name='user_delete'),
    path('comp/', views.comp_form, name='comp_insert'),
    path('comp/list/', views.comp_list),
    path('test/', views.test, name='test'),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('leaderboard/', views.lboard, name='lboard'),
    path('scorecard/', views.score, name='score'),
    path('submit/', views.submit, name='submit'),
    path('base/', views.base, name='base'),
]
