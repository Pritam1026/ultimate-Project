from src.config.configuration import *
from src.constants import *
import os
import sys
from sklearn.model_selection import train_test_split
import numpy as numpy
import pandas as pd

from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer

@dataclass
class DataIngestionConfig:
    raw_data_path:str=RAW_FILE_PATH
    train_data_path:str=TRAIN_FILE_PATH
    test_data_path:str=TEST_FILE_PATH

class DataIngestion:
    def __init__(self):
        self.data_ingestion_Config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            #Reading the dataset from loacal folder
            df=pd.read_csv(DATASET_PATH)

            #Making the directory for raw data and saving the raw data
            raw_data_dir_name=os.path.dirname(self.data_ingestion_Config.raw_data_path)
            os.makedirs(raw_data_dir_name,exist_ok=True)
            df.to_csv(self.data_ingestion_Config.raw_data_path,index=False,header=True)

            #Performing the train test split
            train_Set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            #Saving the training data into the artifact folder
            train_data_dir_name=os.path.dirname(self.data_ingestion_Config.train_data_path)
            os.makedirs(train_data_dir_name,exist_ok=True)
            train_Set.to_csv(self.data_ingestion_Config.train_data_path,index=False,header=True)

            #Saving the test data into artifact folder
            test_data_dir_name=os.path.dirname(self.data_ingestion_Config.test_data_path)
            os.makedirs(test_data_dir_name,exist_ok=True)
            train_Set.to_csv(self.data_ingestion_Config.test_data_path,index=False,header=True)

            return(
                    self.data_ingestion_Config.train_data_path,
                    self.data_ingestion_Config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    trans_obj=DataTransformation()
    train_arr,test_arr,_=trans_obj.initiate_data_transformation(train_data,test_data)

    model_obj=ModelTrainer()
    model_obj.initiate_model_trainer(train_arr,test_arr)

