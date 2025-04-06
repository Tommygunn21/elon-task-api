from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# In-memory task store
current_task = None

class TaskRequest(BaseModel):
    action: str
    message: str

@app.get("/task")
async def get_task():
    global current_task
    if current_task is None:
        return JSONResponse(status_code=204, content={"message": "No task available"})
    task = current_task
    current_task = None
    return task

@app.post("/task")
async def post_task(task: TaskRequest):
    global current_task
    current_task = task.dict()
    return {"status": "success", "message": "Task sent to Elon"}

@app.post("/result")
async def post_result(result: dict):
    print("✅ Elon returned result:", result)
    return {"status": "received"}
