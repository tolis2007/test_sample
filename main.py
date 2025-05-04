import os
import time
import requests
from datetime import datetime

# Get Telegram credentials from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_notification(title, link, price):
    message = f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n📚 {title}\n💰 {price}\n🔗 {link}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")

def main():
    print(f"🔍 Running at {datetime.now().strftime('%H:%M:%S')}")
    # Example data (replace with real scraping logic)
    send_telegram_notification("Test Comic", "https://example.com", "5€")

# Loop forever, checking every 60 seconds
if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)
