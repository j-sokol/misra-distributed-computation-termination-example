from distributedapp.helper.globals import Globals, forward_token
import logging


class EventHandler():

    def handle_send_token():
        logging.info("handling send_token")

        if Globals.token_present and not Globals.is_computing:
            if Globals.colour == "black":
                Globals.round = 0
        else:
            Globals.round += 1

        forward_token(Globals.round)

        Globals.colour = "white"
        Globals.token_present = False

    def handle_waiting_message():
        logging.info("handling waiting_message")
        Globals.is_computing = False

    def handle_received_token(token: str):
        logging.info(f"handling received_token {token}" )
        Globals.round = token
        Globals.token_present = True
        if Globals.round >= len(Globals.nodes) and Globals.colour == "white":
            logging.info("termination detected")

    def handle_received_message():
        logging.info("handling received_message")

        Globals.is_computing = True
        Globals.colour = "black"
