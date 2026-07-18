# Website Uptime & Alert Monitoring System

A lightweight Python tool that monitors the availability of multiple websites in real time, logs the results, and sends automated email alerts when a site goes down.

## Overview

This project automates website availability checks — similar to tools like UptimeRobot or Pingdom — by periodically checking a list of URLs, recording their status, and sending an email alert if something goes offline.

Built to strengthen practical skills in monitoring, automation, and troubleshooting — core responsibilities in an Application Support role.

## Features

- Monitors multiple websites at once
- Detects UP / DOWN status
- Handles timeouts and connection errors gracefully
- Logs every check with a timestamp to `uptime_log.txt`
- Sends automated email alerts when a website goes down
- Runs continuously with a configurable wait interval

## Tech Stack

- **Language:** Python 3
- **Libraries:** `requests`, `smtplib`, `logging`, `time`, `os`

## ⚙️ Installation & Setup

1. Clone the repository - 
git clone https://github.com/sonalstack330/website-uptime-monitor.git
cd website-uptime-monitor
2. Install the required library - pip install requests
3. Set environment variables for email alerts (required before running):
```powershell
   $env:EMAIL_SENDER="your_email@gmail.com"
   $env:EMAIL_PASSWORD="your_16_char_app_password"
   $env:EMAIL_RECEIVER="receiver_email@gmail.com"
```
   > Use a Gmail App Password, not your real Gmail password. Generate one at https://myaccount.google.com/apppasswords

## ▶️ How to Run
python uptime_checker.py

Sample output:
=== Check round 1 ===
https://www.google.com is UP
https://www.github.com is UP
https://thiswebsitedoesnotexist12345.com is DOWN (no response)
Waiting 10 seconds before next check...

Results are also saved to `uptime_log.txt` with timestamps.
