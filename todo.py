from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

tasks = []

hello_msg = """
            Эта страница реализует простой api
            перейди на tasks и все увидешь
            """


@app.get("/")
async def welcome():
  welcome_page = """
    <html>
        <head><title>Главная страница</title></head>
        <body>
            <h1>Добро пожаловать в FastAPI приложение!</h1>
            <p>Доступные ссылки:</p>
            <ul>
                <li><a href="/tasks">Получить все задачи<a></li>
                <li><a href="/docs">API Документация (Swagger)</a></li>
                <li><a href="/redoc">Альтернативная документация (ReDoc)</a></li>
            </ul>
        </body>
    </html>
    """
  return HTMLResponse(content=welcome_page)


@app.get("/tasks")
async def get_all_tasks():
  return tasks


@app.get("/tasks/{task_id}")
async def get_task_by_id(task_id: int):
  for task in tasks:
    if task["id"] == task_id:
      return task
  return {"error": "Task not found"}
