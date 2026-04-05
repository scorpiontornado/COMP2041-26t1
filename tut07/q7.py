#! /usr/bin/env python3

# COMP2041 26T1, W11B Tutorial 7, Q7
#
# "Write a new version of cat so that it accepts a -n command line
# argument and then prints a line number at the start of each line in a
# field of width 6, followed by two spaces, followed by the text of the
# line.
#
# The numbers should constantly increase over all of the input files
# (i.e. don't start renumbering at the start of each file)."

import sys

number = False
if len(sys.argv) > 1 and sys.argv[1].startswith("-"):
    # TODO: error handling - invalid command line arg
    arg = sys.argv.pop(1)
    if arg[1:] == "n":
        number = True

if len(sys.argv) == 1:
    sys.argv.append("-")

line_num = 1
for filename in sys.argv[1:]:
    try:
        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)

        for line in stream:
            if number:
                sys.stdout.write(f"{line_num:6}  {line}")
            else:
                sys.stdout.write(line)
            line_num += 1

        if stream != sys.stdin:
            stream.close()

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
