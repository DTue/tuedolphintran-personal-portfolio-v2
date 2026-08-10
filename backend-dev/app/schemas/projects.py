from pydantic import BaseModel,ConfigDict

class ProjectResponse(BaseModel):
    id: int
    title: str
    slug: str
    category: str
    role: str
    summery: str
    image_url: str
    github_url: str
    demo_url: str
    featured: bool
    display_order: int
    created_at: int

    model_config = ConfigDict(from_attributes=True) #allows to build this schema from SQLAlchemy objects



