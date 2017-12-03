"""
Solution for Day 2 of the Advent of Code 2017.
"""
import sys
if __name__ == "__main__":
    print(
        sum(
            max(line) - min(line)
            for line in [
                [
                    int(cell)
                    for cell in line.split("\t")
                ]
                for line in sys.stdin.read().splitlines()
            ]
        )
    )
