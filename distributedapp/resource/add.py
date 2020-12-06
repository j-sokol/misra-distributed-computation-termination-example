from flask_restful import Resource
from flask_restful import abort
from flask_restful import request
from flask_restful import reqparse
from flask import Response
from distributedapp.helper.config import Config
# from distributedapp.helper.mongo_manager import MongoManger
import json
import logging

from distributedapp.helper.globals import Globals
from distributedapp.helper.my_ip import get_my_ip

# nodes = []

class AddResource(Resource):
    """
    All Resource Endpoint
    """
    
    # def __init__(self, **kwargs):

    #     super(AllUsers, self).__init__()


    def post(self):

        parser = reqparse.RequestParser()
        # parser.add_argument('subnet', type=str, help='Subnet to find nodes')
        parser.add_argument('ip', type=str, help='Ip to add')
        args = parser.parse_args()

        # TODO: delete the default city in future, so far it's here because of the app clients
        node_ip = args['ip']


        if node_ip is None:
            return Response(json.dumps({"status": "err", "message": "ip not passed in param"}), 500)


        my_ip = get_my_ip()

        print("Will add", node_ip)
        print("my ip", my_ip)

        # First 4 bytes from IP 
        # subnet_part = ".".join(subnet.split(".")[0:3])


        if my_ip != node_ip and node_ip not in Globals.nodes:

            logging.info(f"Adding {node_ip}" )
            Globals.nodes.add(node_ip)


            print("All nodes in cluster")
            print(Globals.nodes)

            return Response(json.dumps({"status": "ok", "nodes": list(Globals.nodes)}), 200)

        
        if node_ip == my_ip or node_ip in Globals.nodes:
            return Response(json.dumps({"status": "ok", "message": "already added", "nodes": list(Globals.nodes)}), 200)



        # for node in 


        # json_data = request.get_json(force=True)
        # name = json_data['name']
        # occupation = json_data['occupation']

        # data = { 
        #     "name": name, 
        #     "occupation": occupation 
        #     }

        # with MongoManger(Config()) as mongo:
        #     mongo.get_users().insert_one(data)
        #     print(f'Added {name} - {occupation} to DB...')

        return Response(json.dumps({"status": "err"}), 500)


    # def get(self):


    #     # ret_users = []
    #     # with MongoManger(Config()) as mongo:
    #     #     vehicles = mongo.get_users()
    #     #     cursor = vehicles.find({})
    #     #     for document in cursor:
    #     #         ret_users.append({
    #     #             'name': document['name'],
    #     #             'occupation': document['occupation']
    #     #             })


    #     return Response(json.dumps({"users": "test"}),200)

