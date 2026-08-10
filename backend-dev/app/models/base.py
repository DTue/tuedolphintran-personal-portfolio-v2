"""
Purpose: Provide base class with SQLAlchemy ORM models + parent for all models
"""
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass #null operation

