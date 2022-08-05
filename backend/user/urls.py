from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('index/',index),
    path('register/',register, name= "api-register"),
    path('userList/',UserList, name = "api-userList"),
    path('newsList/',NewsList, name = 'api-newsList'),
]
