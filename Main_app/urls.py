from django.urls import path
from django.shortcuts import render, redirect
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="home")
]