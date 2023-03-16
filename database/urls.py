from django.urls import path, include
from . import views

# two routes for the user_form and user_list
urlpatterns = [
    # calling the functions from views
    # get and post req. for insert operations
    path('', views.user_form, name='user_insert'),
    path('score/', views.score_form, name='score_insert'),
    # get and post req. for update operations
    path('<int:id>/', views.user_form, name='user_update'),
    path('list/', views.user_list),  # get and retrieve req. to display data
    path('delete/<int:id>/', views.user_delete, name='user_delete'),
    path('comp/list/', views.comp_list),
    path('api-auth/', include('rest_framework.urls')),
    path(r'api/input/<int:id>/', views.edit_items, name='api'),
<<<<<<< HEAD
    path(r'comp/<str:code>/', views.comp_test, name='competition')
=======
>>>>>>> a779b3cc11b1f0644b24c7e8c23109e4b3c12388

]
