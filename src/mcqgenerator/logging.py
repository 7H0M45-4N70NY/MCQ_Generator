import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #File name

log_path=os.path.join(os.getcwd(),"logs")   #Creating logs folder

os.makedirs(log_path,exist_ok=True)     #Creating log folder


LOG_FILEPATH=os.path.join(log_path,LOG_FILE)    #inserting log file insider log folder


logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)                       #Creating log file
