#!/usr/bin/env python
import sys

def stdin_to_uppercase():
    for line in sys.stdin:
        print(line.upper(), end="")


if __name__ == "__main__":
    stdin_to_uppercase()
