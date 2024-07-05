import requests

url = "https://calculation-backend-api-by-blake.onrender.com/"
suffix = "division" #division, add, subtract, multiply, mean, median


url += suffix


body = {
  "x": 1,
  "y": 5
}
r = requests.post(url, json=body)
print(r.text)
