"""
database.py

Purpose:
Create and manage the database connection.(for Neon - PostgresSQL)

Responsibilities:
- Connect to Neon
- Create SQLAlchemy Engine
- Provide Sessions

Does NOT:
- Define API routes
- Execute business logic
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from dotenv import load_dotenv #reads variables from a .env file and sets them in os.environment

load_dotenv() #parses .env file

db_url = os.getenv("DATABASE_URL")

def get_engine():
    return create_engine(db_url)

if __name__ == "__main__":
    try: 
        engine = get_engine()
        print("DATABASE: connection to database created sucessfully.")
    except Exception as e:
        print("DATABASE: Failed to connect to the database.")

        


