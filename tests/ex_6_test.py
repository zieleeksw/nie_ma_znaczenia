import pytest

from exercises.ex_6 import merge_and_cube_lists


@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 3], [4, 5, 6], [1, 8, 27, 64, 125, 216]),  # regular
    ([1, 2, 2], [3, 4, 4], [1, 8, 27, 64]),  # duplicates in single list
    ([1, 1, 1], [1, 1, 1], [1]),  # all elements are the same
    ([0, 2, 3], [1, 0, 3], [0, 1, 8, 27]),  # lists includes 0
    ([], [], []),  # both empty
    ([5, 6], [5, 6], [125, 216]),  # duplicates
])
def test_merge_and_cube_lists(list1, list2, expected):
    assert merge_and_cube_lists(list1, list2) == expected
