import os
import sys

import numpy as np
import pandas as pd

from src.exception import CustomException
import dill # this will help us to create pickle file
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

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

def evaluate_models(x_train,y_train,x_test,y_test,models,params):
# def evaluate_models(x_train,y_train,x_test,y_test,models):
    try :
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            # if u have a good GPU then comment out the 4 lines below and in model_trainer.py put params = params
            # para = params[list(models.keys())[i]]

            # gs = GridSearchCV(model,para,cv=3)
            # gs.fit(x_train,y_train)

            # model.set_params(**gs.best_params_)
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


## It will load the pickle file
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    
    except Exception as e:
        raise CustomException(e,sys)