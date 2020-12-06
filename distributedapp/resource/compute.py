from flask_restful import Resource
from flask import Response
import json
# from EventNotifier import Notifier
import time
from distributedapp.helper.globals import notifier

from flask_restful import reqparse

class ComputeResource(Resource):
    """
    Health Resource Endpoint
    """
    
    def get(self):


        parser = reqparse.RequestParser()
        # parser.add_argument('subnet', type=str, help='Subnet to find nodes')
        parser.add_argument('time', type=str, help='Compute time')
        args = parser.parse_args()

        # TODO: delete the default city in future, so far it's here because of the app clients
        compute_time = float(args['time'])



        notifier.raise_event("received_message")


        print("will compute for", compute_time)

        time.sleep(compute_time)


        notifier.raise_event("send_token")
        notifier.raise_event("waiting_message")








        return Response(json.dumps({"status": "ok", "message": f"computed in {compute_time} seconds"}),200)