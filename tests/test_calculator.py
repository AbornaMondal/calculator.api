# tests/test_calculator.py

from app import calculator

def test_add():
    assert calculator.add(3, 4) == 7

def test_divide_by_zero():
    try:
        calculator.divide(5, 0)
        assert False
    except ValueError:
        assert True
