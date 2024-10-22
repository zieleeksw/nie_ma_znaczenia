import pytest

from exercises.ex_5 import contains_value


@pytest.mark.parametrize("my_list, value, expected", [
    ([1, 2, 3, 4, 5], 3, True),
    ([1, 2, 3, 4, 5], 6, False),
    ([10, 20, 30], 10, True),
    ([10, 20, 30], 25, False),
    ([], 1, False),
    ([1, 2, 3], 1, True)
])
def test_contains_value(my_list, value, expected):
    assert contains_value(my_list, value) == expected
