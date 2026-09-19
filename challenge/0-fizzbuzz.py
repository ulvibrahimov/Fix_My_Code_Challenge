#!/usr/bin/python3
"""
FizzBuzz implementation
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    - For numbers divisible by 3 and 5, print "FizzBuzz"
    - For numbers divisible by 3, print "Fizz"
    - For numbers divisible by 5, print "Buzz"
    """
    if n < 1:
        return

    tmp_status = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            tmp_status.append("FizzBuzz")
        elif i % 3 == 0:
            tmp_status.append("Fizz")
        elif i % 5 == 0:
            tmp_status.append("Buzz")
        else:
            tmp_status.append(str(i))
    print(" ".join(tmp_status))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing number")
        sys.exit(1)

    fizzbuzz(int(sys.argv[1]))
