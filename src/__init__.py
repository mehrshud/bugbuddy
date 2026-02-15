import logging
import logging.config
from typing import Dict
import os
from flask import Flask
from bugbuddy.config import Config

# Configure logging
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    }
})

def create_app(config_class=Config) -> Flask:
    """
    Creates a Flask application instance.

    Args:
    config_class (Config): The configuration class to use.

    Returns:
    Flask: A Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    return app

app = create_app()