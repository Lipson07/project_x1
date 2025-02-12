from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, endpoint_example
from app.api.api_v1.endpoints import (
    endpoint_user, endpoint_role, endpoint_file, endpoint_faq, endpoint_locations,
    endpoint_employment_levels, endpoint_employment_types, endpoint_skill_types,
    endpoint_skills, endpoint_has_skils
    )
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

api_router.include_router(endpoint_faq.router, prefix="/faq", tags=["faq"])
api_router.include_router(endpoint_locations.router, prefix="/location", tags=["location"])
api_router.include_router(endpoint_employment_levels.router, prefix="/employment_level", tags=["employment_level"])
api_router.include_router(endpoint_employment_types.router, prefix="/employment_type", tags=["employment_type"])
api_router.include_router(endpoint_skill_types.router, prefix="/skill_type", tags=["skill_type"])
api_router.include_router(endpoint_skills.router, prefix="/skill", tags=["skill"])
api_router.include_router(endpoint_has_skils.router, prefix="/has_skill", tags=["has_skill"])