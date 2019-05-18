"""
Logs
"""

# built-in
import logging

# core
from core import settings


# setup logger
logger = logging.getLogger(settings.LOGGER_NAME)
logger.setLevel(settings.LOGGER_LEVEL)

"""
log error
"""
def error(text):
    # error
    if logger.level <= logging.ERROR:
        print("\n- {}".format(text))
    logger.info(text)

"""
log debug
"""
def debug(text):
    # log
    if logger.level <= logging.DEBUG:
        print("\n- {}".format(text))
    logger.debug(text)

"""
log info
"""
def info(text):
    # log
    if logger.level <= logging.INFO:
        print("\n- {}".format(text))
    logger.info(text)
