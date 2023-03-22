"""ukrcca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from database import views
from database.views import ScoreViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'input', ScoreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('database.urls')),
    path('api/', include(router.urls), name='api'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('test/', views.test, name='test'),
    path('home/', views.home, name='home'),
    path('leaderboard/', views.lboard, name='lboard'),
    path('scorecard/', views.score, name='score'),
    path('submit/', views.submit, name='submit'),
    path('base/', views.base, name='base'),
    path('ruleset/', views.ruleset_form, name='ruleset'),
    path('ruleset/rule', views.rule_form, name='rule'),
    path('comp/', views.comp_form, name='comp_insert'),
    path('comp/<str:ref>/', views.comp_test, name='competition'),
    path('comp/success/<int:id>/', views.comp_success, name='comp_success'),

]
