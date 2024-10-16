import pytest
from arguments_length import arguments_length

def test_single_argument():
    assert arguments_length(5) == 1

def test_multiple_arguments():
    assert arguments_length({}, None, "3") == 3
    assert arguments_length([{}, None, "3"]) == 1
    

def test_no_arguments():
    assert arguments_length() == 0

def test_large_number_of_arguments():
    assert arguments_length(*[i for i in range(100)]) == 100    # here the * as the unpacking operator
    assert arguments_length([i for i in range(100)]) == 1       # here without the * 