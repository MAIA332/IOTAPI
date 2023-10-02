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

        print(t)
        print(self.states)
        data = [self.states]

        if value:
            return render(request,'index.html',{"data":data})#{"trello_boards":boards}

class DocumentacaoView(APIView):
    def get(self,request):
        return render(request, 'documentacao.html')