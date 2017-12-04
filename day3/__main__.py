"""
Runs doctests and then calculates the answer to the puzzle.
"""

import sys
import doctest
from . import calculate_steps, find_limit

INPUT = 277678

doctest.testmod(sys.modules[__package__])
print("Part 1:", calculate_steps(INPUT))
print(find_limit(INPUT))
