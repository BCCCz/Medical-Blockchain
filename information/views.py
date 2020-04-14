from django.shortcuts import render
from django.http import HttpResponse
import requests
import base64
import json
import hashlib
from account.views import ses


def initpage(request):
    return render(request, "information/accountinit.html")

def initdetail(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    idCard = request.POST.get('idCard')
    age = request.POST.get('age')
    tel = request.POST.get('tel')

    return HttpResponse('a')


