import requests

url = "https://requestb.in/1kgfazd1"
json = {
    "month" : "may",
    "result": "1:0",
    "team" : "Manchester"
}

response = requests.post(url, params=json, data="kuku")
print(response.status_code)

url2 = "http://httpbin.org/"
params = {
    'id':[1,2,3],

}
response = requests.get(url2, params=params, data="kuku")
print(response.json())