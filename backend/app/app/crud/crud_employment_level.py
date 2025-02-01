from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.employment_level import Employment_Level
from app.schemas.employment_level import Employment_LevelCreate, Employment_LevelUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDEmployment_Level(CRUDBase[Employment_Level, Employment_LevelCreate, Employment_LevelUpdate]):

    model = Employment_Level

    def __init__(self):
        super().__init__(Employment_Level)


employment_level = CRUDEmployment_Level()
