import requests

source = requests.get('https://api.github.com')

# print(source.status_code)

if source.status_code == 200:
    print("Success!")
elif source.status_code == 404:
    print('Not Found.')   