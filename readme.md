# FastAPI Backend Fundamentals

A practical implementation of the core concepts of **FastAPI**, including API endpoints, HTTP methods, request parameters, validation, and automatic API documentation.

## Overview

FastAPI is a modern, high-performance Python framework for building REST APIs and backend services.

This repository documents my progression from basic API endpoints to building backend services that can later integrate with **Machine Learning, RAG, and AI Agent applications**.

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- Jinja2
- OpenAPI
- Swagger UI
- ReDoc

---

## Project Structure

```text
FAST-API/
│
├── main.py
├── templates/
│   └── index.html
└── README.md
````

---

## Getting Started

### Installation

```bash
python -m pip install fastapi uvicorn jinja2 pydantic
```

### Run the Application

```bash
fastapi dev main.py
```

Alternatively:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# Core Concepts

## 1. FastAPI Application

A FastAPI application is initialized using:

```python
from fastapi import FastAPI

app = FastAPI()
```

The `app` object is the central application instance used to define API routes and configuration.

---

## 2. API Endpoints

An endpoint is a specific route through which a client can communicate with the backend.

Example:

```python
@app.get("/hello")
def hello():
    return {"message": "Hello World"}
```

Endpoint:

```text
GET /hello
```

---

## 3. HTTP Methods

FastAPI supports the standard HTTP methods used by REST APIs.

| Method | Purpose               |
| ------ | --------------------- |
| GET    | Retrieve data         |
| POST   | Create or submit data |
| PUT    | Update data           |
| PATCH  | Partially update data |
| DELETE | Remove data           |

Example:

```python
@app.get("/users")
def get_users():
    return {"users": []}
```

---

# Query Parameters

Query parameters allow clients to send data through the URL.

Example:

```python
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}
```

Request:

```text
GET /add?a=10&b=20
```

Response:

```json
{
    "result": 30
}
```

FastAPI automatically:

1. Extracts the parameters
2. Validates their types
3. Passes them to the Python function
4. Returns the result as a JSON response

---

# Type Validation

FastAPI uses Python type hints for automatic validation.

```python
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}
```

Here:

```python
a: int
b: int
```

indicates that both parameters must be integers.

Invalid input is automatically rejected with an appropriate HTTP validation response.

---

# Automatic API Documentation

One of FastAPI's major advantages is automatic API documentation.

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides an interactive interface for:

* Exploring endpoints
* Viewing parameters
* Sending requests
* Testing APIs
* Inspecting responses

---

## ReDoc

```text
http://127.0.0.1:8000/redoc
```

ReDoc provides a clean, documentation-focused representation of the API.

### Swagger vs ReDoc

| Interface       | Primary Purpose                    |
| --------------- | ---------------------------------- |
| `/docs`         | Interactive API testing            |
| `/redoc`        | API documentation                  |
| `/openapi.json` | Machine-readable API specification |

---

# OpenAPI

FastAPI automatically generates an OpenAPI specification.

```text
http://127.0.0.1:8000/openapi.json
```

The specification describes:

* Available endpoints
* HTTP methods
* Parameters
* Request schemas
* Response schemas
* Data types

The relationship is:

```text
Python Application
       ↓
     FastAPI
       ↓
   OpenAPI Schema
      ↙     ↘
 Swagger    ReDoc
   UI         UI
```

---

# Jinja2 Templates

Jinja2 can be used with FastAPI to generate dynamic HTML pages.

Example:

```python
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
```

A Jinja2 template can contain:

```html
<h1>Hello {{ name }}</h1>
```

Python can provide:

```python
{
    "name": "Vedant"
}
```

Jinja2 renders the final HTML page dynamically.

```text
Python Data
     ↓
  Jinja2
     ↓
Dynamic HTML
     ↓
  Browser
```

---

# Example Application

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "FastAPI is running"
    }


@app.get("/hello")
def hello():
    return {
        "message": "Hello World"
    }


@app.get("/add")
def add(a: int, b: int):
    return {
        "result": a + b
    }
```

### Available Endpoints

| Method | Endpoint        | Description           |
| ------ | --------------- | --------------------- |
| GET    | `/`             | Health/status check   |
| GET    | `/hello`        | Returns a greeting    |
| GET    | `/add`          | Adds two integers     |
| GET    | `/docs`         | Swagger UI            |
| GET    | `/redoc`        | ReDoc                 |
| GET    | `/openapi.json` | OpenAPI specification |

---

# Request Lifecycle

A typical FastAPI request follows this flow:

```text
Client
   ↓
HTTP Request
   ↓
FastAPI Router
   ↓
Parameter Extraction
   ↓
Validation
   ↓
Python Function
   ↓
Response
   ↓
JSON
   ↓
Client
```

For example:

```text
GET /add?a=10&b=20
          ↓
       FastAPI
          ↓
     add(10, 20)
          ↓
        30
          ↓
{"result": 30}
```

---

# FastAPI in AI Applications

FastAPI can serve as the backend layer for modern AI applications.

```text
Frontend
   ↓
FastAPI
   ↓
AI Application
   ↓
┌───────────────┐
│               │
RAG         LangGraph
│               │
Vector DB      Tools
│               │
└───────┬───────┘
        ↓
       LLM
```

This makes FastAPI useful for exposing:

* Machine Learning models
* RAG pipelines
* LLM applications
* LangGraph workflows
* AI Agents
* Data processing services

---

# Learning Roadmap

```text
FastAPI Fundamentals
        ↓
Endpoints & HTTP Methods
        ↓
Query Parameters
        ↓
Path Parameters
        ↓
POST Requests
        ↓
Request Body
        ↓
Pydantic
        ↓
Response Models
        ↓
Error Handling
        ↓
File Uploads
        ↓
CORS
        ↓
Authentication
        ↓
Database Integration
        ↓
Routers
        ↓
ML APIs
        ↓
RAG APIs
        ↓
LangGraph & AI Agents
```

---

## Goal

The objective of this repository is to build a strong foundation in **backend API development with FastAPI** and progressively apply it to production-oriented **AI/ML applications**.

> **FastAPI → Backend APIs → AI/ML Services → RAG → AI Agents**

````

