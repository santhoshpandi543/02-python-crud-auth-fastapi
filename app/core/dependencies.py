from contextvars import ContextVar
from sqlalchemy.orm import Session

from app.core.database import SessionLocal

# Create a request-isolated global context variable
db_context: ContextVar[Session] = ContextVar("db_context")


# Dependency for DB session
async def get_db():
    db = SessionLocal()
    token = db_context.set(db)  # Store the session for specific request
    try:
        yield db
    finally:
        db.close()
        db_context.reset(token)
