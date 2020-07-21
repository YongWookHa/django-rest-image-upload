import json
import base64
import requests
import sys

target = sys.argv[1]

if __name__ == "__main__":
    with open(target, 'rb') as f:
        img = f.read()
    
    x = base64.encodebytes(img).decode('utf8')
    API_HOST = 'http://127.0.0.1:8000/api/v1/base64'

    inp = {
        # 'data_type' : 'byte-string',
        'image' : 'data:image/png;base64,'+x,
        'api_key' : '43102713-18cd-460c-be75-3ab4207dc481',
    }

    res = requests.post(API_HOST, data=inp)
    if res:
        print(res.json())