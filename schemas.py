from pydantic import BaseModel
from models import TStatus, Author


class TodoBase(BaseModel):
    title: str
    author: Author
    keywords: list[str]
    completed: TStatus = TStatus.PENDING

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int
    class Config:
        orm_mode = True