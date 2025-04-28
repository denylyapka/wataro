import json
import uuid

import requests
from requests.auth import HTTPBasicAuth

from src.apps.forecast_app.gigachat.gigachat_config import SECRET


def get_access_token() -> str:
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
        'Authorization': f'Bearer {SECRET}'
    }
    payload = {"scope": "GIGACHAT_API_PERS"}
    result = requests.request("POST", url, headers=headers, data=payload, verify=False)

    print("result.json():", result.json())
    access_token = result.json()['access_token']
    return access_token


def send_prompt(msg: str, access_token: str):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
      "model": "GigaChat",
      "messages": [
        {
          "role": "user",
          "content": msg,
        },
      ],
      "n": 1,
      "stream": False,
      "update_interval": 0
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f'Bearer {access_token}'
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)
    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        print(response.json())
