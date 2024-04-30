import os
import pathlib
# import prediction_model

current_directory = os.path.dirname(os.path.realpath(__file__)) ## Path to root directory of prediction_model
PACKAGE_ROOT = os.path.dirname(current_directory) 

DATAPATH = os.path.join(PACKAGE_ROOT,'datasets') ## Path to datasets appended to og root dir

TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'

MODEL_NAME = 'classification.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,'trained_models') ## Where created model will be saved

TARGET = 'Loan_Status' ## Target feature

FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area','CoapplicantIncome'] ## Final set of features (Loan_ID dropped)

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area']

## In our case it is same as Categorical features
FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area']

FEATURE_TO_MODIFY = ['ApplicantIncome'] ## We add Coapplicant Income to Applicant Income in processing step
FEATURE_TO_ADD = 'CoapplicantIncome'

DROP_FEATURES = ['CoapplicantIncome'] ## We drop this next

LOG_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term'] ## Log transf. of these features

