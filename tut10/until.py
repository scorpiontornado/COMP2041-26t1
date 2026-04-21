#!/usr/bin/env python3

# COMP2041 26T1, W11B Tutorial 10, Q2 (until)
#
# A program that takes as an argument either a line number (e.g. 3) or a
# regular expression (e.g. /.[13579]/) and prints all lines given to it
# by standard input until the given line number, or the first line
# matching the regular expression.

from argparse import ArgumentParser
from re import compile
import sys


def main():
    parser = ArgumentParser()
    parser.add_argument("stop")
    args = parser.parse_args()

    # TODO: handle int and regex (strip "/" & compile)

    for i, line in enumerate(sys.stdin, start=1):
        # TODO: print lines until a given number or matches regex
        pass


if __name__ == "__main__":
    main()
