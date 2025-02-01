from sqlalchemy import Integer, String, Column, Boolean, Float, ForeignKey, TIMESTAMP
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.base_class import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String().with_variant(VARCHAR, "sqlite"))


