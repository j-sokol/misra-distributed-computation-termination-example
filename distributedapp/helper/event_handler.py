from distributedapp.helper.globals import Globals, forward_token
import logging


class EventHandler():

    def handle_send_token():
        # logging.info("Handling send_token")

        logging.info(f"Handling send_token: token_present={Globals.token_present}, is_computing={Globals.is_computing}, colour={Globals.colour}, round={Globals.round}")

        if Globals.token_present and not Globals.is_computing:
            if Globals.colour == "black":
                Globals.round = 0
            else:
                Globals.round += 1

            forward_token(Globals.round)

            Globals.colour = "white"
            Globals.token_present = False

    def handle_waiting_message():
        logging.info(f"Handling waiting_message: token_present={Globals.token_present}, is_computing={Globals.is_computing}, colour={Globals.colour}, round={Globals.round}")
        Globals.is_computing = False

    def handle_received_token(token: str):
        logging.info(f"Handling received_token {token}" )
        logging.info(f"vars: token_present={Globals.token_present}, is_computing={Globals.is_computing}, colour={Globals.colour}, round={Globals.round}")

        Globals.round = token
        Globals.token_present = True
        if Globals.round >= len(Globals.nodes) and Globals.colour == "white":
            # Raise it as error event to see this visibly
            logging.error(">>>> COMPUTATION TERMINATION DETECTED")

    def handle_received_message():
        logging.info("Handling received_message")

        Globals.is_computing = True
        Globals.colour = "black"
