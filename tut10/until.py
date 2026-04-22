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

    # if args.stop.isnumeric():
    #     print("number")
    # else:
    #     print("regex")

    try:
        stop = int(args.stop)
    except:
        stop = compile(args.stop[1:-1])

    for i, line in enumerate(sys.stdin, start=1):
        # if line[-1] == '\n':
        #     line = line[:-1]
        line = line.rstrip("\n")
        print(line)

        if isinstance(stop, int):
            if i == stop:
                break
        else:  # stop is a compiled regex object
            if stop.search(line):
                break


if __name__ == "__main__":
    main()
