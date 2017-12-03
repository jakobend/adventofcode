"""
Solution for Day 1 of the Advent of Code 2017.
"""
import sys
if __name__ == "__main__":
    digits = [int(char) for char in sys.stdin.read().strip()]
    print(
        sum(
            a
            for a, b in zip(digits, digits[1:] + digits[0:1])
            if a == b
        )
    )
