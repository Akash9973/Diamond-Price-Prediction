import logging
import os ## it is used to get the current path
from datetime import datetime  ## when the logging is created it should be wrt to the date and time as well

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  ## we are creating a log file which is used in the naming format of datetime.now() and it would be represented as month(%m), day(%d),year(%Y),hour, min , and second respectively. .log file is being created
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) ## here we are creating a log path with the file name of log 
os.makedirs(logs_path,exist_ok=True) ## this creates a directory

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO

)

## The above is the basic configuration of the log file that what is the file name, what will be the format of the file  etc 