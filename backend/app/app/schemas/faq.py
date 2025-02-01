from typing import Optional, Dict

from pydantic import BaseModel, validator, EmailStr, field_validator, Field
from app.schemas.role import Role
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
import re


class FaqBase(BaseModel):
    nickname: Optional[str] = Field(..., description="")

    question: str = Field(..., description="")
    answer: str = Field(..., description="")




# Properties to receive via API on creation
class FaqCreate( FaqBase):
    ...


# Properties to receive via API on update
class FaqUpdate( FaqBase):
    ...


class FaqInDBBase( FaqBase):
    id: Optional[int] = Field(description="", default=None)

    class Config:
        # orm_mode = True
        from_attributes = True


# Additional properties to return via API
class Faq(FaqInDBBase):
    pass
