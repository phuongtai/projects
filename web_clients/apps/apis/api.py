
from fastapi import APIRouter

from apps.doctor import endpoints as doctor

api_router = APIRouter()
api_router.include_router(doctor.router, prefix="/doctor", tags=["items"])
