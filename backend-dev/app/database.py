"""
database.py

Purpose:
Create and manage the database connection.(for Neon - PostgresSQL)

Goals:
- Connect to Neon
- Create SQLAlchemy Engine
- Provide Sessions
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker
from dotenv import load_dotenv #reads variables from a .env file and sets them in os.environment

load_dotenv() #parses .env file

db_url = os.getenv("DATABASE_URL")

#Modify psycopg2 to psycopg3
if db_url.startswith("postgresql://"):
    db_url = db_url.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    )

if not db_url:
    raise RuntimeError("DATABASE_URL is invalid or missing")

#Engine
def get_engine() -> Engine: #helper
    return create_engine(db_url)

engine = get_engine()

#Session: commenucate database through ORM + Session uses engine to connect resources
DatabaseSession = sessionmaker(bind=engine) #factory that creates sessions -> "class"

def get_session() -> Session: #helper
    return DatabaseSession()

my_session = get_session() #session object -> "object instance created from a class"








        


