"""UKRCCA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from files import views
from django.conf import settings
from django.conf.urls.static import static
from .views import redirect_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test, name='test'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('leaderboard/', views.lboard, name='lboard'),
    path('scorecard/', views.score, name='score'),
    path('submit/', views.submit, name='submit'),
    path('base/', views.base, name='base'),
    path('', redirect_view),
    path('', views.user_form, name='user_insert'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
