from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.project_document_type import Project_Document_Type
from app.schemas.project_document_type import Project_Document_TypeCreate, Project_Document_TypeUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDProject_Document_Type(CRUDBase[Project_Document_Type, Project_Document_TypeCreate, Project_Document_TypeUpdate]):

    model = Project_Document_Type

    def __init__(self):
        super().__init__(Project_Document_Type)


project_document_type = CRUDProject_Document_Type()
