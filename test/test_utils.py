import pytest
from utils import utils

@pytest.fixture
def coll():
    return [{"from": "Maestro 1596837868705199"},{"from": "Счет 75106830613657916952"},{"from": "Visa Classic 6831982476737658"}]

def test_hidden_account_from_maestro(coll):
    assert utils.hidden_account_from(coll,0) == 'Maestro 1596 83** **** 5199 '

def test_hidden_account_from_visa(coll):
    assert utils.hidden_account_from(coll,2) == 'Visa Classic 6831 98** **** 7658 '

def test_hidden_account_from_check(coll):
    assert utils.hidden_account_from(coll,1) == 'Счет **6952'

