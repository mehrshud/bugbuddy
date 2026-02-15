import logging
import os
from typing import Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(file_path: str) -> Dict:
    """
    Loads configuration from a JSON file.

    Args:
    - file_path (str): The path to the configuration file.

    Returns:
    - Dict: A dictionary containing the configuration.

    Raises:
    - FileNotFoundError: If the configuration file is not found.
    - ValueError: If the configuration file is invalid.
    """
    try:
        import json
        with open(file_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        logger.error("Configuration file not found.")
        raise
    except json.JSONDecodeError as e:
        logger.error("Invalid configuration file: %s", e)
        raise ValueError("Invalid configuration file")

def get_env_variable(var_name: str) -> str:
    """
    Retrieves the value of an environment variable.

    Args:
    - var_name (str): The name of the environment variable.

    Returns:
    - str: The value of the environment variable.

    Raises:
    - KeyError: If the environment variable is not set.
    """
    try:
        return os.environ[var_name]
    except KeyError:
        logger.error("Environment variable '%s' is not set.", var_name)
        raise

# Example configuration file path
CONFIG_FILE_PATH = 'config.json'