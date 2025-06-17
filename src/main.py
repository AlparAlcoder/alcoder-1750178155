from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []

class Task(BaseModel):
    id: int
    title: str
    description: str
    done: bool

@app.get("/tasks", response_model=List[Task])
def read_tasks():
    """Endpoint to list all tasks"""
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    """Endpoint to get a single task"""
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    """Endpoint to create a new task"""
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    """Endpoint to update a task"""
    for index, stored_task in enumerate(tasks):
        if stored_task.id == task_id:
            tasks[index] = task
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """Endpoint to delete a task"""
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Task has been deleted successfully!"}
    raise HTTPException(status_code=404, detail="Task not found")