from fastapi import APIRouter
from .endpoints import  endpoints


def create_router_endpoints():

    api_router = APIRouter()

    api_router.include_router(endpoints.router)
    # api_router.include_router(intermodal.router, prefix="/routing")
    # api_router.include_router(intermodal.router, prefix="/routing")
    # api_router.include_router(intermodal.router, prefix="/routing")
    # api_router.include_router(intermodal.router, prefix="/routing")
    # api_router.include_router(intermodal.router, prefix="/routing")
    # api_router.include_router(intermodal.router, prefix="/routing")
    # api_router.include_router(intermodal.router, prefix="/routing")
    # api_router.include_router(intermodal.router, prefix="/routing")
    # api_router.include_router(intermodal.router, prefix="/routing")
    # api_router.include_router(intermodal.router, prefix="/routing")
    # api_router.include_router(intermodal.router, prefix="/routing")
    # api_router.include_router(intermodal.router, prefix="/routing")




    # api.add_resource(HealthResource, '/healthz')
    # api.add_resource(EvalResource, '/eval')
    # api.add_resource(ComputeResource, '/compute')
    # api.add_resource(StartResource, '/start')
    # api.add_resource(AddResource, '/add')
    # api.add_resource(FindResource, '/find_nodes')
    # api.add_resource(MakeFriendResource, '/makefriend')
    # api.add_resource(IsMeResource, '/isme')
    # api.add_resource(IpResource, '/ip')
    # api.add_resource(ReceiveTokenResource, '/receive_token')
    # api.add_resource(NodesResource, '/nodes')

    return api_router
