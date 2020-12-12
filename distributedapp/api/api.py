from fastapi import APIRouter
from .endpoints import  endpoints


def create_router_endpoints():

    api_router = APIRouter()

    api_router.include_router(endpoints.router)
    return api_router
