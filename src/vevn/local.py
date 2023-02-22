import requests

# res = requests.get("http://127.0.0.1:3000/api/courses/0")
# res = requests.delete("http://127.0.0.1:3000/api/courses/1")
# res = requests.post("http://127.0.0.1:3000/api/courses/3", json={"name": "Golang", "videos": 5})
res = requests.post("http://127.0.0.1:5000/api/courses/1")
print(res.json())


