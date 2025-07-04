from fastapi import FastAPI, Form, HTTPException
import json
import os
from typing import Optional

app = FastAPI()
USER_DB_FILE = "user.json"
TASK_DB_FILE = "tasks.json"

def load_user():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, "r") as file:
            return json.load(file)
    return {}

def save_user(users):
    with open(USER_DB_FILE, "w") as file:
        json.dump(users, file)

@app.post("/signup")
def signup(username: str = Form(...), password: str = Form(...)):
    users = load_user()
    if username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[username] = password
    save_user(users)
    return {"message": "Signup successful!"}

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    users = load_user()
    if username not in users or users[username] != password:
        raise HTTPException(status_code=401, detail="Wrong username or password")
    return {"message": "Login successful!"}

def load_tasks():
    if os.path.exists(TASK_DB_FILE):
        with open(TASK_DB_FILE, "r") as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    with open(TASK_DB_FILE, "w") as file:
        json.dump(tasks, file)

from typing import Optional

@app.post("/add-task")
def add_task(
    username: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    status: Optional[str] = Form("pending")
):
    tasks = load_tasks()
    user_tasks = tasks.get(username, [])
    new_id = 1 if not user_tasks else user_tasks[-1]["id"] + 1
    new_task = {"id": new_id, "title": title, "description": description, "status": status}
    user_tasks.append(new_task)
    tasks[username] = user_tasks
    save_tasks(tasks)
    return {"message": "Task added", "task": new_task}


@app.get("/tasks")
def get_tasks(username: str):
    tasks = load_tasks()
    return {"tasks": tasks.get(username, [])}

@app.put("/edit-task/{task_id}")
def edit_task(task_id: int, username: str = Form(...), title: Optional[str] = Form(None), description: Optional[str] = Form(None), status: Optional[str] = Form(None)):
    tasks = load_tasks()
    user_tasks = tasks.get(username, [])
    for task in user_tasks:
        if task["id"] == task_id:
            if title: task["title"] = title
            if description: task["description"] = description
            if status: task["status"] = status
            save_tasks(tasks)
            return {"message": "Task updated", "task": task}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/delete-task/{task_id}")
def delete_task(task_id: int, username: str = Form(...)):
    tasks = load_tasks()
    user_tasks = tasks.get(username, [])
    updated_tasks = [task for task in user_tasks if task["id"] != task_id]
    if len(updated_tasks) == len(user_tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[username] = updated_tasks
    save_tasks(tasks)
    return {"message": "Task deleted"}
