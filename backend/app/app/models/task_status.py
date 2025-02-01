from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class Task_Status(Base):

    __tablename__ = "task_status"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    status: Mapped[str]
