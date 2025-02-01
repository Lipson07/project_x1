from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
# from app.models.usertype import UserType
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    model = User
    def __init__(self):
        super().__init__(User)


user = CRUDUser()
