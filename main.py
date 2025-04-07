from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()

# Simple Task model
class Task(BaseModel):
    action: str
    message: str

# In-memory task queue
task_queue = []

@app.get("/task")
async def get_task():
    if task_queue:
        current_task = task_queue.pop(0)  # Retrieve and remove the first task
        return {"status": "success", "task": current_task}
    else:
        return {"message": "No new tasks", "status": "204"}  # Return a custom message for no tasks

@app.post("/task")
async def add_task(task: Task):
    task_queue.append(task)  # Add the new task to the queue
    return {"status": "success", "message": f"Task '{task.action}' added successfully."}
