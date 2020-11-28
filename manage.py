import os
import logging
from flask import jsonify
from logging.handlers import RotatingFileHandler
from flask import Flask, request
from flask_restful import Api, abort
import sys

from distributedapp.resource.all_users import AllUsers
from distributedapp.resource.health_resource import HealthResource


from distributedapp.resource.add import AddResource
from distributedapp.resource.compute import ComputeResource
from distributedapp.resource.start import StartResource
from distributedapp.resource.make_friend import MakeFriendResource
from distributedapp.resource.isme import IsMeResource
from distributedapp.resource.find import FindResource
from distributedapp.resource.eval import EvalResource
from distributedapp.resource.ip import IpResource


class CustomApi(Api):

    def handle_error(self, e):
        return e.json()


def create_app():

    app = Flask(__name__)

    api = CustomApi(app)

    app.config['DEBUG'] = True


    # ---REGISTER RESOURCE----
    # api.add_resource(AllUsers, '/users')
    api.add_resource(HealthResource, '/healthz')
    api.add_resource(EvalResource, '/eval')
    api.add_resource(ComputeResource, '/compute')
    api.add_resource(StartResource, '/start')
    api.add_resource(AddResource, '/add')
    api.add_resource(FindResource, '/find')
    api.add_resource(MakeFriendResource, '/makefriend')
    api.add_resource(IsMeResource, '/isme')
    api.add_resource(IpResource, '/ip')

    return app


def set_logging():
    root = logging.getLogger()

    loglevel = os.getenv("LOG_LEVEL", "INFO")
    root.setLevel(loglevel)
    

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(loglevel)
    formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)


# Gunicorn setup before init
if __name__ != '__main__':
    set_logging()

    app = create_app()

    # gunicorn_logger = logging.getLogger('gunicorn.error')
    # app.logger.handlers = gunicorn_logger.handlers
    # app.logger.setLevel(gunicorn_logger.level)


# Classic setup before init
if __name__ == '__main__':

    app = create_app()


    port = os.getenv("PORT", "5049")
    app.run(host='0.0.0.0', port=port)


