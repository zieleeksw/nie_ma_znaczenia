import pytest

from exercises.ex_3 import is_even, print_even_or_odd


@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, False),
    (4, True),
])
def test_is_even(num: int, expected: bool) -> None:
    assert is_even(num) == expected


@pytest.mark.parametrize("number, expected_output", [
    (2, "Liczba parzysta\n"),
    (3, "Liczba nieparzysta\n"),
    (0, "Liczba parzysta\n"),
    (-4, "Liczba parzysta\n"),
    (-5, "Liczba nieparzysta\n")
])
def test_print_even_or_odd(capsys, number, expected_output):
    print_even_or_odd(number)

    captured = capsys.readouterr()

    assert captured.out == expected_output
