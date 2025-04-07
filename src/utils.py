import os
import sys

import numpy as np
import pandas as pd

from src.exception import CustomException
import dill # this will help us to create pickle file

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