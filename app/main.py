from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import todos

# Создаем таблицы (если их нет)
models.Base.metadata.create_all(bind=engine)

# Инициализация приложения
app = FastAPI(
    title="FastAPI TODO",
    description="Простое API для управления задачами",
    version="1.0.0"
)

# Подключаем роутер для todos
app.include_router(todos.router)


@app.get("/")
def root():
    return {
        "project": "FastAPI TODO",
        "version": "1.0.0",
        "author": "Gregimuri",
        "docs": "http://127.0.0.1:8000/docs",
        "endpoints": {
            "GET /todos/": "Получить список задач",
            "POST /todos/": "Создать новую задачу",
            "GET /todos/{id}": "Получить задачу по ID",
            "PUT /todos/{id}": "Обновить задачу",
            "DELETE /todos/{id}": "Удалить задачу"
        }
    }
