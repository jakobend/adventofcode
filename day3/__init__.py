"""
Solutions for day 3 of the Advent of Code 2017.
"""

from math import floor, sqrt
import sys

def ulam_transformation(n):
    """
    Transform an integer to a point on the Ulam spiral.
    Implements the formula found at
    <http://danpearcymaths.wordpress.com/2012/09/30/infinity-programming-in-geogebra-and-failing-miserably/>
    """
    p = floor(sqrt(4 * n + 1))
    q = n - floor((p * p) / 4)
    z = q * 1j ** p + (floor((p + 2) / 4) - (floor((p + 1) / 4) * 1j)) * 1j ** (p - 1)
    return (int(z.imag), int(z.real))

def inverse_ulam_transformation(p):
    x, y = p
    if x > -y:
        if x > y: # east
            return (x * 2 - 1)**2 + (x - y) - 1
        else: # south
            return (-y * 2 - 1)**2 + (x - y) - 1
    else:
        if x > y: # north
            return (-y * 2)**2 - (x - y)
        else: # west
            return (x * 2)**2 - (x - y)
        


def manhattan_distance(a, b):
    """
    Calculates the Manhattan distance between two points.
    """
    return int(abs(a[0] - b[0]) + abs(a[1] - b[1]))

def calculate_steps(location):
    """
    Calculates the Manhattan distance between a location on the one-based memory
    spiral and the origin.
    >>> calculate_steps(1)
    0
    >>> calculate_steps(12)
    3
    >>> calculate_steps(23)
    2
    >>> calculate_steps(1024)
    31
    """
    return manhattan_distance((0, 0), ulam_transformation(location - 1))

def neighbours(position):
    """
    Yields the neighbours of a two-dimensional point.
    """
    for y in range(position[0] - 1, position[0] + 2):
        for x in range(position[1] - 1, position[1] + 2):
            if x != position[0] or y != position[1]:
                yield (x, y)

def find_limit(limit):
    """
    FIXME
    """
    memory = {1: 1}

    def calculate_sum(location):
        position = ulam_transformation(location - 1)
        accumulator = 0
        for neighbour_position in neighbours(position):
            neighbour_location = inverse_ulam_transformation(neighbour_position) + 1
            if neighbour_location < location:
                if neighbour_location in memory:
                    neighbour_sum = memory[neighbour_location]
                else:
                    neighbour_sum = calculate_sum(neighbour_location)
                    memory[neighbour_location] = neighbour_sum
                accumulator += neighbour_sum
        return accumulator

    location = 1
    while True:
        location += 1
        if calculate_sum(location) > limit:
            return location
