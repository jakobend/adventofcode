"""
Solutions for day 2 of the Advent of Code 2017.
"""

import sys
from itertools import permutations

def checksum(spreadsheet):
    """
    Calculate the checksum of a spreadsheet by summing up the ranges of all
    lines.
    >>> checksum([
    ...     [5, 1, 9, 5],
    ...     [7, 5, 3],
    ...     [2, 4, 6, 8]
    ... ])
    18
    """
    return sum(
        max(line) - min(line)
        for line in spreadsheet
    )

def divisor_checksum(spreadsheet):
    """
    Calculate the checksum of a spreadsheet by summing up the common divisors of
    all lines.
    >>> divisor_checksum([
    ...     [5, 9, 2, 8],
    ...     [9, 4, 7, 3],
    ...     [3, 8, 6, 5]
    ... ])
    9
    """
    return sum(
        next(
            n // m for n, m in permutations(line, 2)
            if n % m == 0
        )
        for line in spreadsheet
    )
