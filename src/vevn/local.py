import requests

res = requests.get("http://127.0.0.1:4000/")

print(res.json())
