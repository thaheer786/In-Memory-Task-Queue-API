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
