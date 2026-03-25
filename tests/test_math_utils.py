from src.math_utils import add, divide, is_prime
import pytest


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_is_prime():
    assert is_prime(7)
    assert not is_prime(8)
