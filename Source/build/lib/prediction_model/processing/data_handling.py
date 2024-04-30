import os
import pandas as pd
import joblib
from prediction_model.config import config

def load_dataset(data_file_name): ## To load the datsets we will pass config.TRAIN_FILE as param for train.csv
    filepath = os.path.join(config.DATAPATH, data_file_name)
    _data_ = pd.read_csv(filepath) ## Read the csv file as dataframe from the filepath
    return _data_ ## returns dataframe

def save_pipeline(pipeline_to_save): ## Serialization to store our created model
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_path)
    print("Model has been saved as ", config.MODEL_NAME)

def load_pipeline(pipeline_to_load): ## Deserialization to load model
    model_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    model_loaded = joblib.load(model_path)
    print("Model has been loaded")
    return model_loaded
