import requests

def check_website(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"{url} is UP")
        else:
            print(f"{url} is DOWN (status {response.status_code})")
    except requests.exceptions.ConnectionError:
        print(f"{url} is DOWN (no response)")

websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://thiswebsitedoesnotexist12345.com",
]

for site in websites:
    check_website(site)

