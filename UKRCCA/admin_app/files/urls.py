from django.urls import path
from .views import HomePageView, CompCrePageView, CompsPageView, LeadBPageView, LoginPageView

urlpatterns = [
    path('', LoginPageView.as_view(), name='login'),
    path('home/', HomePageView.as_view(), name='home'),
    path('comps/', CompsPageView.as_view(), name='comps'),
    path('compcre/', CompCrePageView.as_view(), name='compcre'),
    path('leadb/', LeadBPageView.as_view(), name='leadb'),
        path('rules/', RulesPageView.as_view(), name='rules'),
    path('lightrules/', LightRulesPageView.as_view(), name='lightrules'),
    path('heavyrules/', HeavyRulesPageView.as_view, name='heavyrules')
]