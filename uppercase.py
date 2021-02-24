#!/usr/bin/env python

def to_uppercase(line:str) -> str:
    """
    returns a copy of `line`, with all characters
    uppercase
    """
    return line.upper()

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        print(to_uppercase(line), end="")
