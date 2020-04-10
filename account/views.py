# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
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


def user_login(request):
    code_url = 'http://127.0.0.1:5001/WeBASE-Node-Manager/account/pictureCheckCode'
    r = requests.get(code_url)
    response = json.loads(r.text)
    base64Image = response['data']['base64Image']
    img = 'data:image/png;base64,{0}'.format(base64Image)
    context = {
        "checkcode_img":img,
    }
    token = response['data']['token']

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        checkcode = request.POST.get("checkcode")
        url = 'http://127.0.0.1:5001/WeBASE-Node-Manager/account/login?checkcode={0}&account={1}&accountPwd={2}'.format(checkcode, username, str(hashlib.sha256(password.encode("utf-8")).hexdigest()))
        headers = {'Content-type': 'application/json', 'token': token}

        r = ses.request(url, headers=headers)
        if 'success' in r.text:
            return HttpResponse('success')
        else:
            return render(request, "account/login.html", context)

    return render(request, "account/login.html", context)