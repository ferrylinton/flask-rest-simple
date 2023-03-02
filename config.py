import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):

    DEBUG = os.environ.get('DEBUG', False)
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_NAME = os.environ.get('DB_NAME')
    DB_CONNECT_TIMEOUT = os.environ.get('DB_CONNECT_TIMEOUT')

