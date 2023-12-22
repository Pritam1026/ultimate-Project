from src.constants import *
from src.logger import logging
from src.exception import CustomException
import os
import sys
from src.config.configuration import *
from dataclasses import dataclass
from src.utils import save_object,evaluate_model

from sklearn.base import BaseEstimator,TransformerMixin
import numpy as numpy
import pandas as pd

from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

@dataclass
class ModelTrainerConfig:
    trained_model_file_path:str=MODEL_OBJ_PATH

class ModelTrainer:
    
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            X_train,X_test,y_train,y_test=(train_array[:,:-1],test_array[:,:-1],
                                           train_array[:,-1],test_array[:,-1])
            
            models={
                "XGBRegressor":XGBRegressor(),
                "DescisionTreeRegressor":DecisionTreeRegressor(),
                "RandomForestRegressor":RandomForestRegressor(),
                "GradientBoosting":GradientBoostingRegressor(),
                "SVR":LinearSVR()
            }

            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)

            #Finding the best model among all
            best_model_name = max(model_report, key=model_report.get)
            best_model_score=model_report[best_model_name]
            best_model=model_report[best_model_name]

            print("*"*50)
            print(f"Best model name is :{best_model_name} and r2 score is :{best_model_score}")
            print("*"*50)

            os.makedirs(os.path.dirname(self.model_trainer_config.trained_model_file_path),exist_ok=True)
            save_object(self.model_trainer_config.trained_model_file_path,best_model)
            
        except Exception as e:
            raise CustomException(e,sys)



