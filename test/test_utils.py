import pytest
from utils import utils


@pytest.fixture
def col_from():
    return [{"from": "Maestro 1596837868705199"},{"from": "Счет 75106830613657916952"},{"from": "Visa Classic 6831982476737658"}]

def test_hidden_account_from_maestro(col_from):
    assert utils.hidden_account_from(col_from, 0) == 'Maestro 1596 83** **** 5199 '

def test_hidden_account_from_visa(col_from):
    assert utils.hidden_account_from(col_from, 2) == 'Visa Classic 6831 98** **** 7658 '

def test_hidden_account_from_check(col_from):
    assert utils.hidden_account_from(col_from, 1) == 'Счет **6952 '


@pytest.fixture
def col_to():
    return [{"to": "Maestro 5648237968706759"}, {"to": "Счет 75106830613657623594"},{"to": "Visa Classic 1369258776733252"}]

def test_hidden_account_to_maestro(col_to):
    assert utils.hidden_account_to(col_to, 0) == 'Maestro 5648 23** **** 6759 '

def test_hidden_account_to_visa(col_to):
    assert utils.hidden_account_to(col_to, 2) == 'Visa Classic 1369 25** **** 3252 '

def test_hidden_account_to_check(col_to):
    assert utils.hidden_account_to(col_to, 1) == 'Счет **3594'



@pytest.fixture
def date_cons():
    return [{"date": "2018-08-19T04:27:37.904916","description": "Перевод организации"}]

def test_date_output(date_cons):
    assert utils.date_output(date_cons, 0) == '19.8.2018 Перевод организации'



@pytest.fixture
def operation():
    return [{"operationAmount": {"amount": "40701.91","currency": {"name": "USD","code": "USD"}}}]
def test_transfer_amount_currency(operation):
    assert utils.transfer_amount_currency(operation,0) == '40701.91 USD\n'



@pytest.fixture
def check_json_executed():
    return [{"state": "EXECUTED"}, {"state": "EXECUTED"},{"state": "CANCELED"},{}]
@pytest.fixture
def check_json_wrong_data():
    return 0
def test_transactions_executed(check_json_executed):
    assert utils.transactions_executed(check_json_executed) == [{"state": "EXECUTED"}, {"state": "EXECUTED"}]

def test_transactions_executed_wrong_data(check_json_wrong_data):
    assert utils.transactions_executed(check_json_wrong_data) == ['Неверный формат файла']



@pytest.fixture
def check_sort_ny_date():
    return [{"date": "2018-09-12T21:27:25.241689"}, {"date": "2018-10-14T08:21:33.419441"},{"date": "2018-01-26T15:40:13.413061"}]
def test_sort_by_date(check_sort_ny_date):
    assert utils.sort_by_date(check_sort_ny_date) == [{'date': '2018-01-26T15:40:13.413061'}, {'date': '2018-09-12T21:27:25.241689'}, {'date': '2018-10-14T08:21:33.419441'}]


