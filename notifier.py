import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

BASE_URL = f"https://api.telegram.org/bot{TOKEN}"


def send_telegram(message):
    requests.post(
        f"{BASE_URL}/sendMessage",
        data={"chat_id": CHAT_ID, "text": message}
    )


def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()