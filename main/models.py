from django.db import models
from django.utils import timezone

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """Модель привычек."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        **NULLABLE,
    )
    place = models.CharField(max_length=50, verbose_name="Место", **NULLABLE)
    time = models.DateTimeField(verbose_name="Время выполнения", default=timezone.now)
    action = models.CharField(max_length=150, verbose_name="Действие")
    is_nice = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE
    )
    is_publish = models.BooleanField(default=False, verbose_name="Признак публичности")

    time_to_done = models.PositiveIntegerField(
        verbose_name="Время для выполнения", **NULLABLE
    )
    award = models.CharField(max_length=50, verbose_name="Вознагрождение", **NULLABLE)
    period = models.PositiveIntegerField(
        default=1, verbose_name="Периодичность выполнения привычки(кол-во дней)"
    )

    def __str__(self):
        return f"{self.owner} будет {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
