import pytest
# TODO: add necessary import
from ml.model import train_model, inference
from train_model import data, test
from ml.data import process_data

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    Test the train_model function
    """
    # Your code here
    assert 15 == data.shape[1]


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Test the inference function
    """
    # Your code here
    expected_columns = [
        "age",
        "workclass",
        "fnlgt",
        "education",
        "education-num",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital-gain",
        "capital-loss",
        "hours-per-week",
        "native-country",
        "salary",
    ]
    assert expected_columns == test.columns.tolist()



# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    Test the process_data function
    """
    # Your code here
    assert data['salary'].dtype == 'object'
