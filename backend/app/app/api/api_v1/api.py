from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, endpoint_example
from app.api.api_v1.endpoints import endpoint_user, endpoint_role, endpoint_file
from app.api.api_v1.endpoints.admin import  endpoint_admin
from  app.api.api_v1.endpoints.common_part import endpoint_mainpage

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(endpoint_example.router, prefix="/example", tags=["example"])

api_router.include_router(endpoint_user.router, prefix="/user", tags=["user"])
api_router.include_router(endpoint_role.router, prefix="/role", tags=["role"])
api_router.include_router(endpoint_file.router, prefix="/file", tags=["file"])

api_router.include_router(endpoint_admin.router, prefix="/admin", tags=["admin"])
api_router.include_router(endpoint_mainpage.router, prefix="", tags=["main_page"])

