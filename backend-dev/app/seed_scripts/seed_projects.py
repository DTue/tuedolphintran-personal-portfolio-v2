#Purpose: How data gets inserted
from seed_scripts.seed_data.projects import projects
from models.projects import Project
from database import get_session
from sqlalchemy import text

def seed_projects(): 
    my_session = get_session()
    try:
        #my_session.execute(text("TRUNCATE TABLE projects RESTART IDENTITY")) 
        my_session.add_all(projects)
        my_session.commit()
        print("SEED: projects added sucessfully")
        for p in projects:
            print(p)
    except Exception:
        my_session.rollback()
        raise

    finally:
        my_session.close()

