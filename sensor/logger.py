import os
import sys
import logging
from datetime import datetime

# The name of the file we want to give it as the time when it is created.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# Creating the folder where we are gonna store the file
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) #os.getcwd() --> current working directory

# But we can not let the folder be created everytime we get a log file
os.makedirs(logs_path, exist_ok=True) #exist_ok=True --> create directory only when it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
