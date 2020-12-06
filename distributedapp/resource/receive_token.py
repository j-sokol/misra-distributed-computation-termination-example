from flask_restful import Resource
from flask_restful import abort
from flask_restful import request
from flask_restful import reqparse
from flask import Response
from distributedapp.helper.config import Config
# from distributedapp.helper.mongo_manager import MongoManger
import json
from distributedapp.helper.globals import notifier
from distributedapp.helper.globals import Globals


class ReceiveTokenResource(Resource):
    """
    All Resource Endpoint
    """
    
    # def __init__(self, **kwargs):

    #     super(AllUsers, self).__init__()


    # def post(self):

    #     # json_data = request.get_json(force=True)
    #     # name = json_data['name']
    #     # occupation = json_data['occupation']

    #     # data = { 
    #     #     "name": name, 
    #     #     "occupation": occupation 
    #     #     }

    #     # with MongoManger(Config()) as mongo:
    #     #     mongo.get_users().insert_one(data)
    #     #     print(f'Added {name} - {occupation} to DB...')

    #     return Response(json.dumps({"status": "ok"}),200)


    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('token', type=int, help='Received token')
        args = parser.parse_args()

        # TODO: delete the default city in future, so far it's here because of the app clients
        token = args['token']

        Globals.round = token


        notifier.raise_event("received_token", token=token)
        notifier.raise_event("send_token")


        # ret_users = []
        # with MongoManger(Config()) as mongo:
        #     vehicles = mongo.get_users()
        #     cursor = vehicles.find({})
        #     for document in cursor:
        #         ret_users.append({
        #             'name': document['name'],
        #             'occupation': document['occupation']
        #             })


        return Response(json.dumps({"status": "token received"}),200)

