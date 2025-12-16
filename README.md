# In-Memory Task Queue API

A simple RESTful API that simulates a **First-In, First-Out (FIFO) task queue** using in-memory data structures.  
This project demonstrates core backend concepts such as **queue management, task lifecycle handling, REST API design, and concurrency control**.

---

## 🚀 Objective

The goal of this project is to build a **thread-safe in-memory task queue** that supports multiple concurrent clients while ensuring:

- FIFO task processing
- Safe concurrent access
- Accurate task lifecycle tracking
- Proper HTTP status codes and error handling

---

## 🛠 Tech Stack

- **Language:** Python 3.12
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Concurrency:** threading.Lock
- **Data Structures:** collections.deque, dict

---

## 📦 Task Data Model

Each task contains the following fields:

```json
{
  "id": "UUID",
  "payload": { "any": "json data" },
  "status": "pending | processing | completed",
  "created_at": "ISO-8601 timestamp"
}
