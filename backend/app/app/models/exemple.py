
from sqlalchemy import Integer, String, Column, Boolean, Float
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class Exemple(Base):
    '''
    This is an exemple of model
    '''

    __tablename__ = "exemples"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    string_attribute: Mapped[str]  = mapped_column(index=True)
    integer_attribute: Mapped[int]  = mapped_column( index=True)
    float_attribute: Mapped[float]  = mapped_column(index=True)
    boolean_attribute: Mapped[bool]  = mapped_column(index=True)
    '''recipes = relationship(
        "Recipe",
        cascade="all,delete-orphan",
        back_populates="submitter",
        uselist=True,
    )'''
    # /*
    # relationship keyword here stands for relatioship with another table
    # */
