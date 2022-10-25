from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('infos/', views.infos, name='infos'),
    path('home/', views.home, name='home'),
]