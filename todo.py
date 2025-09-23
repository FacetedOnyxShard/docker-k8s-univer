from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import signal
import sys

app = FastAPI()

tasks = []
current_id = 1


class Task(BaseModel):
  title: str
  description: str | None = None
  is_completed: bool = False


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


@app.post('/tasks')
async def create_task(task: Task):
  global current_id
  new_task = {
    "id": current_id,
    "title": task.title,
    "description": task.description,
    "is_completed": task.is_completed,
  }
  tasks.append(new_task)
  current_id += 1
  return new_task


@app.put('/tasks/{task_id}')
async def update_task(task_id: int, updated_task: Task):
  for task in tasks:
    if task['id'] == task_id:
      task['title'] = updated_task.title
      task['description'] = updated_task.description
      task['is_completed'] = updated_task.is_completed
      return task
  return {"error": "task not found"}


class TaskStateChanger(BaseModel):
  is_completed: bool | None = None


@app.patch('/tasks/{task_id}')
async def change_task_state(task_id: int, updated_task: TaskStateChanger):
  for task in tasks:
    if task['id'] == task_id:
      task['is_completed'] = updated_task.is_completed
      return task
  return {"error": "task not found"}


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
  for index, task in enumerate(tasks):
    if task['id'] == task_id:
      deleted_task = tasks.pop(index)
      return {"message": "Task deleted", "task": deleted_task}
  return {"error": "Task not Found"}


def signal_handler(signum, frame):
  print("Received shutdown signal")
  sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
