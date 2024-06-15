FROM python:3.11-slim

WORKDIR /app

# Сначала копируем только файлы poetry.lock и pyproject.toml для использования кэширования Docker
COPY poetry.lock pyproject.toml /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false

# Устанавливаем зависимости проекта
RUN poetry install --no-dev

# Теперь копируем остальные файлы проекта
COPY . /app

# Запускаем миграции и сервер Django, указывая хост
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]