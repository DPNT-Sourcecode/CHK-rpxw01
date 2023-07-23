import pytest
from .checkout_solution import checkout


def generate_test_string(input_str: str) -> str:
    """
    Take a  string like `5A 2B` and convert it into `AAAAABB`.
    Requires a number, only works for single letter products
    """
    if not input_str:
        return ""
    result_str = ""
    for subset in input_str.split():
        count = int(subset[:-1])
        product = subset[-1:]
        result_str = result_str + count * product
    return result_str


@pytest.mark.parametrize("input, expected", [
    ("", ""),
    ("1A", "A"),
    ("3A 2B", "AAABB"),
    ("2A 2B 2C 2D", "AABBCCDD"),
])
def test_generate_test_string(input: str, expected: str):
    assert generate_test_string(input) == expected


########################################################


@pytest.mark.parametrize("input_str, expected_price", [
    ("", 0),
    ("1A", 50),
    ("2A", 100),
    ("2B", 45),
    ("1A 2B", 95),
    ("7A", 300),
    ("8A", 330),
    ("9A", 380),
    ("2B 1E", 85),
    ("2B 2E", 110),
    ("2B 2E 1D", 125),

    ("1F", 10),
    ("2F", 20),
    ("3F", 20),
    ("4F", 30),
    ("5F", 40),
    ("6F", 40),

    ("6F 2A", 140),


    ("3Z", 45),
    ("1X 1Y 1Z", 45),
    ("1X 1Y 2Z", 45 + 17),
    ("1S 1T 1X 1Y 1Z", 17 + 20),
    ("1S 1T 1X 1Y 2Z", 90),



])
def test_checkout(input_str, expected_price):
    assert checkout(generate_test_string(input_str)) == expected_price

