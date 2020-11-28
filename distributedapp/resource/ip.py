from flask_restful import Resource
from flask_restful import abort
from flask_restful import request
from flask_restful import reqparse
from flask import Response
from distributedapp.helper.config import Config
# from distributedapp.helper.mongo_manager import MongoManger
import json

class IpResource(Resource):
    """
    All Resource Endpoint
    """
    
    # def __init__(self, **kwargs):

    #     super(AllUsers, self).__init__()


    def post(self):

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

        return Response(json.dumps({"status": "ok"}),200)


    def get(self):

        import socket
        # def get_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'
        finally:
            s.close()
        # return ip

        # ret_users = []
        # with MongoManger(Config()) as mongo:
        #     vehicles = mongo.get_users()
        #     cursor = vehicles.find({})
        #     for document in cursor:
        #         ret_users.append({
        #             'name': document['name'],
        #             'occupation': document['occupation']
        #             })


        return Response(json.dumps({"status": "ok", "ip": ip}),200)

