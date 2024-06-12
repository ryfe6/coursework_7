from datetime import datetime

import pytz
from celery import shared_task
from django.conf import settings

from main.models import Habit  # Замените 'your_app' на название вашего приложения
from main.services import (
    send_telegram_message,
)  # Замените на ваш модуль интеграции с Telegram


@shared_task
def send_habits_information():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    habits_to_send = Habit.objects.filter(is_nice=False)
    for habit in habits_to_send:
        # Проверяем, что время выполнения привычки совпадает с текущим временем до минуты
        if (
            habit.time.hour == current_datetime.hour
            and habit.time.minute == current_datetime.minute
        ):
            tg_id = habit.owner.telegram_id
            message = f"""Выполните привычку: {habit.action} 
                       время: {habit.time.strftime('%H:%M')} 
                       место: {habit.place}"""
            send_telegram_message(tg_id, message)
            habit.save()
