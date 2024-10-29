import requests
url = "http://localhost:8080/predict"
client = {"job": "student", "duration": 280, "poutcome": "failure"}
response = requests.post(url, json=client).json()
print(response)