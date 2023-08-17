FROM python:3
# Определяем переменные среды
# Чтобы python не создавал файлы .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Чтобы чтобы видеть выходные данные приложения в реальном времени
ENV PYTHONUNBUFFERED=1
# Устанавливаем рабочую директорию
WORKDIR /code
# Копируем в рабочую директорию файл зависимостей
COPY requirements.txt /code/
# Обновляем pip устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# Копируем содержимое локальной директории code в рабочую директорию
COPY . /code/