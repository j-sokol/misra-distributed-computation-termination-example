from flask_restful import Resource
from flask_restful import abort
from flask_restful import request
from flask_restful import reqparse
from flask import Response
from distributedapp.helper.config import Config
import json


from distributedapp.helper.globals import Globals
from distributedapp.helper.my_ip import get_my_ip


class NodesResource(Resource):
    """
    Prints nodes
    """

    def get(self):

        return Response(json.dumps({"status": "ok", "nodes": list(Globals.nodes).sort()}), 200)

