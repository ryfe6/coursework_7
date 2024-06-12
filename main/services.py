import requests

from config.settings import TELEGRAM_TOKEN, TG_URL


def send_telegram_message(tg_id, message):
    """Функция для отправки сообщения пользователю в телеграмме."""
    params = {"text": message, "chat_id": tg_id}
    response = requests.post(f"{TG_URL}{TELEGRAM_TOKEN}/sendMessage", params=params)
    return response.json()
