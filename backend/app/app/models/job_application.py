from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.job import Job
from app.models.file import File

class Job_Application(Base):

    __tablename__ = "job_applications"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    fullname: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    letter: Mapped[str]
    job_id: Mapped[int] = mapped_column( ForeignKey("jobs.id", ondelete='cascade') )
    cv_id: Mapped[int] = mapped_column( ForeignKey("files.id", ondelete='cascade') )

    job: Mapped[Job] = relationship("Job", lazy="joined", cascade="all")
    cv: Mapped[File] = relationship("File", lazy="joined", cascade="all")