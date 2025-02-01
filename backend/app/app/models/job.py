from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.employment_type import Employment_Type
from app.models.employment_level import Employment_Level

class Job(Base):

    __tablename__ = "jobs"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    position: Mapped[str]
    description: Mapped[str]
    company: Mapped[str]
    salary: Mapped[int]
    employment_level_id: Mapped[int] = mapped_column( ForeignKey("employment_levels.id", ondelete='cascade') )
    employment_type_id: Mapped[int] = mapped_column( ForeignKey("employment_types.id", ondelete='cascade') )

    employment_level: Mapped[Employment_Level] = relationship("Employment_Level", lazy="joined", cascade="all")
    employment_type: Mapped[Employment_Type] = relationship("Employment_Type", lazy="joined", cascade="all")