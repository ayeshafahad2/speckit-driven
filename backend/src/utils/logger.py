import logging
import os

# Configure basic logging
# In a production environment, you would use a more sophisticated logging setup
# e.g., sending logs to a centralized logging service.

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler() # Log to console
    ]
)

def get_logger(name: str):
    """
    Returns a logger instance for a given name.
    """
    return logging.getLogger(name)

# Example usage:
# logger = get_logger(__name__)
# logger.info("This is an info message.")
# logger.error("This is an error message.")
