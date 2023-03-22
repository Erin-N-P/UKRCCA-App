from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .forms import UserLoginForm

# two routes for the user_form and user_list
urlpatterns = [
    # calling the functions from views
    # get and post req. for insert operations
    path('login/', auth_views.LoginView.as_view(template_name='account/register/login.html',
                                                form_class=UserLoginForm), name='auth-login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('register/', views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>)/',
         views.account_activate, name='activate'),
    path('home/', views.home, name='home'),
    path('score/', views.score_form, name='score_insert'),
    path('enter/', views.dashboard, name='login'),

    # get and post req. for update operations
    path('<int:id>/', views.account_register, name='user_update'),
    path('list/', views.user_list),  # get and retrieve req. to display data
    path('delete/<int:id>/', views.user_delete, name='user_delete'),
    path('comp/list/', views.comp_list, name='finn'),
    path('api-auth/', include('rest_framework.urls')),
    path(r'api/input/<int:id>/', views.edit_items, name='api'),
    path('comp/<int:id>/', views.comp_form, name='comp_update'),
    path('comp/delete/<int:id>/', views.comp_delete, name='comp_delete'),

]
