from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.has_skill import Has_Skill
from app.schemas.has_skill import Has_SkillCreate, Has_SkillUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDHas_Skill(CRUDBase[Has_Skill, Has_SkillCreate, Has_SkillUpdate]):

    model = Has_Skill

    def __init__(self):
        super().__init__(Has_Skill)


has_skill = CRUDHas_Skill()
