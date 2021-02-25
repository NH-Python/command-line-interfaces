#!/usr/bin/env python3

def add_space(line: str) -> str:
    """
    returns a copy of `line`, with a space
    between each character
    """
    return " ".join(line[:])

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        print(add_space(line), end="")
