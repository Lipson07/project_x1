from datetime import datetime
from sqlalchemy import  ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from app.models.user import User

class Message(Base):

    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    sender_id: Mapped[int] = mapped_column( ForeignKey("users.id", ondelete='cascade') )
    recipient_id: Mapped[int] = mapped_column( ForeignKey("users.id", ondelete='cascade') )
    content: Mapped[str] = mapped_column(Text)

    sender: Mapped[User] = relationship("User", foreign_keys=[sender_id],lazy="joined", cascade="all")
    recipient: Mapped[User] = relationship("User", foreign_keys=[recipient_id], lazy="joined", cascade="all")