"""
Calculates the sum of the ranges of tab-separated lines of numbers read from
stdin.
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
