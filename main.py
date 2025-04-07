from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# ✅ Declare current_task at the global scope
current_task = None

class Task(BaseModel):
    action: str
    message: str

@app.post("/task")
async def post_task(task: Task):
    global current_task  # ✅ Tell FastAPI to use the global variable
    current_task = task.dict()
    return {"status": "success", "message": "Task sent to Elon"}

@app.get("/task")
async def get_task():
    global current_task  # ✅ Again, explicitly reference global variable
    if current_task:
        task_to_return = current_task
        current_task = None
        return JSONResponse(content=task_to_return)
    return JSONResponse(status_code=204, content={})

@app.post("/result")
async def post_result(request: Request):
    result = await request.json()
    print("📩 Result from Elon:", result)
    return {"status": "received"}
