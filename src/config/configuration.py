from src.constants import *
import os
import sys

#File path for original data
DATASET_PATH=os.path.join(ROOT_DIR,DATA_DIR,DATA_DIR_KEY) # These variables are fetched from src.constants

#File path to save the ingested data that is raw data,train data,test data.
RAW_FILE_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR,CURRENT_TIME_STAMP,DATA_INGESTION_DIR,
                           RAW_DATA_DIR,RAW_DATA_KEY)# These variables are fetched from src.constants
TRAIN_FILE_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR,CURRENT_TIME_STAMP,DATA_INGESTION_DIR,
                             INGESTED_DATA_DIR,TRAIN_DATA_KEY)# These variables are fetched from src.constants
TEST_FILE_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR,CURRENT_TIME_STAMP,DATA_INGESTION_DIR,
                             INGESTED_DATA_DIR,TEST_DATA_KEY)# These variables are fetched from src.constants


#File paths to save the transformed data and preprocessor object
PREPROCESSOR_OBJ_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR,CURRENT_TIME_STAMP,DATA_TRANSFORMATION_DIR,PROCESSOR_OBJ_DIR,
                                   PRE_PROCESSOR_OBJ_KEY)
FEATURE_ENGINEERING_OBJ_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR,CURRENT_TIME_STAMP,DATA_TRANSFORMATION_DIR,PROCESSOR_OBJ_DIR,
                                   FEATURE_ENGINEERING_OBJ_KEY)
TRANSFORMED_TRAIN_DATA_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR,CURRENT_TIME_STAMP,DATA_TRANSFORMATION_DIR,TRANSFORMED_DATA_DIR,
                                         TRANSFORMED_TRAIN_DATA_KEY)
TRANSFORMED_TEST_DATA_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR,CURRENT_TIME_STAMP,DATA_TRANSFORMATION_DIR,TRANSFORMED_DATA_DIR,
                                         TRANSFORMED_TEST_DATA_KEY)

#File path to save the model
MODEL_OBJ_PATH=os.path.join(ROOT_DIR,ARTIFACT_DIR,CURRENT_TIME_STAMP,"trained_model","model.pkl")


