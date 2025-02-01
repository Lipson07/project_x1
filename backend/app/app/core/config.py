import json
import pathlib
from pydantic import AnyHttpUrl, EmailStr, validator, field_validator, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional, Union, ClassVar
import os

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent


class Settings(BaseSettings):  # 1

    # Here are declared env variables

    API_V1_STR: str = "/api/v1"  # 2
    # You have to change JWT_SECRET in your dev project meanwhile JWT_SECRET: str = "TEST_SECRET_DO_NOT_USE_IN_PROD"
    JWT_SECRET: str = "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    ALGORITHM: str = "HS256"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # My own resolution for activating use account
    ACTIVATION_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins e.g: '["http://localhost", "http://localhost:4200",
    # "http://localhost:3000", \ "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    # BACKEND_CORS_ORIGINS: Union[str, List[AnyHttpUrl]] = Field(..., env="BACKEND_CORS_ORIGINS")
    # BACKEND_CORS_ORIGINS: Union[str, List[AnyHttpUrl]] = os.environ.get('BACKENDS_CORS_ORIGINS') it is woking fine
    # 23.03.2023

    BACKEND_CORS_ORIGINS:ClassVar[List[AnyHttpUrl]] = ["http://localhost:3000/", "http://localhost:8080/", "http://localhost:8001/"]


    # Origins that match this regex OR are in the above list are allowed
    BACKEND_CORS_ORIGIN_REGEX: Optional[
        str
    ] = "https.*\.(netlify.app|herokuapp.com)"  # noqa: W605

    '''
    # @field_validator("BACKEND_CORS_ORIGINS", pre=True)
    @field_validator("BACKEND_CORS_ORIGINS")  # 3
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        # print("\n******** BACKEND_CORS_OIGINS: {}\n".format(v))
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    '''

    # Here are declared env variables
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    FIRST_ADMIN: EmailStr = "djeguede.marc@gmail.com"



    class Config:
        case_sensitive = True  # 4
        # from_attributes = True


settings = Settings()  # 5
