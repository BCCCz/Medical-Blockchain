from account.views import ses
import requests

url = "http://127.0.0.1:5001/WeBASE-Node-Manager" \
      "/transaction/transInfo/groupId/transHash"
headers = {
    "groupId": "1",
    "transHash": "0x552adeee61cbe0c6b696774a70a74f422d0f3cb30f7e4f42ae65fa71190aa906",
}
r = ses.request(url, headers=headers)

print(r.text)
