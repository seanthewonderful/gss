import requests

endpoint = "https://api.twitter.com/2/users/1358218911594864640/liked_tweets"

params = {
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAGefcQEAAAAAWtdc9ZAkIjTgWx%2FP7l7h4KXV%2BX8%3DsEfZdl5ZeZtEaf8om1JPhy51PAJYaEpyuGf1TkAHybiPNAPmGG",
    # "secret_key": "aKOYl7fP4lQauA9yKDaBrC67Kl8d2SYiVtXnY4O3luC5FvurX1"
}
# print(response)

response = requests.get(url=endpoint, params=params)
print(response.json())