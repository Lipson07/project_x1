from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.skill_type import Skill_Type

class Skill(Base):

    __tablename__ = "skills"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    description: Mapped[str]
    skill_type_id: Mapped[int] = mapped_column( ForeignKey("skill_types.id", ondelete='cascade') )

    skill_type: Mapped[Skill_Type] = relationship("Skill_Type", lazy="joined", cascade="all")