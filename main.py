from fastapi import FastAPI, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

# Our File
from schemas import TodoResponse, TodoCreate
from database import SessionLocal, engine, Base
from models import Todo as TodoModel

# To tell Sqlalchemy to build the tables in Postgre
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST - Create Todo
@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):

    # Since `**Pydantic obj**` is differ from `SqlAlchemy obj`, we can't simply pass it in the Database. so,

    todo_data = todo.model_dump() # Pydantic obj -> Python dict

    db_todo = TodoModel(**todo_data) # Python dict -> SqlAlchemy object

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

    return db_todo


# GET - Get All Todos
@app.get("/todos", response_model=list[TodoResponse])
def get_all_todos(
    # filter_query: Annotated[QueryParams, Query()],
    db: Session = Depends(get_db),
):
    # print(filter_query)
    return db.query(TodoModel).all()


# GET - Get Single Todo
@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.todo_id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo id Invalid")
    return todo


# PUT - Update Todo
@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, updated_data: TodoCreate, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.todo_id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo id Invalid")

    updated_dict = updated_data.model_dump()

    for key, value in updated_dict.items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)

    return todo


# DEL - Delete Todo
@app.delete("/todos/{todo_id}", status_code=200)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.todo_id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo id Invalid")

    db.delete(todo)
    db.commit()

    return {"message": f"Todo with id {todo_id} has been successfully deleted"}
