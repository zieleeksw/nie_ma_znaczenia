from exercises.ex_1 import greet


def test_greet():
    result = greet("Jan", "Kowalski")

    expected = "Cześć Jan Kowalski!"
    assert result, expected
