import logging

PRIVATE_LOGGER = logging.getLogger('Live')

def init(filepath):
    hdlr = logging.FileHandler(filepath)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%m-%d %H:%M')
    hdlr.setFormatter(formatter)
    PRIVATE_LOGGER.addHandler(hdlr)

def setLevel(level):
    PRIVATE_LOGGER.setLevel(level)

def error(message):
    PRIVATE_LOGGER.error(message)

def warning(message):
    PRIVATE_LOGGER.warning(message)

def info(message):
    PRIVATE_LOGGER.info(message)

def debug(message):
    PRIVATE_LOGGER.debug(message)

def message(m):
    PRIVATE_LOGGER.info(m)
