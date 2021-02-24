#!/usr/bin/env python
import sys

def add_space():
    characters = 0
    for line in sys.stdin:
        characters = characters + len(line)
        print(" ".join(line[:]), end="")

if __name__ == "__main__":
    add_space()
