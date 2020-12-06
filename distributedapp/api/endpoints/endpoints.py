import time
import requests
import json
import logging
import requests

from typing import List

from fastapi import APIRouter, Response, status, Body, Depends, Request, Query, Path
from fastapi import BackgroundTasks
from typing import Optional


    # api.add_resource(HealthResource, '/healthz')
    # api.add_resource(EvalResource, '/eval')
    # api.add_resource(ComputeResource, '/compute')
    # api.add_resource(StartResource, '/start')
    # api.add_resource(AddResource, '/add')
    # api.add_resource(FindResource, '/find_nodes')
    # api.add_resource(MakeFriendResource, '/makefriend')
    # api.add_resource(IsMeResource, '/isme')
    # api.add_resource(IpResource, '/ip')
    # api.add_resource(ReceiveTokenResource, '/receive_token')
    # api.add_resource(NodesResource, '/nodes')

from distributedapp.helper.config import Config
from distributedapp.helper.globals import notifier
from distributedapp.helper.globals import Globals
from distributedapp.helper.my_ip import get_my_ip




router = APIRouter()


@router.get("/healthz")
async def healthz(city):
    return {"status": "ok"}

# @router.get("/eval")
# async def eval(city):
#     return [{"type": "walk"}, {"city": city}]

@router.get("/compute")
async def compute(compute_time: float):

    notifier.raise_event("received_message")

    print("Will compute for", compute_time)

    # Simulate computing for `compute_time`
    time.sleep(compute_time)

    notifier.raise_event("send_token")
    notifier.raise_event("waiting_message")

    return {"status": "ok", "message": f"computed in {compute_time} seconds"}

# @router.get("/start")
# async def start(city):
#     return [{"type": "walk"}, {"city": city}]

@router.post("/add")
async def add(ip: str):
    my_ip = get_my_ip()
    node_ip = ip

    # print("Will add", node_ip)
    # print("my ip", my_ip)

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


    return {"status": "ok", "nodes": list(Globals.nodes)}

@router.get("/find_nodes")
async def find_nodes(subnet: str):

    # First 4 bytes from IP 
    subnet_part = ".".join(subnet.split(".")[0:3])

    my_ip = get_my_ip()

    # print(subnet_part)

    for i in range(2, 5):
        print(f'Adding node {subnet_part}.{i}')

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

    return [{"status": "ok", "nodes": list(Globals.nodes)}]

# @router.get("/makefriend")
# async def makefriend(city):
#     return [{"type": "walk"}, {"city": city}]

# @router.get("/isme")
# async def isme(city):
#     return [{"type": "bob"}, {"city": city}]

@router.get("/ip")
async def ip(city):
    ip = get_my_ip()
    return {"status": "ok", "ip": ip}

def bgtask():
    notifier.raise_event("send_token")

@router.get("/receive_token")
async def receive_token(token: int, background_tasks: BackgroundTasks):

    Globals.round = token

    notifier.raise_event("received_token", token = token)

    # Slow down the communication a bit
    time.sleep(0.1)

    logging.info(f'Received token {token}')

    background_tasks.add_task(bgtask)

    return {"status": "token received"}

@router.get("/nodes")
async def nodes():
    return {"status": "ok", "nodes": list(Globals.nodes).sort()}

