from src.logger import logging
from src.exception import CustomException
import os,sys

if __name__=="__main__":
    try:
        a=1
        b=0
        c=a/b
    except Exception as e:
        error=CustomException(e,sys)
        logging.info(error.error_message)
        raise error
        