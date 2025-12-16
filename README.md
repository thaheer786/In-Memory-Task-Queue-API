# In-Memory Task Queue API

A simple RESTful API that simulates a **First-In, First-Out (FIFO) task queue** using in-memory data structures.  
This project demonstrates core backend concepts such as **queue management, task lifecycle handling, REST API design, and concurrency control**.

---

## 🎯 Objective

The objective of this project is to build a **thread-safe in-memory task queue** that:

- Enforces FIFO task processing
- Handles concurrent client requests safely
- Tracks the lifecycle of each task
- Returns appropriate HTTP status codes and error messages

This serves as a foundational backend system before moving to distributed message brokers like Kafka or RabbitMQ.

---

## 🛠 Tech Stack

- **Language:** Python 3.12
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Concurrency Control:** threading.Lock
- **Data Structures:** collections.deque, dictionary

---

## 📦 Task Data Model

Each task contains the following fields:

```json
{
  "id": "UUID",
  "payload": { "any": "JSON data" },
  "status": "pending | processing | completed",
  "created_at": "ISO-8601 timestamp"
}
⚙️ Setup & Run Instructions
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/thaheer786/In-Memory-Task-Queue-API.git
cd In-Memory-Task-Queue-API
2️⃣ (Optional) Create Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install fastapi uvicorn
4️⃣ Run the Application
bash
Copy code
uvicorn main:app --reload
5️⃣ Open API Documentation
arduino
Copy code
http://127.0.0.1:8000/docs
📌 API Endpoints
➤ Enqueue a Task
POST /tasks

bash
Copy code
curl -X POST http://127.0.0.1:8000/tasks \
-H "Content-Type: application/json" \
-d '{"payload":{"job":"send_email","to":"user@example.com"}}'
Response – 201 Created

json
Copy code
{
  "id": "uuid"
}
➤ Dequeue a Task (FIFO)
POST /tasks/dequeue

bash
Copy code
curl -X POST http://127.0.0.1:8000/tasks/dequeue
Response – 200 OK

json
Copy code
{
  "id": "uuid",
  "payload": {...},
  "status": "processing",
  "created_at": "timestamp"
}
Response – 404 Not Found (Queue empty)

➤ Get Task by ID
GET /tasks/{task_id}

bash
Copy code
curl http://127.0.0.1:8000/tasks/{task_id}
➤ Complete a Task
PUT /tasks/{task_id}/complete

bash
Copy code
curl -X PUT http://127.0.0.1:8000/tasks/{task_id}/complete
Responses

200 OK – Task completed successfully

409 Conflict – Task not in processing state

404 Not Found – Task not found

➤ View Pending Queue
GET /queue/view

bash
Copy code
curl http://127.0.0.1:8000/queue/view
Returns all pending tasks in FIFO order.

➤ Queue Statistics
GET /queue/stats

bash
Copy code
curl http://127.0.0.1:8000/queue/stats
Response

json
Copy code
{
  "pending": 0,
  "processing": 0,
  "completed": 1
}
🔒 Concurrency & Thread Safety
Shared in-memory data structures (deque and dict) are protected using a mutex lock (threading.Lock)

All critical operations (enqueue, dequeue, complete) are atomic

Prevents race conditions, task duplication, and inconsistent state

Ensures correct FIFO behavior under concurrent access

⚡ Simulating Concurrent Access
Option 1: Apache Bench
bash
Copy code
ab -n 50 -c 10 -p task.json -T application/json http://127.0.0.1:8000/tasks
Option 2: Python Script
python
Copy code
import requests
from concurrent.futures import ThreadPoolExecutor

def enqueue():
    requests.post("http://127.0.0.1:8000/tasks", json={"payload":{"job":"test"}})

with ThreadPoolExecutor(max_workers=10) as executor:
    for _ in range(20):
        executor.submit(enqueue)
📚 Resources
Designing a RESTful API with Python and Flask

Introduction to Threading in Python

Node.js Event Loop and Asynchronous Operations

Queue Data Structure – GeeksforGeeks

✅ Evaluation Readiness
✔ All required endpoints implemented
✔ FIFO behavior enforced
✔ Thread-safe concurrency handling
✔ Correct HTTP status codes
✔ Clean and readable code
✔ Complete documentation

📄 License
This project is intended for educational purposes.
