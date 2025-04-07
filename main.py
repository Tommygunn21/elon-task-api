from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# This variable stores the task in memory
task_storage = {}

from fastapi.responses import JSONResponse

@app.get("/task")
async def get_task():
    if current_task:
        return JSONResponse(content=current_task)
    return Response(status_code=204)


@app.post("/task")
async def post_task(request: Request):
    global task_storage
    task_storage = await request.json()
    return {"status": "success", "message": "Task sent to Elon"}

@app.post("/result")
async def post_result(request: Request):
    result = await request.json()
    print("✅ Result received from Elon:")
    print(result)
    # Clear the task so Elon doesn't repeat it
    global task_storage
    task_storage = {}
    return {"status": "received"}
