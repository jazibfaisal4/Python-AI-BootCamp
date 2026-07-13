from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="To-Do List API",
    description="A simple To-Do List REST API for Lab 6",
    version="1.0.0"
)

# In-memory storage (Python list)
todos = []
current_id = 1

# Pydantic models
class TodoCreate(BaseModel):
    title: str

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

#QUESTION 1: POST /todos
@app.post("/todos", response_model=TodoResponse, status_code=201)
def create_todo(todo: TodoCreate):
    """Add a new task"""
    global current_id
    new_todo = {
        "id": current_id,
        "title": todo.title,
        "completed": False
    }
    todos.append(new_todo)
    current_id += 1
    return new_todo

#QUESTION 2: GET /todos 
@app.get("/todos", response_model=List[TodoResponse])
def get_all_todos():
    """Retrieve all tasks"""
    return todos

#QUESTION 3: GET /todos/{id}
@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo_by_id(todo_id: int):
    """Retrieve a specific task by ID"""
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail=f"Task with ID {todo_id} not found")

#QUESTION 4: PUT /todos/{id}
@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, updated_data: TodoUpdate):
    """Update an existing task"""
    for todo in todos:
        if todo["id"] == todo_id:
            if updated_data.title is not None:
                todo["title"] = updated_data.title
            if updated_data.completed is not None:
                todo["completed"] = updated_data.completed
            return todo
    raise HTTPException(status_code=404, detail=f"Task with ID {todo_id} not found")

#QUESTION 5: DELETE /todos/{id}
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """Delete a task by ID"""
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(index)
            return {"message": f"Task with ID {todo_id} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Task with ID {todo_id} not found")

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to To-Do List API",
        "docs": "/docs",
        "redoc": "/redoc"
    }