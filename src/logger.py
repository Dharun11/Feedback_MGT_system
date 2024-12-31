import logging
import os
from datetime import datetime

# setting up log file path
log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#setting up the logs folder path
logs_folder_path = os.path.join(os.getcwd(), "logs",log_file)
## Creating a directory
os.makedirs(logs_folder_path,exist_ok=True)

log_file_path=os.path.join(logs_folder_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s -%(message)s",
    level=logging.INFO
)


'''
if __name__=="__main__":
    logging.info("This is a log message LOGGING HAS STARTED")
'''
