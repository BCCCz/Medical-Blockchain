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

    url = 'http://127.0.0.1:5002/WeBASE-Front/trans/handle'
    headers = {
        'Content-type': 'application/json',
    }
    data = {
        "useAes": "false",
        "user": "700001",
        "contractName": "Medical",
        "contractAddress": "0xfd0b769192f5a75bbf4f007bcb03a4ad654442e5",
        "funcName": "accountInit",
        "contractAbi":[{"constant":"false","inputs":[{"name":"id","type":"uint64"},{"name":"age","type":"int256"},{"name":"tel","type":"uint64"}],"name":"accountUpdate","outputs":[{"name":"","type":"int256"}],"payable":"false","stateMutability":"nonpayable","type":"function"},{"constant":"false","inputs":[{"name":"id","type":"uint64"},{"name":"times","type":"uint64"}],"name":"medicalQuery","outputs":[{"name":"","type":"uint64"},{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"uint64"}],"payable":"false","stateMutability":"nonpayable","type":"function"},{"constant":"false","inputs":[{"name":"id","type":"uint64"},{"name":"time","type":"uint64"},{"name":"place","type":"string"},{"name":"info","type":"string"},{"name":"timeStamp","type":"uint64"}],"name":"medicalRecord","outputs":[{"name":"","type":"int256"}],"payable":"false","stateMutability":"nonpayable","type":"function"},{"constant":"false","inputs":[{"name":"id","type":"uint64"}],"name":"accountQuery","outputs":[{"name":"","type":"uint64"},{"name":"","type":"string"},{"name":"","type":"string"},{"name":"","type":"uint64"},{"name":"","type":"int256"},{"name":"","type":"uint64"},{"name":"","type":"int256"}],"payable":"false","stateMutability":"nonpayable","type":"function"},{"constant":"false","inputs":[{"name":"id","type":"uint64"},{"name":"name","type":"string"},{"name":"sex","type":"string"},{"name":"idCard","type":"uint64"},{"name":"age","type":"int256"},{"name":"tel","type":"uint64"}],"name":"accountInit","outputs":[{"name":"","type":"int256"}],"payable":"false","stateMutability":"nonpayable","type":"function"},{"anonymous":"false","inputs":[{"indexed":"false","name":"id","type":"uint64"},{"indexed":"false","name":"name","type":"string"},{"indexed":"false","name":"sex","type":"string"},{"indexed":"false","name":"idCard","type":"uint64"},{"indexed":"false","name":"age","type":"int256"},{"indexed":"false","name":"tel","type":"uint64"}],"name":"accountInitEvent","type":"event"},{"anonymous":"false","inputs":[{"indexed":"false","name":"id","type":"uint64"},{"indexed":"false","name":"age","type":"int256"},{"indexed":"false","name":"tel","type":"uint64"}],"name":"accountUpdateEvent","type":"event"},{"anonymous":"false","inputs":[{"indexed":"false","name":"id","type":"uint64"},{"indexed":"false","name":"time","type":"uint64"},{"indexed":"false","name":"place","type":"string"},{"indexed":"false","name":"info","type":"string"},{"indexed":"false","name":"timeStamp","type":"uint64"}],"name":"medicalRecordEvent","type":"event"}],
        "funcParam":[str(id),str(name),str(sex),str(idCard),str(age),str(tel)],
        "groupId": "1",
        'user': "0x67b945032e20d6f9041a68e989275ba67870fb9f"
    }
    r = requests.post(url, json=data, headers=headers)
    return HttpResponse(r.text)


