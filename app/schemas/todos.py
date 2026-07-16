from pydantic import BaseModel, ConfigDict, Field
from app.models.todos import TStatus
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

# Pagination, Filtering & Search Schema
class QueryParams(BaseModel):
    page:int = Field(1, ge=1)
    skip: int = Field(0, ge=0)
    limit: int = Field(10, ge=0)
    search: str = ''
    filter_by: Literal['PENDING','SUCCESS','COMPLETED'] | None = None
    sort_by: Literal['asc','desc'] = 'asc'