from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class Project_Document_Type(Base):
    __tablename__ = "project_document_types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    doctype: Mapped[str]