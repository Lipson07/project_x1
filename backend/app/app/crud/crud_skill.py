from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDSkill(CRUDBase[Skill, SkillCreate, SkillUpdate]):

    model = Skill

    def __init__(self):
        super().__init__(Skill)


skill = CRUDSkill()
