from sqlalchemy import Column, ForeignKey, String, Boolean
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from enum import Enum


class TStatus(Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class Author:
    name: str
    age: int


class Todo(Base):
    __tablename__ = "todos"

    todo_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[Author]
    keywords: Mapped[list[str]]
    completed: Mapped[TStatus] = mapped_column(default="PENDING")
