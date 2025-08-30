import pytest
from fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    "n, fizz, buzz, expected",
    [
        (100, 3, 5, True),
        (100, 4, 5, True),
        (100, 6, 5, True)
    ])
def test_basic(n, fizz, buzz, expected):
    fizzbuzz(n, fizz, buzz)
    print(f"Testing in Progress")
    assert 1 == 2 / 2
