import time


def slow_square(n):
    time.sleep(2)  # simulate slow computation
    return n * n


def slow_sum(numbers):
    time.sleep(3)
    return sum(numbers)
