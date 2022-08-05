import sys
from loguru import logger

logger.add(sys.stdout, format="{time} {level} {message}", level="DEBUG")
logger.add('log/api-server.log',
           format="{time} {level} {message}", level="INFO")