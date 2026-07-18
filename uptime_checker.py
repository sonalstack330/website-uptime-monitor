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

check_website("https://www.google.com")
check_website("https://www.github.com")
check_website("https://thiswebsitedoesnotexist12345.com")
