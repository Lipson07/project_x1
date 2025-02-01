from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.project_document import Project_Document
from app.schemas.project_document import Project_DocumentCreate, Project_DocumentUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDProject_Document(CRUDBase[Project_Document, Project_DocumentCreate, Project_DocumentUpdate]):

    model = Project_Document

    def __init__(self):
        super().__init__(Project_Document)


project_document = CRUDProject_Document()
