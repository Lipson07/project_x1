from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.employment_type import Employment_Type
from app.schemas.employment_type import Employment_TypeCreate, Employment_TypeUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDEmployment_Type(CRUDBase[Employment_Type, Employment_TypeCreate, Employment_TypeUpdate]):

    model = Employment_Type

    def __init__(self):
        super().__init__(Employment_Type)


employment_type = CRUDEmployment_Type()
