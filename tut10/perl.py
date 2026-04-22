#! /usr/bin/env python3

# COMP2041 26T1, W11B Tutorial 10, Q6

import sys


def chomp(string: str) -> str:
    """A Python implementation of the Perl function chomp.

    Removes a single newline from the end of a string (if there is one).
    """
    if string[-1] == "\n":
        return string[:-1]
    return string


def qw(string: str) -> list[str]:
    """A Python implementation of the Perl function qw.

    Splits a string into a list of words.
    """
    return string.split()


def die(message: str):
    """A Python implementation of the Perl function die.

    Prints an error message and exits the program.
    """
    print(sys.argv[0], "Error", message, sep=": ", file=sys.stderr)
    sys.exit(1)
