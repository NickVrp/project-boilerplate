import os
if not os.path.exists(os.getcwd()+"/logs"):
    os.makedirs(os.getcwd()+"/logs")

import logging
import logging.config
logging.config.fileConfig("logging.config")
from rich.logging import RichHandler

def setup_logger():
    logger = logging.getLogger(__name__)
    logger = logging.getLogger()
    logger.handlers[0] = RichHandler(markup=True)
    return logger