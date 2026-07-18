import requests
import logging
import time

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

check_count = 0
max_checks = 3       # stop after 3 rounds
wait_seconds = 10    # wait 10 seconds between checks

while check_count < max_checks:
    check_count += 1
    print(f"\n=== Check round {check_count} ===")

    for site in websites:
        check_website(site)

    if check_count < max_checks:
        print(f"Waiting {wait_seconds} seconds before next check...")
        time.sleep(wait_seconds)

print("\nFinished monitoring.")