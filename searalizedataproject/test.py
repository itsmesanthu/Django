import json
import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def resource():
    data=requests.get(BASE_URL+ENDPOINT)
    print(data)
    print(data.status_code)
    print(data.json())

resource()