import requests

print('requests version: ', requests.__version__)

google = requests.get("http://www.google.com")
print('\nGoogle Status Code: ', google.status_code)

rawURL = 'https://raw.githubusercontent.com/dijonron/cmput404_lab1/main/lab1.py'
sourceCode = requests.get(rawURL)
print('\n--------- Source Code From GitHub ---------')
print(sourceCode.text)
print('-------------------------------------------')