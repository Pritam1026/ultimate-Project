import os
import sys
import logging
from datetime import datetime

LOG_DIR=os.path.join(os.getcwd(),'logs')
LOGS_FILE_NAME=datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

os.makedirs(LOG_DIR,exist_ok=True)
file_name=os.path.join(LOG_DIR,f"{LOGS_FILE_NAME}.log")

logging.basicConfig(filename=file_name,
                    filemode='w',
                    format='[%(asctime)s] %(name)s- %(levelname)s - %(message)s',
                    level=logging.INFO
)




