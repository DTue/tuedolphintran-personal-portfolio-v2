from pydantic import BaseModel,ConfigDict
from datetime import datetime

class ProjectResponse(BaseModel):

    title: str
    slug: str
    category: str
    role: str
    summary: str
    image_url: str | None
    github_url: str | None
    demo_url: str | None
    featured: bool
    display_order: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True) #allows to build this schema from SQLAlchemy objects



