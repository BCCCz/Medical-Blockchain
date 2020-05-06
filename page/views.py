from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def index(request):
    return render(request, 'account/index.html')

def prevention(requset):
    return render(requset,'account/prevention.html')

def faqs(requset):
    return render(requset,'account/faqs.html')

