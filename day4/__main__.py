"""
Runs doctests and then calculates the answer to the puzzle.
"""

import sys
import os
import doctest
from . import is_simple_passphrase, is_anagram_passphrase

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rU") as f:
    PASSHPHRASES = [
        line.strip().split(" ")
        for line in f
    ]

doctest.testmod(sys.modules[__package__])
print("Part 1:", sum(is_simple_passphrase(phrase) for phrase in PASSHPHRASES))
print("Part 2:", sum(is_anagram_passphrase(phrase) for phrase in PASSHPHRASES))
