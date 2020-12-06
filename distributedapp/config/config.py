# import secrets
# from typing import List, Union
from functools import lru_cache
# import os
# from typing import Optional

from pydantic import BaseSettings # AnyHttpUrl, BaseSettings, validator, Field, BaseModel


@lru_cache()
def get_settings():
    return Settings()



class Settings(BaseSettings):

    PROJECT_NAME = "Distributed App example"
