import logging

def setup_logger():
    logger = logging.getLogger("house_price_api")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.FileHandler("app.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

def log_event(message):
    logging.info(message)

def log_error(message):
    logging.error(message)