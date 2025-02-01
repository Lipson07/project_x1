from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.faq import Faq
from app.schemas.faq import FaqCreate, FaqUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDFaq(CRUDBase[Faq, FaqCreate, FaqUpdate]):

    model = Faq

    def __init__(self):
        super().__init__(Faq)


faq = CRUDFaq()
