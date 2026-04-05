#! /usr/bin/env python3

# COMP2041 26T1, W11B Tutorial 7, Q5
#
# "Write a simple version of the head command in Python, that accepts an
# optional command line argument in the form -n, where n is a number,
# and displays the first n lines from its standard input.
#
# If the -n option is not used, then the program simply displays the
# first ten lines from its standard input."

import sys

n_lines = 10
if len(sys.argv) > 1 and sys.argv[1].startswith("-"):
    # TODO: error handling - invalid command line arg
    arg = sys.argv[1]
    n_lines = int(arg[1:])

# i = 1
# for line in sys.stdin:
#     if i > n_lines:
#         break
#     # print(line, end="")
#     sys.stdout.write(line)
#     i += 1

for i, line in enumerate(sys.stdin):
    # Note: enumerate is 0-indexed
    if i >= n_lines:
        break
    sys.stdout.write(line)
