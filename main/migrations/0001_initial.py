# Generated by Django 5.0.6 on 2024-06-11 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Место"
                    ),
                ),
                (
                    "time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Время выполнения"
                    ),
                ),
                ("action", models.CharField(max_length=150, verbose_name="Действие")),
                (
                    "is_nice",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "is_publish",
                    models.BooleanField(
                        default=False, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "time_to_done",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Время для выполнения"
                    ),
                ),
                (
                    "award",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Вознагрождение",
                    ),
                ),
                (
                    "period",
                    models.PositiveIntegerField(
                        default=1,
                        verbose_name="Периодичность выполнения привычки(кол-во дней)",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
