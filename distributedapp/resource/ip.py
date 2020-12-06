from flask_restful import Resource
from flask_restful import abort
from flask_restful import request
from flask_restful import reqparse
from flask import Response
from distributedapp.helper.config import Config
from distributedapp.helper.my_ip import get_my_ip
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

        # return ip

        ip = get_my_ip()
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

