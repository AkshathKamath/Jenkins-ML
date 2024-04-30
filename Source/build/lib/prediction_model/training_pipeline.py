import pandas as pd
import numpy as np 
from prediction_model.config import config  
from prediction_model.processing.data_handling import load_dataset,save_pipeline
import prediction_model.processing.pre_processing as pp 
import prediction_model.pipeline as pipe 


def model_training_saving():
    df_train = load_dataset(config.TRAIN_FILE) ## Load the training dataset & this returns it as dataframe
    y_train = df_train[config.TARGET]
    y_train = y_train.map({'N':0, 'Y':1})
    pipe.classification_pipeline.fit(df_train[config.FEATURES], y_train)
    save_pipeline(pipe.classification_pipeline)

if __name__=='__main__': ## For automating
    model_training_saving()