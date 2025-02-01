
from typing import Optional, ClassVar, Dict
from pydantic import BaseModel, EmailStr, validator, field_validator, Field
from fastapi.param_functions import Form
from fastapi import HTTPException
import re


class AuthPhoneForm(BaseModel):
    phone: str = Form()  # indeed it's a phone number
    password: str = Form()

    @field_validator("phone")
    def phone_validation(cls, v):
        regex = r"^(\+)[1-9][0-9]{9,15}$"
        if v and not re.search(regex, v, re.I):
            raise HTTPException(status_code=400, detail="Phone Number Invalid.")
        return v


class LoginBase(BaseModel):
    password: str


class LoginPhone(LoginBase):
    phone: str
