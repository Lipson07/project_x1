from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class Location(Base):

    __tablename__ = "locations"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    city: Mapped[str]
    country: Mapped[str]