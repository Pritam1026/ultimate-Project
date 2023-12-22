import os
import sys
from src.constants import *
from src.config.configuration import *
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from sklearn.base import BaseEstimator,TransformerMixin
import numpy as np
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from src.utils import save_object

class FeatureEngineering(BaseEstimator,TransformerMixin):
    def __init__(self):
        logging.info("*********************FEATURE ENGINEERING STARTED************************")
    
    def geospatial_distance(self,df:pd.DataFrame,lat1:str,lon1:str,lat2:str,lon2:str):
        """
        This function will add a distance column in the datafame base on the latitude and longitude of the data provided.
        """
        p = np.pi/180
        a = 0.5 - np.cos((df[lat2]-df[lat1])*p)/2 + np.cos(df[lat1]*p) * np.cos(df[lat2]*p) * (1-np.cos((df[lon2]-df[lon1])*p))/2
        df['distance'] = 12734 * np.arccos(np.sort(a))
    
    def transform_data(self,df:pd.DataFrame)->pd.DataFrame:
        try:
            df.drop(['ID'],axis=1,inplace=True)

            self.geospatial_distance(df,'Restaurant_latitude',
                                'Restaurant_longitude',
                                'Delivery_location_latitude',
                                'Delivery_location_longitude')
            
            df.drop(['Delivery_person_ID', 'Restaurant_latitude',
                     'Restaurant_longitude','Delivery_location_latitude',
                     'Delivery_location_longitude',
                     'Order_Date','Time_Orderd','Time_Order_picked'],
                     axis=1,inplace=True)
            
            logging.info("Dropping columns from our original dataset")

            return df
    
        except Exception as e:
            raise CustomException(e,sys)
        
    def fit(self,X,y=None):
        return self
    
    def transform(self,X,y=None):
        try:
            transform_df=self.transform_data(X)
            return transform_df
        except Exception as e:
            raise CustomException(e,sys)
        


@dataclass
class DataTransformationConfig:
    preprocessor_obj_path:str=PREPROCESSOR_OBJ_PATH
    feature_engineering_obj_path:str=FEATURE_ENGINEERING_OBJ_PATH
    transformed_train_path:str=TRANSFORMED_TRAIN_DATA_PATH
    transformed_test_path:str=TRANSFORMED_TEST_DATA_PATH

class DataTransformation:

    def __init__(self):
        self.datatransformationconfig=DataTransformationConfig()


    def get_data_transformation_obj(self):
        try:
            Road_traffic_density = ['Low', 'Medium', 'High', 'Jam']
            Weather_conditions = ['Sunny', 'Cloudy', 'Fog', 'Sandstorms', 'Windy', 'Stormy']

            categorical_columns = ['Type_of_order','Type_of_vehicle','Festival','City']
            ordinal_encoder = ['Road_traffic_density', 'Weather_conditions']
            numerical_column=['Delivery_person_Age','Delivery_person_Ratings','Vehicle_condition',
                              'multiple_deliveries','distance']

            # Numerical pipeline
            numerical_pipeline = Pipeline(steps = [
                ('impute', SimpleImputer(strategy = 'constant', fill_value=0)),
                ('scaler', StandardScaler(with_mean=False))
            ])

            # Categorical Pipeline
            categorical_pipeline = Pipeline(steps = [
                ('impute', SimpleImputer(strategy = 'most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown = 'ignore')),
                ('scaler', StandardScaler(with_mean=False))
            ])

            # ordinal Pipeline
            ordinal_pipeline = Pipeline(steps = [
                ('impute', SimpleImputer(strategy = 'most_frequent')),
                ('ordinal', OrdinalEncoder(categories=[Road_traffic_density,Weather_conditions])),
                ('scaler', StandardScaler(with_mean=False))
            ])


            preprocssor = ColumnTransformer([
                ('numerical_pipeline', numerical_pipeline,numerical_column ),
                ('categorical_pipeline', categorical_pipeline,categorical_columns ),
                ('ordinal_pipeline', ordinal_pipeline,ordinal_encoder )
            ])

            logging.info("Pipeline Steps Completed")
            return preprocssor

        except Exception as e:
            raise CustomException(e,sys)
        

    def get_feature_engineering_object(self):
        try:
            feature_engineering=Pipeline(steps=[('fe',FeatureEngineering())])
            return feature_engineering
        
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):
        """
        This function will perform the feature engineering
        """
        try:
            #reading the train and test data as datframe
            train_df=pd.read_csv(train_path)
            logging.info(f"{train_df.head()}")
            
            test_df=pd.read_csv(test_path)
            logging.info(f"{test_df.head()}")

            #creating the fe and preprocessor object
            fe_obj=self.get_feature_engineering_object()
            preprocessor_obj=self.get_data_transformation_obj()

            #fitting the data with both objects
            #First with feature engineering object
            train_df=fe_obj.fit_transform(train_df)
            test_df=fe_obj.transform(test_df)

            #Lets save this feature engineered dataset.
            train_df.to_csv('train_data.csv')
            test_df.to_csv('test_data.csv')

            #Preprocessing the data for model training
            TARGET_COLUMN='Time_taken (min)'
            X_train=train_df.drop(TARGET_COLUMN,axis=1)
            y_train=train_df[TARGET_COLUMN]

            X_test=test_df.drop(TARGET_COLUMN,axis=1)
            y_test=test_df[TARGET_COLUMN]

            X_train_processed=preprocessor_obj.fit_transform(X_train)
            X_test_processed=preprocessor_obj.transform(X_test)

            train_arr=np.c_[X_train_processed,np.array(y_train)]
            test_arr=np.c_[X_test_processed,np.array(y_test)]

            #Converting this array into pandas dataframe
            df_train=pd.DataFrame(train_arr)
            df_test=pd.DataFrame(test_arr)


            #Creating the Dirs required to save the data and preprocessor objects
            os.makedirs(os.path.dirname(self.datatransformationconfig.transformed_train_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.datatransformationconfig.transformed_train_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.datatransformationconfig.feature_engineering_obj_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.datatransformationconfig.preprocessor_obj_path),exist_ok=True)

            #saving the data and objects
            df_train.to_csv(self.datatransformationconfig.transformed_train_path,index=False,header=True)
            df_test.to_csv(self.datatransformationconfig.transformed_test_path,index=False,header=True)

            #saving the preprocessor object and feature engineering object
            save_object(self.datatransformationconfig.preprocessor_obj_path,preprocessor_obj)
            save_object(self.datatransformationconfig.feature_engineering_obj_path,fe_obj)

            return (
                train_arr,
                test_arr,
                self.datatransformationconfig.preprocessor_obj_path
            )
        except Exception as e:
            raise CustomException(e,sys)
    
        






