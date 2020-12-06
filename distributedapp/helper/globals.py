
from EventNotifier import Notifier
from distributedapp.helper.my_ip import get_my_ip
import requests

import logging

notifier = Notifier(["received_message", "waiting_message", "send_token", "received_token"])

class Globals(object):
    """
    Global vars
    """
    nodes: set = set()

    # Misra algorithm init
    colour: str = "black"
    round: int = 0
    is_computing: bool = False
    token_present: bool = False


# Will return next node in circle topology
def get_next_node():

    node_list: list = list(Globals.nodes)
    node_list.sort()

    # print("sorted_nodes")
    # print(Globals.nodes)


    my_ip: str = get_my_ip()

    # print(node_list)

    my_index = node_list.index(my_ip)

    logging.info(my_index)
    logging.info(f'{len(node_list)}, {my_index}')
    logging.info(f'{node_list.__str__()}, {my_index}')

    # Select first node in list
    if my_index >= (len(node_list)-1):
        logging.info(f'[{my_ip}] Next node is {node_list[0]}')
        return node_list[0]
    # Select next node in list
    else:
        # print(node_list)
        logging.info(f'[{my_ip}] Next node is {node_list[my_index+1]}')
        return node_list[my_index+1]

# Will forward token to next node in circle topology
def forward_token(token):
    next_node = get_next_node()

    logging.info(f"forwarding token {token} to {next_node}")

    try:
        response = requests.get(f'http://{next_node}:5049/receive_token?token={token}')
        response.raise_for_status()
    except requests.exceptions.ReadTimeout as e:
        logging.error(f'{e}')
