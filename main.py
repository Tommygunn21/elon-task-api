from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# 🧠 Store the task in a global variable
task_storage = {"task": None}

@app.post("/task")
async def post_task(request: Request):
    task_data = await request.json()
    task_storage["task"] = task_data
    return {"status": "success", "message": "Task sent to Elon"}

@app.get("/task")
async def get_task():
    task = task_storage.get("task")
    if task:
        task_storage["task"] = None  # Clear after it's picked up
        return task
    return JSONResponse(status_code=204, content={"message": "No new task"})

@app.post("/result")
async def post_result(result: dict):
    print("📥 Elon returned result:", result)
    return {"status": "received"}
