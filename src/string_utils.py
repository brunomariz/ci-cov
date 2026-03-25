def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")
