"""Определяет схемы URL для пользователей"""
from django.urls import path
from . import views

urlpatterns = [
    # Включить URL авторизации по умолчанию.
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]