import pytest
import datetime
from lib.age_limit import *


def test_if_underage():
    result = age_limit("2010-3-14")
    assert result == "Access denied. Current age: 13. Required age: 16"

def test_if_age_passes():
    result = age_limit("2002-3-14")
    assert result == "Access granted."

def test_for_value_error():
    with pytest.raises(ValueError, match="time data 'error' does not match format '%Y-%m-%d'"):
        age_limit("error")

