from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.index,name='index'),
    path('index', views.index,name='index'),
    path('register', views.register,name='index'),
]
