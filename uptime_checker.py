import requests
import logging
import time
import smtplib
from email.mime.text import MIMEText

from Downloads.uptime_checker import EMAIL_SENDER

logging.basicConfig(
    filename="uptime_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

EMAIL_SENDER = "Sonalgajbhiye2001@gmail.com"
EMAIL_PASSWORD = "setrtsltemtbhiak"  # your 16-char app password
EMAIL_RECEIVER = "Sonalgajbhiye04@gmail.com"

def check_website(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            message = f"{url} is UP"
        else:
            message = f"{url} is DOWN (status {response.status_code})"
            send_email_alert(url)
    except requests.exceptions.RequestException:
        message = f"{url} is DOWN (no response)"
        send_email_alert(url)

    print(message)
    logging.info(message)

def send_email_alert(url):
    msg = MIMEText(f"Alert: {url} appears to be DOWN.")
    msg["Subject"] = f"Website Down: {url}"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

    print(f"Email alert sent for {url}")

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