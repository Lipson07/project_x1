from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.task_status import Task_Status
from app.schemas.task_status import Task_StatusCreate, Task_StatusUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDTask_Status(CRUDBase[Task_Status, Task_StatusCreate, Task_StatusUpdate]):

    model = Task_Status

    def __init__(self):
        super().__init__(Task_Status)


task_status = CRUDTask_Status()
