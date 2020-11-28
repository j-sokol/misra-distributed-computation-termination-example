import os
from enum import Enum




class Config(object):
    """"
    ConfigReader - parse yml config file
    Args:
        config_path - path to config file
    Methods:
        google_api_key - returns google api key
    """
    def __init__(self):

        self.app = {
            'mongo': {}
        }
        self.app['mongo']['hostname'] = os.getenv("MONGO_HOSTNAME", "localhost")
        self.app['mongo']['port']     = os.getenv("MONGO_PORT", 27017)
        self.app['mongo']['username'] = os.getenv("MONGO_USERNAME", None)
        self.app['mongo']['password'] = os.getenv("MONGO_PASSWORD", None)


    # --------------APP-----------------------


    def mongo_hostname(self):
        return self.app['mongo']['hostname']

    def mongo_port(self):
        return self.app['mongo']['port']

    def mongo_password(self):
        return self.app['mongo']['password']

    def mongo_username(self):
        return self.app['mongo']['username']

