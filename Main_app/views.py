from django.shortcuts import render, redirect
from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.apps import apps
import sys
import os
from django.apps import apps
import numpy as np
# Create your views here.

class IndexView(APIView):
    states = {"lamp":"","fan":""}

    def get(self,request):
        return render(request, 'index.html')
    
    def post(self,request):
        data = request.data
        value = data["dados"]

        t = value.split("-")
        self.states[t[1]] = t[0]

        

        app_config = apps.get_app_config('Main_app')
        Settings = app_config.Settings()
        Integrations = app_config.Integrations(Settings.configs.ip)

        print(f"\n ==== NEW POST === \n {t} \n {Settings.configs}")
        print(f"\n {t[1]} IS {t[0]}")

        route_func ={
            "lamp":{
                "ON":Settings.configs.baseroute,
                "OFF":Settings.configs.baseroute
            },
            "fan":{
                "ON":Settings.configs.baseroute,
                "OFF":Settings.configs.baseroute
            }
        }

        

        cmd = Integrations.get(route_func[t[1]][t[0]])
        print(cmd)

        print(self.states)
        data = [self.states]

        if value:
            return render(request,'index.html',{"data":data})#{"trello_boards":boards}

class DocumentacaoView(APIView):
    def get(self,request):
        return render(request, 'documentacao.html')
    
class DashboardView(APIView):
    def get(self,request):
        return render(request, 'dashboard.html')
    
    def post(self,request):
        data = request.data
        value = data["dados"]
        print(value)

class LogsView(APIView):
    def get(self,request):

        with open('logs/django.log') as f:
            lines = f.readlines()
        
        text = [l.split("\n") for l in lines]
    
        return render(request, 'logs.html',{"data":text})
