from flask_restful import Resource
from flask import Response
import json
from flask_restful import request
import base64


import logging


class EvalResource(Resource):
    """
    Health Resource Endpoint
    """
    
    def post(self):

        json_data = request.get_json(force=True)
        code = json_data['code']
        code_decoded = base64.b64decode(code).decode(encoding='UTF-8')
        # occupation = json_data['occupation']


        try:
            logging.info(f'Running eval of {code_decoded}')
            # i = "a"
            resp = eval(code_decoded)
            # print(exec(code_decoded))

            # print(i)
            return Response(json.dumps({"status": "ok", "response": resp}),200)

        except Exception as e:
            logging.error(e)

            return Response(json.dumps({"status": "err"}),500)

        