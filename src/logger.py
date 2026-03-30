import logging
from pathlib import Path

LOG_FILE = Path("logs/run.log")

def get_logger():

    LOG_FILE.parent.mkdir(exist_ok=True)


    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()