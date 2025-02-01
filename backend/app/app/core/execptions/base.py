from fastapi import HTTPException
from typing import Any


class BaseExcption(HTTPException):
    status_code: Any = ...
    detail: Any = ...
    headers: Any = ...

    def __int__(self) -> None:
        super.__init__(status_code=self.status_code, detail=self.detail, headers=self.headers)
