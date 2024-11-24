import pytest

from exercises.ex_4 import is_sum_of_first_and_second_higher_than_third


@pytest.mark.parametrize("first, second, third,  expected", [
    (5, 5, 10, False),
    (4, 6, 9, True),
    (1, 2, 5, False),
    (0, 0, 0, False),
    (-3, 7, 3, True),
    (-5, -5, -10, False)
])
def test_is_even(first: int, second: int, third: int, expected: bool) -> None:
    assert (is_sum_of_first_and_second_higher_than_third(first, second, third)
            == expected)
