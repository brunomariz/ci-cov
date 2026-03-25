import pytest
from src.slow_ops import slow_square, slow_sum


@pytest.mark.slow
def test_slow_square():
    assert slow_square(3) == 9


@pytest.mark.slow
def test_slow_sum():
    assert slow_sum([1, 2, 3]) == 6
