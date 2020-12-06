from flask_restful import Resource
from flask import Response
import json
from flask_restful import reqparse
import requests
import logging
from distributedapp.helper.my_ip import get_my_ip
from distributedapp.helper.globals import Globals

class FindResource(Resource):
    """
    Health Resource Endpoint
    """
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('subnet', type=str, help='Subnet to find nodes')
        args = parser.parse_args()

        # TODO: delete the default city in future, so far it's here because of the app clients
        subnet = args['subnet']

        # First 4 bytes from IP 
        subnet_part = ".".join(subnet.split(".")[0:3])

        my_ip = get_my_ip()


        print(subnet_part)

        for i in range(2, 5):
            print(f'Adding node {subnet_part}.{i}')
            # try:
            #     response = requests.get(f'http://{subnet_part}.{i}:5049/isme')
            #     response.raise_for_status()
            # except requests.exceptions.ReadTimeout as e:
            #     logging.error(f'{e}')

            tested_ip = f'{subnet_part}.{i}'

            if tested_ip == my_ip:
                continue

            try:
                response = requests.post(f'http://{tested_ip}:5049/add?ip={my_ip}', timeout=1)
                # http://${subnet.split('.').slice(0,3).join('.')}.${i}:3000/add_friend?ip=${me_ip}
                response.raise_for_status()
            except requests.exceptions.ReadTimeout as e:
                # logging.error(f'{e}')
                print(f'{e}')

            except requests.exceptions.ConnectTimeout as e:
                print(f'{e}')

            


    #         let myself = crypto.createHash('md5').update('some_string').digest("hex")
    # console.log(`[${me_ip}]Searching for friends on ${subnet}/24`)
    # for (let i = 1; i < 256; i++) {
    #     let options = {
    #         method: 'GET',
    #         url: `http://${subnet.split('.').slice(0,3).join('.')}.${i}:3000/isme`,
    #         timeout: 100
    #     };
    #     let req;
    #     try {
    #         req = await requestp({
    #             method: "POST",
    #             url: `http://${subnet.split('.').slice(0,3).join('.')}.${i}:3000/add_friend?ip=${me_ip}`,
    #             timeout: 100
    #         })
    #     } catch (error) {
    #         if (error.code !== "ETIMEDOUT" && error.code !== "ECONNREFUSED" && error.code !== "ESOCKETTIMEDOUT")
    #             console.error(error)
    #     }
    #     //request(options, function (error, response, body) {
    #     //    if (error){
    #     //        //TODO error handling
    #     //        if (error.code !== "ETIMEDOUT" && error.code !== "ECONNREFUSED" && error.code !== "ESOCKETTIMEDOUT")
    #     //            console.error(error);
    #     //        // throw new Error(error)
    #     //    } else {
    #     //        nodes.push(`${subnet.split('.').slice(0,3).join('.')}.${i}`);
    #     //        let options = {
    #     //            method: 'POST',
    #     //            url: `http://${subnet.split('.').slice(0,3).join('.')}.${i}:3000/find_friends?subnet=${subnet}`
    #     //        };
    #     //        // dont really care about  response
    #     //        request(options, (error, response, body)=>{
    #     //            if (error) {
    #     //                console.error(error);
    #     //            }
    #     //        })
    #     //    }
    #     hosts_found++;
    #     //});
    # }
    # log("Finished looking for friends")
    # log(nodes.toString())


        return Response(json.dumps({"status": "ok", "nodes": list(Globals.nodes)}),200)