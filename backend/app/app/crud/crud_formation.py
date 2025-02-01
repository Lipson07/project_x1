from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.formation import Formation
from app.schemas.formation import FormationCreate, FormationUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDFormation(CRUDBase[Formation, FormationCreate, FormationUpdate]):

    model = Formation

    def __init__(self):
        super().__init__(Formation)


formation = CRUDFormation()
