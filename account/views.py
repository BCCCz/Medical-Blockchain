# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.urls import reverse
from django.template import loader
import requests
import base64
import json
import hashlib
from PIL import Image

ses = requests.session()
token = ""


def user_login(request):
    code_url = 'http://127.0.0.1:5001/WeBASE-Node-Manager/account/pictureCheckCode'
    r = requests.get(code_url)
    response = json.loads(r.text)
    base64Image = response['data']['base64Image']
    global token
    token = response['data']['token']
    img = 'data:image/png;base64,{0}'.format(base64Image)
    context = {
        "checkcode_img": img,
    }
    return render(request, "account/login.html", context)


def detail(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        checkcode = request.POST.get("checkcode")
        url = 'http://127.0.0.1:5001/WeBASE-Node-Manager/account/login?checkCode={0}&account={1}&accountPwd={2}'.format(checkcode, username, str(hashlib.sha256(password.encode("utf-8")).hexdigest()))
        headers = {'Content-type': 'application/json', 'token': token}

<<<<<<< HEAD
        r = ses.post(url, headers=headers)
        return HttpResponse(r.text)
=======
    r = ses.post(url, headers=headers)
    return render(request, "information/page.html")
>>>>>>> bc
