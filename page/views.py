from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.


def homepage(request):
    return render(request, 'account/homepage.html')
