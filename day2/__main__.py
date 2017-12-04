"""
Runs doctests and then calculates the answer to the puzzle.
"""

import sys
import os
import doctest
from . import checksum, divisor_checksum

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    SPREADSHEET = [
        [
            int(cell)
            for cell in line.split("\t")
        ]
        for line in f.read().splitlines()
    ]

doctest.testmod(sys.modules[__package__])
print("Part 1:", checksum(SPREADSHEET))
print("Part 2:", divisor_checksum(SPREADSHEET))
