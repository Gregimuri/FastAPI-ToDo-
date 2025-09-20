# 📌 FastAPI ToDo API

Простой **ToDo сервис на FastAPI** с базой данных SQLite и автотестами (pytest).  
Проект создан для демонстрации навыков работы с Python, FastAPI, SQLAlchemy и тестированием API.

---

## 🚀 Функционал
- Создание задачи  
- Получение списка задач  
- Хранение в базе данных (SQLite)  
- Автотесты с использованием pytest  
- Swagger UI для документации  

---

## ⚙️ Установка и запуск

### 1. Клонируем репозиторий
```bash
git clone https://github.com/username/fastapi-todo.git
cd fastapi-todo
```

### 2. Устанавливаем зависимости
```bash
pip install -r requirements.txt
```

### 3. Запускаем сервер
```bash
uvicorn app.main:app --reload
```

Сервис будет доступен по адресу:  
👉 http://127.0.0.1:8000  

Документация Swagger:  
👉 http://127.0.0.1:8000/docs  

---

## 🧪 Тесты

Запуск автотестов:
```bash
pytest
```

---

## 📂 Структура проекта
```
fastapi-todo/
│── app/
│   ├── main.py          # Точка входа (FastAPI)
│   ├── models.py        # SQLAlchemy модели
│   ├── database.py      # Настройки базы
│   ├── crud.py          # CRUD-функции
│   └── schemas.py       # Pydantic-схемы
│
│── tests/
│   └── test_main.py     # Pytest-тесты
│
│── requirements.txt
│── README.md
```

---

## 📖 Примеры запросов

### Создание задачи
```bash
POST /todos/
Content-Type: application/json

{
  "title": "Buy milk",
  "description": "Remember to buy milk",
  "completed": false
}
```

### Получение всех задач
```bash
GET /todos/
```

Пример ответа:
```json
[
  {
    "id": 1,
    "title": "Buy milk",
    "description": "Remember to buy milk",
    "completed": false
  }
]
```

---

## 🛠 Используемые технологии
- [FastAPI](https://fastapi.tiangolo.com/)  
- [SQLite](https://www.sqlite.org/index.html)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [Pydantic](https://docs.pydantic.dev/)  
- [Pytest](https://docs.pytest.org/)  

---

## 👨‍💻 Автор
- Григорий Ильич  
- [GitHub](https://github.com/Gregimuri)  
