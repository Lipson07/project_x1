from datetime import datetime
from sqlalchemy import  ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.project import Project

class Task(Base):

    __tablename__ = "tasks"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    project_id: Mapped[int] = mapped_column( ForeignKey("projects.id", ondelete='cascade') )

    project: Mapped[Project] = relationship("Project", lazy="joined", cascade="all")


