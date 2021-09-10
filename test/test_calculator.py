from src.calculator import Calculator

calculator = Calculator()


def test_should_add_two_numbers():
    assert calculator.add(2, 4) == 6


def test_should_add_two_strings():
    assert calculator.add("one", "two") == "onetwo"
