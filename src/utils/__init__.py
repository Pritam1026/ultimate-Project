import os
import sys
import joblib
from src.exception import CustomException
from sklearn.metrics import r2_score

def save_object(filepath:str,obj):
    """
    This function is used to save the obejcts as binary files in pickel format
    """
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path, exist_ok=True)
        with open(filepath,"wb") as file_obj:
            joblib.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        for i in range(len(models.keys())):
            #fetching the model from the dictionary of models
            model=list(models.values())[i]
            #fitting the model
            model.fit(X_train,y_train)

            #Getting the prediction score from y_test_pred
            y_test_pred=model.predict(X_test)
            test_model_score=r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]=test_model_score

            return report

    except Exception as e:
        raise CustomException(e,sys)