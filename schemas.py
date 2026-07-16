from pydantic import BaseModel, ConfigDict, Field
from models import TStatus
from typing import Literal


class AuthorSchema(BaseModel):
    name: str
    age: int


class TodoBase(BaseModel):
    title: str
    author: AuthorSchema
    keywords: list[str]
    completed: TStatus = TStatus.PENDING


class TodoCreate(TodoBase):
    pass


class TodoResponse(TodoBase):
    todo_id: int
    model_config = ConfigDict(from_attributes=True)


