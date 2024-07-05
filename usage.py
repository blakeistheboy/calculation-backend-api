import requests

url = "YOUR_URL"
suffix = "division" #division, add, subtract, multiply, mean, median


url += suffix


body = {
  "x": 1,
  "y": 5
}
r = requests.post(url, json=body)
print(r.text)
