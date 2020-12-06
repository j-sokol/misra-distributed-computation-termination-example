import os
import string
import time
import random
import logging
import uvicorn

from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from starlette.middleware.cors import CORSMiddleware
from distributedapp.api.api import create_router_endpoints
from distributedapp.config.config import get_settings, Settings
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse

from distributedapp.helper.globals import Globals
from distributedapp.helper.event_handler import EventHandler
from distributedapp.helper.globals import notifier

from distributedapp.helper.my_ip import get_my_ip


# OPEN API Design
def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Fuzee Routing",
        version="2.0.1",
        openapi_version='2',
        description="Fuzee Routing Planner",
        routes=app.routes,
    )

    # app.openapi_schema = openapi_schema

    return app.openapi_schema


def create_app(settings: Settings = get_settings()) -> FastAPI:
    logger = logging.getLogger("Server")
    logger.setLevel(logging.DEBUG)


    Globals.nodes = set()
    Globals.nodes.add(get_my_ip())

    notifier.subscribe("received_message",  EventHandler.handle_received_message)
    notifier.subscribe("received_token",  EventHandler.handle_received_token)
    notifier.subscribe("waiting_message",  EventHandler.handle_waiting_message)
    notifier.subscribe("send_token",  EventHandler.handle_send_token)


    # FAST API INIT
    app = FastAPI(title=settings.PROJECT_NAME, )

    # # Set all CORS enabled origins
    # if settings.BACKEND_CORS_ORIGINS:
    #     app.add_middleware(
    #         CORSMiddleware,
    #         allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    #         # allow_credentials=True,
    #         allow_methods=["GET", "OPTIONS", "POST"],
    #         allow_headers=["*"],
    #     )

    # API ROUTER and endpoints
    app.include_router(create_router_endpoints())

    # # ======================== MIDDLEWARE ===========================
    # @app.middleware("http")
    # async def log_requests(request: Request, call_next):
    #     idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    #     logger.info(f"rid={idem} start request path={request.url.path}")
    #     start_time = time.time()

    #     response = await call_next(request)

    #     process_time = (time.time() - start_time) * 1000
    #     formatted_process_time = '{0:.2f}'.format(process_time)
    #     logger.info(
    #         f"rid={idem} completed_in={formatted_process_time}ms status_code={response.status_code}")

    #     return response


    return app


# uvicorn run
if __name__ != "__main__":
    app = create_app()


# local run
if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=6003, debug=True, log_level=logging.DEBUG)
