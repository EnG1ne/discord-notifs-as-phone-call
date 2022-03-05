import datetime
import logging

def print_and_log(message: str, log_type: logging, new_line=False):
    if new_line:
        print(f"{datetime.datetime.now()} - {message}\n")
    else:
        print(f"{datetime.datetime.now()} - {message}")

    if log_type == logging.INFO:
        logging.info(message)
    elif log_type == logging.WARNING:
        logging.warning(message)
    elif log_type == logging.ERROR:
        logging.error(message)
    elif log_type == logging.CRITICAL:
        logging.error(message)