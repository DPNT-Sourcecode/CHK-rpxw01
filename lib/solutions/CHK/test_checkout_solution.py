import pytest
from .checkout_solution import checkout

def generate_test_string(input_str: str) -> str:
    """
    Take a  string like `5A 2B` and convert it into `AAAAABB`
    """
    if not input_str:
        return ""
    result_str = ""
    for subset in input_str.split():
        count = int(subset[:-1])
        product = subset[-1:]
        result_str = result_str + count * product



@pytest.mark.parametrize("input_str, expected_price", [
    ("A", 50),
    ("AA", 100),
    ("AAA", 130),
    ("AAAAA", 200),
    ("", ),
    ("AB", 80),
    ("BAB", 95),
    ("DD", 30),
    ("ABCDAB", 180),
    ("ABCDABE", -1),
    ("CCCCC", 100),
])
def test_checkout(input_str, expected_price):
    assert checkout(input_str) == expected_price


