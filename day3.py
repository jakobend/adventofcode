"""
Solution for Day 3 of the Advent of Code 2017.
"""

from math import floor, sqrt
import sys

def ulam_transformation(n):
    """
    Transforms an integer to a point on an Ulamb spiral.
    http://danpearcymaths.wordpress.com:80/2012/09/30/infinity-programming-in-geogebra-and-failing-miserably/
    """
    p = floor(sqrt(4 * n + 1))
    q = n - floor((p * p) / 4)
    z = q * 1j ** p + (floor((p + 2) / 4) - (floor((p + 1) / 4) * 1j)) * 1j ** (p - 1)
    return (z.imag, z.real)

def manhattan_distance(a, b):
    """
    Calculates the Manhattan distance between two points.
    """
    return int(abs(a[0] - b[0]) + abs(a[1] - b[1]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: {} N".format(sys.argv[0]))
        sys.exit(1)
    n = int(sys.argv[1])
    print(manhattan_distance((0, 0), ulam_transformation(n - 1)))
