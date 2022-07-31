from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='home'),
    path('login/', views.login, name='home'),
    path('explore/', views.explore, name='home'),
]