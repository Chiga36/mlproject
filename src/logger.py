import logging 
# any execution that happens or any execution we can log into text file
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
# so all the logs will be stored in the current working directory with "logs" and then the mssg
os.makedirs(logs_path,exist_ok=True)
# eeven if it's a file or filder just append it

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d - %(levelname)s - %(message)s",
    level=logging.INFO # ?
)

# eg: 
# if __name__ == "__main__":
#     logging.info("Logging has started")