from sqlalchemy.orm import Session
from fastapi import Query
from typing import Annotated

from app.models.todos import Todo as TodoModel
from app.schemas.todos import TodoCreate, QueryParams
from app.core.dependencies import db_context


class TodoService:

    @property
    def db(self):
        return db_context.get()

    def create(self, todo: TodoCreate) -> TodoModel:
        # Since `**Pydantic obj**` is differ from `SqlAlchemy obj`, we can't simply pass it in the Database. so,

        todo_data = todo.model_dump()  # Pydantic obj -> Python dict

        db_todo = TodoModel(**todo_data)  # Python dict -> SqlAlchemy object

        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)

        return db_todo

    def get_all(self, filter_query: Annotated[QueryParams, Query()]) -> list[TodoModel]:
        print(filter_query)
        return self.db.query(TodoModel).all()

    def get_by_id(self, todo_id: int) -> TodoModel | None:
        todo = self.db.query(TodoModel).filter(TodoModel.todo_id == todo_id).first()
        return todo

    def update(self, todo_id: int, updated_data: TodoCreate):
        todo = self.get_by_id(todo_id)

        if not todo:
            return {"success": False, "error": "NOT_FOUND", "message": "Todo not found"}

        updated_dict = updated_data.model_dump()

        for key, value in updated_dict.items():
            setattr(todo, key, value)

        self.db.commit()
        self.db.refresh(todo)

        return {"success": True, "message": "Todo Updated", "data": todo}

    def delete(self, todo_id: int):
        todo = self.get_by_id(todo_id)

        if not todo:
            return {"success": False, "error": "NOT_FOUND", "message": "Todo not found"}

        self.db.delete(todo)
        self.db.commit()

        return {
            "success": True,
            "message": f"Todo with id {todo_id} has been successfully deleted",
        }
