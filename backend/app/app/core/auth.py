from typing import Optional, MutableMapping, List, Union
from datetime import datetime, timedelta

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from jose import jwt

from app.models.user import User
from app.core.config import settings
from app.core.security import verify_password

JWTPayloadMapping = MutableMapping[
    str, Union[datetime, bool, str, List[str], List[int]]
]

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth_prefix/login", scheme_name="JWT")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth_prefix/login")

get_bearer_token = HTTPBearer(auto_error=False)  # Alternative to OAuth2PasswordBearer


async def authenticate(
        *,
        phone: str,
        password: str,
        db: AsyncSession,
) -> Optional[User]:
    user = await db.execute(select(User).where(User.phone == phone))
    user = user.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code="404", detail="Unknown phone number")
    if user and not verify_password(password, user.hashed_password):  # 1
        raise HTTPException(status_code="404", detail="Incorrect password")
    return user



def create_access_token(*, sub: str) -> str:  # 2
    return _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),  # 3
        sub=sub,
    )


def create_activation_token(*, sub: str) -> str:  # 2
    return _create_token(
        token_type="activation_token",
        lifetime=timedelta(minutes=settings.ACTIVATION_TOKEN_EXPIRE_MINUTES),  # 3
        sub=sub,
    )


def _create_token(
        token_type: str,
        lifetime: timedelta,
        sub: str,
) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire  # 4
    payload["iat"] = datetime.utcnow()  # 5
    payload["sub"] = str(sub)  # 6

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)  # 8


def _decode_token(token, ) -> str:
    decoded_token = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
    return decoded_token["sub"]
