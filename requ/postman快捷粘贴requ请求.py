import requests

# url = "http://192.144.148.91:2333/login"

# payload = "{\r\n\"username\":\"tan123\", \r\n\"password\":\"a1234567\" \r\n}"
# headers = {
#   'Content-Type': 'application/json'
# }

# response = requests.request("POST", url, headers=headers, data = payload)

# print(response.text)

url = "http://192.144.148.91:2333/inspirer/new"

payload = "{\r\n\"content\":\"的人\"\r\n}"
headers = {
  'Content-Type': 'application/json',
  'token': '34775491df009f6d9413f18321natad31a0a172768b7a0'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
