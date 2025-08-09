import requests
import time
import schedule
import tkinter as tk
from tkinter import messagebox
import argparse
import threading

SAFE_BROWSING_API_KEY = "YOUR_API_KEY_HERE"

def check_url_with_google_safe_browsing(url):
    endpoint = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
    headers = {"Content-Type": "application/json"}

    payload = {
        "client": {
            "clientId": "yourcompanyname",
            "clientVersion": "1.5.2"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    params = {"key": SAFE_BROWSING_API_KEY}
    response = requests.post(endpoint, json=payload, headers=headers, params=params)

    if response.status_code == 200:
        threats = response.json()
        if threats.get("matches"):
            return True
        else:
            return False
    else:
        print("Error checking URL:", response.status_code, response.text)
        return None

def monitor_urls(urls, notify_func):
    for url in urls:
        result = check_url_with_google_safe_browsing(url)
        if result is True:
            notify_func(f"⚠️ ALERT: {url} is flagged as HARMFUL!")
        elif result is False:
            print(f"[SAFE] {url}")
        else:
            print(f"[ERROR] Could not check {url}")

######################## CLI Notification ########################

def notify_cli(message):
    print(message)

######################## GUI Code ########################

def notify_gui(message):
    messagebox.showwarning("Website Alert", message)

def run_gui_monitor(urls, interval):
    def task():
        monitor_urls(urls, notify_gui)

    def loop():
        while True:
            task()
            time.sleep(interval)

    thread = threading.Thread(target=loop)
    thread.daemon = True
    thread.start()

    root = tk.Tk()
    root.title("Website Harmful Alert Tool")
    root.geometry("400x200")

    tk.Label(root, text="Monitoring the following URLs:", font=("Arial", 12)).pack(pady=5)
    for url in urls:
        tk.Label(root, text=url, fg="blue").pack()

    tk.Label(root, text=f"Interval: Every {interval} seconds").pack(pady=5)

    root.mainloop()

######################## Main ########################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Website Harmful Detection Alert Tool")
    parser.add_argument("-u", "--urls", nargs="+", required=True, help="List of URLs to monitor")
    parser.add_argument("-i", "--interval", type=int, default=300, help="Interval in seconds")
    parser.add_argument("--gui", action="store_true", help="Run in GUI mode")

    args = parser.parse_args()

    if args.gui:
        run_gui_monitor(args.urls, args.interval)
    else:
        def job():
            monitor_urls(args.urls, notify_cli)

        schedule.every(args.interval).seconds.do(job)
        print(f"Monitoring URLs every {args.interval} seconds...")
        job()  # run immediately once
        while True:
            schedule.run_pending()
            time.sleep(1)
