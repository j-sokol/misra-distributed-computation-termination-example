# import os
# import logging
# from flask import jsonify
# from logging.handlers import RotatingFileHandler
# from flask import Flask, request
# from flask_restful import Api, abort
# import sys

# # from distributedapp.resource.all_users import AllUsers
# from distributedapp.resource.health_resource import HealthResource
# from distributedapp.helper.globals import Globals
# from distributedapp.helper.event_handler import EventHandler
# from distributedapp.helper.globals import notifier

# from distributedapp.helper.my_ip import get_my_ip


# from distributedapp.resource.add import AddResource
# from distributedapp.resource.compute import ComputeResource
# from distributedapp.resource.start import StartResource
# from distributedapp.resource.make_friend import MakeFriendResource
# from distributedapp.resource.isme import IsMeResource
# from distributedapp.resource.find import FindResource
# from distributedapp.resource.eval import EvalResource
# from distributedapp.resource.ip import IpResource
# from distributedapp.resource.receive_token import ReceiveTokenResource
# from distributedapp.resource.nodes import NodesResource



# class CustomApi(Api):

#     def handle_error(self, e):
#         return e.json()


# def create_app():

#     app = Flask(__name__)

#     api = CustomApi(app)

#     app.config['DEBUG'] = True


#     # ---REGISTER RESOURCE----
#     # api.add_resource(AllUsers, '/users')
#     api.add_resource(HealthResource, '/healthz')
#     api.add_resource(EvalResource, '/eval')
#     api.add_resource(ComputeResource, '/compute')
#     api.add_resource(StartResource, '/start')
#     api.add_resource(AddResource, '/add')
#     api.add_resource(FindResource, '/find_nodes')
#     api.add_resource(MakeFriendResource, '/makefriend')
#     api.add_resource(IsMeResource, '/isme')
#     api.add_resource(IpResource, '/ip')
#     api.add_resource(ReceiveTokenResource, '/receive_token')
#     api.add_resource(NodesResource, '/nodes')

#     return app


# def set_logging():
#     root = logging.getLogger()

#     loglevel = os.getenv("LOG_LEVEL", "INFO")
#     root.setLevel(loglevel)
    

#     handler = logging.StreamHandler(sys.stdout)
#     handler.setLevel(loglevel)
#     formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
#     handler.setFormatter(formatter)
#     root.addHandler(handler)


# # Gunicorn setup before init
# if __name__ != '__main__':
#     set_logging()
#     Globals.nodes = set()
#     Globals.nodes.add(get_my_ip())

#     notifier.subscribe("received_message",  EventHandler.handle_received_message)
#     notifier.subscribe("received_token",  EventHandler.handle_received_token)
#     notifier.subscribe("waiting_message",  EventHandler.handle_waiting_message)
#     notifier.subscribe("send_token",  EventHandler.handle_send_token)


#     app = create_app()




#     # gunicorn_logger = logging.getLogger('gunicorn.error')
#     # app.logger.handlers = gunicorn_logger.handlers
#     # app.logger.setLevel(gunicorn_logger.level)


# # Classic setup before init
# if __name__ == '__main__':

#     app = create_app()


#     port = os.getenv("PORT", "5049")
#     app.run(host='0.0.0.0', port=port)


