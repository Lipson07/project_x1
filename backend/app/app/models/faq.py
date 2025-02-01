from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base


class Faq(Base):

    __tablename__ = "faqs"

    id: Mapped[int]  = mapped_column(primary_key=True, autoincrement=True, index=True)
    question:Mapped[str]
    answer: Mapped[str]