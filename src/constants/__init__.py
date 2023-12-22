import os,sys
from datetime import datetime

def get_current_time_stamp():
    """
    This function return the current time in (YEAR-MONTH-DAY-HOUR-MINUT-SECOND) FORMAT
    """
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

#Creating a current time stamp object
CURRENT_TIME_STAMP=get_current_time_stamp()

#Dir to read original data
ROOT_DIR=os.getcwd()
DATA_DIR="Data"
DATA_DIR_KEY="final_train.csv"

#Artifact dir to save all the pipeline data and object
ARTIFACT_DIR="Artifact"

#Directories and file keys for data ingestion
DATA_INGESTION_DIR="data_ingestion"
RAW_DATA_DIR="raw_data"
INGESTED_DATA_DIR="ingested_data"
RAW_DATA_KEY="raw.csv"
TRAIN_DATA_KEY="train.csv"
TEST_DATA_KEY="test.csv"

#Directories and file keys for data_transformation
DATA_TRANSFORMATION_DIR="data_transformation"
PROCESSOR_OBJ_DIR="processor"
TRANSFORMED_DATA_DIR="transformed_data"
PRE_PROCESSOR_OBJ_KEY="pre_processor.pkl"
FEATURE_ENGINEERING_OBJ_KEY="feature_engineering.pkl"
TRANSFORMED_TRAIN_DATA_KEY="transformed_train.csv"
TRANSFORMED_TEST_DATA_KEY="transformed_test.csv"




