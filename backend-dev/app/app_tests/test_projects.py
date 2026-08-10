from app.database import get_session
from app.models.projects import Project
from sqlalchemy import select



#mock 
project = Project(
    title="DARK",
    slug="dark",
    category="Software",
    role="Lead Developer",
    summary="Privacy-first AI SMS system connecting unhoused individuals with community resources.",
    image_url=None,
    github_url=None,
    demo_url=None,
    featured=True,
    display_order=1,
    
)

my_session = get_session()

try:
    my_session.add(project) #add mock project data
    my_session.commit() #commit changes
    my_session.refresh(project) #reload values
    statement = select(Project) #accep new column args
    projects = my_session.scalars(statement).all()

    for p in projects:
        print(p)
finally:
    my_session.close_all
