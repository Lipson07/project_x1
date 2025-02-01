
from sqlalchemy import Integer, String, Column, Boolean, Float, Text
from sqlalchemy.dialects.mysql import VARCHAR
from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class Project(Base):

    __tablename__ = "projects"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    started_at: Mapped[datetime]
    deadline: Mapped[datetime]