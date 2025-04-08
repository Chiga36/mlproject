from catboost import CatBoostClassifier
import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            x_train,y_train,x_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forst": RandomForestRegressor(),
                "Decision Tree":DecisionTreeRegressor(),
                "Gradient Boosting":GradientBoostingRegressor(),
                "Linear Regressor":LinearRegression(),
                "K-Neighbours Regressor":KNeighborsRegressor(),
                "XGBRegressor":XGBRegressor(),
                "Catboosting":CatBoostClassifier(verbose=False),
                "AdaBoost Regressor":AdaBoostRegressor(),
            }

            ## Comment indicates that if u have a grest gpu then run uncomment it and then run

            params = {
                "Decision Tree":{
                    "criterion":["squared_error","friedman_mse","absolute_error","poisson"],
                    # "splitter":["best","random"],
                    "max_features" : ['sqrt','log2']
                },
                "Random Forst":{
                    "n_estimators": [8,16,32,64,128,256],
                    # "criterion":["squared_error","friedman_mse","absolute_error","poisson"],
                    # "max_features" : ['sqrt','log2',None]
                },
                "Gradient Boosting":{
                    # "loss":["squared_error","huber","quantile","absolute_error"],
                    "learning_rate":[0.01,0.1,0.05,0.2,0.3],
                    "subsample" : [0.6,0.7,0.75,0.8,0.85,0.9],
                    # "criterion":["squared_error","friedman_mse","absolute_error","poisson"],
                    "n_estimators": [8,16,32,64,128,256],
                    # "max_features" : ['sqrt','log2',None]
                },
                "Linear Regressor":{},
                "K-Neighbours Regressor":{
                    "n_neighbors":[3,5,7,9,11],
                    "weights":["uniform","distance"],
                    "algorithm":["ball_tree","kd_tree","brute"]
                },
                "XGBRegressor":{
                    "learning_rate":[0.01,0.1,0.05,0.2,0.3],
                    "n_estimators": [8,16,32,64,128,256],
                },
                "Catboosting":{
                    'depth':[6,8,10],
                    "learning_rate":[0.01,0.1,0.05,0.2,0.3],
                    "n_estimators": [8,16,32,64,128,256],
                },
                "AdaBoost Regressor":{
                    "n_estimators": [8,16,32,64,128,256],
                    "learning_rate":[0.01,0.1,0.05,0.2,0.3],
                    # "loss" :["linear","square","exponential"],
                },
            }
            model_report:dict = evaluate_models(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models,params=None)
            # If u have a good gpu then in params = None replace it by params = params

            # to get best model score from dict 
            best_model_score = max(sorted(model_report.values()))

            # To get best model name from dictionary

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            ## To keep a threshhold for best models
            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info("Best model found on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(x_test)

            r2 = r2_score(y_test,predicted)

            return r2
        
        except Exception as e:
            raise CustomException(sys,e)