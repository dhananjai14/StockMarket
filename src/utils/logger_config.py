import logging
from datetime import datetime


def get_logger() -> logging.Logger:
    logger = logging.getLogger()
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_handler = logging.FileHandler(f"logs/application_{current_time}.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger