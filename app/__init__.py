from flask import Flask
from mysql.connector import pooling
from flask_cors import CORS
from config import Config
from .controllers import register_routes

connection_pool = pooling.MySQLConnectionPool(pool_name="pynative_pool",
                                                  pool_size=5,
                                                  pool_reset_session=True,
                                                  host=Config.DB_HOST,
                                                  database=Config.DB_NAME,
                                                  user=Config.DB_USER,
                                                  password=Config.DB_PASSWORD)

def create_app():
    app = Flask(__name__)
    configure_logging(app)
    app.config.from_object(Config)
    register_routes(app)
    
    return app

def configure_logging(app):
    import logging
    from flask.logging import default_handler
    from logging.handlers import RotatingFileHandler

    # Deactivate the default flask logger so that log messages don't get duplicated 
    app.logger.removeHandler(default_handler)

    # Create a file handler object
    file_handler = RotatingFileHandler('logs/flasksimple.log', maxBytes=16384, backupCount=20)

    # Set the logging level of the file handler object so that it logs INFO and up
    file_handler.setLevel(logging.DEBUG)

    # Create a file formatter object
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s: %(lineno)d]')

    # Apply the file formatter object to the file handler object
    file_handler.setFormatter(file_formatter)

    # Add file handler object to the logger
    app.logger.addHandler(file_handler)