#!/usr/bin/env python3

# COMP2041 26T1, W11B Tutorial 10, Q3 (vowels)
#
# A program that maps all lower-case vowels (a,e,i,o,u) in its standard
# input into their upper-case equivalents and, at the same time, maps all
# upper-case vowels (A, E, I, O, U) into their lower-case equivalents.

# Shell equivalent:
# tr "AEIOUaeiou" "aeiouAEIOU"

import sys

VOWELS = "aeiou"

# "AEIOUaeiou"
# "aeiouAEIOU"


def main():
    tt = str.maketrans(VOWELS.upper() + VOWELS.lower(), VOWELS.lower() + VOWELS.upper())
    for line in sys.stdin:
        print(line.translate(tt), end="")


if __name__ == "__main__":
    main()
