import requests

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload = {
    'scope': 'GIGACHAT_API_PERS'
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': 'e9e4fa07-fdbf-4645-ba0d-7a61a639f058',
    'Authorization': 'ZTllNGZhMDctZmRiZi00NjQ1LWJhMGQtN2E2MWE2MzlmMDU4OmI5ZDZiZDhjLWUzZDMtNDZiNi05MTIzLWEwN2U1YzQ0YjQ1Mg=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
