import os
import string
import time
import random
import logging
import uvicorn
import sys

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
        title="Distributed App",
        version="0.0.1",
        openapi_version='2',
        description="Distributed app showcase",
        routes=app.routes,
    )

    # app.openapi_schema = openapi_schema

    return app.openapi_schema

def set_logging():
    root = logging.getLogger()

    class AppFilter(logging.Filter):
        def filter(self, record):
            record.ip = Globals.my_ip
            return True


    loglevel = os.getenv("LOG_LEVEL", "INFO")
    root.setLevel(loglevel)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(loglevel)
    handler.addFilter(AppFilter())

    formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] [%(ip)s] %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

def create_app(settings: Settings = get_settings()) -> FastAPI:
    # logger = logging.getLogger("Server")
    # logger.setLevel(logging.DEBUG)


    Globals.my_ip = get_my_ip()
    Globals.nodes = set()
    Globals.nodes.add(Globals.my_ip)

    set_logging()


    notifier.subscribe("received_message",  EventHandler.handle_received_message)
    notifier.subscribe("received_token",  EventHandler.handle_received_token)
    notifier.subscribe("waiting_message",  EventHandler.handle_waiting_message)
    notifier.subscribe("send_token",  EventHandler.handle_send_token)


    # FAST API INIT
    app = FastAPI(title=settings.PROJECT_NAME, )

    # API ROUTER and endpoints
    app.include_router(create_router_endpoints())


    return app


# uvicorn run
if __name__ != "__main__":

    app = create_app()


# local run
if __name__ == "__main__":
    # set_logging()

    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=6003, debug=True, log_level=logging.DEBUG)
