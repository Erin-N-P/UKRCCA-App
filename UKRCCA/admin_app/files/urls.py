from django.contrib import admin
from django.urls import path
from files import views
from django.conf import settings
from django.conf.urls.static import static
from .views import redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('competitions/', views.comps, name='comps'),
    path('leaderboard/', views.leadb, name='leadb'),
    path('create competition/', views.compcre, name='compcre'),
    path('base/', views.base, name='base'),
    path('/home', redirect_view)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)