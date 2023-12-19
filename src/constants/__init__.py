import os,sys
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP=get_current_time_stamp()

ROOT_DIR=os.getcwd()
DATA_DIR="Data"
DATA_DIR_KEY="final_train.csv"


ARTIFACT_DIR="Artifact"
DATA_INGESTION_DIR="data_ingestion"
RAW_DATA_DIR="raw_data"
INGESTED_DATA_DIR="ingested_data"
RAW_DATA_KEY="raw.csv"
TRAIN_DATA_KEY="train.csv"
TEST_DATA_KEY="test.csv"



