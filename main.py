from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
import json
import asyncio

app = FastAPI()

# Use an in-memory store for tasks in this version
latest_task = None

@app.get("/")
def root():
    return {"message": "✅ Elon Task API is Live"}

@app.post("/task")
async def post_task(request: Request):
    global latest_task
    data = await request.json()
    latest_task = data
    return {"status": "success", "message": "Task sent to Elon"}

@app.get("/task")
async def get_task():
    global latest_task
    if latest_task is None:
        return JSONResponse(status_code=204, content={})
    task = latest_task
    latest_task = None  # Clear after sending
    return task

@app.post("/result")
async def post_result(request: Request):
    data = await request.json()
    print("📥 Elon sent result:", json.dumps(data, indent=2))
    return {"status": "received"}
