from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.skill_type import Skill_Type
from app.schemas.skill_type import Skill_TypeCreate, Skill_TypeUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDSkill_Type(CRUDBase[Skill_Type, Skill_TypeCreate, Skill_TypeUpdate]):

    model = Skill_Type

    def __init__(self):
        super().__init__(Skill_Type)


skill_type = CRUDSkill_Type()
