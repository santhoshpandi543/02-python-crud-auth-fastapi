from sqlalchemy import Column, ForeignKey, String, Boolean, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from enum import Enum

# From our File
from database import Base


class TStatus(Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class Todo(Base):
    __tablename__ = "todos"

    todo_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[dict] = mapped_column(JSONB, nullable=False)
    keywords: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    completed: Mapped[TStatus] = mapped_column(
        SqlEnum(TStatus), default=TStatus.PENDING
    )
