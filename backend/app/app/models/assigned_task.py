from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from  app.models.task import Task
from app.models.user import User
from app.models.task_status import Task_Status

class Assigned_Task(Base):

    __tablename__ = "assigned_tasks"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    task_id: Mapped[int] = mapped_column( ForeignKey("tasks.id", ondelete='cascade') )
    user_id: Mapped[int] = mapped_column( ForeignKey("users.id", ondelete='cascade') )
    task_status_id: Mapped[int] = mapped_column(ForeignKey("task_status.id", ondelete='cascade'))
    assigned_at: Mapped[datetime]
    deadline: Mapped[datetime]

    task: Mapped[Task] = relationship("Task", lazy="joined", cascade="all")
    user: Mapped[User] = relationship("User", lazy="joined", cascade="all")
    task_status: Mapped[Task_Status] = relationship("Task_Status", lazy="joined", cascade="all")
