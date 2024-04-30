import pytest
from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_predictions

# output from predict script not null
# output from predict script is str data type
# the output is Y for an example data

#Fixtures --> functions before test function (functions with test_*) --> ensure single_prediction() before test funcs

@pytest.fixture
def single_prediction():
    df_test = load_dataset(config.TEST_FILE)
    single_row = df_test[:1]
    result = generate_predictions(single_row)
    return result

## Tests
def test_single_pred_not_none(single_prediction): ## output is not none
    assert single_prediction is not None

def test_single_pred_str_type(single_prediction): ## Data type is string
    assert isinstance(single_prediction.get('Predictions')[0],str)

def test_single_pred_validate(single_prediction): ## Check the output is Y
    assert single_prediction.get('Predictions')[0] == 'Y'