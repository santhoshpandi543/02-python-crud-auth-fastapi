from fastapi import FastAPI, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated

# Our File
from app.routers import todos
from app.schemas.todos import TodoResponse, TodoCreate, QueryParams
from app.database import engine, Base
from app.models.todos import Todo as TodoModel

# To tell Sqlalchemy to build the tables in Postgre
Base.metadata.create_all(bind=engine)


def create_app()->FastAPI:   

    # app = FastAPI(dependencies=[Depends(get_db)])
    app = FastAPI(title='Todo App')

    # To link the various routers [users, products, orders]
    app.include_router(todos.router)

    return app

app = create_app()

