"""
Runs doctests and then calculates the answer to the puzzle.
"""

import sys
import os
import doctest
from . import reverse_captcha, halfway_reverse_captcha

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    DIGITS = [int(char) for char in f.read().strip()]

doctest.testmod(sys.modules[__package__])
print("Part 1:", reverse_captcha(DIGITS))
print("Part 2:", halfway_reverse_captcha(DIGITS))
