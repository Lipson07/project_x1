from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models.exemple import Exemple
from app.schemas.exemple import ExempleCreate, ExempleUpdate


class CRUDExemple(CRUDBase[Exemple, ExempleCreate, ExempleUpdate]):
    '''We have to define your methods here'''

    def __init__(self):
        super().__init__(Exemple)

    async def get(self, db: AsyncSession, id: Any) -> Optional[Exemple]:
        return await super().get_by_id(db, id)

    async def get_multi(self, db: AsyncSession, *, skip: int = 0, limit: int = 5000) -> List[Exemple]:
        print(self.model)
        return await super().get_all(db, skip=skip, limit=limit)

        # result = await db.execute(select(Exemple).limit(limit))
        # return result.scalars().all()


exemple = CRUDExemple()

#/****
#
#
# ***/
