import pytest

from exercises.ex_2 import multiply


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (0, 0, 0),
    (-1, 1, -1),
    (6, 7, 42),
    (10, 10, 100)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
