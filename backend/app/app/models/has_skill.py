from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.user import User
from app.models.skill import Skill

class Has_Skill(Base):

    __tablename__ = "has_skills"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    user_id: Mapped[int] = mapped_column( ForeignKey("users.id", ondelete='cascade') )
    skill_id: Mapped[int] = mapped_column( ForeignKey("skills.id", ondelete='cascade') )

    user: Mapped[User] = relationship("User", lazy="joined", cascade="all")
    skill: Mapped[Skill] = relationship("Skill", lazy="joined", cascade="all")