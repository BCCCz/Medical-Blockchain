import requests
import base64
import json
import hashlib
from PIL import Image

ses = requests.session()


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    checkcode = request.POST.get("checkcode")
    code_url = 'http://127.0.0.1:5001/WeBASE-Node-Manager/account/pictureCheckCode'
    r = requests.get(code_url)
    response = json.loads(r.text)
    base64Image = response['data']['base64Image']
    token = response['data']['token']
    imagedata = base64.b64decode(base64Image)

    url = 'http://127.0.0.1:5001/WeBASE-Node-Manager/account/login?checkcode={0}&account={1}&accountPwd={2}'.format(
        checkcode, username, str(hashlib.sha256(password.encode("utf-8")).hexdigest()))
    headers = {'Content-type': 'application/json', 'token': token}

    r = ses.post(url, headers=headers)
    if 'success' in r.text:
        return HttpResponse('success')
