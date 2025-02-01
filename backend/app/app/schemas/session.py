from pydantic import BaseModel, Field

class SessionData(BaseModel):
    username: str