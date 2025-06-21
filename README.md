# Todo App (FastAPI)

## Features
- Create, Read, Update, Delete todos
- Built with FastAPI and SQLite

## APIs

### POST /todos/
Create a todo
```json
{ "title": "Test", "description": "Test desc", "completed": false }
```

### GET /todos/
List all todos

### PUT /todos/{id}
Update a todo

### DELETE /todos/{id}
Delete a todo

## Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
