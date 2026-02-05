# Базовий образ Python
FROM python:3.11

# Робоча директорія
WORKDIR /app

# Копіюємо залежності
COPY requirements.txt .

# Оновлюємо pip та встановлюємо залежності
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код
COPY . .

# Відкриваємо порт
EXPOSE 5000

# Запуск Flask
CMD ["python", "app.py"]
