# Write pytest tests for the calculator class
import pytest
from docs.example2 import Calculator
@pytest.fixture
def calc():
    return Calculator()
def test_add(calc):
    assert calc.add(10, 5) == 15
    assert calc.add(-1, 1) == 0
def test_subtract(calc):
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(-1, -1) == 0
def test_multiply(calc):
    assert calc.multiply(10, 5) == 50
    assert calc.multiply(-1, 1) == -1
def test_divide(calc):
    assert calc.divide(10, 5) == 2
    with pytest.raises(ValueError):
        calc.divide(10, 0)
def test_divide_negative(calc):
    assert calc.divide(-10, 2) == -5
    assert calc.divide(-10, -2) == 5
def test_add_floats(calc):
    assert calc.add(10.5, 5.5) == 16.0
    assert calc.add(-1.1, 1.1) == 0.0
def test_subtract_floats(calc):
    assert calc.subtract(10.5, 5.5) == 5.0
    assert calc.subtract(-1.1, -1.1) == 0.0
def test_multiply_floats(calc):
    assert calc.multiply(10.5, 2) == 21.0
    assert calc.multiply(-1.5, 2) == -3.0
def test_divide_floats(calc):
    assert calc.divide(10.5, 2) == 5.25
    with pytest.raises(ValueError):
        calc.divide(10.5, 0)
def test_chain_operations(calc):
    result = calc.add(10, 5)
    result = calc.subtract(result, 3)
    result = calc.multiply(result, 2)
    result = calc.divide(result, 4)
    assert result == 6.0
def test_zero_operations(calc):
    assert calc.add(0, 0) == 0
    assert calc.subtract(0, 0) == 0
    assert calc.multiply(0, 10) == 0
    with pytest.raises(ValueError):
        calc.divide(0, 0)
    assert calc.divide(10, 1) == 10
def test_large_numbers(calc):

    assert calc.add(1e10, 1e10) == 2e10
    assert calc.subtract(1e10, 1e9) == 9e9
    assert calc.multiply(1e5, 1e5) == 1e10
    assert calc.divide(1e10, 1e5) == 1e5
def test_negative_numbers(calc):
    assert calc.add(-10, -5) == -15
    assert calc.subtract(-10, -5) == -5
    assert calc.multiply(-10, -5) == 50
    assert calc.divide(-10, -5) == 2

    