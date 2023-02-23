import pytest
from utils import utils

def test_load_json():
    with pytest.raises(AssertionError):
        assert utils.load_json() == 0