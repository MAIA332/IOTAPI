from django.urls import path
from django.shortcuts import render, redirect
from .views import *
from django.views.generic import RedirectView

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('docs', DocumentacaoView.as_view(), name="docs"),
    path('home', RedirectView.as_view(url='/fecaf/')),
    path('dash', DashboardView.as_view(),name='dash'),
    path('logs', LogsView.as_view(),name='logs'),
]