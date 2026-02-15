import logging
import os
from typing import Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config:
    """
    Configuration class for BugBuddy project.
    
    This class provides a centralized way to manage configuration settings.
    It loads configuration from environment variables and provides type hints for configuration keys.
    """

    def __init__(self):
        self.CONFIG: Dict[str, str] = {
            'MODE': os.environ.get('MODE', 'dev'),
            'TF_MODEL_PATH': os.environ.get('TF_MODEL_PATH', '/models/bug_detection_model'),
            'FLASK_HOST': os.environ.get('FLASK_HOST', '0.0.0.0'),
            'FLASK_PORT': os.environ.get('FLASK_PORT', '5000'),
        }

    def get_config(self, key: str) -> str:
        """
        Retrieves a configuration value by key.
        
        Args:
        key (str): The configuration key.
        
        Returns:
        str: The configuration value.
        
        Raises:
        KeyError: If the configuration key is not found.
        """
        try:
            return self.CONFIG[key]
        except KeyError:
            logger.error(f"Configuration key '{key}' not found")
            raise

config = Config()