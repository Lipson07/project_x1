from .base import BaseExcption
from fastapi import status


class CredentialsException(BaseExcption):
    status_code = status.HTTP_401_UNAUTHORIZED,
    detail = "Could not validate credentials",
    headers = {"WWW-Authenticate": "Bearer"}


class ExistedEmailException(BaseExcption):
    status_code = 400
    detail = "The user with this email already exists in the system"


class UserAlreadyExistsException(BaseExcption):
    status_code = 400
    detail = "The user with this phone already exists in the system"


class IncorrectUsernameOrPasswordException(BaseExcption):
    status_code = 400,
    detail = "Incorrect username or password"


class IncorrectPhoneOrPasswordException(BaseExcption):
    status_code = 400,
    detail = "Incorrect phone or password"


class IncorrectPhoneException(BaseExcption):
    status_code = 400,
    detail = "Incorrect phone"

class PasswordMismatchException(BaseExcption):
    status_code = 400,
    detail = "Password Mismatch"