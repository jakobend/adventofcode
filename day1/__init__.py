"""
Solutions for day 1 of the Advent of Code 2017.
"""

def reverse_captcha(digits):
    """
    Calculate the sum of all identical consecutive digits in an iterator.
    >>> reverse_captcha([1,1,2,2])
    3
    >>> reverse_captcha([1,1,1,1])
    4
    >>> reverse_captcha([1,2,3,4])
    0
    >>> reverse_captcha([9,1,2,1,2,1,2,9])
    9
    """
    return sum(
        a
        for a, b in zip(digits, digits[1:] + digits[0:1])
        if a == b
    )

def halfway_reverse_captcha(digits):
    """
    Calculate the sum of all digits that are equal to the digit on the opposite
    end of a circular list.
    >>> halfway_reverse_captcha([1,2,1,2])
    6
    >>> halfway_reverse_captcha([1,2,2,1])
    0
    >>> halfway_reverse_captcha([1,2,3,1,2,3])
    12
    >>> halfway_reverse_captcha([1,2,1,3,1,4,1,5])
    4
    """
    assert len(digits) % 2 == 0, "list must be of even length"
    offset = len(digits) // 2
    return sum(
        a
        for a, b in zip(digits, digits[offset:] + digits[:offset])
        if a == b
    )
