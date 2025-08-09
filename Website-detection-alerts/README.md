🧠 Goal
Tool: Real-time website harmful detection and alerting system.

Use Cases:

Get notified if your website is:

Blacklisted (e.g., Google Safe Browsing)

Hosting malware or phishing

Redirecting users suspiciously

Real-time or periodic checking with alerting system

✅ Features
Feature	Description
Website URL monitoring	You input the URL(s) you want to monitor
Periodic scanning	Scans every few minutes or hours
Blacklist/API checking	Uses APIs like Google Safe Browsing, VirusTotal
Real-time alerts	Email / Desktop notification / Telegram
CLI + GUI	Both command-line and Tkinter GUI support

🛠️ Technologies
Python

Google Safe Browsing API

VirusTotal API (optional, requires API key)

Tkinter (GUI)

requests, schedule, smtplib (for alerts)

🧪 Sample Workflow
User inputs URL(s)

Every N minutes:

Query threat intelligence APIs

Check DNS anomalies

If flagged:

Send notification (email or desktop)

Display history and logs in GUI (optional)

🧰 Code: Website Monitor (Safe Browsing Check)

🔐 Prerequisites
Get a Google Safe Browsing API key:
https://developers.google.com/safe-browsing/v4/get-started

🖥️ Usage
📌 CLI Mode Command
python website_monitor.py -u (https://example.com) (https://yourdomain.com) --interval 600

📌 GUI Mode Command
python website_monitor.py -u (https://example.com) (https://yourdomain.com) --gui

🛑 Important Notes
Don’t exceed API rate limits — Google Safe Browsing has free and premium tiers.

You must replace "YOUR_API_KEY_HERE" with a real API key.