from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import  ForeignKey

from app.db.base_class import Base
from app.models.user import User
from app.models.project import Project

class Participant(Base):

    __tablename__ = "participants"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id", ondelete='cascade'))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete='cascade'))

    project: Mapped[Project] = relationship("Project", lazy="joined", cascade="all")
    user: Mapped[User] = relationship("User", lazy="joined", cascade="all")