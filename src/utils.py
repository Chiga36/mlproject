import os
import sys

import numpy as np
import pandas as pd

from src.exception import CustomException
import dill # this will help us to create pickle file
from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        # this will dump as pickle
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)
    
    ## This wil go to data_transformation.py

def evaluate_models(x_train,y_train,x_test,y_test,models):
    try :
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(x_train,y_train)

            y_train_predict = model.predict(x_train)

            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train,y_train_predict)

            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    
    except Exception as e:
        raise CustomException(sys,e)
    
    ## this will go to model_training.py