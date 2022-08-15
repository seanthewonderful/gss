import requests
import json


endpoint = "https://api.twitter.com/2/tweets/search/recent?query="

headers = {
    "access_token": "PbCpzCP5aVq39GembNWSAo89V",
    "token_secret": "aKOYl7fP4lQauA9yKDaBrC67Kl8d2SYiVtXnY4O3luC5FvurX1",
    "bearer_token": "Bearer AAAAAAAAAAAAAAAAAAAAAGefcQEAAAAAWtdc9ZAkIjTgWx%2FP7l7h4KXV%2BX8%3DsEfZdl5ZeZtEaf8om1JPhy51PAJYaEpyuGf1TkAHybiPNAPmGG"
}

params = {
    'id': "2620199928"
}

hashtag_params = "sponsored"

url = endpoint + hashtag_params

response = requests.get(url=endpoint, params=params, headers=headers)
print(response.json())