import requests

headers = {"Content-Type": "application/json"}

# PUT request
res1 = requests.post(
    "http://127.0.0.1:5000/put",
    json={"key": "name", "value": "leela"},
    headers=headers
)
print("PUT:", res1.status_code, res1.text)

# GET request
res2 = requests.get("http://127.0.0.1:5000/get/name")
print("GET:", res2.status_code, res2.text)