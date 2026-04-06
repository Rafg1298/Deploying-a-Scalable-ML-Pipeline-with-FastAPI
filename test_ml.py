import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, compute_model_metrics, inference


# TODO: implement the first test. Change the function name and input as needed
def test_one():

    X = np.array([[1, 2], [3, 4]])
    y = np.array([0, 1])
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier)



# TODO: implement the second test. Change the function name and input as needed
def test_two():

    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([0, 1, 0, 1])
    model = train_model(X, y)
    preds = inference(model, X)
    precision, recall, fbeta = compute_model_metrics(y, preds)
    
    # Assert metrics are within valid range [0, 1]
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1

# TODO: implement the third test. Change the function name and input as needed
def test_three():

    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([0, 1, 0, 1])
    model = train_model(X, y)
    preds = inference(model, X)
    
    # Assert input shape is correct
    assert X.shape == (4, 2)
    
    # Assert output shape is correct (should have same number of samples as input)
    assert preds.shape == (4,)
    assert len(preds) == X.shape[0]