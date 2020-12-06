from flask_restful import Resource
from flask import Response
import json


class StartResource(Resource):
    """
    Health Resource Endpoint
    """
    
    def get(self):

        return Response(json.dumps({"status": "ok"}),200)