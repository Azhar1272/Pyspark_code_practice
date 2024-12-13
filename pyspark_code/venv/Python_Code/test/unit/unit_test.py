# test_max_value.py
import pytest
from test import max_val

def test_max_val():
    # Test case 1: Standard dictionary
    input_dict = {'a': 10, 'b': 20, 'c': 15}
    assert max_val(input_dict) == 'b'

    # Test case 2: Dictionary with negative values
    input_dict = {'x': -10, 'y': -5, 'z': -20}
    assert max_val(input_dict) == ''

    # Test case 3: Dictionary with zero values
    input_dict = {'p': 0, 'q': 0, 'r': 0}
    assert max_val(input_dict) == ''  # No key has a value greater than 0

    # Test case 4: Empty dictionary
    input_dict = {}
    assert max_val(input_dict) is None  # No key in the dictionary

    # Test case 5: Single key-value pair
    input_dict = {'only': 42}
    assert max_val(input_dict) == 'only'
