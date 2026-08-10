#Goal: Enpoints
from fastapi import FastAPI  
from sqlalchemy import select

from app.database import get_session
from app.models.projects import Project
from app.schemas.projects import ProjectResponse


app = FastAPI(
    title="Dolphin Portfolio API",
    version="0.2.0",
)


#GET
@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Dolphin Portfolio API is running"
    }

@app.get("/api/projects", response_model=ProjectResponse) #defines path and automatically format to match schema
def get_project():
    session = get_session()
    try:
        statement = select(Project)
        projects = session.scalars(statement).all() 
        return projects
    except Exception:
        print("API/GET - Project: Invalid")
    finally:
        session.close()


        


