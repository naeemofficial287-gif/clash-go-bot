import requests
import time
import os
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_telegram(msg):
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(API_URL, data=data)

def main():
    send_telegram("✅ Clash of Clans Go Bot Started!")
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        print(f"Bot running... {now}")
        time.sleep(60)

if __name__ == "__main__":
    main()
