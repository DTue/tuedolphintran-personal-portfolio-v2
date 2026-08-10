from app.database import get_session
from app.models.projects import Project
from sqlalchemy import select


my_session = get_session()

try:
    statement = select(Project) #accep new column args
    projects = my_session.scalars(statement).all()

    for p in projects:
        print(p)
finally:
    my_session.close_all
