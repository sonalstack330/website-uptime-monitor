
import requests
import logging

logging.basicConfig(
    filename="uptime_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

def check_website(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            message = f"{url} is UP"
        else:
            message = f"{url} is DOWN (status {response.status_code})"
    except requests.exceptions.RequestException:
        message = f"{url} is DOWN (no response)"

    print(message)
    logging.info(message)
websites = [
    "https://www.google.com",
    "https://www.github.com",
    "https://thiswebsitedoesnotexist12345.com",
]

for site in websites:
    check_website(site)