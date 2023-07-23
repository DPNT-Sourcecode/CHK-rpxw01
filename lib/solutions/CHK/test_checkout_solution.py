import pytest
from .checkout_solution import checkout


@pytest.mark.parametrize("input_str, expected_price", [
    ("A", 50),
    ("AA", 100),
    ("AAA", 130),
    ("AB", 80),
    ("BAB", 95),
    ("DD", 30),
    ("ABCDAB", 180),
    ("ABCDABE", -1),
    ("CCCCC", 100),
])
def test_checkout(input_str, expected_price):
    assert checkout(input_str) == expected_price


