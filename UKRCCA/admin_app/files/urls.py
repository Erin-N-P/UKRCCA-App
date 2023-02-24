from django.urls import path
from .views import HomePageView, CompCrePageView, CompsPageView, LeadBPageView, LoginPageView

urlpatterns = [
    path('', LoginPageView.as_view(), name='login'),
    path('home/', HomePageView.as_view(), name='home'),
    path('comps/', CompsPageView.as_view(), name='comps'),
    path('compcre/', CompCrePageView.as_view(), name='compcre'),
    path('leadb/', LeadBPageView.as_view(), name='leadb')
]