import time
import requests
import json
import logging
import requests
import asyncio

from typing import List

from fastapi import APIRouter, Response, status, Body, Depends, Request, Query, Path
from fastapi import BackgroundTasks
from typing import Optional

# from distributedapp.helper.config import Config
from distributedapp.helper.globals import notifier
from distributedapp.helper.globals import Globals
from distributedapp.helper.my_ip import get_my_ip




router = APIRouter()


@router.get("/healthz")
async def healthz():
    return {"status": "ok"}



@router.get("/assign_token")
async def assign_token():
    if Globals.token_present:
        return {"status": "ok", "message": "token already assigned"}
    else:
        Globals.token_present = True
        return {"status": "ok", "message": "token assigned"}


# @router.get("/eval")
# async def eval(city):
#     return [{"type": "walk"}, {"city": city}]

@router.get("/compute")
async def compute(compute_time: float):

    notifier.raise_event("received_message")

    logging.info(f"Will compute for {compute_time}")

    # Simulate computing for `compute_time`
    await asyncio.sleep(compute_time)
    logging.info(f"Computation finished")

    notifier.raise_event("waiting_message")

    notifier.raise_event("send_token")

    return {"status": "ok", "message": f"computed in {compute_time} seconds"}


@router.post("/add")
async def add(ip: str):
    my_ip = get_my_ip()
    node_ip = ip

    if my_ip != node_ip and node_ip not in Globals.nodes:

        logging.info(f"Adding {node_ip}" )
        Globals.nodes.add(node_ip)

        logging.info("All nodes in cluster")
        logging.info(Globals.nodes)

        return Response(json.dumps({"status": "ok", "nodes": list(Globals.nodes)}), 200)
    
    if node_ip == my_ip or node_ip in Globals.nodes:
        return Response(json.dumps({"status": "ok", "message": "already added", "nodes": list(Globals.nodes)}), 200)


    return {"status": "ok", "nodes": list(Globals.nodes)}

@router.get("/find_nodes")
async def find_nodes(subnet: str):

    # First 4 bytes from IP 
    subnet_part = ".".join(subnet.split(".")[0:3])

    my_ip = get_my_ip()

    for i in range(2, 5):
        logging.info(f'Adding node {subnet_part}.{i}')

        tested_ip = f'{subnet_part}.{i}'

        if tested_ip == my_ip:
            continue

        try:
            response = requests.post(f'http://{tested_ip}:5049/add?ip={my_ip}', timeout=1)
            response.raise_for_status()
        except requests.exceptions.ReadTimeout as e:
            logging.error(f'{e}')

        except requests.exceptions.ConnectTimeout as e:
            logging.error(f'{e}')

    return [{"status": "ok", "nodes": list(Globals.nodes)}]

@router.get("/ip")
async def ip(city):
    ip = get_my_ip()
    return {"status": "ok", "ip": ip}

def bgtask():
    notifier.raise_event("send_token")

@router.get("/receive_token")
async def receive_token(token: int, background_tasks: BackgroundTasks, request: Request):

    logging.info(f'Received token {token} from {request.client.host}')

    Globals.round = token

    notifier.raise_event("received_token", token = token)

    # Slow down the communication a bit
    await asyncio.sleep(1)


    background_tasks.add_task(bgtask)

    return {"status": "token received"}

@router.get("/nodes")
async def nodes():
    return {"status": "ok", "nodes": list(Globals.nodes).sort()}

