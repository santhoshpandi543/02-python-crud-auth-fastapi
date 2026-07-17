from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Annotated
from sqlalchemy.orm import Session

# Our Files
from app.schemas.todos import TodoResponse, TodoCreate, QueryParams
from app.models.todos import Todo as TodoModel
from app.core.dependencies import get_db
from app.services.todos import TodoService

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    dependencies=[Depends(get_db)],
    # responses={}
)

service = TodoService()


# POST - Create Todo
@router.post("/", response_model=TodoResponse)
def create_todo(todo: TodoCreate):
    return service.create(todo)


# GET - Get All Todos
@router.get("/", response_model=list[TodoResponse])
def get_all_todos(filter_query: Annotated[QueryParams, Query()]):
    return service.get_all(filter_query)


# GET - Get Single Todo
@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo_by_id(todo_id: int):
    todo = service.get_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo id Invalid")
    return todo


# PUT - Update Todo
@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, updated_data: TodoCreate):

    result = service.update(todo_id=todo_id, updated_data=updated_data)

    if result["success"] == False:
        if result["error"] == "NOT_FOUND":
            raise HTTPException(status_code=404, detail=result["message"])

    return result["data"]


# DEL - Delete Todo
@router.delete("/{todo_id}", status_code=200)
def delete_todo(todo_id: int):
    
    result = service.delete(todo_id=todo_id)

    if result["success"] == False:
        if result["error"] == "NOT_FOUND":
            raise HTTPException(status_code=404, detail=result["message"])

    return result
