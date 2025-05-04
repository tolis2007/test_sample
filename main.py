from flask import Flask
import threading
import time
from datetime import datetime
import requests

# Your keywords
KEYWORDS = ["κόμιξ", "ποπάυ", "μεγάλο μίκυ"]

# Telegram bot config
CHAT_ID = "6488198943"
TOKEN = "7783096712:AAHg-dJQyVMCH5HBnPmHbr37NIUjaxhVKU4"

# Flask app for Render
app = Flask(__name__)

# Simulated scraping function
def scrape_loop():
    while True:
        # Replace with your Vendora + Metabook scraping logic
        print(f"🔍 Running at {datetime.now().strftime('%H:%M:%S')}")

        # Dummy result for testing
        title = "Μεγάλο Μίκυ Νο 123"
        price = "€3"
        link = "https://example.com"

        if any(k in title.lower() for k in KEYWORDS):
            send_telegram(f"{datetime.now()}\n{title}\n{price}\n{link}")

        time.sleep(60)  # run every minute

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Telegram error: {e}")

@app.route("/")
def home():
    return "Comic scraper is running."

# Start scraper in background thread
threading.Thread(target=scrape_loop, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
