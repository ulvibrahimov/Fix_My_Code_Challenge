#!/usr/bin/python3
"""
FizzBuzz module
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers 1 to n separated by space
    """
    if n < 1:
        return

    res = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    print(" ".join(res))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing number")
        sys.exit(1)

    fizzbuzz(int(sys.argv[1]))
