from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker, DeclarativeBase;

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo= True, # Prints SQL queries in terminal
    pool_pre_ping=True # Tests connection before running..
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase):
    pass


