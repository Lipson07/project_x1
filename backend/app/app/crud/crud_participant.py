from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.participant import Participant
from app.schemas.participant import ParticipantCreate, ParticipantUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDParticipant(CRUDBase[Participant, ParticipantCreate, ParticipantUpdate]):

    model = Participant

    def __init__(self):
        super().__init__(Participant)


participant = CRUDParticipant()
