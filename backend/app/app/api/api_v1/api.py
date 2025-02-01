from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, endpoint_example
from app.api.api_v1.endpoints import endpoint_user, endpoint_role, endpoint_file
from app.api.api_v1.endpoints.admin import  endpoint_admin
from  app.api.api_v1.endpoints.common_part import endpoint_mainpage

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth_prefix", tags=["auth_prefix"])
api_router.include_router(endpoint_example.router, prefix="/example_prefix", tags=["example_prefix"])

api_router.include_router(endpoint_user.router, prefix="/user_prefix", tags=["user_prefix"])
api_router.include_router(endpoint_role.router, prefix="/role_prefix", tags=["role_prefix"])
api_router.include_router(endpoint_file.router, prefix="/file_prefix", tags=["file_prefix"])

api_router.include_router(endpoint_admin.router, prefix="/admin_prefix", tags=["admin_prefix"])
api_router.include_router(endpoint_mainpage.router, prefix="/main_page", tags=["main_page"])

