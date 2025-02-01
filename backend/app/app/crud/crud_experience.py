from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.experience import Experience
from app.schemas.experience import ExperienceCreate, ExperienceUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDExperience(CRUDBase[Experience, ExperienceCreate, ExperienceUpdate]):

    model = Experience

    def __init__(self):
        super().__init__(Experience)


experience = CRUDExperience()
