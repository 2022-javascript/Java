from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('index/',index),
    path('register/',register, name= "api-register"),
    path('userList/',UserList, name = "api-userList"),
    path('newsList/',NewsList, name = 'api-newsList'),
    path('UserInfoList/',UserInfoList, name='api-UserInfoList'),
    path('UserInfoPost/',UserInfoPost, name='api-UserInfoPost'),
    path('LastLogin/<str:pk>/',UpdateLastLogin, name='api-LastLogin'),
    path('AIData/',AIData, name='api-AIData'),
    path('Trade_data/',Trade, name='api-trade'),
]
