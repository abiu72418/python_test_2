from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    task: str
    completed: bool = False

@app.get('/todos', response_model=List[Todo])
def get_todos():
    return todos

@app.post('/todos', response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, todo: Todo):
    for index, t in enumerate(todos):
        if t.id == todo_id:
            todos[index] = todo
            return todo
    return None

@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return {'message': 'Todo deleted'}
