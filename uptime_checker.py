import requests

url = "https://www.google.com"
response = requests.get(url)

if response.status_code ==200:
    print(f"{url} is UP")
else:
    print(f"{url} is DOWN")


