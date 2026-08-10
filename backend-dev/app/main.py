#Goal: Enpoints
from fastapi import FastAPI  
from sqlalchemy import select

from app.database import get_session
from app.models.projects import Project
from app.schemas.projects import ProjectResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Dolphin Portfolio API",
    version="0.2.0",
)

origin = [ "http://localhost:5173"]

app.add_middleware(CORSMiddleware, allow_origins=origin, allow_credentials=True, allow_methods=["*"],allow_headers=["*"])


#GET
@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Dolphin Portfolio API is running"
    }

@app.get("/api/projects", response_model=list[ProjectResponse]) #defines path and automatically format to match schema
def get_projects():
    session = get_session()

    try:
        statement = select(Project).order_by(Project.display_order)
        projects = session.scalars(statement).all() 

        return projects
    except Exception as error:
        print(f"API/GET - Project failed: {error}")
        raise
    finally:
        session.close()


        


