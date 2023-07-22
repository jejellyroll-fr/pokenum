import logging
import sys

def configure_logger(log_file):
    # Create a logger and set the log level to DEBUG
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a file handler for the log file
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler for the console (stdout)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)

    # Set the format for log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
