from sqlalchemy import Integer, String, Column, Boolean, Float, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship, validates, Mapped, mapped_column

from app.db.base_class import Base
from typing import TYPE_CHECKING, Optional

from app.models.role import Role

class User(Base):
    __tablename__ = "users"


    id: Mapped[int] = mapped_column( primary_key=True, index=True, autoincrement=True)
    nickname: Mapped[str] = mapped_column(String().with_variant(VARCHAR, "sqlite"))
    firstname: Mapped[Optional[str]]
    lastname: Mapped[Optional[str]]
    hashed_password: Mapped[str] = mapped_column(String().with_variant(VARCHAR, "sqlite"))
    email: Mapped[Optional[str]]
    phone: Mapped[str]  = mapped_column(String().with_variant(VARCHAR, "sqlite"), index=True, unique=True)
    activated: Mapped[Optional[bool]] = mapped_column()
    role_id: Mapped[Optional[int]] = mapped_column( ForeignKey("roles.id", ondelete='cascade') )

    role:Mapped[Optional[Role]] = relationship("Role", lazy="joined", cascade="all")

    '''
    @validates("role")
    def validate_model_role(cls, key, value) -> Role:
        """Instantiate User_Type object if it is only dict."""
        if value and isinstance(value, dict):
            return Role(**value)
        return value
    '''