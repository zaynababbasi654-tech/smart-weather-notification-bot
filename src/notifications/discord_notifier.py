import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


def send_discord_notification(message):
    payload = {
        "content": message
    }

    response = requests.post(
        WEBHOOK_URL,
        json=payload
    )

    response.raise_for_status()

    return True