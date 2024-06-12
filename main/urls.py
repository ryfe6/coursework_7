from django.urls import path

from main.apps import MainConfig
from main.views import (
    HabitCreateApiView,
    HabitDestroyApiView,
    HabitListApiView,
    HabitRetrieveApiView,
    HabitUpdateApiView,
    PublishHabitListApiView,
)

app_name = MainConfig.name

urlpatterns = [
    path("", HabitListApiView.as_view(), name="habit_list"),
    path("<int:pk>/", HabitRetrieveApiView.as_view(), name="habit_retrieve"),
    path("create/", HabitCreateApiView.as_view(), name="habit_create"),
    path("delete/<int:pk>/", HabitDestroyApiView.as_view(), name="habit_delete"),
    path("update/<int:pk>/", HabitUpdateApiView.as_view(), name="habit_update"),
    path("published/", PublishHabitListApiView.as_view(), name="habit_publish"),
]
