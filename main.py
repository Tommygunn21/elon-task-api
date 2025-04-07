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
    global current_task
    if current_task:
        task_to_send = current_task
        current_task = {}  # Clear after sending
        return JSONResponse(content=task_to_send)
    else:
        # Don't send any body for 204 status
        return JSONResponse(status_code=204, content=None)

@app.post("/result")
async def post_result(result: dict):
    print("📥 Elon returned result:", result)
    return {"status": "received"}
