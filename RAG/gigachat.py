import json
import requests
import os


def get_token():
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    
    payload={
      'scope': 'GIGACHAT_API_PERS'
    }
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept': 'application/json',
      'RqUID': 'd22d8f5c-f2f2-4dc1-b8e6-77fd0dcbd7de',
      'Authorization': f'Basic {os.environ["SBER_TOKEN"]}'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    
    access_token = response.json()['access_token']
    return access_token


def get_gigachat_response(prompt):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    
    payload = json.dumps({
      "model": "GigaChat",
      "messages": [
        {
          "role": "system",
          "content": ""
        },
        {
          "role": "user",
          "content": prompt
        }
      ],
      "stream": False,
      "update_interval": 0
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': f'Bearer {get_token()}'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    try:
        return response.json()['choices'][0]['message']['content']
    except KeyError:
        print(response.json())