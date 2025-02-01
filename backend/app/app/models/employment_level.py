from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class Employment_Level(Base):

    __tablename__ = "employment_levels"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    level: Mapped[str]
