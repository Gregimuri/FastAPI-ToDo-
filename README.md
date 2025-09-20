# FastAPI ToDo API

Простой ToDo сервис на FastAPI с базой данных SQLite и автотестами (pytest).  
Проект демонстрирует навыки работы с Python, FastAPI, SQLAlchemy, Pydantic и тестированием API.

---

## 🚀 Функционал

- Создать задачу  
- Получить список задач  
- Хранение данных в SQLite  
- Автотесты с pytest  
- Автоматическая документация через Swagger

---

## 📁 Структура проекта

```
fastapi-todo/
│── app/
│   ├── __init__.py        # пакет приложения
│   ├── main.py            # точка входа, маршруты API
│   ├── models.py          # модели SQLAlchemy
│   ├── schemas.py         # Pydantic схемы
│   ├── crud.py            # функции CRUD
│   └── database.py        # настройка подключения к БД
│
│── tests/
│   ├── __init__.py        # (опционально) тестовый пакет
│   └── test_main.py       # тесты для API
│
│── requirements.txt
│── README.md
```

---

## ⚙ Установка и запуск

1. Клонирование репозитория  
   ```bash
   git clone https://github.com/Gregimuri/fastapi-todo.git
   cd fastapi-todo
   ```

2. Создание и активация виртуального окружения (рекомендуется)  
   ```bash
   python -m venv venv
   venv\Scripts\activate     # Windows
   # или
   source venv/bin/activate  # Linux / Mac
   ```

3. Установка зависимостей  
   ```bash
   pip install -r requirements.txt
   ```

4. Запуск сервера  
   ```bash
   uvicorn app.main:app --reload
   ```

   Затем открой:
   - Документация Swagger UI: http://127.0.0.1:8000/docs  
   - Проверка API через браузер или Postman/curl.

---

## 🧪 Тесты

Запуск автотестов:
```bash
python -m pytest
```

Ожидается, что тесты проходят успешно и отсутствуют предупреждения по Pydantic и SQLAlchemy.

---

## 🛠 Технологии

- FastAPI  
- SQLite  
- SQLAlchemy  
- Pydantic  
- Pytest

---

## ✅ Что уже реализовано

- Основные маршруты: `POST /todos/` и `GET /todos/`  
- Работа с базой данных (через SQLAlchemy)  
- Схемы в Pydantic + совместимость с Pydantic v2  
- Тестирование маршрутов API

---

## 💡 Что планируется добавить

- Возможность обновления / удаления задач  
- Обработка ошибок (например, если задачи нет по ID)  
- Pagination / фильтрация задач  
- Docker‑контейнеризация  
- CI (GitHub Actions) + линтер / форматтер кода

---

## 👨‍💻 Автор

Титков Григорий Ильич  
[GitHub](https://github.com/Gregimuri)  
