from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
from collections import deque
from uuid import uuid4
from datetime import datetime
from threading import Lock
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, HTTPException



app = FastAPI(title="In-Memory Task Queue API")

# -----------------------------
# In-memory storage
# -----------------------------
task_queue = deque()          # FIFO queue (stores task IDs)
tasks: Dict[str, Dict] = {}   # All tasks by ID
lock = Lock()                 # Thread safety


# -----------------------------
# Request Model
# -----------------------------
class TaskPayload(BaseModel):
    payload: Dict[str, Any]


# -----------------------------
# POST /tasks → Enqueue Task
# -----------------------------
@app.post("/tasks", status_code=201)
def enqueue_task(data: TaskPayload):
    with lock:
        task_id = str(uuid4())
        task = {
            "id": task_id,
            "payload": data.payload,
            "status": "pending",
            "created_at": datetime.utcnow().isoformat()
        }

        tasks[task_id] = task
        task_queue.append(task_id)

    return {"id": task_id}


# -----------------------------
# Root (health check)
# -----------------------------
@app.get("/")
def root():
    return {"message": "Task Queue API is running"}

from fastapi import HTTPException

@app.post("/tasks/dequeue")
def dequeue_task():
    with lock:
        if not task_queue:
            raise HTTPException(status_code=404, detail="Queue is empty")

        task_id = task_queue.popleft()
        task = tasks[task_id]
        task["status"] = "processing"

    return task

@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: str):
    with lock:
        task = tasks.get(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        if task["status"] != "processing":
            raise HTTPException(
                status_code=409,
                detail="Task is not in processing state"
            )

        task["status"] = "completed"

    return {"message": "Task completed successfully"}

@app.get("/queue/view")
def view_queue():
    with lock:
        return [tasks[task_id] for task_id in task_queue]

@app.get("/queue/stats")
def queue_stats():
    stats = {
        "pending": 0,
        "processing": 0,
        "completed": 0
    }

    with lock:
        for task in tasks.values():
            stats[task["status"]] += 1

    return stats
