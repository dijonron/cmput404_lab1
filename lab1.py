import requests

print('requests version: ', requests.__version__)

google = requests.get("http://www.google.com")

print(google.status_code)
print(google.text)