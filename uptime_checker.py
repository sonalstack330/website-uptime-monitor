import requests

def check_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is UP")
    else:
        print(f"{url} is DOWN")

check_website("https://www.google.com")
check_website("https://www.github.com")
