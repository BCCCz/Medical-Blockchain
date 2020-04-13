from django.shortcuts import render
from django.http import HttpResponse
import requests
import base64
import json
import hashlib


def accountinit(request):
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
        "funcParam":["request.POST.get('id')","request.POST.get('name')","request.POST.get('sex')",
                     "request.POST.get('idCard')","request.POST.get('age')","request.POST.get('tel')"],
        "groupId": "1",
        'user': "0xd8904921a83ffe1b77b48873eca0f7948a4e8333"
    }
    r = requests.post(url,json=data,headers=headers)
    return render(request,"information/accountInit.html")

def accountupdate(request):
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
        "funcParam":["request.POST.get('id')","request.POST.get('age')","request.POST.get('tel')"],
        "groupId": "1",
        'user': "0xd8904921a83ffe1b77b48873eca0f7948a4e8333"
    }
    r = requests.post(url,json=data,headers=headers)
    return render(request,"information/accountUpdate.html")

def accountquery(request):
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
        "funcParam":["request.POST.get('id')"],
        "groupId": "1",
        'user': "0xd8904921a83ffe1b77b48873eca0f7948a4e8333"
    }
    r = requests.post(url,json=data,headers=headers)
    return render(request,"information/accountQuery.html")


def medicalrecord(request):
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
        "funcParam":["request.POST.get('id')","request.POST.get('time')","request.POST.get('place')",
                     "request.POST.get('info')","request.POST.get('timeStamp')"],
        "groupId": "1",
        'user': "0xd8904921a83ffe1b77b48873eca0f7948a4e8333"
    }
    r = requests.post(url,json=data,headers=headers)
    return render(request,"information/medicalRecord.html")


def meidcalquery(request):
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
        "funcParam":["request.POST.get('id')","request.POST.get('times')"],
        "groupId": "1",
        'user': "0xd8904921a83ffe1b77b48873eca0f7948a4e8333"
    }
    r = requests.post(url,json=data,headers=headers)
    return render(request,"information/medicalQuery.html",)

#111111111