from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class File(Base):

    __tablename__ = "files"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    path: Mapped[str]