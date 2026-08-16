"""
Purpose:
Represent the PostgreSQL projects table as a Python ORM model.

Responsibilities:
- Define project columns
- Define column types
- Define database constraints

"""

from sqlalchemy import Integer, Boolean, String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base
from datetime import datetime


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    slug: Mapped[str] = mapped_column(String(150), nullable=False) #URL-friendly identifier
    category: Mapped[str] = mapped_column(String(150), nullable=False)
    role: Mapped[str] = mapped_column(String(100), nullable=True)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    image_url: Mapped[str | None]  = mapped_column(Text, nullable = True)
    github_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    demo_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    featured: Mapped[bool] = mapped_column(Boolean, nullable=True)
    display_order: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)

    def __repr__(self) -> str:
        return f"Project(id={self.id}, title={self.title}, slug={self.slug}, category={self.category}, role={self.role})"



