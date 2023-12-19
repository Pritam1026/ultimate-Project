from src.constants import *
import os
import sys

DATASET_PATH=os.path.join(ROOT_DIR,DATA_DIR,DATA_DIR_KEY) # These variables are fetched from src.constants


RAW_FILE_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR,DATA_INGESTION_DIR,CURRENT_TIME_STAMP,
                           RAW_DATA_DIR,RAW_DATA_KEY)# These variables are fetched from src.constants
TRAIN_FILE_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR,DATA_INGESTION_DIR,CURRENT_TIME_STAMP,
                             INGESTED_DATA_DIR,TRAIN_DATA_KEY)# These variables are fetched from src.constants
TEST_FILE_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR,DATA_INGESTION_DIR,CURRENT_TIME_STAMP,
                             INGESTED_DATA_DIR,TEST_DATA_KEY)# These variables are fetched from src.constants
