from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.project import Project
from app.models.project_document_type import Project_Document_Type
from app.models.file import File
from app.models.user import User


class Project_Document(Base):

    __tablename__ = "project_documents"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    project_id: Mapped[int] = mapped_column( ForeignKey("projects.id", ondelete='cascade') )
    doctype_id: Mapped[int] = mapped_column( ForeignKey("project_document_types.id", ondelete='cascade') )
    file_id: Mapped[int] = mapped_column( ForeignKey("files.id", ondelete='cascade') )
    user_id: Mapped[int] = mapped_column( ForeignKey("users.id", ondelete='cascade') )

    project: Mapped[Project] = relationship("Project", lazy="joined", cascade="all")
    doctype: Mapped[Project_Document_Type] = relationship("Project_Document_Type", lazy="joined", cascade="all")
    file: Mapped[File] = relationship("File", lazy="joined", cascade="all")
    user: Mapped[User] = relationship("User", lazy="joined", cascade="all")