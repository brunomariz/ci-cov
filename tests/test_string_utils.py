from src.string_utils import reverse_string, is_palindrome, count_vowels


def test_reverse():
    assert reverse_string("abc") == "cba"


def test_palindrome():
    assert is_palindrome("A man a plan a canal Panama")
    assert not is_palindrome("hello")


def test_vowels():
    assert count_vowels("hello") == 2
